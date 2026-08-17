# CONTEXT.md — Shared Ground Truth for the Resume System

**Role of this file:** the single source of durable facts and rules. Every skill in
`skills/` declares this file as a required input. Skills contain *procedures*; this file
contains *facts, definitions, and rules*. If a skill's procedure appears to conflict with
this file, this file wins.

**System architecture:**
- `bullet-library.yaml` — master bullet library, complete inventory (schema in §5)
- `skills-evidence-matrix.yaml` — GENERATED from the libraries (`python3 gen_matrix.py`); do
  not hand-edit
- `publication-library.yaml` — publication library, complete record (schema in §5)
- `academic-record.yaml` — co-organized workshops, academic service, invited talks and
  panels (schema in §5)
- `variants/` — three base resumes: `variant-A.md`, `variant-B.md`, `variant-C.md`
- `skills/build-variant/` — create or edit a base variant
- `skills/tailor-to-jd/` — match one JD, or a set of them, to a variant and tailor one copy to it
- `skills/score-resume/` — score any resume draft (JD optional; a set of JDs scores per JD)

**Never invent facts, metrics, titles, or technologies.** If a claim needs a number that is
not in this file or the libraries, ask the candidate. Every claim on a resume must be
defensible in a live interview.

---

## 1. Invariants

### Identity
- Yubin Kim — yubink.cs@gmail.com — 412-204-7134
- Based in Pittsburgh, PA. Targets: remote-friendly, or Pittsburgh-based. State
  location/remote posture explicitly in the resume header.
- U.S. Citizen
- Google Scholar: user 3F_QHHQAAAAJ

### Education
- Ph.D. Computer Science, Language Technologies Institute, Carnegie Mellon University (Dec 2018)
- B.S. Software Engineering, University of Waterloo (Apr 2011)
- Dissertation: *Robust Selective Search* — large-scale distributed retrieval over topically
  partitioned shards (`thesis19` in `publication-library.yaml`; the thesis itself is rarely
  listed as a publication, since Education covers the degree).

**PhD visibility — the credential sentence.** The CMU doctorate is a differentiator that
otherwise dies at the bottom of page two, so every variant and every tailored copy carries it in
the Summary as the **final sentence**, in this canonical form:

> PhD from Carnegie Mellon University in computer science.

- **Final position, always.** The summary argues the archetype thesis first and the credential
  closes it. Leading with the degree at 15+ years of experience reads as credentialing, which is
  the opposite of the intent; closing with it reads as a fact.
- **The Education entry still carries the full degree line.** The credential sentence does not
  repeat the institute (LTI), the date, or the dissertation title — that would be the same claim
  twice. Spell out "Carnegie Mellon University" rather than "CMU"; the initialism costs an ATS
  keyword match and saves nothing.
- **Dissertation detail is JD-conditional, and off by default.** The base variants carry the
  canonical sentence and nothing more. A tailored copy may extend it — "…, with a dissertation
  on large-scale distributed search" — only when the posting makes the subject matter directly
  relevant (a search, retrieval, ranking, or IR role). Everywhere else it is noise that pulls the
  summary toward an academic register. The dissertation fact is recorded above, so adding it is
  rewording from a known fact, not invention.
- **Tailoring may reword it, never cut or move it.** It is a standing element, like the
  remote-leadership evidence.
- **Archetype A's summary also names "PhD- and Staff-level ICs"** as report composition (see the
  report-composition rule above). That is a claim about *reports*, not about the candidate's
  credential — keep both, but keep them in separate sentences so the word doesn't stack.
- **Banned, all of them:** post-nominals in the masthead ("Yubin Kim, Ph.D."), "Dr." anywhere,
  the credential in the contact line, and moving Education above Experience. Each one converts a
  low-key signal into a credentialing one.

### Career spine — lives in `bullet-library.yaml`
**The spine is not duplicated here.** Titles, orgs, dates, team size and composition, hires,
promotions, calibration, managed-out counts, internships, and the aggregate tenure claims all
live in `bullet-library.yaml` under `tenure:`, `roles:` (`title` / `org` / `dates` / `context` /
`team` / `management`), and `internships:` — one hand-editable file for every career-experience
fact. Read it alongside this file; when a role fact is needed, take it from there.

This section holds only the **rules** for using those facts:

