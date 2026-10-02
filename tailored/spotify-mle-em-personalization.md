# Yubin Kim

yubink.cs@gmail.com · 412-204-7134 · Pittsburgh, PA (Eastern time, remote) · [Google Scholar](https://scholar.google.com/citations?user=3F_QHHQAAAAJ)

## Summary

Technical machine learning leader with 15+ years in ML and 7+ building and leading multi-disciplinary teams that own personalized search and recommendation models in production at scale, with an active publication record and academic leadership (SIGIR, RecSys, CIKM, WSDM, ICLR). Led the Etsy ML team behind the retrieval systems powering search, recommendations, and ads for a two-sided marketplace of 90M+ active buyers and 100M items, generating $70M+, validated by A/B experiments. At Vody I built the team from zero, grew revenue 0 → $2.5M, and took fine-tuned LLM pipelines into production, championing generative AI where it creates real user value. I set technical direction, coach engineers and scientists to Staff+, and have led fully remote teams throughout. PhD from Carnegie Mellon University in computer science.

**Coaching and team leadership track record:** built Vody's team from zero (11 hires); managed PhD scientists at both Vody and Etsy; delivered 3 IC promotions (2 at Etsy, 1 at UPMC), 2 of them to Staff level; participated in leveling calibration at Etsy and UPMC; performance-managed out 4 low performers across UPMC, Etsy, and Vody.

## Experience

### Chief Science Officer — Vody — 01/2024–present
*Seed-stage e-commerce startup with $B enterprise customers, built from 0 → $2.5M revenue; owned the technical and product roadmap.*

- Optimized product data feeds for conversational agents and product search, improving customer GMV by 10%+.
- Grew revenue 0 → $2.5M ARR by converting Grubhub and Academy Sports & Outdoors into customers, and served as their primary technical contact.
- Fine-tuned and productionized RAG + LLM pipeline on vLLM and Kubernetes for a 150k+ product catalog; lessons published at the SIGIR eCom'25.
- Trained and scaled efficient, distilled BERT-based classifiers for Grubhub's 50M item catalog; built datasets for training/evaluation from scratch, and built efficient daily inference data pipelines with Airflow.
- Productionized continuous model evaluation with human-in-the-loop review and LLM-based evaluation.
- Hired 11 and led a fully remote team of ~11 across science, engineering, product, and ops, including PhD scientists.
- Personally built v1 of the production attribute-tagging models by fine-tuning Qwen VLM with SFT + LoRA.
- Initiated academic collaborations on generative engine optimization (using LLMs fine-tuned with GRPO) and user simulation, yielding peer-reviewed publications (ICLR 2026; WSDM under review).

### Adjunct Instructor — Carnegie Mellon University — 08/2025–12/2025

- Taught *[Large Language Models: Methods and Applications](https://2025.cmu-llms.org/)*, a graduate-level course for 100+ students.

### Senior Engineering Manager, Search Retrieval — Etsy — 04/2022–10/2023
*Built real-time, low-latency, large-scale retrieval systems powering search, recommendations, and ads at etsy.com, a two-sided marketplace of 90M+ active buyers and 100M items.*

- Generated $40M+ in GMS over 1.5 years by increasing conversion, validated by A/B experiments: Solr improvements, personalization in retrieval, and Etsy's first GNN embeddings, initialized for cold-start items and served from a Faiss ANN index.
- Generated $30M+ in ad revenue by increasing CTR through cross-org collaboration with the Ads team.
- Led, coached, and developed a fully remote team of ~5 machine learning and engineering ICs up to Sr. Staff level, including PhD scientists; technical mentorship, hiring (3), performance management, career development, and team processes.
- Doubled the success rate of online experiments within 2 quarters by developing robust offline evaluation metrics and processes.
- Doubled online experiment velocity by partnering with analytics, product, and platform teams to build new tooling, e.g. interleaving tests, end-to-end model testing.
- Co-authored the 3-year technical direction and roadmap for the Search Retrieval initiative.

### Director of Technology — UPMC Enterprises — 07/2019–03/2022

- Led an applied ML team of ~3 ML engineers; created career paths and owned hiring (1), performance management, and technical mentorship; delivered 1 promotion and managed out 1 low performer.
- Led a product team of ~12 engineering/QA ICs and product/engineering managers, building an Elasticsearch-based search engine over 160M+ clinical documents.
- Identified ML projects worth $Ms in savings, pitched to SVPs and the CTO, developed prototypes, and executed pilots partnering with provider/payor stakeholders.

### Senior Data Scientist — UPMC Enterprises — 09/2018–07/2019

## Selected Publications & Academic Leadership

- Yujiang Wu, Shanshan Zhong, **Yubin Kim**, Chenyan Xiong. 2026. [What Generative Search Engines Like and How to Optimize Web Content Cooperatively](https://arxiv.org/abs/2510.11438). *ICLR 2026*.
- Jon Eskreis-Winkler, **Yubin Kim**, Andrew Stanton. 2023. [XWalk: Random Walk Based Candidate Retrieval for Product Search](https://ceur-ws.org/Vol-3589/paper_22.pdf). *eCom'23: ACM SIGIR Workshop on eCommerce*.
- **Yubin Kim**, Arthur Maciejewicz, Brandon Beveridge. 2025. [Lessons from the bleeding edge: large-scale production inference of LLMs](https://ceur-ws.org/Vol-4123/paper_31.pdf). *eCom'25: ACM SIGIR Workshop on eCommerce*.
- Nicola Ferro, **Yubin Kim**, Mark Sanderson. 2019. Using Collection Shards to Study Retrieval Performance Effect Sizes. *ACM Transactions on Information Systems (TOIS)* 37(3), 1–40.

Full list on [Google Scholar](https://scholar.google.com/citations?user=3F_QHHQAAAAJ).

**Academic leadership:** Organizer, Workshop on Data Quality-Aware Multimodal Recommendation @ RecSys (2025–2026) and Workshop on eCommerce @ SIGIR (2023–2026); Sponsorship Chair, SIGIR (2026); Demonstration Track Chair, SIGIR (2025); AnalytiCup Chair, CIKM (2026); WSDM Cup Chair, WSDM (2026).

## Skills

- **Leadership & management:** leading and developing high-performing ML engineering teams, coaching & mentoring (to Sr. Staff), career development, performance management & feedback, hiring & recruiting, leveling calibration, technical direction & roadmap, cross-functional partnership, cross-org influence, distributed/remote team leadership
- **Personalization & recommendations:** recommendations, personalization, ranking, candidate retrieval, embedding-based retrieval, ANN indexing, cold-start, graph ML, graph neural networks, ads retrieval, real-time large-scale systems
- **LLMs & generative AI:** large language models, LLM fine-tuning (GRPO, SFT, LoRA), VLM fine-tuning (Qwen), multimodal models, RAG, LLM inference & serving, generative AI applications, conversational agents, generative engine optimization, model distillation, BERT, transformer-based models
- **ML lifecycle & production:** production ML at scale, end-to-end ML lifecycle, training & evaluation dataset construction, production deployment, continuous evaluation & model monitoring, data pipelines, GPU-efficient inference
- **Experimentation & measurement:** A/B experimentation, interleaving tests, experiment velocity, offline evaluation metrics, quality & relevance measurement, LLM-based evaluation, human-in-the-loop evaluation
- **Tools & platforms:** PyTorch, Hugging Face, Python, SQL, Solr, Elasticsearch, Faiss, vLLM, Kubernetes, Airflow, AWS, GCP, Jupyter
- **Domains:** large-scale consumer marketplace & e-commerce, healthcare / clinical NLP

## Education

- Ph.D., Computer Science — Language Technologies Institute, Carnegie Mellon University (Dec 2018)
- B.S., Software Engineering — University of Waterloo (Apr 2011)
