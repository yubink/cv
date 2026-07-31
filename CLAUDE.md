# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is not a software project — it is a **structured resume-authoring system** for one candidate (Yubin Kim). Content is data (YAML libraries + Markdown), and the "programs" are the three Claude Code skills in `.claude/skills/`. The governing principle is **never invent facts, metrics, titles, or technologies**; every claim on a generated resume must trace to `CONTEXT.md` or a library and be defensible in a live interview. When a needed fact is missing, ask the candidate — do not fabricate or guess.

## Source-of-truth hierarchy

Read in this order; when they conflict, the earlier one wins:

1. **`CONTEXT.md`** — durable facts and rules: candidate identity, career spine, the three archetypes (§2), global resume rules (§3), skills↔evidence traceability (§4), and library schemas (§5). This is the authority. Skills contain *procedures*; `CONTEXT.md` contains *facts*.
2. **The libraries** (complete inventories; resumes show selected subsets):
   - `bullet-library.yaml` — every experience bullet, tagged with `role`, `skills[]`, `archetypes[]`, `domain`, `evidence_strength`. Bullets marked `evidence_strength: weak` contain bracketed placeholders (e.g. `[X]%`) keyed to open questions in `TODO.md §3` — treat placeholders as gaps to fill from the candidate, never invent the number.
   - `publication-library.yaml` — full publication record. `venue_tier` is authoritative; never inflate a workshop paper into a conference paper.
   - `academic-record.yaml` — co-organized `workshops:` (these are **service, never publications**), `service:`, and `talks:`.
3. **`TODO.md`** — point-in-time state: build order, open evidence questions, migration notes. Not a source of durable rules. Delete items as they resolve.

Outputs (`variants/variant-{A,B,C}.md` and `tailored/{slug}.md`) do not exist yet — the base variants have not been built. See `TODO.md §1` for build order (B, then A, then C).

## The three archetypes (A/B/C)

Every skill routes through one of these; full specs in `CONTEXT.md §2`:
- **A** — player-coach product-ML manager (Sr. EM / Manager of Applied Science with direct IC reports).
- **B** — strategic senior IC (Principal Applied Scientist / ML-direction Principal Engineer). Apply the Principal Engineer discriminator in §2B to reject systems/infra PE roles.
- **C** — startup AI exec (0→1 Head of AI / Chief Scientist).

Each archetype dictates section order, foreground/compress guidance, and publication/academic-service budgets.

## The three skills (`.claude/skills/`)

- **`build-variant`** — creates or edits a base variant from the libraries for a given archetype. Ask for the archetype; never guess. Ends by running `score-resume` without a JD.
- **`tailor-to-jd`** — classifies a job description to an archetype, then produces a tailored *copy* of that base variant. Tailoring is **subtraction, reordering, and rewording only** — never invention, never a fact change. Requires the base variant to already exist; do not improvise one from the libraries.
- **`score-resume`** — grades a draft against a 12-item scorecard (`CONTEXT.md`-derived). Any item below 4 is a blocker. This skill **only reports**; it never edits.

The `.zip` files alongside each skill directory are packaged copies for distribution — the live, editable versions are the unpacked `SKILL.md` files.

## Editing conventions

- **Fixing a bad bullet:** correct it **in `bullet-library.yaml`**, not just in a generated variant. The library is the source of truth; variants are derived.
- **After changing any `skills[]` field** in a bullet or publication, regenerate the evidence matrix:
  ```
  python3 gen_matrix.py
  ```
  Run from the repo root. It rewrites the `# ---- GENERATED: skills_evidence_matrix` block at the bottom of `bullet-library.yaml` (do not hand-edit that block) and prints publication-only skills. (Note: `TODO.md` refers to `scripts/gen_matrix.py` from a "resume-system root" — that path is stale; the script lives at the repo root.)
- **Traceability rule (`CONTEXT.md §4`), enforced in both directions on every variant:** no orphan skills (every Skills entry traces to a surviving bullet, publication, or named project) and no unlisted tools (every tool named in a bullet appears in Skills). The "pruning corollary": when tailoring cuts the last bullet evidencing a skill, that skill must also leave the Skills section. Foundational tier (Python, Java, C++, SQL, git, Jupyter) is exempt.
- **Bullet formula:** action → mechanism → measured outcome, with a budget of 1–3 named technologies per bullet.
- **ATS constraint:** variant files are the plain, single-column, ATS-safe versions (no multi-column layouts, floated sidebars, or tables-for-layout). A designed PDF for humans is a separate downstream rendering step.

## Legacy files (being retired)

`prettycv.html`, `cv.html`, the dated PDFs, `YubinKim.ps`, and the Google Scholar HTML export are legacy source material. Content is being migrated into the libraries; see `TODO.md §2` and §4. Do not treat these as authoritative once a fact has been captured in a library. `resume-system/` is a stale empty directory.