- **Report composition — has managed scientists, not only engineers.** The per-role counts are
  in the library's `team` fields; applied-science manager postings screen for this literally.
  - **Rendering rule:** on the resume, be explicit *that* scientists were managed; do not
    enumerate scientist headcount. "Led a team of ~5 applied scientists and engineers,
    including PhD scientists" — not "led 2 PhD scientists." The library's counts are for
    interview answers, not for the page.
- **Built-from-zero vs. inherited-and-grew is a scope signal** — the library's `team` fields
  record which each role was; say which when the archetype rewards team-building.
- **Remote leadership must appear in every variant.** Both the Etsy and Vody teams were fully
  remote (recorded in their `team` fields) — continuous distributed-team leadership since 2022.
  Remote-first employers screen for it explicitly.
- **Promotions, calibration, and performance-managed-out counts** (library `management` fields)
  are archetype-A evidence; they compress to a supporting role in B and C.
- **Every role in the spine appears in every variant — the timeline is never broken.** When a
  role has no bullets tagged for the target archetype, it still renders: `title`, `org`, and
  `dates`, with no bullets and no scope line. Dropping the role instead silently rewrites the
  employment history — it shortens a tenure, hides an internal promotion, or opens a gap the
  reader has to ask about. Bullet tags decide what a role *says*, never whether it *appears*.
  This holds for tailored copies too: subtraction can empty a role, never remove it.

### Academic footprint
- Complete record lives in two libraries: `publication-library.yaml` (papers) and
  `academic-record.yaml` (co-organized workshops, service roles, invited talks and panels).
- **Preference:** academic involvement should be an asset the employer supports (conference
  travel, collaborations). No novel-research mandate. Target output ~1 short/workshop paper
  per year, opportunistic.

### Constraints and preferences
- **Comp floor:** $400k total comp (salary + bonus + equity) for archetypes A and B.
  Flexible for C (see §2C).
- **Timeline:** flexible, no urgency.
- **Wants:** direct technical mentorship of ICs; product ML with external-customer-facing
  KPIs; strategic/roadmap ownership; cross-org influence.
- **Does not want:** managing only managers; pure platform/infra ML; a role that reads as a
  scope downgrade.
- **"Not a downgrade" means:** scope first, how the sequence reads to a *future* employer
  second. Title is negotiable. Sr. EM at a strong brand is acceptable despite being a nominal
  title step down from CSO, because scope increases.
- Willing to sit a full IC loop including coding.
- Strong presenter and technical storyteller; wants to keep exercising this (fundraising,
  customer-facing, keynotes).

---

## 2. The three archetypes

### A — Applied-science / product-ML manager with direct reports

- **Target titles:** Manager or Senior Manager of Applied Science, Senior Engineering Manager,
  Engineering Manager (senior scope), Manager of Machine Learning, Director of ML/AI at a
  100–500 person company **with direct reports**.
- **Neither the title nor the ladder is the filter — direct reports plus delivery
  accountability are.** Applied-science and engineering ladders both route this role, and
  which one a company uses says little. A posting qualifies when it has (a) direct IC reports
  and (b) accountability for shipped model outcomes against customer or revenue KPIs. A
  "Manager, Applied Science" whose team only advises other teams is out; a "Sr. EM" whose team
  owns ranking quality is in.
- **Target orgs:** big tech and scaled tech with product ML surfaces (search, recommendations,
  ads, personalization, marketplace). Small-org Director only if it is a direct line-manager
  role. **Soft filter, used as a tie-break:** prefer orgs with visible academic tolerance —
  conference travel, teams that publish, external collaborations. The publication record is
  load-bearing evidence in this archetype, and an org hostile to it wastes the differentiator
  (§1 academic-footprint preference).
- **Hard requirement:** direct IC reports, not managers-of-managers. Product ML with revenue
  or customer-facing KPIs, not platform/infra.
- **Team-size floor:** ~5 at a strong brand. Willing to build from zero.
- **Thesis:** *"Technical leader with a track record of building and leading applied science teams 
  that ship production ML systems driving measureable business impact."*
- **Foreground:**
  - Etsy — metric wins, experiment velocity, offline-evaluation rigor, cross-org partnerships.
  - **Report composition, stated explicitly at every role** (§1): PhD scientists at Vody,
    Intermediate–Sr. Staff applied-science and engineering ICs including PhD scientists at
    Etsy, ~3 applied-ML engineers at UPMC. "Has managed scientists" is a literal screen on
    applied-science manager postings, and "led an ML team" does not clear it. Follow the §1
    rendering rule: name the composition, not the scientist headcount.
  - The rest of the §1 people-management evidence; remote team leadership; UPMC Director scope.
