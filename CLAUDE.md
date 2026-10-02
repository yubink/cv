# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is not a software project — it is a **structured resume-authoring system** for one candidate (Yubin Kim). Content is data (YAML libraries + Markdown), and the "programs" are the three Claude Code skills in `.claude/skills/`. The governing principle is **never invent facts, metrics, titles, or technologies**; every claim on a generated resume must trace to `CONTEXT.md` or a library and be defensible in a live interview. When a needed fact is missing, ask the candidate — do not fabricate or guess.

## Source-of-truth hierarchy

Read in this order; when they conflict, the earlier one wins:

1. **`CONTEXT.md`** — durable facts and rules: candidate identity, education, the three archetypes (§2), global resume rules (§3), skills↔evidence traceability (§4), and library schemas (§5). This is the authority. Skills contain *procedures*; `CONTEXT.md` contains *facts* — except the career spine, which lives in `bullet-library.yaml` (§1 points there and keeps only the rules for rendering it).
2. **The libraries** (complete inventories; resumes show selected subsets):
   - `bullet-library.yaml` — **the full career-experience record**: the career spine (`tenure`, `roles` with `title`/`org`/`dates`/`context`/`team`/`management`, `internships`) plus every experience bullet nested under its role's `bullets:` list, and `cross-role` for bullets spanning roles. Each bullet carries `skills[]` and `archetypes[]` and nothing else. Domain lives in `skills[]` as `e-commerce` / `healthcare`. Role headings, dates, and scope lines on a variant come from the role fields — never retype them from memory. Bullets with an open evidence gap carry a `# TODO` comment as their last line, usually alongside a bracketed placeholder in the text (e.g. `[X]%`) keyed to `TODO.md §3` — treat placeholders as gaps to fill from the candidate, never invent the number, and prefer TODO-free bullets when selecting.
   - `publication-library.yaml` — full publication record. `venue_tier` is authoritative; never inflate a workshop paper into a conference paper.
   - `academic-record.yaml` — co-organized `workshops:` (these are **service, never publications**), `service:`, and `talks:`.
   - `skills-evidence-matrix.yaml` — **generated** (do not hand-edit): one row per skill listing the bullet and publication IDs that evidence it. Regenerate with `python3 gen_matrix.py`.
3. **`TODO.md`** — point-in-time state: build order, open evidence questions, migration notes. Not a source of durable rules. Delete items as they resolve.

`variants/variant-A.md` and `variants/variant-B.md` exist; **`variants/variant-C.md` is currently missing** (deleted in commit 994926b) and must be rebuilt with `build-variant` before any C tailoring — `/tailor-to-jd C` fails without it. `tailored/{slug}.md` copies are produced per job posting by `tailor-to-jd`. See `TODO.md §1` for current state and next steps.

## The three archetypes (A/B/C)

