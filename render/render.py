#!/usr/bin/env python3
"""Render resume variant Markdown into a printable HTML file (and optional PDF).

The Markdown in `variants/` and `tailored/` is the source of truth, and doubles
as the plain single-column ATS-safe artifact. This script only *re-presents* it
for human readers: it never adds, removes, reorders, or rewords content. Section
order comes from the Markdown, so each archetype's ordering is preserved.

Usage
-----
    python3 render/render.py variants/variant-A.md
    python3 render/render.py --all --pdf
    python3 render/render.py tailored/acme-mgr.md --pdf -o build/acme.html

Output defaults to `build/<stem>.html` (and `build/<stem>.pdf` with --pdf).
PDF generation shells out to headless Chrome and reports the page count, since
two pages is the target length (CONTEXT.md §3).

Structure the renderer recognizes
---------------------------------
    # Name                          -> masthead; the paragraph after it is the
                                       contact line (emails/phones auto-linked)
    ## Section                       -> green small-caps heading; content is
                                       wrapped in <section class="sec sec-KEY">
    ### Title — Org — 04/2022–10/2023
                                     -> role heading; a trailing date-like field
                                        is floated right, the org is bolded
    *Scope line under a role*        -> muted italic context line
    - bullet                         -> square-marker list (nesting supported)

    <!-- page-break -->              -> force a page break at that point
"""

from __future__ import annotations

import argparse
import base64
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from xml.etree import ElementTree as etree

try:
    import markdown
    from markdown.extensions import Extension
    from markdown.inlinepatterns import InlineProcessor
    from markdown.treeprocessors import Treeprocessor
except ImportError:  # pragma: no cover
    sys.exit("error: the `markdown` package is required (pip install markdown)")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DEFAULT_CSS = os.path.join(HERE, "resume.css")
DEFAULT_OUTDIR = os.path.join(ROOT, "build")
FONT_DIR = os.path.join(HERE, "fonts")
FONT_MANIFEST = os.path.join(FONT_DIR, "manifest.json")

MD_EXTENSIONS = ["extra", "sane_lists", "smarty"]

# Type-density presets, as (--base-size, --lead). Vertical rhythm in resume.css
# is em-based, so shrinking the base size tightens the whole page proportionally.
# This is the content-safe way to close a short overflow: --fit walks the list
# until the PDF hits the page target instead of cutting bullets.
DENSITIES = {
    "normal": ("10.5pt", "1.36"),
    "compact": ("10.1pt", "1.30"),
    "tight": ("9.7pt", "1.25"),
}
FIT_ORDER = ["normal", "compact", "tight"]

# --- fonts ------------------------------------------------------------------
# Fonts are vendored into render/fonts/ and embedded as base64 data URIs, so a
# rendered HTML file is self-contained: it prints identically offline and can be
# emailed as one file. It also avoids a real bug -- headless Chrome will print
# before a CDN webfont finishes downloading, silently falling back to Arial.
FONT_CSS_URL = (
    "https://fonts.googleapis.com/css2"
    "?family=Gentium+Book+Plus:ital,wght@1,400"
    "&family=Roboto:ital,wght@0,400;0,500;0,700;1,400"
    "&display=swap"
)
# An old-style UA makes Google Fonts serve complete TTFs (one file per face, no
# unicode-range splitting) rather than pre-subset woff2 we cannot re-subset
# without brotli. Both outcomes are handled; TTF is preferred.
TTF_UA = "Mozilla/5.0"
KEEP_SUBSETS = {"latin", "latin-ext", None}

# Glyphs kept when subsetting: ASCII, Latin-1, Latin Extended-A (accented
# co-author names), General Punctuation (curly quotes, en/em dashes, bullets),
# arrows (the "0 -> $2M ARR" bullets), and common math signs.
SUBSET_RANGES = [
    (0x0020, 0x007E),
    (0x00A0, 0x00FF),
    (0x0100, 0x017F),
    (0x2000, 0x206F),
    (0x2190, 0x21FF),
    (0x2202, 0x22FF),
    (0x20AC, 0x20AC),
    (0x2122, 0x2122),
    (0x2126, 0x2126),
]