- **Technical credibility comes from mechanism and publications, not from a hands-on bullet.**
  Every leadership bullet names the technique it rests on (graph ML, Solr candidate retrieval,
  offline-eval design), so depth travels inside the leadership claims; the publication record
  carries the rest. Personal hands-on work from §1 stays supporting — a clause at most, never
  a headline. This archetype does not argue "I'm still an IC"; it argues "I'm a scientist who
  manages."
- **Compress:** publications to the budget below — but never bury or delete them; here they
  are primary depth evidence, not decoration. For non-healthcare JDs, compress bullets about
  healthcare-specific problems.
- **Section order:** Summary → Experience → Selected Publications & Academic Leadership →
  Skills → Education. Publications sit above Skills: they are evidence, and Skills is a
  keyword surface.
- **Summary opens on the applied-science-manager identity** — manager + years in ML + active
  publication record — then the headline business metric. Not on process management.
- **Keyword emphasis:** constant across JDs — hiring, performance management, technical
  mentorship, roadmap, A/B experimentation, offline evaluation, cross-functional, distributed
  team. **The technical center of gravity defaults to search** (retrieval, ranking,
  recommendations) **and is swapped to match the JD** — LLM/GenAI product, personalization,
  ads — when the posting leads elsewhere. Swap by reordering and rewording only (§3).
- **Publication budget:** ~4 entries.
- **Academic record budget:** co-organized workshops 1–2 compact lines — include these; they
  evidence leadership and collaboration-building, which is the archetype's core claim.
  Service: one line, 2–3 most senior roles (may merge with the workshop lines into a single
  "Academic Leadership" block). Talks: omit, or one line if the JD emphasizes communication
  or evangelism.

### B — Strategic senior IC (Principal Applied Scientist / Principal Engineer)

- **Target titles:** Principal Applied Scientist, Senior Principal Applied Scientist,
  Principal Research Scientist, Principal ML Scientist, Principal Engineer, Principal ML
  Engineer, Distinguished Engineer.
- **Title is not the filter — the work is.** Many organizations have no Applied Scientist
  ladder and route exactly this role through the engineering ladder as Principal Engineer. If
  the JD describes multi-year technical direction for ML/search/recsys systems, cross-org
  influence, and applied use of existing research for customer impact, the title is fine.
- **Target orgs:** (a) companies with real applied-science ladders and academic tolerance —
  Amazon, Google, Netflix, Spotify, Pinterest, eBay, Shopify, Instacart, DoorDash, industrial
  research labs; (b) companies with a single engineering ladder where the Principal role
  covers ML direction.
- **Thesis:** *"I set multi-year technical direction for search and recommendation systems,
  drive adoption across orgs, and can be hands-on"*
- **Positioning:** applied, not academic. Applying existing research to direct customer
  impact. Scope is cross-org influence, not a single team. Reports optional; mentorship
  expected.
- **A vs B:** direct reports *plus* delivery accountability. A posting is A when someone holds
  direct IC reports and is accountable for that team's shipped model outcomes; it is B when the
  scope is technical direction and cross-org influence without owning a single team's delivery.
  Both archetypes claim technical depth and the publication record — that is not the
  discriminator.
- **Foreground:** technical depth and system design; cross-org collaboration wins; the
  academic record fully expanded — a differentiator almost no competing candidate has; recent
  hands-on work from §1 to establish current fluency.
- **Compress:** people-management mechanics (headcount, promos, performance) to a supporting
  role. Keep team leadership as evidence of influence and mentorship, not as the headline.
- **Section order:** Summary → Experience → Publications → Academic Service → Skills → Education.
- **Keyword emphasis:** technical strategy, multi-year vision, cross-org influence, applied
  research, retrieval, ranking, LLM, RAG, evaluation, mentorship, publications.
- **Publication budget:** 5–8 entries, expanded. **Academic record budget:** full service
  list — recent chair roles, editorial board, senior PC line — plus co-organized workshops as
  a compact block within the Academic Service section, and 2–3 talk lines (keynotes and
  invited talks first) folded into the same section rather than given their own.

