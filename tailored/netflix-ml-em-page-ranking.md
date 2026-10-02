# Yubin Kim

yubink.cs@gmail.com · 412-204-7134 · Pittsburgh, PA (remote) · [Google Scholar](https://scholar.google.com/citations?user=3F_QHHQAAAAJ)

## Summary

Technical applied ML leader with 15+ years in machine learning and 7+ building and leading multi-disciplinary teams that own personalized search and recommendations models in production at consumer scale, with an active publication record. Led the Etsy ML team behind the real-time, low-latency retrieval systems serving search, recommendations, and ads for a two-sided marketplace of 90M+ active buyers and 100M items, generating $70M+, validated by A/B experiments. At Etsy, I led the shift from traditional random-walk graph ML to graph neural networks and CLIP embeddings. At Vody, I led the productionization of fine-tuned LLMs from zero. I set technical vision and roadmap, mentor PhD and Staff+ ICs, and have led fully remote teams throughout. PhD from Carnegie Mellon University in computer science, with a dissertation on large-scale distributed search.

**Team leadership track record:** built Vody's team from zero (11 hires); managed PhD scientists at both Vody and Etsy; delivered 3 IC promotions (2 at Etsy, 1 at UPMC), 2 of them to Staff level; participated in leveling calibration at Etsy and UPMC; performance-managed out 4 low performers across UPMC, Etsy, and Vody.

## Experience

### Chief Science Officer — Vody — 01/2024–present
*Seed-stage e-commerce startup with $B enterprise customers, built from 0 → $2.5M revenue; owned the technical/product roadmap and technical sales.*

- Optimized e-commerce product data feeds for conversational agents and product search, improving customer GMV by 10%+.
- Grew revenue 0 → $2.5M ARR by converting Grubhub and Academy Sports & Outdoors into customers, and served as their primary technical contact.
- Raised $1.6M in funding by writing/presenting pitches to VCs.
- Fine-tuned and productionized RAG + Qwen VLM pipeline on vLLM and Kubernetes for a 150k+ product catalog.
- Trained and scaled efficient, distilled BERT-based classifiers for Grubhub's 50M item catalog; built datasets for training/evaluation from scratch, and built efficient daily inference data pipelines with Airflow.
- Productionized continuous model evaluation with human-in-the-loop review and LLM-based evaluation.
- Hired 11 and led a fully remote team of ~11 across science, engineering, product, and ops, including PhD scientists.
- Initiated academic collaborations on generative engine optimization (using LLMs fine-tuned with GRPO) and e-commerce user simulation, yielding peer-reviewed publications (ICLR 2026; WSDM under review).

### Adjunct Instructor — Carnegie Mellon University — 08/2025–12/2025

- Taught *[Large Language Models: Methods and Applications](https://2025.cmu-llms.org/)*, a graduate-level course for 100+ students.

### Senior Engineering Manager, Search Retrieval — Etsy — 04/2022–10/2023
*Built real-time, low-latency, large-scale retrieval systems powering search, recommendations, and ads at etsy.com, a two-sided marketplace of 90M+ active buyers and 100M items.*

- Generated $40M+ in GMS over 1.5 years by increasing conversion, validated by A/B experiments: Solr improvements, personalization in retrieval, CLIP embeddings, and Etsy's first GNN embeddings, initialized for cold-start items and served from a Faiss ANN index.
- Generated $30M+ in ad revenue by increasing CTR through cross-org collaboration with the Ads team.
- Led a fully remote product ML team of ~5 science and engineering ICs up to Sr. Staff level, including PhD scientists; technical mentorship, hiring (3), performance management, and team processes.
- Doubled the success rate of online experiments within 2 quarters by developing robust offline evaluation metrics and processes.
- Doubled online experiment velocity by partnering with analytics, product, and platform teams to build new tooling, e.g. interleaving tests, end-to-end model testing.
- Co-authored the 3-year technical vision and roadmap for the Search Retrieval initiative.

### Director of Technology — UPMC Enterprises — 07/2019–03/2022

- Led an applied ML team of ~3 ML engineers; created career paths and owned hiring (1), performance management, and technical mentorship.
- Led a product team of ~12 engineering/QA ICs and product/engineering managers, building an Elasticsearch-based search engine over 160M+ clinical documents.
- Identified ML projects worth $Ms in savings, pitched to SVPs and the CTO, developed prototypes, and executed pilots partnering with provider/payor stakeholders.

### Senior Data Scientist — UPMC Enterprises — 09/2018–07/2019

## Selected Publications & Academic Leadership

- Yujiang Wu, Shanshan Zhong, **Yubin Kim**, Chenyan Xiong. 2026. [What Generative Search Engines Like and How to Optimize Web Content Cooperatively](https://arxiv.org/abs/2510.11438). *ICLR 2026*.
- **Yubin Kim**, Arthur Maciejewicz, Brandon Beveridge. 2025. [Lessons from the bleeding edge: large-scale production inference of LLMs](https://ceur-ws.org/Vol-4123/paper_31.pdf). *eCom'25: ACM SIGIR Workshop on eCommerce*.
- Jon Eskreis-Winkler, **Yubin Kim**, Andrew Stanton. 2023. [XWalk: Random Walk Based Candidate Retrieval for Product Search](https://ceur-ws.org/Vol-3589/paper_22.pdf). *eCom'23: ACM SIGIR Workshop on eCommerce*.
- Zhuyun Dai, **Yubin Kim**, Jamie Callan. 2017. [Learning to Rank Resources](https://www.cs.cmu.edu/~callan/Papers/sigir17-Zhuyun-Dai.pdf). *SIGIR 2017*, 837–840.

Full list on [Google Scholar](https://scholar.google.com/citations?user=3F_QHHQAAAAJ).

**Academic leadership:** Organizer, Workshop on Data Quality-Aware Multimodal Recommendation @ RecSys (2025–2026) and Workshop on eCommerce @ SIGIR (2023–2026); Sponsorship Chair, SIGIR (2026); Demonstration Track Chair, SIGIR (2025); AnalytiCup Chair, CIKM (2026); WSDM Cup Chair, WSDM (2026).

## Skills

- **Leadership & management:** leading and growing applied ML teams, hiring & team building, technical mentorship (to Sr. Staff), career development, performance management, leveling calibration, technical vision & roadmap, cross-functional stakeholder management, cross-org influence, executive communication, distributed/remote team leadership
- **Ranking, retrieval & personalization:** ranking, learning to rank, listwise ranking, recommender systems, personalization, candidate retrieval, embeddings, ANN indexing, cold-start, graph ML, graph neural networks, search, ads retrieval, conversion, real-time low-latency serving
- **Generative & LLM methods:** large language models, LLM fine-tuning (GRPO, SFT, LoRA), VLM (Qwen), RAG, LLM inference & serving, generative AI applications, conversational agents, generative engine optimization, model distillation, BERT, transformer-based models
- **ML production lifecycle:** large-scale production ML, data pipelines, training & evaluation dataset construction, production deployment & serving, continuous model evaluation, GPU-efficient inference
- **Experimentation & measurement:** A/B experimentation, experimentation strategy, interleaving tests, experiment velocity, offline evaluation metrics, LLM-based evaluation, human-in-the-loop evaluation
- **Tools & platforms:** PyTorch, Hugging Face, Python, SQL, Solr, Elasticsearch, Faiss, vLLM, Airflow, Kubernetes, AWS, GCP, Jupyter
- **Domains:** consumer marketplace search & recommendations, healthcare / clinical NLP

## Education

- Ph.D., Computer Science — Language Technologies Institute, Carnegie Mellon University (Dec 2018)
- B.S., Software Engineering — University of Waterloo (Apr 2011)