FONT_FACE_BLOCK = re.compile(
    r"(?:/\*\s*(?P<subset>[\w-]+)\s*\*/\s*)?@font-face\s*\{(?P<body>[^}]*)\}", re.S
)

# Section-heading keyword -> class suffix. First match in this order wins, so
# "Selected Publications & Academic Leadership" resolves to `publications`.
SECTION_KEYS = [
    ("summary", "summary"),
    ("experience", "experience"),
    ("publication", "publications"),
    ("talk", "talks"),
    ("speaking", "talks"),
    ("service", "service"),
    ("skill", "skills"),
    ("education", "education"),
    ("teaching", "teaching"),
    ("award", "awards"),
    ("project", "projects"),
]

# Boilerplate lines that are set as muted italic notes rather than body text.
NOTE_PREFIXES = ("name in", "full list on", "venue tiers")

# Role-heading field separator: em or en dash with surrounding spaces.
FIELD_SEP = re.compile(r"\s+[—–]\s+")
# Trailing "(Dec 2018)"-style date on a list item.
TRAILING_PAREN_DATE = re.compile(r"\s*\(([^()]*\b\d{4}\b[^()]*)\)\s*$")
PAGE_BREAK_COMMENT = re.compile(r"<!--\s*page[-_ ]?break\s*-->", re.I)
# Apostrophe between a letter and a digit ("eCom'25"): smarty curls this the
# wrong way, so pre-normalize it to a real right single quote.
LETTER_DIGIT_APOSTROPHE = re.compile(r"(?<=[A-Za-z])'(?=\d)")


def looks_like_date(field: str) -> bool:
    """True for role-heading fields such as '04/2022–10/2023' or '08/2025–present'."""
    return len(field) <= 32 and bool(re.search(r"\b\d{4}\b", field))


def section_key(heading: str) -> str:
    lowered = heading.lower()
    for needle, key in SECTION_KEYS:
        if needle in lowered:
            return key
    return re.sub(r"[^a-z0-9]+", "-", lowered).strip("-") or "other"


def element_text(el: etree.Element) -> str:
    return "".join(el.itertext())


def make_date_span(text: str) -> etree.Element:
    span = etree.Element("span")
    span.set("class", "date")
    span.text = text
    return span


def float_trailing_date(el: etree.Element) -> None:
    """Move a trailing '(Dec 2018)' out of `el` into a right-floated span.

    The span is inserted first so the float lands at the top right of the block
    even when the text wraps to several lines.
    """
    target, attr = (el, "text") if len(el) == 0 else (el[-1], "tail")
    text = getattr(target, attr) or ""
    match = TRAILING_PAREN_DATE.search(text)
    if not match:
        return
    setattr(target, attr, text[: match.start()])
    span = make_date_span(match.group(1))
    leading = el.text
    el.text = None
    el.insert(0, span)
    span.tail = leading