**Principal Engineer discriminator.** Two different roles share this title:

| Pursue (ML-direction PE) | Skip (systems PE) |
|---|---|
| Owns direction for ranking, retrieval, recsys, or LLM product systems | Owns distributed systems, storage, compilers, or core infra |
| "Partner with product," business or customer KPIs named | Latency/throughput/uptime are the only stated outcomes |
| Applied research, evaluation, experimentation, model quality | Deep language runtime, kernel, or database internals |
| Cross-org technical strategy, mentorship, setting the roadmap | "Hands-on-keyboard majority of the time" as the primary expectation |
| Publications or conference involvement listed as a plus | No ML in the requirements at all |

**Loop-prep note (not a filter).** PE loops weight coding and ML system design more heavily
than PAS loops and lean on systems designed and shipped personally. This affects preparation,
not whether to apply. Where both ladders exist at one company for overlapping scope, prefer
the Applied Scientist posting.

### C — Startup AI exec (0→1 Head of AI)

- **Target titles:** Head of AI, Chief Scientist, VP of AI/ML. Open to co-founding as well as
  joining.
- **Target orgs:** Series B–D, ready to stand up a serious AI/ML function. Target end-state
  org ~10–15 people, not 30.
- **Comp:** floor bends here. Market-competitive cash preferred; genuine liquidity preferred
  over illiquid paper. Willing to flex below $400k for the right 0→1 mandate.
- **Thesis:** *"I've built an AI function from zero inside a real business — including the
  commercial side: customers, pitches, revenue."*
- **Foreground:** Vody end-to-end (0→$2M ARR, Grubhub and Academy Sports & Outdoors as
  customers, $1M raised, hired ~9, reported to CEO, owned technical and product roadmap);
  breadth (code + tech lead + pitching + business building); speaking and storytelling; UPMC
  pitching to SVPs/CTO and identifying $M opportunities.
- **Compress:** publications to the budget below — credibility signal, not the point.
  Academic service to one line. Big-co process detail.
- **Section order:** Summary → Experience → Selected Talks & Speaking → Skills → Publications
  (brief) → Education.
- **Keyword emphasis:** 0→1, founding, GTM, ARR, fundraising, enterprise customers, roadmap,
  hiring, hands-on, LLM, agents, product strategy.
- **Publication budget:** 2–3 one-line entries, or a single line plus Scholar link.
  **Academic record budget:** talks get their own "Selected Talks & Speaking" section, 3–5
  entries, keynotes first. Service and workshops: one line total, combined.

---

## 3. Global resume rules

**Do**
- Bullet formula: **action → mechanism → measured outcome.** Mechanism earns technical
  credibility; outcome earns the interview.
- Pair business metrics with model/system metrics.
- Mirror the JD's exact vocabulary. If the JD says "recommender systems," don't write "recs."
- Front-load the most JD-relevant role; compress the rest.
- **Two pages is the default length for every variant and every tailored copy.** 15+ years with
  four roles, a publication record, and academic service does not fit on one page, and forcing
  it there cuts exactly the scope and metric evidence these archetypes are screened on. Never
  compress to one page unless a specific posting demands it. Two pages is a target, not a quota:
  don't pad to fill it — if a variant runs short, the fix is stronger evidence, not filler.
- **Page one carries the decision.** Page two is skimmed, so the summary, the foregrounded role,
  and the headline metrics belong above the fold; supporting roles, older evidence, and the
  Skills keyword payload can run onto page two.
- Tailor by **subtraction and reordering only.** Never by invention.
- Ship two artifacts per variant: a designed PDF for humans/direct email, and a plain
  single-column ATS-safe version for portals.

**Don't**
- Don't use multi-column layouts, floated sidebars, text boxes, or tables-for-layout in any
  artifact that will pass through an ATS. Many parsers scramble or drop that content — and
  the sidebar is typically where the keyword payload sits. Single column, standard headings.
- Don't dump tool lists in place of outcomes. Tools belong inside the mechanism clause of a
  bullet that has an outcome — not in a standalone list. Budget: 1–3 named technologies per
  bullet, distributed across bullets. A bullet naming five tools is naming none.
- Don't leave orphan skills. Anything in the Skills section must be traceable to experience,
  a publication, or a named project in the same document (§4).
- Don't use ownership verbs without results ("Owned the technical and product roadmap" is a
  job description, not an accomplishment).
