---
name: tailor-to-jd
description: Take a job description, classify it to archetype A, B, or C, then produce a tailored copy of that archetype's base variant aligned to the JD — reordered bullets, JD-matched wording, pruned skills. Use when the user provides a specific job posting. Do NOT use to build or restructure a base variant — that is `build-variant`.
---

## Required inputs

| Input | Source | If missing |
|---|---|---|
| `CONTEXT.md` | ${CLAUDE_PROJECT_DIR} | Stop. Ask the user for it. |
| The JD | User | Ask for the full text, not a link summary. |
| Base variant for the matched archetype | `variants/variant-{X}.md` | **Stop. Report: "The base variant for archetype {X} does not exist yet — run build-variant first." Do not improvise a variant from the libraries.** |
| `bullet-library.yaml` | ${CLAUDE_PROJECT_DIR} | Optional but recommended — enables bullet *swaps*. Without it, tailoring is limited to reordering, rewording, and subtraction of what's already in the variant. Note the limitation in the output. |
| `academic-record.yaml` | ${CLAUDE_PROJECT_DIR} | Optional — enables talk swaps by `topic_tags` and workshop/service adjustments. Without it, the base variant's academic content is kept as-is. |

## Preconditions

1. Read `CONTEXT.md` in full.
2. Tailoring is **subtraction, reordering, and rewording only** — never invention. A
   JD-matched rewording must preserve the factual content of the original bullet exactly.
   Wording changes adjust vocabulary, not claims.

## Procedure

### 1. Triage the JD to an archetype

Classify by signal, in priority order:

- JD says **"direct reports," "manage a team of N," "hiring," "performance"** and names a
  product surface → **A**.
- JD says **"Principal," "Staff+," "Distinguished," "technical strategy," "influence without
  authority," "applied research,"** or lists publications as a plus → **B**, regardless of
  whether the title says Scientist or Engineer. Apply the Principal Engineer discriminator in
  CONTEXT.md §2B to confirm it is the ML-direction flavor.
- JD is at a **Series B–D company** and says **"first," "build the team," "0→1," "define the
  AI strategy," "Head of AI"** → **C**.

**Skip signals** — recommend not applying, with the reason, and stop:
- "Director" managing managers, not ICs.
- Platform/infra ML with no product KPI, regardless of level.
- Principal/Distinguished Engineer whose scope is core systems or infra rather than ML
  direction (fails the CONTEXT.md §2B discriminator).
- Research scientist with a publication mandate (conflicts with the ~1 paper/year preference).
- Sr. EM below the comp floor, unless the brand materially improves the next hop — flag for
  the user to decide.

**Edge cases:**
- "Director" with direct ICs at a small org → A.
- Startup exec role that is really a hands-on-only founding engineer → C, but flag the level
  mismatch to the user.
- Both a PAS and a PE posting open at the same company for overlapping scope → recommend the
  PAS posting.
- Genuinely ambiguous between two archetypes → present both readings and ask; do not guess.

State the classification and the signals that drove it before proceeding.

### 2. Extract the JD's demand profile
- Required skills, preferred skills, and responsibilities — **in the JD's own vocabulary**.
- Note exact term variants ("recommender systems" vs "recsys"; "LLM" vs "GenAI"; "experiment"
  vs "A/B test"). The tailored resume mirrors the JD's variants.
- Note the JD's domain (e-commerce, healthcare, other) for bullet reordering via the
  `domain` field.
- Flag JD demands the candidate has **no evidence for**. These go on an interview-prep list
  in the output — never onto the resume.

### 3. Tailor the base variant
Working on a **copy** of `variants/variant-{X}.md` — never modify the base:

1. **Reorder** bullets so those evidencing the JD's highest-priority skills lead each role.
   If the JD is domain-specific, promote matching-`domain` bullets.
2. **Reword** for keyword alignment: swap synonyms to the JD's exact terms in bullets, the
   summary, and Skills. Facts, numbers, and claims stay identical.
3. **Swap** (only if `bullet-library.yaml` is available): replace a weakly matching bullet
   with a stronger library bullet for the same role and archetype, respecting the tool
   budget (1–3 named technologies per bullet).
4. **Subtract** bullets irrelevant to this JD if space is tight — foregrounded role stays
   dominant, compressed roles can shrink to a single line.
5. **Retune the summary** — one or two sentences of the archetype thesis rephrased toward
   this JD's language. No new claims.
6. **Adjust publications within the archetype's budget** (CONTEXT.md §2): swap entries so the
   most JD-relevant papers occupy the slots, applying the publication rules in CONTEXT.md §3.
   Do not exceed the budget because the JD is academic-flavored; that is an archetype-B
   signal that should have been caught in triage.
7. **Adjust the academic record within the archetype's budget** (only if
   `academic-record.yaml` is available): swap talk slots toward entries whose `topic_tags`
   overlap the JD's domain and keywords; a panel or judge entry may take a slot when the JD
   is community- or communication-flavored. If the JD emphasizes cross-team collaboration or
   community leadership, ensure the co-organized workshop lines are present (within budget)
   — they are direct evidence. All rendering rules in CONTEXT.md §3 apply, including
   workshops-are-never-publications.
8. **Prune the Skills section** to what survived (the pruning corollary, CONTEXT.md §4), then
   verify traceability in both directions.

### 4. Score before presenting
Run the `score-resume` skill on the tailored copy **with the JD**. Fix any blocker before
showing the user.

## Output

- The tailored resume as a new file: `tailored/{company-or-role-slug}.md`. The base variant
  is untouched.
- A change log: classification and reasoning; reorderings; rewordings (old term → JD term);
  swaps, subtractions, and publication changes with one-line rationale.
- The interview-prep list: JD demands with no resume evidence.
- The scorecard result.

## Exit conditions

- Base variant missing → report and stop (see inputs table). Do not build one ad hoc.
- JD matches a skip signal → report the reason and stop.
- Classification ambiguous → ask.
- JD text not provided or too fragmentary to extract a demand profile → ask for the full text.
