---
name: tailor-to-jd
description: Take one or more job descriptions and produce a tailored copy of a base variant aligned to them — reordered bullets, JD-matched wording, pruned skills. With several JDs it produces one resume that hits every posting's notes, shared demands first. The user may name the variant to tailor (archetype letter A/B/C or a variant file path); if they don't, classify the JD(s) to an archetype first. Use when the user provides specific job postings. Do NOT use to build or restructure a base variant — that is `build-variant`.
---

## Required inputs

| Input | Source | If missing |
|---|---|---|
| `CONTEXT.md` | ${CLAUDE_PROJECT_DIR} | Stop. Ask the user for it. |
| **One or more JDs** | User — pasted text, or `jds/*.txt` paths | Ask for the full text, not a link summary. Any number is accepted; two or more trigger the multi-JD rules below. |
| **Variant selection (optional)** | User — skill argument or prompt | Absent means the skill picks the variant by triaging the JD(s) (step 1). |
| Base variant to tailor | `variants/variant-{X}.md`, or the user-supplied path | **Stop. Report: "The base variant {path} does not exist yet — run build-variant first." Do not improvise a variant from the libraries.** |
| `bullet-library.yaml` | ${CLAUDE_PROJECT_DIR} | Optional but recommended — enables bullet *swaps*. Without it, tailoring is limited to reordering, rewording, and subtraction of what's already in the variant. Note the limitation in the output. |
| `academic-record.yaml` | ${CLAUDE_PROJECT_DIR} | Optional — enables talk swaps by `topic_tags` and workshop/service adjustments. Without it, the base variant's academic content is kept as-is. |

## Preconditions

1. Read `CONTEXT.md` in full.
2. Tailoring is **subtraction, reordering, and rewording only** — never invention. A
   JD-matched rewording must preserve the factual content of the original bullet exactly.
   Wording changes adjust vocabulary, not claims.
3. **One JD or many, the product is a single resume.** Multiple JDs widen the demand profile
   the resume must answer; they do not relax any rule — two pages stays the default
   (CONTEXT.md §3), the archetype's budgets stay fixed, and page one still has to make one
   argument rather than list every keyword from every posting.

## Procedure

Steps 0–4 run once for the whole set, and produce one resume. Where a step says "per JD", do that
part once per posting and carry the results forward together.

### 0. Read the invocation

Arguments may name the variant, the JDs, both, or neither:

```
/tailor-to-jd B jds/reddit-ml-em-ads.txt jds/netflix-ml-em-ads.txt
/tailor-to-jd jds/spotify-mle-em-personalization.txt jds/duolingo-sr-ai-manager.txt
/tailor-to-jd variants/variant-A.md          # JDs pasted in the request
```

Disambiguate by shape, not by position: a bare `A`/`B`/`C` or a Markdown resume path
(`variants/`, `tailored/`, `*.md`) is the **variant**; anything under `jds/`, any `*.txt`, and any
JD text in the request body is a **JD**. Every JD given is in the set — never silently tailor to
just the first one. If the request mentions several postings but supplies text for only some, ask
for the missing text rather than working from the company name.

### 1. Establish which variant to tailor

**If the user specified one** — as a skill argument (`/tailor-to-jd B`, `/tailor-to-jd
variants/variant-C.md`), or anywhere in their request — that choice governs. Accept either form:

- A bare archetype letter `A`, `B`, or `C` → `variants/variant-{X}.md`.
- A path to a Markdown resume file → use that file as the base. It may be a `tailored/` copy or
  any other variant; treat it exactly as a base variant (read-only source, tailor a copy).
  Infer its archetype from its content and CONTEXT.md §2 for the budget rules in steps 3.6–3.7;
  if the archetype is unclear, ask rather than guessing which budgets apply.

With a specified variant, **skip triage as a decision** but still run the signal read below as a
**check** — once per JD — and report it:

- If a JD's signals point to a different archetype, say so in one line per JD —
  classification, signals, and the fact that you are proceeding with the user's choice anyway.
  Do not stop, and do not re-tailor toward the triaged archetype.
