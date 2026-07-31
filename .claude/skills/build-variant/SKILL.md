---
name: build-variant
description: Create or edit one of the three base resume variants (A: player-coach product-ML manager; B: strategic senior IC; C: startup AI exec) from the master bullet library and publication library. Use when the user asks to build, rebuild, restructure, or substantively edit a base variant. Do NOT use for tailoring a resume to a specific job posting — that is `tailor-to-jd`.
---

## Required inputs

| Input | Source | If missing |
|---|---|---|
| `CONTEXT.md` | ${CLAUDE_PROJECT_DIR} | Stop. Ask the user for it. |
| `bullet-library.yaml` | ${CLAUDE_PROJECT_DIR} | Stop. Report that the library must be created first (schema in CONTEXT.md §5). |
| `publication-library.yaml` | ${CLAUDE_PROJECT_DIR} | Stop. Same as above. |
| `academic-record.yaml` | ${CLAUDE_PROJECT_DIR} | Stop. Same as above. |
| Target archetype (A, B, or C) | User | Ask. Never guess between archetypes. |
| Existing variant file, if editing | `variants/variant-{X}.md` | Only needed for edits; absence means this is a fresh build. |

## Preconditions

1. Read `CONTEXT.md` in full. §2 defines the archetype being built; §3–§4 constrain every
   line of output.
2. Confirm with the user whether this is a fresh build or an edit of the existing variant.
3. **Never invent content.** Every bullet comes from `bullet-library.yaml`; every publication
   from `publication-library.yaml`; every fact from `CONTEXT.md`. If something needed is in
   none of them, ask the user, and record the answer as a proposed library addition rather
   than writing it directly into the variant only.

## Procedure

### 1. Frame
- Load the archetype spec from CONTEXT.md §2: thesis, foreground/compress guidance, section
  order, keyword emphasis, publication and academic-service budgets.
- The variant's summary section is the archetype thesis, rendered in the candidate's voice —
  not copied verbatim.

### 2. Select bullets
- Filter `bullet-library.yaml` to entries whose `archetypes[]` includes the target.
- Within each role, order by the archetype's foreground guidance, preferring
  `evidence_strength: strong`.
- Respect the foreground/compress split: the foregrounded role gets the most bullets and
  page-one position; compressed roles get 1–3 lines each.
- Every selected bullet must satisfy the formula (action → mechanism → outcome) and the tool
  budget (1–3 named technologies). If a library bullet fails these, fix it **in the library**,
  not just in the variant — the library is the source of truth.

### 3. Select publications
Run in order; stop when the archetype's budget (CONTEXT.md §2) is full:

1. **Reserve traceability slots.** Any publication that is the *sole* evidence for a skill
   being kept in the Skills section is required. A publication is valid evidence regardless
   of its age.
2. **Anchor with the strongest recent peer-reviewed venue** (highest `venue_tier`, most
   recent). This slot is non-negotiable in all three archetypes.
3. **Prioritize double-duty papers** — those whose `work_origin` matches the foregrounded
   role. They corroborate the employment claim and evidence the skill simultaneously.
4. **Rank the remainder** by relevance to the archetype's keyword emphasis. Where two papers
   tie, prefer the more applied one — in all three archetypes, including B.
5. **Tie-break:** venue tier → recency → first authorship (all read from `citation`).
6. **Truncate and link.** If the list is a subset, close with the "Full list on Google
   Scholar" line.

Apply the publication rules from CONTEXT.md §3 throughout (venue-tier accuracy, under-review
handling, name bolding, etc.).

### 4. Select from the academic record
From `academic-record.yaml`, per the archetype's academic record budget (CONTEXT.md §2) and
the academic record rules (CONTEXT.md §3):

- **Workshops (co-organized):** compact one-line-per-workshop format with year ranges,
  rendered with the organizing role explicit ("Co-organizer, {name} @ {host}, {years}").
  Placement: archetype A — within the brief academic block (they evidence
  leadership and collaboration-building, the archetype's core claim); archetype B — a
  compact block within Academic Service; archetype C — merged into the single combined line,
  if at all. **Never inside a Publications section.**
- **Service:** rank chair/organizer roles above standing reviewer roles, then by recency.
  Fill the archetype's budget.
- **Talks:** rank keynote > invited-talk > panel > judge, then recency. Archetype C gets a
  dedicated "Selected Talks & Speaking" section (3–5 entries, keynotes first); archetype B
  gets 2–3 lines folded into Academic Service; archetype A omits, or one line if warranted.
  Panel and judge entries earn a slot only when space is cheap.

### 5. Build the Skills section
- Candidate skills = union of `skills[]` across the bullets and publications that survived
  steps 2–3, plus the foundational tier (CONTEXT.md §4).
- **Prune:** any skill whose only evidence was cut in selection comes out.
- **Verify both directions** (CONTEXT.md §4): every Skills entry traces to a surviving
  bullet, publication, or named project; every technology named in a surviving bullet
  appears in Skills.

### 6. Assemble
- Section order per the archetype spec.
- Header: name, email, phone, location + remote posture, Scholar link where the archetype
  warrants it.
- Single-column, ATS-safe structure (CONTEXT.md §3). The designed-PDF rendering is a separate
  downstream step; the variant file itself is the plain, parseable version.
- Include the remote-leadership evidence — required in every variant (CONTEXT.md §1).

### 7. Score before presenting
- Run the `score-resume` skill on the draft **without a JD** (base variants are
  JD-independent). Fix any blocker (any item below 4) before showing the user.

## Output

- Write to `variants/variant-{A|B|C}.md`. If editing, show the user a summary of what
  changed and why before overwriting.
- Report: bullets selected per role, publications selected with one-line rationale each,
  skills pruned (and why), and the scorecard result.
- If any library entry was flagged as weak or fixed during the build, list the proposed
  library edits separately for the user to approve.

## Exit conditions

- Missing library or CONTEXT.md → report which file is missing and stop.
- Archetype ambiguous → ask; do not guess.
- A required fact is in no library → ask the user; do not fabricate.