Every skill routes through one of these; full specs in `CONTEXT.md §2`:
- **A** — applied-science / product-ML manager (Manager of Applied Science / Sr. EM with direct IC reports, accountable for the team's shipped outcomes).
- **B** — strategic senior IC (Staff or Principal Applied Scientist / ML Engineer, ML-direction Principal Engineer). §2B was rewritten 2026-08-19 from the candidate's own account of the role they want (`archetype-B.txt`), and three of its rules bind every B build and every B tailoring:
  - **The narrative rule** — Director → Sr. EM → CSO → Staff/Principal IC is a move toward leverage, never a retreat from leadership. Both halves stay on the page at once: accumulated leadership scope *and* a live personal technical practice. No objective statement, no transition framing, no "returning to hands-on work," nothing apologetic. Cutting leadership evidence to look more like an IC is the failure mode this archetype is most prone to.
  - **Hands-on work is a named bullet here, not a clause** — the opposite of archetype A. At least one per recent role where the evidence exists.
  - **Two screening tables in §2B, both applied** — the **job-design test** (does the posting hand over a problem space, autonomy over approach, a voice in the roadmap, and mentorship expectations, or is it a Staff-titled implementation job?) on every posting, and the **Principal Engineer discriminator** on engineering-ladder postings, to reject systems/infra PE roles.
- **C** — startup AI exec (0→1 Head of AI / Chief Scientist).

Each archetype dictates section order, foreground/compress guidance, and publication/academic-service budgets.

## The three skills (`.claude/skills/`)

- **`build-variant`** — creates or edits a base variant from the libraries for a given archetype. Ask for the archetype; never guess. Ends by running `score-resume` without a JD.
- **`tailor-to-jd`** — produces a tailored *copy* of a base variant for one job description **or a set of them**. The variant can be named explicitly (`/tailor-to-jd B`, or a path like `/tailor-to-jd variants/variant-C.md`); without one, the skill classifies the JD(s) to an archetype itself. An explicit choice wins — triage still runs, but only reports a mismatch or skip signal as a caution. Tailoring is **subtraction, reordering, and rewording only** — never invention, never a fact change. Requires the base variant to already exist; do not improvise one from the libraries.
  - **Multi-JD** (`/tailor-to-jd B jds/a.txt jds/b.txt`) produces **one** resume covering the whole set, not a file per posting. Demands are merged into **core** (asked by 2+ JDs — these drive the summary and lead each role block) and **distinct** (one JD only — each gets at least one bullet, never lead position); clashing vocabulary picks one primary form for the prose and carries both variants in Skills. Multiple JDs never relax the two-page default, the archetype budgets, or the no-orphan-skills rule. With no variant named, all the JDs must triage to the same archetype — a clash stops the skill and asks.
- **`score-resume`** — grades a draft against a 7-item scorecard (`CONTEXT.md`-derived). Any item below 4 is a blocker. Accepts a JD set: the JD-dependent items (1 and 7) are scored per JD and the **worst** score governs. This skill **only reports**; it never edits.

The `.zip` files alongside each skill directory are packaged copies for distribution — the live, editable versions are the unpacked `SKILL.md` files. **The zips are stale** (packaged 2026-07-30, before several `SKILL.md` edits); repackage before distributing, and never read them as the current procedure.

## Editing conventions

- **Fixing a bad bullet:** correct it **in `bullet-library.yaml`**, not just in a generated variant. The library is the source of truth; variants are derived.
- **After changing any `skills[]` field** in a bullet or publication, regenerate the evidence matrix:
  ```
  python3 gen_matrix.py
  ```
  Run from the repo root. It reads `bullet-library.yaml` + `publication-library.yaml`, writes the generated `skills-evidence-matrix.yaml`, and prints the skill/bullet/pub counts and the publication-only skills.
- **Traceability rule (`CONTEXT.md §4`), enforced in both directions on every variant:** no orphan skills (every Skills entry traces to a surviving bullet, publication, or named project) and no unlisted tools (every tool named in a bullet appears in Skills). The "pruning corollary": when tailoring cuts the last bullet evidencing a skill, that skill must also leave the Skills section. Foundational tier (Python, Java, C++, SQL, git, Jupyter) is exempt.
- **Bullet formula:** action → mechanism → measured outcome, with a budget of 1–3 named technologies per bullet.
- **Bullets render verbatim from the libraries.** A build copies the `bullet:` text as-is; rewording is `tailor-to-jd`'s job, and even there facts and numbers never change. Drifting a word during a build silently forks the source of truth. Worth a mechanical check after any build: every bullet on the page should string-match its library entry. **Citations are the one exception** — they render in the condensed form defined in `CONTEXT.md §3` (venue short form, no "In Proceedings of the Nth …", no volume/pages), which drops presentation only: the venue-tier words and every fact stay.
- **Archetype-specific phrasing uses one of exactly two mechanisms** (`CONTEXT.md §5`), and picking the wrong one is how this library forks:
  - *Emphasis marker* — same composition, a word of difference. Bullet text in the library is **always neutral about who did the work** (no "Personally", no "hands-on"); that fact lives in `skills[]` as the `hands-on-ml` tag, and archetypes B/C add the marker at render time while A renders neutral. No second entry.
  - *Alternate framing* — different composition (different lead clause, two bullets merged, mechanics dropped). That gets its own `id` and `archetypes[]`, plus a comment naming the sibling(s) it must **never render beside**. Current sets: `xrole-ic-growth` (B) vs `xrole-promos-calibration` (A); `upmc-ml-applied-lead` (B) vs `upmc-ml-applications` + `upmc-ml-team` (A).
  
  If a variant's bullet text matches no library entry under either mechanism, the variant is wrong or the library is missing an entry — never leave the fork in place.
- **ATS constraint:** variant files are the plain, single-column, ATS-safe versions (no multi-column layouts, floated sidebars, or tables-for-layout). A designed PDF for humans is a separate downstream rendering step — see "Rendering" below.
- **Length:** two pages is the default for every variant and tailored copy (`CONTEXT.md §3`). Don't compress to one page or pad to fill; keep page one carrying the decision.

## Rendering (`render/`)

`render/render.py` turns any variant or tailored Markdown file into the designed, human-facing
artifact: a printable single-column HTML file and, optionally, a PDF via headless Chrome.

```
python3 render/render.py --all --fit          # every variants/*.md + tailored/*.md, HTML + PDF
python3 render/render.py variants/variant-A.md --pdf
python3 render/render.py tailored/acme.md --pdf -o build/acme.html
python3 render/render.py --fetch-fonts        # re-vendor the webfonts (needs network, one-time)
```

Outputs land in `build/` (git-ignored, regenerable). Visual language follows the legacy
`prettycv.html` — italic serif name, green small-caps section headings with a rule, right-floated
italic dates — but single-column rather than sidebar, so it prints reliably across a page break.

- **The Markdown stays the source of truth.** The renderer only re-presents it: it never adds,
  removes, reorders, or rewords content, and section order comes from the Markdown, so each
  archetype's ordering (`CONTEXT.md §2`) survives. Never fix resume content by editing the
  renderer or `render/resume.css` — fix `bullet-library.yaml`, then the variant.
- **Structure it recognizes**, all of it already idiomatic in the variants: `# Name` (masthead;
  the paragraph after it is the contact line, with emails/phones auto-linked), `## Section`,
  `### Title — Org — 04/2022–10/2023` (trailing date floats right, org is bolded), a `*single
  italic line*` under a role heading (muted scope line), `- bullets` (nesting supported), and a
  trailing `(Dec 2018)` on Education entries (floats right). `<!-- page-break -->` forces a break.
- **Length.** Every PDF render reports its page count against the two-page target
  (`CONTEXT.md §3`). `--fit` walks the type-density presets (`normal` → `compact` → `tight`) until
  the PDF fits, which is the content-safe way to close a short overflow — the alternative is
  cutting bullets, and that is a content decision, not a rendering one. `--density` sets one
  explicitly.
- **Fonts** are vendored in `render/fonts/` and embedded as base64 data URIs, so the HTML is
  self-contained and prints identically offline (see `render/fonts/README.md`). `--link-fonts`
  uses the Google Fonts CDN instead, which is smaller but can print with Arial substituted if the
  fonts don't load in time.
- **Dependencies:** the `markdown` package (required), `fontTools` (only for `--fetch-fonts`
  subsetting), and Chrome/Chromium (only for `--pdf`).

## Legacy files (being retired)

`prettycv.html`, `cv.html`, the dated PDFs, `YubinKim.ps`, and the Google Scholar HTML export are legacy source material. Content is being migrated into the libraries; see `TODO.md §2` and §4. Do not treat these as authoritative once a fact has been captured in a library. `resume-system/` is a stale empty directory.