- If a JD matches a **skip signal**, report it as a caution, naming which JD, and proceed. An
  explicit variant choice is an explicit decision to apply; the skip signals inform it, they do
  not veto it.

**If the user did not specify one**, triage **each** JD independently and classify by signal, in
priority order:

- JD says **"direct reports," "manage a team of N," "hiring," "performance"** and names a
  product surface → **A**.
- JD says **"Staff," "Staff+," "Principal," "Distinguished," "technical strategy," "technical
  direction," "influence without authority," "applied research,"** or lists publications as a
  plus → **B**, regardless of whether the title says Scientist or Engineer. Then run the
  **job-design test** in CONTEXT.md §2B — the archetype is about what the role is given
  (a problem space, autonomy, a voice in the roadmap), not about the level in the title — and,
  on an engineering-ladder posting, the Principal Engineer discriminator to confirm it is the
  ML-direction flavor.
- JD is at a **Series B–D company** and says **"first," "build the team," "0→1," "define the
  AI strategy," "Head of AI"** → **C**.

**Archetype clash across JDs** — with several JDs and no variant specified, every JD must triage
to the **same** archetype. If they don't, **stop**: report each JD's classification and the
signals that drove it, and ask the user either to name the variant to tailor or to split the set
into per-archetype groups and run the skill once per group. Do not tailor to a majority, do not
average the archetypes, and do not silently drop the outlier — a resume aimed at two archetypes
answers neither, and the archetype choice governs section order and every budget
(CONTEXT.md §2). This is the same rule as the ambiguous-classification edge case below,
applied across postings instead of within one.

**Skip signals** — when no variant was specified, recommend not applying, with the reason, and
stop (when one was specified, these become cautions per the rule above). With several JDs, a skip
signal on one JD stops only that JD: exclude it from the demand profile, report the exclusion and
its reason in the change log, note that the user can re-run with it forced back in, and continue
with the rest — unless the exclusions take the set to zero, in which case stop:
- "Director" managing managers, not ICs.
- Platform/infra ML with no product KPI, regardless of level.
- Principal/Distinguished Engineer whose scope is core systems or infra rather than ML
  direction (fails the CONTEXT.md §2B discriminator).
- Staff/Principal posting that is a Staff-titled implementation job — executes a roadmap
  defined elsewhere, no problem-space ownership, no autonomy over approach, no stated influence
  on other people's technical work (fails the CONTEXT.md §2B job-design test).
- Research scientist with a publication mandate (conflicts with the ~1 paper/year preference).
- Sr. EM below the comp floor, unless the brand materially improves the next hop — flag for
  the user to decide.

**Edge cases:**
- "Director" with direct ICs at a small org → A.
- Startup exec role that is really a hands-on-only founding engineer → C, but flag the level
  mismatch to the user.
- Both a PAS and a PE posting open at the same company for overlapping scope → recommend the
  PAS posting. If **both are in the JD set**, do not merge them: tailor to the PAS posting,
  exclude the PE one, and say so — they are one application, not two demands to satisfy.
- Genuinely ambiguous between two archetypes → present both readings and ask; do not guess.
  (A user-specified variant resolves this — never ask when the user has already chosen.)

State the base variant being tailored, how it was chosen (user-specified or triaged), the JDs in
the set (and any excluded), and the signals that drove the classification, before proceeding.

### 2. Extract the demand profile

**2a. Per JD**, extract:
- Required skills, preferred skills, and responsibilities — **in the JD's own vocabulary**.
- Exact term variants ("recommender systems" vs "recsys"; "LLM" vs "GenAI"; "experiment"
  vs "A/B test"). The tailored resume mirrors the JD's variants — when several JDs disagree on a
  term, step 2c decides which form the prose uses.
- The JD's domain (e-commerce, healthcare, other) for bullet reordering. Domain is a
  `skills[]` tag in `bullet-library.yaml` — `e-commerce` / `healthcare` — not a separate field.
- Demands the candidate has **no evidence for**. These go on that JD's interview-prep list in
  the output — never onto the resume.

**2b. With a single JD**, that profile is the demand profile; skip to step 3.

