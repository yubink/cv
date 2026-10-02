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
  - **Rendering rule: name the count, and name it as a career aggregate.** Reversed 2026-08-19
    (user). Summed across roles the total is substantial, and stating it converts a soft claim
    into a screenable one — "technically mentored 6 PhD scientists and ICs up to Sr. Staff"
    rather than "including PhD scientists." The earlier rule suppressed the number because
    per-role counts understate; the fix is to aggregate, not to hedge.
  - **Compute the aggregate from the library's `team` fields every time — never copy it from an
    older variant or from this file.** It is a derived number, so it is exactly the kind that
    goes stale silently: the Etsy count was wrong here until 2026-08-19, which made every
    aggregate built on it wrong too. Re-add the per-role counts whenever any `team` field
    changes, and keep the per-role breakdown in the library for interview answers.
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
  KPIs; strategic/roadmap ownership; cross-org influence; ownership of a problem space with
  autonomy over the technical path to it; a seat at the strategic table.
- **Does not want:** managing only managers; pure platform/infra ML; a role that reads as a
  scope downgrade; a career path whose progression requires moving progressively farther from
  technical work; a pure-execution IC role that receives a defined problem and implements it.
- **Ideal weekly shape (drives the §2B job-design test, not the resume copy):** ~1 day hands-on
  (coding, modeling, analysis, prototypes, with occasional longer deep dives), ~2 days technical
  direction (what to investigate, shaping approaches, reviewing experiments, guiding others),
  ~1 day product and strategy, ~1 day mentorship; high-value communication and 1–2 academic
  conferences a year on top. Management as an increasingly abstract activity — resource
  allocation, org politics, solving problems through layers of people — is the substance being
  moved away from, not leadership itself.
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
    rendering rule: name the composition **and the aggregate PhD-scientist count**, computed
    from the library's `team` fields.
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

### B — Strategic senior IC (Staff / Principal Applied Scientist or ML Engineer)

- **Target titles:** Staff Applied Scientist, Principal Applied Scientist, Senior Principal
  Applied Scientist, Principal Research Scientist, Principal ML Scientist, Staff ML Engineer,
  Principal ML Engineer, Principal Engineer, Distinguished Engineer.
- **Neither the title nor the ladder is the filter — the job design is.** Many organizations
  have no Applied Scientist ladder and route exactly this role through the engineering ladder.
  A posting qualifies when it hands over a **problem space** rather than a backlog: a business
  or product north star, autonomy over the technical path to it, a voice in roadmap definition,
  and the expectation of guiding other scientists and engineers. Apply the job-design test
  below to every posting, and the Principal Engineer discriminator to engineering-ladder ones.
- **Target orgs:** (a) companies with real applied-science ladders and academic tolerance —
  Amazon, Google, Netflix, Spotify, Pinterest, eBay, Shopify, Instacart, DoorDash, industrial
  research labs; (b) companies with a single engineering ladder where the Staff/Principal role
  covers ML direction.
- **Thesis:** *"I find the technically ambitious opportunities inside a product north star,
  build enough conviction to bet on them — hands-on when that is what it takes — set the
  technical direction, and bring the org along. Measured in shipped systems and revenue."*
- **Positioning:** applied, not academic — a technical leader whose leadership is grounded in
  ongoing technical practice. Applying existing research to direct customer impact. Scope is
  cross-org influence over a problem space, not one team's delivery. Reports optional;
  mentorship expected.
- **A vs B:** direct reports *plus* delivery accountability. A posting is A when someone holds
  direct IC reports and is accountable for that team's shipped model outcomes; it is B when the
  scope is technical direction and cross-org influence without owning a single team's delivery.
  Both archetypes claim technical depth and the publication record — that is not the
  discriminator. **B is not a smaller A.** Same altitude, routed through technical judgment and
  influence instead of the org chart.

**The narrative rule — a move toward leverage, never a retreat from leadership.** Director →
Sr. EM → CSO → Staff/Principal IC is the one thing a reader can misread, so the page has to
answer it before it is asked. It answers correctly by carrying *both* halves of the claim at
once: accumulated leadership scope (teams built, strategy set, revenue delivered,
executive-level ownership) **and** a live personal technical practice (models built, prototypes
shipped, analysis run). B does not argue "I am still an IC," and it does not argue "I am done
managing." It argues that direction-setting, incubation, and mentorship are worth more from
someone who is still close to the work.

- **Never frame the move.** State what the candidate does and has done; never explain a
  transition. No objective statement, no "seeking," no "transitioning to," no "returning to
  hands-on work," no "individual contributor" as a self-description. Explaining the move
  concedes that it needs explaining.
