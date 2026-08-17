# Yubin Kim

yubink.cs@gmail.com · 412-204-7134 · Pittsburgh, PA (remote) · [Google Scholar](https://scholar.google.com/citations?user=3F_QHHQAAAAJ)

## Summary

Technical machine learning leader with 15+ years in ML and 7+ building and leading collaborative, multi-disciplinary teams that own search, retrieval, and GenAI models in production, with measurable business impact: $70M+ at Etsy, 0 → $2.5M at Vody. Led the Etsy ML team building real-time retrieval feeding search, recommendations, and ads for a two-sided marketplace of 90M+ active buyers and 100M items, where sparse, embedding-based and graph ML advances drove $40M+ in GMS and $30M+ in ad revenue, validated by A/B experiments. I define technical vision and long-term roadmap in ambiguous problem spaces, grow engineers and applied scientists to Staff+, and maintain an active publication record in search and recommender systems, having led fully remote teams throughout. PhD from Carnegie Mellon University in computer science, with a dissertation on large-scale distributed search.

**Team leadership track record:** built Vody's team from zero (11 hires); managed PhD scientists at both Vody and Etsy; managed/mentored Sr. Staff; delivered 3 IC promotions (2 at Etsy, 1 at UPMC), 2 of them to Staff level; participated in leveling calibration at Etsy and UPMC; performance-managed out 4 low performers across UPMC, Etsy, and Vody.

## Experience

### Chief Science Officer — Vody — 01/2024–present
*Seed-stage e-commerce startup with $B enterprise customers; owned the technical/product roadmap and technical sales.*

- Optimized e-commerce product data feeds for conversational agents and product search, improving customer GMV by 10%+.
- Grew revenue 0 → $2.5M ARR by converting Grubhub and Academy Sports & Outdoors into customers, and served as primary technical contact for customers.
- Raised $1.6M in funding by writing/presenting pitches to VCs.
- Trained and scaled efficient, distilled BERT-based classifiers for Grubhub's 50M item catalog; built datasets for training/evaluation from scratch, and built efficient daily inference data pipelines with Airflow.
- Fine-tuned and productionized RAG + LLM pipeline on vLLM and Kubernetes for a 150k+ product catalog; lessons published at the SIGIR eCom'25.
- Productionized continuous model evaluation with human-in-the-loop review and LLM-based evaluation.
- Hired 11 and led a fully remote team of ~11 across science, engineering, product, and ops, including PhD scientists.
- Initiated academic collaborations on generative engine optimization (using LLMs fine-tuned with GRPO) and e-commerce user simulation, yielding peer-reviewed publications (ICLR 2026; WSDM under review).

### Adjunct Instructor — Carnegie Mellon University — 08/2025–12/2025

- Taught *[Large Language Models: Methods and Applications](https://2025.cmu-llms.org/)*, a graduate-level course for 100+ students.

### Senior Engineering Manager, Search Retrieval — Etsy — 04/2022–10/2023
*Built real-time, low-latency, large-scale retrieval systems powering search, recommendations, and ads at etsy.com, a two-sided marketplace of 90M+ active buyers and 100M items.*

- Generated $40M+ in GMS through increasing conversion, validated by A/B experiments: graph ML and Solr retrieval improvements; personalization in retrieval; introducing Etsy's first GNN embeddings, initialized for cold-start items and served from a Faiss ANN index.
- Generated $30M+ in ad revenue by increasing CTR through cross-org collaboration with the Ads team.
- Led a fully remote product ML team of ~5 engineering and applied science ICs up to Sr. Staff level, including PhD scientists; technical mentorship, hiring (3), performance management, and team processes.
- Co-authored the 3-year technical vision and roadmap for the Search Retrieval initiative.
- Doubled the success rate of online experiments within 2 quarters by developing robust offline evaluation metrics and processes.
- Doubled online experiment velocity by partnering with analytics, product, and platform teams to build new tooling, e.g. interleaving tests, end-to-end model testing.

### Director of Technology — UPMC Enterprises — 07/2019–03/2022

- Led an applied ML team of ~3 ML engineers; created career paths, hiring (1), performance management, and technical mentorship; delivered 1 promotion and managed out 1 low performer.
- Led a product team of ~12 engineering/QA ICs and product/engineering managers, building an Elasticsearch-based search engine over 160M+ clinical documents.
- Identified ML projects worth $Ms in savings, pitched to SVPs and the CTO, developed prototypes, and executed pilots partnering with provider/payor stakeholders.

### Senior Data Scientist — UPMC Enterprises — 09/2018–07/2019

## Selected Publications & Academic Leadership

- Jon Eskreis-Winkler, **Yubin Kim**, Andrew Stanton. 2023. [XWalk: Random Walk Based Candidate Retrieval for Product Search](https://ceur-ws.org/Vol-3589/paper_22.pdf). *eCom'23: ACM SIGIR Workshop on eCommerce*.
- Yujiang Wu, Shanshan Zhong, **Yubin Kim**, Chenyan Xiong. 2026. [What Generative Search Engines Like and How to Optimize Web Content Cooperatively](https://arxiv.org/abs/2510.11438). *ICLR 2026*.
- **Yubin Kim**, Arthur Maciejewicz, Brandon Beveridge. 2025. [Lessons from the bleeding edge: large-scale production inference of LLMs](https://ceur-ws.org/Vol-4123/paper_31.pdf). *eCom'25: ACM SIGIR Workshop on eCommerce*.
- Zhuyun Dai, **Yubin Kim**, Jamie Callan. 2017. [Learning to Rank Resources](https://www.cs.cmu.edu/~callan/Papers/sigir17-Zhuyun-Dai.pdf). *SIGIR 2017*, 837–840.

Full list on [Google Scholar](https://scholar.google.com/citations?user=3F_QHHQAAAAJ).

**Academic leadership:** Organizer, Workshop on Data Quality-Aware Multimodal Recommendation @ RecSys (2025–2026) and Workshop on eCommerce @ SIGIR (2023–2026); Sponsorship Chair, SIGIR (2026); AnalytiCup Chair, CIKM (2026).

## Skills

- **Leadership & management:** building and managing high-performing ML teams, hiring & recruiting, technical mentorship (to Sr. Staff), coaching & career development, performance management, leveling calibration, technical vision, strategy & long-term roadmap, cross-functional partnership, cross-org influence, executive communication, distributed/remote team leadership
- **Recommender systems & retrieval:** recommender systems, candidate retrieval, ranking, learning to rank, embedding-based retrieval, indexing, graph ML, graph neural networks, cold-start, personalization, discovery, ads retrieval, search, low-latency serving, large-scale retrieval
- **Modeling & ML lifecycle:** large-scale production ML, end-to-end training, evaluation & deployment, deep learning architectures, GNNs, BERT, transformer-based models, model distillation, LLM fine-tuning (SFT, GRPO), RAG, LLM inference & serving, GPU-efficient inference, LLMs for search & content understanding, dataset construction
- **Measurement & experimentation:** measurement strategies, offline evaluation metrics, A/B experimentation, interleaving tests, experimentation velocity, content quality measurement (human review and model-based), LLM-based evaluation, human-in-the-loop evaluation
- **Tools & platforms:** PyTorch, Hugging Face, Python, SQL, Solr, Elasticsearch, ANN, Faiss, vLLM, Kubernetes, AWS, GCP, Jupyter
- **Domains:** e-commerce marketplace search & recommendations, ads retrieval & monetization, healthcare / clinical NLP

## Education

- Ph.D., Computer Science — Language Technologies Institute, Carnegie Mellon University (Dec 2018)
- B.S., Software Engineering — University of Waterloo (Apr 2011)