class ResumeStructure(Treeprocessor):
    """Group the flat heading/paragraph stream into a masthead plus sections."""

    def run(self, root: etree.Element) -> None:
        children = list(root)
        for child in children:
            root.remove(child)

        container = root  # where subsequent blocks are appended
        current_key = ""
        header: etree.Element | None = None
        seen_contact = False
        prev_tag = ""

        for el in children:
            tag = el.tag

            if tag == "h1":
                header = etree.SubElement(root, "header")
                header.set("class", "masthead")
                el.set("class", "name")
                header.append(el)
                container = header

            elif tag == "h2":
                header = None
                current_key = section_key(element_text(el))
                container = etree.SubElement(root, "section")
                container.set("class", f"sec sec-{current_key}")
                container.append(el)

            elif tag == "h3":
                self.split_role_heading(el)
                container.append(el)

            elif tag == "p":
                text = element_text(el).strip()
                if header is not None and not seen_contact:
                    el.set("class", "contact")
                    seen_contact = True
                elif prev_tag == "h3" and self.is_wholly_italic(el):
                    el.set("class", "context")
                elif text.lower().startswith(NOTE_PREFIXES):
                    el.set("class", "note")
                container.append(el)

            elif tag == "ul" and current_key == "education":
                for item in el.findall("li"):
                    float_trailing_date(item)
                container.append(el)

            else:
                container.append(el)

            prev_tag = tag

    @staticmethod
    def is_wholly_italic(el: etree.Element) -> bool:
        """True for a paragraph that is a single <em> spanning the whole line."""
        return (
            not (el.text or "").strip()
            and len(el) == 1
            and el[0].tag == "em"
            and not (el[0].tail or "").strip()
        )

    @staticmethod
    def split_role_heading(el: etree.Element) -> None:
        """Turn 'Title — Org — dates' into title + bold org + floated date."""
        if len(el):  # contains inline markup; leave it alone
            return
        fields = FIELD_SEP.split((el.text or "").strip())
        date = fields.pop() if len(fields) > 1 and looks_like_date(fields[-1]) else None
        title, orgs = fields[0], fields[1:]

        el.text = None
        if date:
            el.append(make_date_span(date))
        if orgs:
            org = etree.SubElement(el, "span")
            org.set("class", "org")
            org.text = " — ".join(orgs)
            org.tail = None
            # Title text precedes the org span.
            if date:
                el[0].tail = f"{title} — "
            else:
                el.text = f"{title} — "
        else:
            if date:
                el[0].tail = title
            else:
                el.text = title


class MailtoProcessor(InlineProcessor):
    def handleMatch(self, m, data):  # noqa: N802 (markdown API)
        link = etree.Element("a")
        link.set("href", f"mailto:{m.group(1)}")
        link.text = m.group(1)
        return link, m.start(0), m.end(0)


class TelProcessor(InlineProcessor):
    def handleMatch(self, m, data):  # noqa: N802 (markdown API)
        link = etree.Element("a")
        link.set("href", "tel:+1" + re.sub(r"\D", "", m.group(1)))
        link.text = m.group(1)
        return link, m.start(0), m.end(0)


class ResumeExtension(Extension):
    def extendMarkdown(self, md):  # noqa: N802 (markdown API)
        md.treeprocessors.register(ResumeStructure(md), "resume_structure", 15)
        md.inlinePatterns.register(
            MailtoProcessor(r"(?<![\w.+-])([\w.+-]+@[\w-]+\.[\w.-]*\w)", md),
            "resume_mailto",
            175,
        )
        md.inlinePatterns.register(
            TelProcessor(r"(?<![\d-])(\d{3}-\d{3}-\d{4})(?![\d-])", md),
            "resume_tel",
            174,
        )


def parse_font_css(css: str) -> list[dict]:
    """Extract face descriptors + file URLs from a Google Fonts stylesheet."""
    faces = []
    for match in FONT_FACE_BLOCK.finditer(css):
        body = match.group("body")

        def prop(name: str) -> str | None:
            found = re.search(rf"\b{name}\s*:\s*([^;]+);", body)
            return found.group(1).strip() if found else None

        url = re.search(r"url\((https://[^)\s]+\.(?:ttf|woff2))\)", body)
        family = prop("font-family")
        if not url or not family:
            continue
        faces.append(
            {
                "subset": match.group("subset"),
                "family": family.strip("'\""),
                "style": prop("font-style") or "normal",
                "weight": prop("font-weight") or "400",
                "unicode_range": prop("unicode-range"),
                "url": url.group(1),
            }
        )
    return faces