- **Banned register:** anything apologetic, anything that reads as stepping back, and any
  phrasing that makes coding the goal ("back to building," "closer to the code" as a motive).
  Hands-on work appears as *evidence of current fluency*, never as an aspiration.
- **Leadership evidence stays on the page.** Cutting it to look more like an IC is the failure
  mode this archetype is most prone to — it converts 7+ years of leadership into a gap and
  makes the move read as a demotion. Compress the mechanics (below); keep the scope.

- **Foreground — the whole combination, in this order of emphasis:**
  1. **Technical depth and current fluency.** Recent hands-on work from §1 earns *named
     bullets, not clauses*: models built and fine-tuned personally, prototypes, production
     inference, hands-on analysis. At least one per recent role where the evidence exists.
     (Contrast archetype A, where hands-on work is a clause at most.)
     - **Say which work was personal.** Library bullet text is deliberately neutral about it, so
       B adds the marker at render time — "Built v1 … hands-on," "personally developing" — on any
       bullet tagged `hands-on-ml`. See the two mechanisms in §5. Leaving every bullet neutral is
       the quiet way this archetype fails: a reader cannot tell a system the candidate built from
       one their team built, and B's whole claim is that they still build.
  2. **Technical direction.** Multi-year technical strategy and system design for search,
     retrieval, recommendations, and LLM product systems.
  3. **Incubation — the loop this archetype is selling.** Spotted the opportunity,
     investigated it deeply enough to hold conviction, prototyped, made the case, got it
     funded, shipped it. A bullet carrying the whole loop is the highest-value evidence here;
     prefer it over any single-step claim.
  4. **Measured business impact.** Business and model metrics paired — the answer to whether
     this person's technical judgment pays.
  5. **Cross-org influence and executive communication.** Adoption driven across orgs;
     pitching to SVPs and CTOs; customer-facing technical storytelling.
  6. **Mentorship as a multiplier.** Growing strong ICs into more senior technical leaders —
     promotions delivered and the levels reached, framed as growth *caused*, not as performance
     management *performed*.
  7. **Product and business thinking.** Roadmap ownership and opportunity identification, as
     the thing that aims the technical work.
  8. **The academic record, fully expanded** — a differentiator almost no competing candidate
     has, and standing evidence of engagement with the frontier.
- **Compress — do not cut — people-management mechanics.** Headcount, hiring counts,
  performance management, calibration, and managed-out counts drop to scope lines and single
  clauses: context that establishes seniority, not the argument. The test: *"grew ICs to Staff
  level"* is B evidence; *"ran leveling calibration and managed out 2"* is A evidence.
- **Section order:** Summary → Experience → Publications → Academic Service → Skills → Education.
- **Summary shape:** (1) Staff/Principal-level technical-leader identity + years in ML + the
  systems domain; (2) the combination claim — sets direction *and* builds, with cross-org
  influence; (3) the headline business metric; (4) the credential sentence (§1). No sentence in
  it may describe a career transition.
- **Keyword emphasis:** technical direction, technical strategy, multi-year vision, cross-org
  influence, influence without authority, problem-space ownership, applied research,
  prototyping, incubation, product strategy, roadmap, retrieval, ranking, recommendations, LLM,
  RAG, evaluation, experimentation, technical mentorship, Staff/Principal, executive
  communication, publications.
- **Publication budget:** **~5 entries, condensed** (§3 condensed citation form). Six only when
  a posting makes a sixth paper directly relevant. B used to run 5–8 expanded; that plus the full
  service block pushed the variant to three pages, and the entries past the fifth were buying
  less than the bullets and page-one space they cost.
- **Academic record budget:** full service list — recent chair roles, editorial board, senior PC
  line — plus co-organized workshops as a compact block within the same Academic Service section.
  **Talks are off by default.** The chair roles and co-organized workshops already establish
  community standing, and they do it in fewer lines.
  - **Speaking trigger.** When a posting explicitly asks for public speaking, evangelism,
    conference presence, or external technical communication, add up to **2 talk lines**
    (keynote first) *and* promote `vody-fundraising` — writing and presenting pitches to VCs —
    into the Vody block as the experience-side half of the same claim. The two move together:
    a talk list without a bullet behind it is a hobby, and the pitching bullet without the talks
    reads as fundraising rather than communication skill.
  - `vody-fundraising` is tagged for B for exactly this reason and **stays out of the base
    variant** — it enters only on that trigger.

**Job-design test.** Applies to every B posting regardless of ladder or title. Read the JD for
what the role is *given*, not for what it is called.