- **Don't stack the credential.** The PhD appears exactly twice: the summary's closing
  credential sentence (§1) and the Education entry. No post-nominals, no credential in the
  contact line, no third mention.
- Don't let the resume, LinkedIn, and Google Scholar contradict each other.
- Don't maintain more than three base variants.
- Don't let the title sequence carry the seniority story on its own. Director → Sr. EM → CSO
  reads as a zigzag; make team size, org context, and business impact legible at each role so
  the progression is visible in the scope rather than the titles.

**Publication rules (apply wherever publications appear)**
- **Never inflate a venue.** Workshop papers are labeled as workshop papers. A citation
  containing "SIGIR Workshop" is not a SIGIR main-conference paper, and a
  program-committee-level reader will catch the difference immediately. `venue_tier` in the
  publication library is authoritative.
- **A publication is valid evidence regardless of its age.** Some target roles explicitly
  value historical depth in the IR field.
- **Prefer experience as primary evidence.** Where a skill is evidenced by both a bullet and
  a paper, the bullet is primary and the paper reinforces.
- **Last-author supervising papers are an asset in B** — they evidence mentorship and
  collaboration-building. Don't obscure the position.
- **Omit citation counts.** Scholar is linked for anyone who wants to check.
- **Bold the candidate's name** in every listed entry.
- **Link the title when the library has a URL.** If an entry's `url` in
  `publication-library.yaml` is non-empty, render the paper title as a Markdown link to it —
  `[Title](url)` — so a reader can pull the PDF in one click. The link goes on the title only,
  so the citation text itself is unchanged, and it costs no line length. Leave the title as
  plain text when `url` is empty. **Never invent, guess, or reconstruct a URL** (no DOI
  assembly, no arXiv search): an empty `url` is an evidence gap to fill in the library first.
- **Pre-2019 papers** are included only when uniquely relevant to the JD, or to fill out an
  otherwise thin list in B.
- **Stay a subset of Scholar.** Nothing on the resume that isn't verifiable there, except
  clearly labeled under-review work.
- **Truncate and always link.** Whenever the list is a subset, close with the "Full list on
  Google Scholar" line.

**Academic record rules (workshops, service, talks)**
- **Workshops are service, never publications.** The `workshops` entries in
  `academic-record.yaml` are *co-organized* events. Render them with the organizing role
  explicit — e.g. "Co-organizer, Workshop on eCommerce @ SIGIR, 2023–2026" — under an
  Academic Service / Academic Leadership heading. Never place them in a Publications section,
  where they would read as papers.
- **Compact multi-year format.** Recurring workshop roles collapse to one line per workshop
  with a year range, not one line per year.
- **Selection ranking within each category:** for service, chair/organizer roles outrank
  reviewer roles, then recency; for talks, keynote > invited talk > panel > judge, then
  recency, then `topic_tags` overlap with the JD. Panel and judge entries earn a slot only
  when space is cheap or the JD is community- or communication-flavored.
- **Talk titles are quoted verbatim** from the library; venue and year always included.
- Always include years on service roles; prefer venues a non-specialist recruiter might
  recognize.

---

## 4. Skills ↔ evidence traceability rule

Both directions, checked in every variant and every tailored copy:

1. **No orphan skills.** Every entry in the Skills section must be traceable to at least one
   surviving bullet in Experience, a listed publication, or a named project in the same
   document. If a reader can't answer "where did they use this?", the skill is a liability.
2. **No unlisted tools.** Any technology named in an Experience bullet should also appear in
   Skills, so keyword filters catch it in both places.

**Foundational tier exemption.** Programming languages and universal tooling (Python, Java,
C++, SQL, git, Jupyter, notebooks) may be listed without a dedicated evidence bullet.
Everything else needs evidence: frameworks, model families, serving stacks, search engines,
orchestration, cloud platforms, and all named techniques.

**The pruning corollary.** Tailoring by subtraction removes bullets; if the only bullet
evidencing a skill is cut, that skill must also come out of the Skills section. This is the
step that silently breaks traceability — every skill procedure includes it explicitly.

---

## 5. Library schemas

The two YAML libraries are the complete inventories. Resumes show selected subsets.

### `bullet-library.yaml` — the career spine plus every bullet

This is the whole career-experience record: the spine (§1 points here) and the bullets, in one
hand-editable file. Four top-level keys:

