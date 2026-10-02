# Yubin Kim

yubink.cs@gmail.com · 412-204-7134 · Pittsburgh, PA (Eastern time, remote) · [Google Scholar](https://scholar.google.com/citations?user=3F_QHHQAAAAJ)

## Summary

Machine learning engineering manager with 15+ years in ML and 7+ leading teams of machine learning engineers and data scientists who own production ML on consumer product surfaces, with an active publication record in search and recommender systems. At Etsy I led the search retrieval team behind a two-sided marketplace of 90M+ active buyers and 100M items, delivering $70M+ in GMS and ad revenue validated by A/B experiments, and doubling both experiment velocity and experiment success rate by rebuilding the team's offline evaluation and A/B testing processes through cross-functional collaboration. At Vody I built the team from zero, grew revenue 0 → $2.5M, and took fine-tuned LLM pipelines into production end to end, from data collection through productionization and monitoring. I coach ICs to Staff+ and have led fully remote teams throughout. PhD from Carnegie Mellon University in computer science.

**Coaching and team leadership track record:** built Vody's team from zero (11 hires); managed 6 PhD scientists across Vody and Etsy; delivered 3 IC promotions (2 at Etsy, 1 at UPMC), 2 of them to Staff level; participated in leveling calibration at Etsy and UPMC; performance-managed out 4 low performers across UPMC, Etsy, and Vody.

## Experience

### Chief Science Officer — Vody — 01/2024–present
*Seed-stage e-commerce startup with $B enterprise customers, built from 0 → $2.5M revenue; owned the technical/product roadmap and technical sales; reported to the CEO.*

- Hired 11 and led a fully remote team of ~11 across science, engineering, UX, product, and ops
- Grew revenue 0 → $2.5M ARR by converting Grubhub and Academy Sports & Outdoors into customers, and serving as their primary technical contact.
- Optimized e-commerce product data feeds for conversational agents and product search, improving customer GMV by 10%+.
- Personally built v1 of the production attribute-tagging models by fine-tuning Qwen VLMs with SFT + LoRA.
- Trained and scaled efficient, distilled BERT-based classifiers for Grubhub's 50M item catalog; built datasets for training/evaluation from scratch, and built efficient daily inference data pipelines with Airflow.
- Fine-tuned and productionized RAG + LLM pipeline on vLLM and Kubernetes for a 150k+ product catalog.
- Productionized continuous model evaluation and monitoring with human-in-the-loop review and LLM-based evaluation.

### Adjunct Instructor — Carnegie Mellon University — 08/2025–12/2025

- Taught *[Large Language Models: Methods and Applications](https://2025.cmu-llms.org/)*, a graduate-level course for 100+ students.

### Senior Engineering Manager, Search Retrieval — Etsy — 04/2022–10/2023
*Built real-time, low-latency, large-scale retrieval systems powering search, recommendations, and ads at etsy.com, a two-sided marketplace of 90M+ active buyers and 100M items.*

- Led, coached, and developed a fully remote product ML team of ~5 machine learning and engineering ICs up to Sr. Staff level, including 3 PhD scientists; technical mentorship, hiring (3), performance management, career development, and team processes.
- Generated $40M+ in GMS over 1.5 years by increasing conversion, validated by A/B experiments: Solr improvements, personalization in retrieval, and Etsy's first GNN embeddings, initialized for cold-start items and served from a Faiss ANN index.
- Generated $30M+ in A/B-validated ad revenue by increasing CTR through cross-org collaboration with the Ads team.
- Doubled the success rate of online experiments within 2 quarters by developing robust offline evaluation metrics and processes.
- Doubled online experiment velocity by partnering with analytics, product, and platform teams to build new tooling, e.g. interleaving tests, end-to-end model testing.
- Co-authored the 3-year technical strategy for the Search Retrieval initiative.

### Director of Technology — UPMC Enterprises — 07/2019–03/2022

- Led an applied ML team of ~3 ML engineers; created career paths and owned hiring (1), performance management, and technical mentorship; delivered 1 promotion and managed out 1 low performer.
- Led a product team of ~12 engineering/QA ICs and product/engineering managers, building an Elasticsearch-based search engine over 160M+ clinical documents.
- Identified ML projects worth $Ms in savings, pitched to SVPs and the CTO, developed prototypes, and executed pilots partnering with provider/payor stakeholders.

### Senior Data Scientist — UPMC Enterprises — 09/2018–07/2019

## Selected Publications & Academic Leadership

- Yujiang Wu, Shanshan Zhong, **Yubin Kim**, Chenyan Xiong. 2026. [What Generative Search Engines Like and How to Optimize Web Content Cooperatively](https://arxiv.org/abs/2510.11438). *ICLR 2026*.
- **Yubin Kim**, Arthur Maciejewicz, Brandon Beveridge. 2025. [Lessons from the bleeding edge: large-scale production inference of LLMs](https://ceur-ws.org/Vol-4123/paper_31.pdf). *eCom'25: ACM SIGIR Workshop on eCommerce*.
- Jon Eskreis-Winkler, **Yubin Kim**, Andrew Stanton. 2023. [XWalk: Random Walk Based Candidate Retrieval for Product Search](https://ceur-ws.org/Vol-3589/paper_22.pdf). *eCom'23: ACM SIGIR Workshop on eCommerce*.
- Nicola Ferro, **Yubin Kim**, Mark Sanderson. 2019. Using Collection Shards to Study Retrieval Performance Effect Sizes. *ACM Transactions on Information Systems (TOIS)* 37(3), 1–40.

Full list on [Google Scholar](https://scholar.google.com/citations?user=3F_QHHQAAAAJ).

**Academic leadership:** Organizer, Workshop on eCommerce @ SIGIR (2023–2026) and Workshop on Data Quality-Aware Multimodal Recommendation @ RecSys (2025–2026); Sponsorship Chair, SIGIR (2026); AnalytiCup Chair, CIKM (2026); Demonstration Track Chair, SIGIR (2025).

## Skills

- **Leadership & management:** coaching machine learning engineers and data scientists, career development, performance management & feedback, hiring & team building, leveling calibration, technical mentorship (to Sr. Staff), technical strategy & multi-year planning, cross-functional partnership (product, software engineering, UX, analytics), cross-org influence, distributed/remote team leadership, executive communication
- **Search & recommedations at scale:** search, candidate retrieval, recommendations, personalization, cold-start, embeddings, ANN indexing, graph ML, graph neural networks, ads retrieval, conversion, CTR, real-time low-latency large-scale systems, two-sided marketplace ML
- **Experimentation & measurement:** A/B testing, experimental design, interleaving tests, experiment velocity, offline evaluation metrics, experiment analysis, ML & experimentation process design, LLM-based evaluation, human-in-the-loop evaluation
- **Full-stack ML lifecycle:** data collection, aggregation, and dataset construction, model development, production ML at scale, productionization & deployment, continuous evaluation & model monitoring, data pipelines, GPU-efficient inference
- **LLMs & generative AI:** large language models, LLM fine-tuning (SFT, LoRA), VLM fine-tuning (Qwen), multimodal models, RAG, LLM inference & serving, conversational agents, model distillation, BERT
- **Tools & platforms:** Python, SQL, PyTorch, Hugging Face, Solr, Elasticsearch, Faiss, vLLM, Kubernetes, Airflow, AWS, GCP, Jupyter
- **Domains:** two-sided marketplace & e-commerce, consumer product ML, healthcare / clinical NLP

## Education

- Ph.D., Computer Science — Language Technologies Institute, Carnegie Mellon University (Dec 2018)
- B.S., Software Engineering — University of Waterloo (Apr 2011)