| Pursue | Skip |
|---|---|
| Owns a problem area end-to-end toward a named business or product outcome | Executes a roadmap someone else defined ("implement," "deliver the backlog") |
| Autonomy over the technical approach — "you decide how" | Approach pre-specified; the role is the implementation |
| Named in product strategy or roadmap definition | No product surface, or product decisions sit entirely elsewhere |
| Sets technical direction and guides other scientists/engineers | Purely individual output; no stated influence on others' work |
| Mentorship of ICs stated as an expectation | "Senior engineer, plus" — the same job one level up |
| Conference travel, publications, or external technical presence supported | Explicit no-research, no-conference posture |
| "Influence without authority," "technical leadership across teams" | "Hands-on-keyboard the majority of the time" as the primary expectation |

A posting failing several right-hand rows is a Staff-titled implementation job: a skip even at
strong comp, because it is the pure-execution IC role the candidate has ruled out (§1
constraints).

**Principal Engineer discriminator.** On a single engineering ladder, two different roles share
this title:

| Pursue (ML-direction PE) | Skip (systems PE) |
|---|---|
| Owns direction for ranking, retrieval, recsys, or LLM product systems | Owns distributed systems, storage, compilers, or core infra |
| "Partner with product," business or customer KPIs named | Latency/throughput/uptime are the only stated outcomes |
| Applied research, evaluation, experimentation, model quality | Deep language runtime, kernel, or database internals |
| Cross-org technical strategy, mentorship, setting the roadmap | ML absent from the requirements entirely |
| Publications or conference involvement listed as a plus | No stated room for external technical engagement |

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
- **Foreground:** Vody end-to-end — the revenue ramp, the named enterprise customers, the raise,
  the hires, reporting to the CEO, owning the technical and product roadmap; breadth (code + tech
  lead + pitching + business building); speaking and storytelling; UPMC pitching to SVPs/CTO and
  identifying $M opportunities. **Speaking and storytelling is carried by bullets, not by a talks
  section** (changed 2026-08-24, user): `vody-fundraising` (writing and presenting VC pitches),
  `upmc-pitching` (SVPs and the CTO), and `cmu-teach` (a graduate course for 100+ students) each
  attach the claim to money or scale, which a panel appearance does not.
  - **Take every Vody number from the library** — the `vody` role's `context` / `team` fields and
    the `vody-arr` / `vody-fundraising` bullets. This section names *which* facts to foreground and
    deliberately does not restate them: the figures written here in July 2026 (ARR, amount raised,
    headcount) were all stale within weeks, and a foreground list is the last place anyone thinks
    to look for a stale number. Same discipline as §1 keeping the spine in the library.
- **Compress:** publications to the budget below — credibility signal, not the point. Big-co
  process detail. **Academic leadership is no longer compressed** (changed 2026-08-24, user): the
  chair roles, editorial board, and organized workshops are a differentiator for the Chief
  Scientist end of this archetype's title range — hiring leverage, conference presence, and
  academic-recruiting pull are things a Series B–D company standing up an AI function is buying.
  "Service" undersells it; render it as *leadership*.
- **Section order:** Summary → Experience → Selected Publications & Academic Leadership →
  Skills → Education. Publications sit above Skills for the same reason as in A: they are
  evidence, and Skills is a keyword surface. This makes C's section order identical to A's —
  intentional. A and C are differentiated by bullet selection, summary, and Skills grouping, not
  by where the headings sit.
- **Keyword emphasis:** 0→1, founding, GTM, ARR, fundraising, enterprise customers, roadmap,
  hiring, hands-on, LLM, agents, product strategy.
- **Publication budget:** 2–3 one-line entries, or a single line plus Scholar link. Do not spend
  the promoted academic block on a fourth paper — the chair roles differentiate more than another
  citation does.
  **Academic record budget** (rewritten 2026-08-24, user): publications and academic leadership
  merge into **one** section with bolded sub-labels — one heading, not two, because C is the most
  compressed archetype and two headings spend chrome on a short block. Inside it: a
  **conference-leadership** line (chair roles, editorial board, senior PC) and an **organized
  workshops** line, both compact and multi-year per §3.
  - **No "Selected Talks & Speaking" section.** Dropped 2026-08-24 (user): the talk record is
    three stale healthcare entries at venues a non-specialist doesn't recognize, and on a page
    arguing "I built an AI function from zero inside a real business" they date the résumé and
    pull it toward a healthcare identity.
  - **The one keynote stays**, as a single labeled line inside the merged block: it is current,
    it states this archetype's thesis out loud (startup + GenAI + from-the-trenches), and it is
    the only concrete anchor for the summary's "conference audiences" claim and the Skills entry
    for public speaking — without it both are orphans under §4. Rank per §3 (keynote first); the
    invited talks, panels, and judging stay off.

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
- Don't leave orphan skills. Anything in the Skills section must be traceable to experience, a
  specific claim in the Summary, a publication, or a named project in the same document (§4).
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
- **Condensed citation form is the default.** Render `citation` compressed: authors, year, title,
  then the venue in short form — *ICLR 2026*, *SIGIR 2017*, *ACM Transactions on Information
  Systems (TOIS)*, *eCom'25: ACM SIGIR Workshop on eCommerce*. Drop "In Proceedings of the Nth
  International …", volume and issue numbers, and page ranges: each costs a line across a list
  and no reader checks them. **The words carrying the venue tier are not droppable** — "Workshop"
  stays in a workshop citation, "Under review at X" stays on under-review work, and a journal
  keeps its journal name. This is the one place a variant deliberately does not reproduce the
  library string verbatim; every other fact in the citation is unchanged.