**2c. With two or more JDs**, merge the per-JD profiles into one profile with three parts. Match
demands by *concept*, not by string — "recsys" in one JD and "recommender systems" in another are
one demand with two surface forms.

- **Core** — demands appearing in **two or more** JDs. These drive the summary and lead each
  role block. A demand required by every JD outranks one required by two of five; rank core
  demands by how many JDs carry them, then by whether the JD marks them required vs preferred.
- **Distinct** — demands appearing in exactly **one** JD. Each must end up with **at least one**
  surviving bullet, publication, or Skills entry, but never lead position and never the summary.
  One line of coverage is the target, not proportional representation.
- **Uncovered** — demands with no evidence anywhere in the libraries, tracked per JD for the
  interview-prep lists.

**Vocabulary clashes.** When two JDs name one concept differently, pick a single **primary form**
for the bullets and summary — the form used by the JD whose overall match is strongest, or the
expanded form when they match equally — and carry **both** surface forms in the Skills section so
an ATS filter on either one hits. Never write two forms of the same term into one bullet, and
never write a slashed hybrid ("recsys/recommender systems").

**Divergence caution.** If the core set covers less than half of any single JD's *required*
skills, the postings are too far apart for one resume to serve well. Report this as a caution —
name the JD and what it loses — recommend a separate tailored copy for it, and proceed with the
combined resume anyway. This is a caution, not a stop; the user asked for one resume.

### 3. Tailor the base variant
Working on a **copy** of the variant established in step 1 — never modify the source file, even
when it is itself a `tailored/` copy:

1. **Reorder** bullets so those evidencing the highest-priority demands lead each role — core
   demands first, in the rank set in step 2c. If the JDs share a domain, promote bullets carrying
   the matching domain skill tag; if they split across domains, treat the domain of the majority
   as core and the others as distinct.
2. **Reword** for keyword alignment: swap synonyms to the JDs' exact terms in bullets, the
   summary, and Skills, using the primary form for any clashing term (step 2c). Facts, numbers,
   and claims stay identical.
3. **Swap** (only if `bullet-library.yaml` is available): replace a weakly matching bullet
   with a stronger bullet from the same role's `bullets:` list under `roles:`, tagged for this
   archetype — keeping the archetype's phrasing mechanism intact (CONTEXT.md §5: the `hands-on-ml`
   marker survives in a B copy, and a swapped-in bullet must not be the alternate-framing sibling
   of one already on the page) — respecting the tool budget (1–3 named technologies per bullet). With several JDs,
   prefer the bullet that covers the most demands at once — one bullet evidencing two core
   demands beats two bullets evidencing one each, and that consolidation is what buys the space
   the distinct demands need. Role headings, dates, and scope lines are never edited during
   tailoring — they are facts from the role fields.
4. **Subtract** bullets irrelevant to **every** JD in the set — foregrounded role stays dominant,
   compressed roles can shrink to a single line. Subtract for *relevance*, not for length: two
   pages is the default (CONTEXT.md §3), so never drop a strong, relevant bullet to save space.
   A bullet that is the **only** evidence for a distinct demand is not irrelevant — it stays, low
   in its block. Subtraction can empty a role but never removes one: when a role's last bullet
   goes, its heading stays — `title`, `org`, `dates` (CONTEXT.md §1).
   **Archetype-B guard:** never subtract the last leadership-scope evidence from a B copy to make
   it read more like an IC resume, and never add transition framing while rewording. CONTEXT.md
   §2B's narrative rule requires both halves on the page — accumulated leadership scope *and* a
   live hands-on practice — and forbids any sentence that explains the move.
5. **Retune the summary** — one or two sentences of the archetype thesis rephrased toward the
   JDs' language. With several JDs the summary speaks to the **core** demands only; a demand
   unique to one posting never reaches the summary, because a summary trying to be all of them
   argues for none. No new claims. The closing **credential sentence** (CONTEXT.md §1) is a
   standing element: reword it toward the JDs' vocabulary if useful, but never cut it, never
   move it out of final position, and never promote it into the opening sentence. Extend it with
   the dissertation detail **only** when the postings are search/retrieval/ranking/IR-flavored
   (CONTEXT.md §1) — with several JDs, only when that flavor is *core* to the set — the
   extension is off by default.