| Key | Contents |
|---|---|
| `tenure` | `ml` and `leadership` — the aggregate years-in-field claims used in resume summaries |
| `roles` | One entry per role, reverse-chronological, keyed `vody` / `etsy` / `upmc-director` / `upmc-sds`; each holds its own `bullets:` list |
| `cross-role` | Bullets spanning several roles — render inside a role block or a leadership summary line, never as a standalone role |
| `internships` | Plain strings; listed on a resume only when a JD makes them relevant |

Per-role fields (the resume's role heading and scope line come from these — never retype them
into a variant from memory):

| Field | Purpose |
|---|---|
| `title` | Exact title as it should appear |
| `org` | Employer |
| `dates` | `MM/YYYY–MM/YYYY`, or `–present` |
| `context` | Optional one-line scope framing, rendered as the italic subtitle under the role heading |
| `team` | Size, composition, PhD-scientist presence, hires, built-from-zero vs. inherited, remote posture |
| `management` | Promotions, leveling calibration, performance-managed-out counts |
| `bullets[]` | The role's bullets |

Per-bullet fields — these four and nothing else:

| Field | Purpose |
|---|---|
| `id` | Short unique key |
| `bullet` | Full text, mechanism and outcome included |
| `skills[]` | Every skill and tool this bullet evidences, **including domain** — `e-commerce` / `healthcare`. Domain-general bullets simply carry neither. |
| `archetypes[]` | A, B, C, or any subset |

`team` and `management` are prose fields holding durable facts; §1 holds the rules for
rendering them (notably: name scientist *presence*, never scientist headcount).

**Open evidence questions are `# TODO` comments**, written as the last line of the bullet
entry they belong to and keyed to `TODO.md §3` where applicable. A bullet carrying a TODO is
not resume-ready: it is missing a number or an outcome, usually flagged inline in the text with
a bracketed placeholder (`[X]%`). Selection prefers bullets with no TODO; a placeholder is a
question for the candidate, never a number to invent. When the candidate answers, fold the
fact into the bullet and delete the comment.

The **skills-evidence matrix** is generated into `skills-evidence-matrix.yaml` — one row per
skill, listing the bullet and publication IDs that evidence it. Regenerate it with
`python3 gen_matrix.py` (from the repo root) after editing any `skills[]` field; do not
hand-edit it. Any skill with zero IDs is either cut from every variant or becomes an open
evidence question in TODO.md.

### `publication-library.yaml` — one entry per publication

| Field | Purpose |
|---|---|
| `id` | Short key, e.g. `iclr26-geo`, `ecom25-inference` |
| `citation` | Full formatted entry: authors, year, title, venue, pages |
| `venue_tier` | `top-tier-conference` / `journal` / `workshop` / `under-review` |
| `work_origin` | vody / etsy / upmc / cmu — which role produced the work |
| `skills[]` | Techniques, frameworks, and tools the paper demonstrates |
| `relevance_note` | One line: what this paper proves about the candidate |
| `url` | Link, if public |

Year, venue name, and author position are read from `citation`, not stored separately.

### `academic-record.yaml` — three sections

Designed for hand editing: minimal fields, no selection metadata (selection is computed by
the skills from the rules in §3).

**`workshops:`** — peer-reviewed workshops the candidate **co-organized**.

| Field | Purpose |
|---|---|
| `name` | Workshop name, e.g. "Workshop on eCommerce" |
| `host` | Hosting conference, e.g. "SIGIR" |
| `years` | Single year or range, e.g. "2023–2026" — the compact rendering unit |

**`service:`** — chair, editorial, and committee roles.

| Field | Purpose |
|---|---|
| `role` | e.g. "Sponsorship Co-chair", "Editorial board", "Senior PC" |
| `venue` | Conference or journal; may list several for standing roles |
| `year` | Year, range, or `ongoing` for standing roles |

**`talks:`** — invited talks, keynotes, panels, judging.

| Field | Purpose |
|---|---|
| `title` | Verbatim talk/panel title; empty for untitled appearances |
| `kind` | `keynote` / `invited-talk` / `panel` / `judge` — drives selection ranking |
| `venue` | Event and host; multiple venues for repeated talks go in one string |
| `year` | Year of (most recent) delivery |
| `topic_tags[]` | Lowercase tags for JD matching, e.g. `[genai, e-commerce]` |
