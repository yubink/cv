---
name: score-resume
description: Score a resume draft against the system scorecard. Works on base variants (no JD) or tailored copies (with JD). Use when the user asks to evaluate, review, or grade a resume — and as the final step of `build-variant` and `tailor-to-jd`.
---

## Required inputs

| Input | Source | If missing |
|---|---|---|
| `CONTEXT.md` | ${CLAUDE_PROJECT_DIR} | Stop. Ask the user for it. |
| The resume to score | User, or a `variants/` / `tailored/` file | Ask. |
| The JD | User | **Optional.** Without it, JD-dependent items are scored N/A and the result is a base-variant score. |
| Target archetype | Infer from the file, or ask | Needed for budget and section-order checks. If it can't be inferred, ask. |

## Scoring

Grade each item 1–5. **Any item below 4 is a blocker.** N/A items are excluded, not
averaged in.

| # | Item | Needs JD? |
|---|---|---|
| 1 | Would an ATS keyword filter pass this against the JD? | Yes |
| 2 | Can a recruiter identify the target level in under 30 seconds? | No |
| 3 | Does the top third of page 1 answer "why this person for this job"? (Without a JD: "why this person for this *archetype*") | No |
| 4 | Does every bullet have a mechanism *and* an outcome? | No |
| 5 | Is scope legible — team size, org context, system scale, dollars? | No |
| 6 | Is technical currency obvious from the last two years? | No |
| 7 | Does the scope story read as progression rather than a title zigzag? | No |
| 8 | Is it parseable as plain text — single column, standard headings, no layout tables? | No |
| 9 | Does every Skills entry trace to a surviving bullet, publication, or named project, and does every tool named in a bullet appear in Skills? (CONTEXT.md §4, both directions; foundational tier exempt) | No |
| 10 | Are the publication list and academic record within the archetype's budgets (CONTEXT.md §2), accurately labeled (venue tiers correct; co-organized workshops rendered as service with the organizing role explicit, never as publications), and closed with a Scholar link if the publication list is truncated? | No |
| 11 | Does the resume mirror the JD's exact vocabulary for its required skills? | Yes |
| 12 | Are the archetype's section order and foreground/compress rules followed? | No |

Notes on specific items:
- **Item 1:** extract the JD's required/preferred skills and check literal presence
  (accounting for the JD's own term variants). List every required skill that is missing.
- **Item 4:** quote each failing bullet and name what's missing (mechanism, outcome, or both).
- **Item 6:** satisfied by recent experience bullets and recent publications together. Older
  publications are legitimate depth evidence and do not *lower* this score; the check is
  whether recent evidence exists, not whether old evidence is present.
- **Item 9:** produce the orphan list explicitly — skill → evidence found or none.
- **Item 10:** venue-tier accuracy means workshop papers read as workshop papers; verify
  against `publication-library.yaml` `venue_tier` if the library is available. Any entry from
  `academic-record.yaml` `workshops:` appearing under a Publications heading, or without its
  organizing role stated, is an automatic blocker on this item — it mislabels service as
  publication output.

## Output

A scorecard table: item, score (or N/A), one-line justification. Then:

1. **Blockers** — every item below 4, with the specific failing content quoted and a concrete
   fix. Fixes must respect the no-invention rule: if the fix needs a fact or number that
   isn't in the resume or libraries, say so — it is an evidence gap for the user, not
   something to write in.
2. **Non-blocking improvements** — briefly.
3. **Verdict** — pass (no blockers) or fail (list of blockers), and if a JD was provided, a
   one-line judgment: would you advise submitting this to this posting as-is?

## Exit conditions

- CONTEXT.md or the resume missing → report and stop.
- Archetype not inferable and not provided → ask.
- This skill **only reports.** It never edits the resume; fixes are applied by the user, or
  by `build-variant` / `tailor-to-jd` on request.
