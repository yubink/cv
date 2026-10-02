# Yubin Kim

yubink.cs@gmail.com · 412-204-7134 · Pittsburgh, PA (remote-friendly) · [Google Scholar](https://scholar.google.com/citations?user=3F_QHHQAAAAJ)

## Summary

Principal-level applied scientist with 15+ years in information retrieval and machine learning, spanning search, semantic retrieval, recommendations, and LLMs, combining research depth, production experience, business impact, and organizational influence. Owns problem spaces end-to-end: identifying new opportunities, prototyping and experimenting hands-on, then scaling what works through technical direction and mentorship. At Etsy, led the team behind the real-time retrieval powering search, recommendations, and ads for a 90M+ buyer, 100M-item marketplace, generating $70M+ in A/B-validated GMS and ad revenue. At Vody, built the ML org and productionized LLM and retrieval systems from zero while owning the technical and product roadmap, growing revenue from 0 to $2.5M. Grows senior ICs: delivered 3 IC promotions across Etsy and UPMC, 2 of them to Staff, and technically mentored 6 PhD scientists and ICs up to Sr. Staff. Has led fully remote, cross-functional teams throughout, collaborating across product, platform, and analytics orgs. Publishes in top-tier conferences and journals and holds leadership roles at SIGIR, CIKM, WSDM, and RecSys. PhD in Computer Science from Carnegie Mellon University, with a dissertation on large-scale distributed search.

## Experience

### Chief Science Officer — Vody — 01/2024–present
*Seed-stage e-commerce startup with $B enterprise customers; owned the technical and product roadmap; hired and led a multi-disciplinary, fully remote team of 11 across science, engineering, product, and ops.*

- Fine-tuned and productionized RAG + LLM pipeline on vLLM and Kubernetes for a 150k+ product catalog.
- Trained and scaled efficient, distilled BERT-based classifiers for Grubhub's 50M item catalog; built datasets for training/evaluation from scratch, and built efficient daily inference data pipelines with Airflow.
- Built v1 of the production attribute-tagging models by fine-tuning Qwen VLMs with SFT + LoRA hands-on.
- Productionized continuous model evaluation with human-in-the-loop review and LLM-based evaluation.
- Initiated academic collaborations on generative engine optimization (using LLMs fine-tuned with GRPO) and e-commerce user simulation, yielding peer-reviewed publications (ICLR 2026; WSDM under review).
- Optimized e-commerce product data feeds for conversational agents and product search, improving customer GMV by 10%+.
- Drove opportunity and error analysis hands-on over production logs and customer query logs using DuckDB and Jupyter, feeding the product roadmap.
- Grew revenue 0 → $2.5M ARR by converting Grubhub and Academy Sports & Outdoors into customers, and serving as their primary technical contact.

### Adjunct Instructor — Carnegie Mellon University — 08/2025–12/2025

- Taught *[Large Language Models: Methods and Applications](https://2025.cmu-llms.org/)*, a graduate-level course for 100+ students.

### Senior Engineering Manager, Search Retrieval — Etsy — 04/2022–10/2023
*Led a fully remote team of ~5 science and engineering ICs to Sr. Staff level, building real-time, large-scale retrieval systems for search, recommendations, and ads at etsy.com — a two-sided marketplace of 90M+ active buyers and 100M items.*

- Generated $40M+ in GMS over 1.5 years by increasing conversion, validated by A/B experiments: Solr improvements, personalization in retrieval, and Etsy's first GNN embeddings, initialized for cold-start items and served from a Faiss ANN index.
- Doubled the success rate of online experiments within 2 quarters by developing robust offline evaluation metrics and processes hands-on.
- Doubled online experiment velocity by partnering with analytics, product, and platform teams to build new tooling, e.g. interleaving tests, end-to-end model testing.
- Co-authored the 3-year technical strategy for the Search Retrieval initiative.
- Generated $30M+ in A/B-validated ad revenue by increasing CTR through cross-org collaboration with the Ads team.

### Director of Technology — UPMC Enterprises — 07/2019–03/2022

- Led a product team of ~12 engineering/QA ICs and product/engineering managers, building an Elasticsearch-based search engine over 160M+ clinical documents.
- Identified ML projects worth $Ms in savings, pitched to SVPs and the CTO, developed prototypes, and executed pilots partnering with provider/payor stakeholders.

### Senior Data Scientist — UPMC Enterprises — 09/2018–07/2019

- Developed a search engine for social-determinants-of-health indicators across millions of clinical documents to identify high-risk patients for intervention.

## Select Publications

- Yujiang Wu, Shanshan Zhong, **Yubin Kim**, Chenyan Xiong. 2026. [What Generative Search Engines Like and How to Optimize Web Content Cooperatively](https://arxiv.org/abs/2510.11438). *ICLR 2026*.
- **Yubin Kim**, Arthur Maciejewicz, Brandon Beveridge. 2025. [Lessons from the bleeding edge: large-scale production inference of LLMs](https://ceur-ws.org/Vol-4123/paper_31.pdf). *eCom'25: ACM SIGIR Workshop on eCommerce*.
- Jon Eskreis-Winkler, **Yubin Kim**, Andrew Stanton. 2023. [XWalk: Random Walk Based Candidate Retrieval for Product Search](https://ceur-ws.org/Vol-3589/paper_22.pdf). *eCom'23: ACM SIGIR Workshop on eCommerce*.
- Nicola Ferro, **Yubin Kim**, Mark Sanderson. 2019. Using Collection Shards to Study Retrieval Performance Effect Sizes. *ACM Transactions on Information Systems (TOIS)*.
- Zhuyun Dai, **Yubin Kim**, Jamie Callan. 2017. [Learning to Rank Resources](https://www.cs.cmu.edu/~callan/Papers/sigir17-Zhuyun-Dai.pdf). *SIGIR 2017*.
- **Yubin Kim**, Jamie Callan, J. Shane Culpepper, Alistair Moffat. 2017. [Efficient Distributed Selective Search](https://www.cs.cmu.edu/~callan/Papers/IRJ16-yubink.pdf). *Information Retrieval Journal*.

Full list on [Google Scholar](https://scholar.google.com/citations?user=3F_QHHQAAAAJ).

## Recent Academic Service

**Conference organization & program committees:** Sponsorship Chair, SIGIR (2026) · PC Area Chair, ICTIR (2026) · AnalytiCup Chair, CIKM (2026) · WSDM Cup Chair, WSDM (2026) · Demonstration Track Chair, SIGIR (2025) · Editorial board, *Foundations and Trends in Information Retrieval* (ongoing) · Senior PC, SIGIR / CIKM / WSDM / TheWebConf (ongoing)

**Organized workshops & panels:** Workshop on eCommerce @ SIGIR (2023–2026) · Workshop on Data Quality-Aware Multimodal Recommendation @ RecSys (2025–2026) · Workshop on Multimodal Search and Recommendations @ ICDM (2025) · Panel on Applications and Future of Dense Retrieval in Industry @ SIGIR (2022)

## Skills

- **Information retrieval & search:** information retrieval, search, semantic search, dense retrieval, candidate retrieval, embeddings, ANN indexing, learning-to-rank, listwise ranking, federated search, recommender systems, product search, personalization, cold-start, graph ML, graph neural networks, ads retrieval, CTR, conversion, real-time systems
- **LLMs & generative AI:** LLMs, LLM fine-tuning (SFT, LoRA, GRPO), vision-language models (Qwen), multimodal ML, RAG, LLM inference & serving, distributed inference, GPU-efficient inference, model distillation, BERT, conversational agents, generative engine optimization, user simulation
- **Evaluation, experimentation & data:** A/B experimentation, offline evaluation, evaluation methodology, experiment success & velocity, LLM-based evaluation, human-in-the-loop evaluation, interleaving test, training & evaluation dataset construction, data pipelines, error analysis, query-log analysis
- **Technical leadership & strategy:** multi-year technical strategy, technical direction, cross-functional partnership, cross-org influence, product strategy & roadmap, opportunity analysis, prototyping, academic research collaboration, technical mentorship, executive and customer-facing technical communication, technical teaching, distributed/remote team leadership
- **Platforms & domains:** Python, SQL, PyTorch, Hugging Face, Solr, Elasticsearch, Faiss, vLLM, Airflow, Kubernetes, DuckDB, Jupyter, AWS, GCP, production ML, e-commerce marketplace search, ads retrieval & monetization, clinical NLP / healthcare search, information extraction

## Education

- Ph.D., Computer Science — Language Technologies Institute, Carnegie Mellon University (Dec 2018)
- B.S., Software Engineering — University of Waterloo (Apr 2011)
