# Vendored fonts

Downloaded from Google Fonts by `python3 render/render.py --fetch-fonts` and subset to the
Latin ranges the resumes use (see `SUBSET_RANGES` in `render.py`). `render.py` embeds these as
base64 data URIs so a rendered HTML file is self-contained: it prints identically offline, and
headless Chrome can't print a page before a CDN font arrives (which silently substituted Arial
for body text before these were vendored).

Committed deliberately — the rendering should not depend on network access or on which fonts
happen to be installed on the machine doing the printing.

| Family | Faces | License |
| --- | --- | --- |
| Roboto | 400, 500, 700, 400 italic | Apache License 2.0 |
| Gentium Book Plus | 400 italic (the name in the masthead) | SIL Open Font License 1.1 |

Both licenses permit redistribution and subsetting. Re-run `--fetch-fonts` to refresh; delete
this directory to fall back to the Google Fonts CDN (`--link-fonts` does the same per render).
