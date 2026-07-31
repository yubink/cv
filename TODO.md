# TODO.md — Current State, Open Questions, and Migration Notes

Point-in-time information. Nothing here is a durable rule — durable rules live in
`CONTEXT.md` and the skills. Delete items as they resolve.

**Last updated:** 2026-07-30

---

## 1. Build order

0. ~~Create `academic-record.yaml`~~ — **done 2026-07-30**, seeded from the current CV
   including its commented-out talks, panels, and workshop entries. Verify completeness
   against memory (§4.2).
1. ~~Create `publication-library.yaml`~~ — **done 2026-07-30**, 15 entries from the Scholar
   export plus the under-review eCSM paper and the previously commented-out IRJ 2017 paper.
   Workshop-overview papers for co-organized workshops excluded by design (they live in
   `academic-record.yaml`). Two `work_origin` values flagged `# VERIFY` in the file
   (`ctr26-rumination`, `sigir22-dense-retrieval`) — user to confirm.
2. ~~Create `bullet-library.yaml`~~ — **seeded 2026-07-30**: 26 bullets (12 marked
   `evidence_strength: weak` with bracketed placeholders keyed to the §3 questions), plus a
   generated `skills_evidence_matrix`. Regenerate the matrix after editing any `skills[]`
   field: `python3 scripts/gen_matrix.py` from the resume-system root. Remaining work: fill
   placeholders as §3 answers arrive; decompose `vody-serving-stack` (the legacy tool-dump
   remnant).
3. **Build the three base variants** via the build-variant skill. Suggested order: B (largest
   structural change from the current CV), then A, then C.
4. Retire the legacy CV as a source document once the libraries capture everything in it.

---

## 2. Legacy source files

- `prettycv.html` — the current single master CV. Two-column layout with a floated sidebar
  (ATS risk — CONTEXT.md §3 bans this format going forward). Contains commented-out content
  that must be recovered into the libraries before retirement: keynotes, panels, invited
  talks, and additional publications.
- `_Yubin_Kim__-__Google_Scholar_.html` — Scholar export; source for the complete publication
  list.

---

## 3. Open evidence questions

Answers feed `bullet-library.yaml`. **Do not fabricate values.** A bullet needing one of
these is `evidence_strength: weak` until answered.

**Etsy (blocks A and B)**
- QPS, p99 latency, index size, requests/day for the retrieval systems.
- Highest IC level managed — were there Staff or Sr. Staff direct reports?
- Attribution method for the $40M GMS; sole vs. shared with partner teams.
- On-call / reliability / SLO ownership.
- *Mechanism* for 2x experiment velocity and 2x offline-online success rate.

**Vody (blocks B and C)**
- Production LLM inference numbers from the eCom'25 work: GPU cost reduction, tokens/sec,
  quantization, batching strategy.
- Fine-tuning specifics: LoRA/QLoRA/full SFT, dataset size, eval methodology, lift over
  baseline.
- **Agent work** — tool use, multi-step orchestration. Highest-value missing keyword in the
  current market.
- Total raised, customer count, retention/renewals.
- Budget, comp decision, and vendor negotiation ownership.

**UPMC (blocks applications to healthcare employers)**
- Realized vs. pipeline savings.
- PHI/HIPAA, model governance, clinical validation experience.
- Dollar scale of contracts negotiated.

**Cross-cutting**
- Where former reports are now; any who followed between companies.
- Full list of keynotes/talks/panels (partially recoverable from the commented-out HTML).
- Infrastructure beyond the listed stack: Spark, Ray, Kafka/Flink, feature stores,
  Triton/TensorRT.
- Patents, open source, advisory/board roles, teaching.
- Whether any eval harness or LLM-judge framework was built as a durable asset vs. ad hoc.

---

## 4. Migration notes from the current CV

### 4.1 Suspected orphan skills

The current CV's Skills sidebar lists items with no evidence bullet. Resolve each during
library construction — cut, evidence with a real bullet, or foundational tier:

- Learning-to-rank — evidenced only by the SIGIR 2017 "Learning to Rank Resources" paper.
  The paper is sufficient evidence to keep the skill; an Etsy bullet would make it stronger.
- Query understanding — no bullet names it. Vody's query enrichment work would evidence it,
  but that work isn't in any bullet yet. Evidence question, not a cut.
- Semantic search / two-tower dense retrieval via ANN — ANN appears only in the Vody tool
  dump; the two-tower claim has no bullet.
- PyTorch, Scikit-learn — no bullet names either.
- Airflow, Metaflow, LangChain — no bullet names any of the three.
- Lucene — Solr (Etsy) and Elasticsearch (UPMC) are evidenced; Lucene itself is not.
- Cursor, Claude Code, vim, git — foundational tier at most. Cursor and Claude Code are a
  worthwhile currency signal in 2026; vim and git are noise and can go.

### 4.2 Recovery from commented-out HTML — mostly done

Talks, panels, judging, and the commented-out WSDM 2020 workshop are now captured in
`academic-record.yaml` (2026-07-30). Remaining:

- User to verify `academic-record.yaml` for completeness — anything delivered but never
  written into the HTML (recent 2025–2026 talks especially).
- Two talk entries have empty titles (SIRIP 2023 panel; CMU capstone judging) — fill in
  official titles if they exist.
- ~~Commented-out publication (Efficient Distributed Selective Search, IRJ 2017)~~ —
  recovered into `publication-library.yaml` as `irj17-selective-search`.

### 4.2b Workshop block mislabeling in the legacy CV

The current CV lists the co-organized workshops ("Recent peer-reviewed workshops") **inside
the Selected Publications section**, where they read as papers rather than organizing roles.
Per the user (2026-07-30) these are co-organized events — i.e. service. CONTEXT.md §3 now
requires them rendered as service with the organizing role explicit; score-resume item 10
treats the old placement as a blocker. Fix during variant construction; also check LinkedIn
for the same mislabeling during the sync pass (§5).

### 4.3 Known bullet-quality issues to fix during library construction

- The Vody tool-dump bullet ("Utilized fine-tuned multimodal LLMs, RAG, CLIP, BERT, graph
  models served with vLLM, ANN, Kubernetes on AWS and GCP") violates the tool-budget rule.
  Decompose into 2–3 bullets, each with an outcome and 1–3 technologies.
- "Owned technical and product roadmap, primary point of contact for customers" — ownership
  verb without result; needs an outcome or merging into one.
- Several UPMC bullets list techniques (LSTM, CNN, time series, decision trees) without
  outcomes.

### 4.4 Not-on-resume items (handle live, strategize separately)

- Employment gap 10/2023 → 04/2024 (~6 months): prepare a verbal answer; do not draw
  layout attention to it.
- Reason for leaving Vody / "did it fail?" question: deliberately not on the resume; needs a
  prepared conversational framing before recruiter screens begin.

---

## 5. Deferred decisions

- Designed-PDF rendering pipeline for the human-facing artifact (the variants themselves are
  the ATS-safe plain versions). Decide tooling when the first variant is done.
- ~~Whether to add a talks/speaking library~~ — resolved 2026-07-30: `academic-record.yaml`
  holds talks, service, and co-organized workshops.
- LinkedIn synchronization pass once variant A or B is final (CONTEXT.md §3: no
  contradictions between resume, LinkedIn, Scholar). Include the workshop-mislabeling check
  from §4.2b.