def subset_ttf(data: bytes, dest: str) -> bool:
    """Cut a full TTF down to SUBSET_RANGES. Returns False if fontTools is absent."""
    try:
        from fontTools.subset import Options, Subsetter
        from fontTools.ttLib import TTFont
    except ImportError:
        return False

    import io

    options = Options()
    options.layout_features = ["*"]  # keep kerning and ligatures
    options.notdef_outline = True
    font = TTFont(io.BytesIO(data))
    subsetter = Subsetter(options=options)
    subsetter.populate(
        unicodes=[cp for start, end in SUBSET_RANGES for cp in range(start, end + 1)]
    )
    subsetter.subset(font)
    font.flavor = None
    font.save(dest)
    font.close()
    return True


def fetch_fonts(font_dir: str = FONT_DIR, quiet: bool = False) -> bool:
    """Download and vendor the webfonts into `font_dir`. Returns True on success."""
    def say(message: str) -> None:
        if not quiet:
            print(message)

    say(f"fetching fonts -> {display_path(font_dir)}")
    request = urllib.request.Request(FONT_CSS_URL, headers={"User-Agent": TTF_UA})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            css = response.read().decode("utf-8")
    except (urllib.error.URLError, OSError) as exc:
        print(f"  ! could not reach Google Fonts: {exc}", file=sys.stderr)
        return False

    faces = [f for f in parse_font_css(css) if f["subset"] in KEEP_SUBSETS]
    if not faces:
        print("  ! no usable @font-face rules in the stylesheet", file=sys.stderr)
        return False

    os.makedirs(font_dir, exist_ok=True)
    manifest = []
    for face in faces:
        slug = re.sub(r"[^a-z0-9]+", "-", face["family"].lower()).strip("-")
        parts = [slug, face["weight"], face["style"]]
        if face["subset"]:
            parts.append(face["subset"])
        is_ttf = face["url"].endswith(".ttf")
        filename = "-".join(parts) + (".ttf" if is_ttf else ".woff2")
        dest = os.path.join(font_dir, filename)

        try:
            with urllib.request.urlopen(
                urllib.request.Request(face["url"], headers={"User-Agent": TTF_UA}),
                timeout=30,
            ) as response:
                data = response.read()
        except (urllib.error.URLError, OSError) as exc:
            print(f"  ! failed to download {filename}: {exc}", file=sys.stderr)
            return False

        entry = {
            "family": face["family"],
            "style": face["style"],
            "weight": face["weight"],
            "file": filename,
        }
        if is_ttf and subset_ttf(data, dest):
            entry["format"] = "truetype"
            entry["mime"] = "font/ttf"
            # Subsetting covers SUBSET_RANGES for every face, so no
            # unicode-range gating is needed (or wanted) at render time.
        else:
            with open(dest, "wb") as handle:
                handle.write(data)
            entry["format"] = "truetype" if is_ttf else "woff2"
            entry["mime"] = "font/ttf" if is_ttf else "font/woff2"
            if face["unicode_range"]:
                entry["unicode_range"] = face["unicode_range"]

        size_kb = os.path.getsize(dest) / 1024
        say(f"  {filename}  {size_kb:.0f} KB")
        manifest.append(entry)

    with open(FONT_MANIFEST, "w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2)
        handle.write("\n")
    return True


def embedded_font_css(font_dir: str = FONT_DIR) -> str | None:
    """Build @font-face rules with base64 data URIs from the vendored fonts."""
    if not os.path.exists(FONT_MANIFEST):
        return None
    with open(FONT_MANIFEST, encoding="utf-8") as handle:
        manifest = json.load(handle)

    rules = []
    for entry in manifest:
        path = os.path.join(font_dir, entry["file"])
        if not os.path.exists(path):
            return None
        with open(path, "rb") as handle:
            payload = base64.b64encode(handle.read()).decode("ascii")
        rule = [
            "@font-face {",
            f"  font-family: '{entry['family']}';",
            f"  font-style: {entry['style']};",
            f"  font-weight: {entry['weight']};",
            "  font-display: swap;",
            f"  src: url(data:{entry['mime']};base64,{payload}) "
            f"format('{entry['format']}');",
        ]
        if entry.get("unicode_range"):
            rule.append(f"  unicode-range: {entry['unicode_range']};")
        rule.append("}")
        rules.append("\n".join(rule))
    return "\n".join(rules) if rules else None


FONT_LINK_FALLBACK = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    f'<link rel="stylesheet" href="{FONT_CSS_URL}">'
)


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
{fonts}
<style>
{css}
</style>
</head>
<body>
<div class="resume">
{body}
</div>
</body>
</html>
"""


def render_html(
    md_text: str,
    css: str,
    title: str | None = None,
    fonts: str | None = None,
    density: str = "normal",
) -> str:
    md_text = LETTER_DIGIT_APOSTROPHE.sub("’", md_text)
    md_text = PAGE_BREAK_COMMENT.sub('<div class="page-break"></div>', md_text)

    converter = markdown.Markdown(extensions=MD_EXTENSIONS + [ResumeExtension()])
    body = converter.convert(md_text)

    if title is None:
        match = re.search(r'<h1 class="name">(.*?)</h1>', body, re.S)
        name = re.sub(r"<[^>]+>", "", match.group(1)).strip() if match else "Resume"
        title = f"{name} — Resume"

    if fonts is None:
        fonts = FONT_LINK_FALLBACK

    css = css.strip()
    if density != "normal":
        size, lead = DENSITIES[density]
        css += (
            f"\n\n/* density: {density} */\n"
            f":root {{ --base-size: {size}; --lead: {lead}; }}"
        )

    return HTML_TEMPLATE.format(title=title, css=css, body=body, fonts=fonts)


def resolve_fonts(embed: bool, quiet: bool = False) -> str:
    """Return the <head> font block: embedded @font-face, or the CDN link."""
    if not embed:
        return FONT_LINK_FALLBACK

    rules = embedded_font_css()
    if rules is None:
        if not quiet:
            print("fonts not vendored yet; fetching once into render/fonts/")
        if fetch_fonts(quiet=quiet):
            rules = embedded_font_css()
    if rules is None:
        print(
            "  ! falling back to the Google Fonts CDN -- printing may use Arial if\n"
            "    the fonts do not load in time. Run --fetch-fonts when online.",
            file=sys.stderr,
        )
        return FONT_LINK_FALLBACK
    return f"<style>\n{rules}\n</style>"


def pdf_page_count(path: str) -> int | None:
    try:
        with open(path, "rb") as handle:
            data = handle.read()
    except OSError:
        return None
    count = len(re.findall(rb"/Type\s*/Page(?!s)", data))
    if count:
        return count
    tree_count = re.search(rb"/Count\s+(\d+)", data)
    return int(tree_count.group(1)) if tree_count else None


def find_chrome() -> str | None:
    for name in (
        "google-chrome",
        "google-chrome-stable",
        "chromium",
        "chromium-browser",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    ):
        found = shutil.which(name) or (name if os.path.exists(name) else None)
        if found:
            return found
    return None


def html_to_pdf(html_path: str, pdf_path: str) -> bool:
    chrome = find_chrome()
    if not chrome:
        print("  ! no Chrome/Chromium found; skipping PDF", file=sys.stderr)
        return False

    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--no-pdf-header-footer",
        "--virtual-time-budget=6000",  # let the webfonts load before printing
        f"--print-to-pdf={pdf_path}",
        f"file://{os.path.abspath(html_path)}",
    ]
    if hasattr(os, "geteuid") and os.geteuid() == 0:
        cmd.insert(1, "--no-sandbox")

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if result.returncode != 0 or not os.path.exists(pdf_path):
        print(f"  ! chrome failed: {result.stderr.strip()[:400]}", file=sys.stderr)
        return False
    return True


def display_path(path: str) -> str:
    """Repo-relative path when the file lives in the repo, else absolute."""
    relative = os.path.relpath(os.path.abspath(path), ROOT)
    return os.path.abspath(path) if relative.startswith("..") else relative


def collect_inputs(paths: list[str], use_all: bool) -> list[str]:
    if use_all:
        found = sorted(glob.glob(os.path.join(ROOT, "variants", "*.md")))
        found += sorted(glob.glob(os.path.join(ROOT, "tailored", "*.md")))
        return found
    return paths


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render resume Markdown into printable HTML (and optional PDF).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="examples:\n"
        "  python3 render/render.py variants/variant-A.md --pdf\n"
        "  python3 render/render.py --all --pdf\n",
    )
    parser.add_argument("paths", nargs="*", help="Markdown files to render")
    parser.add_argument(
        "--all",
        action="store_true",
        help="render every variants/*.md and tailored/*.md",
    )
    parser.add_argument("-o", "--output", help="output HTML path (single input only)")
    parser.add_argument(
        "--outdir", default=DEFAULT_OUTDIR, help=f"output directory (default: {DEFAULT_OUTDIR})"
    )
    parser.add_argument("--pdf", action="store_true", help="also render a PDF via headless Chrome")
    parser.add_argument(
        "--density",
        choices=list(DENSITIES),
        default="normal",
        help="type density (default: normal)",
    )
    parser.add_argument(
        "--fit",
        nargs="?",
        type=int,
        const=2,
        metavar="PAGES",
        help="tighten density until the PDF fits PAGES pages (default 2);"
        " implies --pdf and never changes content",
    )
    parser.add_argument("--css", default=DEFAULT_CSS, help=f"stylesheet (default: {DEFAULT_CSS})")
    parser.add_argument("--title", help="override the HTML <title>")
    parser.add_argument(
        "--fetch-fonts",
        action="store_true",
        help="(re)download the vendored webfonts into render/fonts/ and exit",
    )
    parser.add_argument(
        "--link-fonts",
        action="store_true",
        help="link the Google Fonts CDN instead of embedding fonts (smaller HTML,"
        " but needs network at print time)",
    )
    args = parser.parse_args()

    if args.fetch_fonts:
        return 0 if fetch_fonts() else 1

    inputs = collect_inputs(args.paths, args.all)
    if not inputs:
        parser.error("no input files (pass Markdown paths or --all)")
    if args.output and len(inputs) > 1:
        parser.error("-o/--output takes a single input file")

    with open(args.css, encoding="utf-8") as handle:
        css = handle.read()

    fonts = resolve_fonts(embed=not args.link_fonts)
    want_pdf = args.pdf or args.fit is not None
    target_pages = args.fit if args.fit is not None else 2
    attempts = FIT_ORDER if args.fit is not None else [args.density]

    exit_code = 0
    for path in inputs:
        if not os.path.exists(path):
            print(f"! missing: {path}", file=sys.stderr)
            exit_code = 1
            continue

        with open(path, encoding="utf-8") as handle:
            md_text = handle.read()

        if args.output:
            html_path = args.output
        else:
            stem = os.path.splitext(os.path.basename(path))[0]
            html_path = os.path.join(args.outdir, f"{stem}.html")
        os.makedirs(os.path.dirname(os.path.abspath(html_path)), exist_ok=True)
        pdf_path = os.path.splitext(html_path)[0] + ".pdf"

        print(f"{path} -> {display_path(html_path)}")

        for index, density in enumerate(attempts):
            html = render_html(md_text, css, args.title, fonts, density)
            with open(html_path, "w", encoding="utf-8") as handle:
                handle.write(html)

            if density != "normal":
                size, lead = DENSITIES[density]
                print(f"  density: {density} ({size}/{lead})")

            if not want_pdf:
                break

            if not html_to_pdf(html_path, pdf_path):
                exit_code = 1
                break

            pages = pdf_page_count(pdf_path)
            last_attempt = index == len(attempts) - 1
            if args.fit is not None and pages and pages > target_pages and not last_attempt:
                continue  # retry tighter

            label = f"{pages} page{'' if pages == 1 else 's'}" if pages else "page count unknown"
            over = pages is not None and pages > target_pages
            flag = f"  <- over the {target_pages}-page target (CONTEXT.md §3)" if over else ""
            print(f"  -> {display_path(pdf_path)} ({label}){flag}")
            break

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