6. **Adjust publications within the archetype's budget** (CONTEXT.md §2): swap entries so the
   most relevant papers occupy the slots, applying the publication rules in CONTEXT.md §3.
   With several JDs, a paper relevant to two postings outranks one relevant to a single posting;
   the budget does not grow with the number of JDs. Do not exceed the budget because a JD is
   academic-flavored; that is an archetype-B signal that should have been caught in triage.
7. **Adjust the academic record within the archetype's budget** (only if
   `academic-record.yaml` is available): swap talk slots toward entries whose `topic_tags`
   overlap the set's domains and keywords, preferring entries that serve more than one JD; a
   panel or judge entry may take a slot when a JD is community- or communication-flavored. If any
   JD emphasizes cross-team collaboration or community leadership, ensure the co-organized
   workshop lines are present (within budget) — they are direct evidence. All rendering rules in
   CONTEXT.md §3 apply, including workshops-are-never-publications.
8. **Prune the Skills section** to what survived (the pruning corollary, CONTEXT.md §4), then
   verify traceability in both directions. The Skills section is where clashing vocabulary
   variants both appear (step 2c) — but only for skills that a surviving bullet, publication, or
   named project actually evidences. Multiple JDs do **not** license a longer Skills list: no
   orphan skills, no matter how many postings ask for them.
9. **Check coverage before scoring** (multi-JD only): walk each JD's required skills and confirm
   each is either evidenced in the tailored copy or on that JD's interview-prep list. A required
   skill that *is* evidenced in the libraries but got subtracted is a tailoring failure — restore
   it and re-run this check. Record the result as the coverage matrix in the output.

### 4. Score before presenting
Run the `score-resume` skill on the tailored copy **with the JD** — with several JDs, pass the
whole set; the skill scores the JD-dependent items per JD and the worst score governs. Fix any
blocker before showing the user. A blocker against any single JD is a blocker.

## Output

- The tailored resume as **one** new file: `tailored/{slug}.md`. The source variant is untouched —
  if the slug would collide with the source file, pick a distinct slug rather than overwriting it.
  For the slug: use the one the user gave; otherwise, with a single JD use the
  company-or-role slug as before, and with several JDs name the *shared theme* rather than the
  companies (`recsys-em`, `ads-ranking-em`) — falling back to the per-JD slugs joined by `-and-`
  when there are two and no clean theme. Do not write one file per JD.
- A change log: the base variant used and whether the user specified it or triage chose it; the
  JDs in the set, each one's classification and reasoning, and any excluded JD with its reason;
  any user-choice/triage disagreement, skip-signal caution, or divergence caution; the core /
  distinct split from step 2c; reorderings; rewordings (old term → chosen term, noting which JD's
  vocabulary won any clash); swaps, subtractions, and publication changes with one-line rationale.
- The coverage matrix (multi-JD only): one row per JD required skill, columns for which JDs ask
  for it and where the resume evidences it — or "prep only" when it is uncovered.
- The interview-prep list: demands with no resume evidence, **grouped by JD**, since the gaps
  differ per posting.
- The scorecard result — per JD for the JD-dependent items when there are several.

## Exit conditions

- Base variant missing → report and stop (see inputs table). Do not build one ad hoc. This
  applies to a user-specified path too: a bad path is reported, not silently swapped for a
  triaged variant.
- JD matches a skip signal **and no variant was specified** → report the reason and stop. With
  several JDs, exclude that JD and continue on the rest; stop only if nothing is left. With a
  specified variant, report the caution and continue.
- Classification ambiguous **and no variant was specified** → ask.
- **JDs triage to different archetypes and no variant was specified** → report each
  classification and stop; ask for a variant or for the set to be split by archetype.
- JD text not provided or too fragmentary to extract a demand profile → ask for the full text.
  With several JDs, a fragmentary one is excluded (reported) rather than stopping the run — unless
  it is the only JD.