- **Don't state a publication twice.** When a variant lists the paper in Publications, the
  experience bullet does not also name it — "lessons published at eCom'25" is the same claim two
  inches apart, and it costs line length in the block where space is tightest. Library bullets
  therefore stay clean of publication pointers. The exception is a variant whose publication list
  is cut so far that the paper is not listed at all: there, naming it in the bullet is the only
  place the work appears, so name it.
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
- **Workshops are service, never publications.** Render the `workshops` entries in
  `academic-record.yaml` under an Academic Service / Academic Leadership heading — never in a
  Publications section, where they would read as papers.
- **"Organized" is sufficient; the "Co-" prefix is optional.** These events are co-organized, and
  the earlier rule required saying so explicitly. Dropped 2026-08-19 (user): in IR, workshops are
  effectively never solo-organized, so a reader in the field takes co-organization as given, and
  "Co-organized workshops" spends a word on something nobody misreads. Either form is correct —
  what must stay explicit is that the entry is an *organizing* role, not a paper.
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
   surviving bullet in Experience, **a claim stated in the Summary**, a listed publication, or a
   named project in the same document. If a reader can't answer "where did they use this?", the
   skill is a liability. The Summary counts because a claim made there is on the page and
   defensible in the interview — that is the whole test (added 2026-08-19: archetype B moves
   mentorship into the summary, which would otherwise orphan `technical mentorship`). It counts
   only when the summary makes the claim *specifically*: "technically mentored 6 PhD scientists"
   evidences technical mentorship; "deep ML expertise" evidences nothing.
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

**Archetype-specific phrasing — two mechanisms, and which one to use.** The same work often has
to read differently per archetype. Archetype B must make personal, hands-on execution explicit;
archetype A wants that same work stated neutrally (§2A keeps hands-on to a clause at most, §2B
gives it a named bullet). Two mechanisms cover this, and choosing between them is not a matter of
taste:

1. **Emphasis marker — same composition, a word of difference. No new entry.** The canonical
   `bullet:` text is **always neutral**: it never carries "Personally," "hands-on," or any other
   marker of who did the work. The bullet records that fact as the **`hands-on-ml` skill tag**
   instead, and archetypes B and C may render it with an explicit marker — "Built v1 … hands-on"
   — while A renders it neutral. The tag is the data; the marker is rendering. This is why
   `vody-attribute-tagging`, `vody-error-analysis`, and `etsy-experiment-success` read neutrally
   in the library and carry the marker on variant B.
2. **Alternate framing — different composition. Separate entry.** When an archetype needs the same
   facts *composed* differently — a different lead clause, two bullets merged into one, the
   people-management mechanics dropped — that is a second bullet with its own `id`, its own
   `archetypes[]`, and a comment naming the sibling(s) it must never render beside. Existing sets:
   `xrole-ic-growth` (B) vs `xrole-promos-calibration` (A); `upmc-ml-applied-lead` (B) vs
   `upmc-ml-applications` + `upmc-ml-team` (A).

**Choosing.** If the difference is emphasis only and every fact, number, and named technology is
identical, use mechanism 1 — a second entry would fork one fact across two places that then drift
apart. If the lead clause changes, or facts are added, dropped, or merged, use mechanism 2 — an
"emphasis marker" that quietly changes what the bullet claims is invention in a rendering costume.
**There is no third option:** a variant may never carry bullet text that no library entry supports
under one of these two.

`team` and `management` are prose fields holding durable facts; §1 holds the rules for
rendering them (notably: name the aggregate PhD-scientist count on the page, summed from these
fields — never copied from an older variant).

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
