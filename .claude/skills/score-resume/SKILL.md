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
| 4 | Does each role block carry mechanism *and* measured outcome across its bullets — at least one measured outcome per role, every outcome attributable, and no pure-activity bullets? | No |
| 5 | Is scope legible — team size, org context, system scale, dollars? | No |
| 6 | Is technical currency obvious from the last two years? | No |
| 7 | Does the resume mirror the JD's exact vocabulary for its required skills? | Yes |

Notes on specific items:
- **Item 2:** check that the summary closes with the credential sentence (CONTEXT.md §1, "PhD
  visibility") and that CONTEXT.md §3's anti-stacking rule holds — no post-nominals, no
  credential in the contact line. A missing or misplaced credential sentence is a **non-blocking
  improvement**; stacking or post-nominals is a real defect worth scoring down.
- **Item 1:** extract the JD's required/preferred skills and check literal presence
  (accounting for the JD's own term variants). List every required skill that is missing.
- **Item 4:** the unit of judgment is the **role block, not the individual bullet.** CONTEXT.md
  §3's formula (action → mechanism → measured outcome) describes what a role's bullets must
  deliver *between them*, not a quota every line has to hit on its own. A bullet legitimately
  carries no outcome when:
  - the outcome for that work is stated in a sibling bullet in the same role — a mechanism
    bullet sitting next to the bullet that carries the number (feed optimization alongside
    "+10% GMV") is one claim split across two lines, not a defect;
  - it is a team or scope bullet whose scope *is* the outcome (headcount, composition, level);
  - its value is the mechanism itself — mechanism earns technical credibility (CONTEXT.md §2A),
    and on a manager's resume some bullets exist to prove depth, not impact.

  Score down only for:
  - a role block with **no measured outcome anywhere** — the whole block reads as a job
    description;
  - a bullet with **neither mechanism nor outcome** — an ownership or activity verb with nothing
    behind it ("Owned the technical and product roadmap"), which CONTEXT.md §3 bans outright;
  - an **unattributable outcome** — a number no bullet in the block explains the source of.

  Beyond those three, thin per-bullet outcome density is a **non-blocking improvement**, not a
  blocker. Quote what fails and name which of the three it is.
- **Item 6:** satisfied by recent experience bullets and recent publications together. Older
  publications are legitimate depth evidence and do not *lower* this score; the check is
  whether recent evidence exists, not whether old evidence is present.

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
