# Big Data and Data Science

**Status:** Populated — core module complete. Revised per `reviews/big_data_and_data_science_review.md`.
**DMBOK2 Reference:** DMBOK2 2nd Ed., Ch.14 — Big Data and Data Science
**Exam weight:** Part of the "remaining weight spread" tier alongside Data Architecture, Data Storage and Operations, Data Security, Data Integration and Interoperability, Document and Content Management, Data Management Maturity Assessment, and Data Ethics — see `research/cdmp_exam_overview.md`.

> **Editorial note on sourcing:** Sourced per the priority hierarchy defined in `research/source_map.md` — DAMA-DMBOK2 concepts are primary authority, official DAMA guidance is used for certification framing, and named tools/frameworks are illustrative examples only, never treated as DAMA definitions. Concepts are tagged **[DAMA]** for DMBOK2's official framing or **[Industry Practice]** for real-world conventions (the 3/5 Vs, CRISP-DM, specific ML terminology) DMBOK2 references loosely or doesn't mandate. This module follows the standard 14-section template documented in `knowledge_base/README.md`. No DMBOK2 text is reproduced verbatim anywhere in this file.

---

## 1. Overview

### Simple explanation (for beginners)

Traditional data management assumes data arrives in predictable volumes, at a predictable pace, in a known shape — a database row, a warehouse fact table. **Big Data** describes the situation where one or more of those assumptions breaks: too much data to fit comfortably on one machine, arriving too fast to process in the usual batch windows, or in too many different shapes (text, images, sensor logs) to fit a fixed schema at all. **Data Science** is the discipline of extracting insight and building predictive models from data — often, though not exclusively, big data — combining statistics, programming, and domain expertise.

The two concepts travel together in practice (data science projects often work with big data) but are genuinely distinct: Big Data is about the *characteristics of the data itself*; Data Science is about *what you do with data* (any data, big or small) to answer a question or build a predictive capability.

### Professional / DAMA-level explanation

**[DAMA]** DMBOK2 frames Big Data and Data Science as the Knowledge Area covering the technologies, techniques, and governance considerations for managing datasets that exceed traditional data management tools' practical capacity, and for the analytical discipline (data science) that increasingly depends on such data. DMBOK2's central point — and the one most likely to be tested — is that **big data and data science do not exempt an organization from the governance, quality, and management principles established throughout the rest of DMBOK2**; if anything, the scale, opacity, and decision-making weight of big data and ML systems make governance more consequential, not less.

**[Industry Practice, widely DAMA-referenced]** Big Data is commonly characterized by the **3 Vs** — **Volume** (data quantity beyond traditional practical processing capacity), **Velocity** (the speed at which data arrives and must be processed), and **Variety** (the range of formats and structures, from structured to entirely unstructured) — sometimes extended to the **5 Vs** with **Veracity** (the trustworthiness/quality of the data) and **Value** (whether the data actually yields usable business insight). This is real-world grounding for the concept, not a DMBOK2-invented framework — verify exact enumeration against your own copy.

---

## 2. Why This Knowledge Area Exists

**[DAMA]** As organizations increasingly generate and depend on data that doesn't fit traditional structured, moderate-volume assumptions, and as data science techniques become central to real business decisions (pricing, fraud detection, personalization, risk scoring), this Knowledge Area exists to ensure both the technical capability *and* the governance discipline scale together — rather than treating "it's big data" or "it's a model, not a rule" as an excuse to skip the accountability this project has established for every other Knowledge Area.

### Business problems Big Data and Data Science solve — and create

1. **Traditional tools can't handle the scale or shape of the data.** Relational databases and traditional ETL weren't designed for the volume, velocity, and variety many modern data sources present, requiring different storage and processing architectures.
2. **Untapped predictive value.** Without data science capability, an organization can describe *what happened* (reporting, BI) but not *what's likely to happen next* or *what should be done about it* — the specific value data science adds beyond descriptive analytics.
3. **Governance gaps specific to scale and opacity.** A machine learning model's decision logic is often far less transparent than a documented business rule, and big data platforms' scale makes ad hoc, undocumented data sprawl easy — both amplify, rather than reduce, the need for deliberate governance (Section 9).
4. **Bias and fairness risk in automated decisions.** A model trained on biased or unrepresentative historical data can systematize and scale that bias into real decisions affecting real people — a governance and, ultimately, ethical concern this Knowledge Area surfaces and `data_ethics.md` addresses directly.
5. **Ungoverned data lakes becoming unusable.** Without deliberate governance, a data lake meant to be a flexible, high-value asset can degrade into an unusable, undocumented "data swamp" (Section 4) — data goes in, but nothing trustworthy or findable comes back out.
6. **Model risk going unmanaged.** Deploying a predictive model into a real business process without ongoing monitoring for degrading accuracy (model drift) or unexpected behavior creates real, often invisible, business risk.

---

## 3. DAMA Definitions and Terminology

| Term | Definition |
|---|---|
| **Big Data** | Datasets whose volume, velocity, and/or variety exceed the practical capacity of traditional data management tools and techniques. |
| **Data Science** | The multidisciplinary practice of extracting insight and building predictive/analytical capability from data, combining statistics, computer science, and domain expertise. |
| **Data Lake** | A large-scale storage repository holding raw data in its native format, structured or unstructured, without requiring a predefined schema at ingestion. |
| **Schema-on-Read** | An approach where data is stored in its raw form and structure is applied/interpreted at the time of query or use, rather than enforced at the time of storage. |
| **Machine Learning (ML)** | **[Industry Practice, DAMA-referenced]** A data science technique in which a model learns patterns from data (training data) rather than being explicitly programmed with fixed rules. |

### Data Lake vs. Data Warehouse

**[DAMA]** Already introduced conceptually in `data_warehousing_and_business_intelligence.md`, Section 9, this distinction is central to this Knowledge Area's own scope:

| Dimension | Data Warehouse | Data Lake |
|---|---|---|
| **Schema approach** | Schema-on-write — structure enforced before/during load | Schema-on-read — raw data stored as-is, structure applied at query/use time |
| **Data types** | Primarily structured | Structured, semi-structured, and unstructured |
| **Primary use** | Reporting, BI, defined analytical queries | Data science, exploratory analysis, ML training, flexible/undefined future use |
| **Governance maturity required** | Governance is typically built into the load process itself | Governance must be deliberately layered on, or the lake risks becoming a "data swamp" (Section 4) |

*(See Section 9, Exam Traps, for the common mistake of treating these as interchangeable or a data lake as strictly a newer, superior replacement for a warehouse.)*

---

## 4. Core Concepts

### The Data Science Lifecycle

**[Industry Practice, DAMA-referenced]** DMBOK2 discusses data science as following a structured process, closely aligned with the widely-used **CRISP-DM** (Cross-Industry Standard Process for Data Mining) framework — a real, independently established industry methodology DMBOK2 references rather than originates:

1. **Business Understanding / Problem Definition** — defining the actual business question or decision the data science effort must support, before touching any data (echoing `data_warehousing_and_business_intelligence.md`'s "start from business questions, not available data" principle).
2. **Data Acquisition** — identifying and obtaining the relevant data, which may span structured, semi-structured, and unstructured sources.
3. **Data Preparation** — cleaning, transforming, and structuring data for analysis; widely recognized as typically the most time-consuming step in a real data science project, directly dependent on the data quality discipline established in `data_quality.md`.
4. **Exploratory Data Analysis** — investigating the data's characteristics, distributions, and relationships before committing to a modeling approach.
5. **Modeling** — building and training a predictive or analytical model (or applying a statistical technique) against the prepared data.
6. **Evaluation** — assessing the model's accuracy and validity, typically against data not used in training, before deployment.
7. **Deployment** — putting the model into production use, feeding a real business process or decision.
8. **Monitoring** — the same operational discipline established throughout this project, ongoing tracking of a deployed model's performance and behavior over time (see Model Drift, below).

### Machine Learning Fundamentals

**[Industry Practice]** Foundational vocabulary a Data Engineer supporting data science work will encounter regularly, not DAMA-original terminology:

- **Supervised learning** — training a model on labeled historical examples (input plus known correct output) to predict outcomes for new, unlabeled inputs.
- **Unsupervised learning** — finding patterns or structure in data without labeled outcomes (e.g., clustering similar customers together).
- **Training / Validation / Test data** — the practice of splitting available data into separate sets: training data (used to fit the model), validation data (used to tune it), and test data (used only for final, unbiased evaluation) — using the same data for training and evaluation produces a misleadingly optimistic assessment of model quality.
- **Overfitting** — a model that has learned the specific noise/quirks of its training data rather than the general underlying pattern, performing well on training data but poorly on new, unseen data.
- **Feature Engineering** — transforming raw data into the specific input variables ("features") a model actually uses, often requiring significant domain expertise and data preparation work.

### Model Governance

**[DAMA]** Extending this project's established governance principles specifically to predictive models, which carry unique risks structured business rules typically don't:

- **Model Risk Management** — treating a deployed model as a governed asset with an accountable owner, documented purpose and limitations, and defined review cadence — not a "set it and forget it" artifact once deployed.
- **Explainability / Interpretability** — the degree to which a model's decision logic can be understood and explained, as opposed to functioning as an opaque "black box." Some model types (e.g., simple decision trees) are inherently more explainable than others (e.g., complex neural networks), and the appropriate tradeoff between accuracy and explainability depends on the decision's stakes — a model influencing a person's credit or medical treatment needs stronger explainability justification than one recommending a movie.
- **Model Drift** — the degradation of a deployed model's accuracy over time as real-world conditions diverge from what the training data reflected, requiring ongoing monitoring (echoing the Data Storage and Operations Success Metrics pattern of measuring actual, not just assumed, performance) and periodic retraining.
- **Bias and Fairness** — **[Industry Practice, DAMA-referenced]** a model trained on biased or unrepresentative historical data can learn and systematize that bias into its predictions, disproportionately and unfairly affecting certain groups — a governance concern this Knowledge Area surfaces and `data_ethics.md` addresses in full ethical depth.

**Governance doesn't stop because a decision is made by a model rather than a person:** a common and costly misconception is treating an algorithmic decision as somehow exempt from the accountability, explainability, and fairness scrutiny a human-made business decision would receive — DMBOK2 explicitly frames model governance as an extension of, not an exception to, this project's established governance principles.

### Big Data Processing Architectures: Lambda and Kappa

**[Industry Practice, DAMA-referenced]** Two named architecture patterns commonly used to reconcile Big Data's Velocity and Volume characteristics within one pipeline design, extending the batch/real-time integration patterns already established in `data_integration_and_interoperability.md`:

- **Lambda Architecture** — runs a **batch layer** (processing the complete historical dataset for accuracy and completeness) alongside a **speed layer** (processing recent data in near-real-time for low-latency views), with a serving layer merging both to answer queries — trading additional architectural complexity (maintaining two processing paths) for both comprehensive accuracy and low latency.
- **Kappa Architecture** — simplifies this by treating all data as a single, continuous stream, using the same stream-processing logic for both real-time and reprocessed historical views (reprocessing is done by replaying the stream), avoiding the complexity of maintaining two separate codebases at the cost of requiring the stream platform to durably retain and replay historical data.

**Choosing between them is an architecture tradeoff**, not a default — Lambda suits organizations needing well-established, separately-optimized batch accuracy and real-time speed; Kappa suits organizations prioritizing a single, simpler processing model where a capable stream-replay platform is available, echoing the same "no single approach is unconditionally best" principle already established across this project's other architecture-choice discussions.

### Self-Service / Citizen Data Science

**[Industry Practice]** Paralleling the Self-Service BI governance tension already established in `data_warehousing_and_business_intelligence.md`, Section 4, many organizations now enable "citizen data scientists" — business analysts building models or advanced analyses using accessible, low-code tools, without a dedicated Data Science team's specialist involvement. This lowers the barrier to data science value but carries the same governance risk pattern already documented for self-service BI: without classification-aware access controls, model governance requirements, and basic training-data quality discipline extended to these self-service tools, citizen-built models can bypass the explainability, bias evaluation, and ownership accountability this Knowledge Area establishes as non-negotiable (Section 4, above) — "self-service" must not become a loophole around Model Governance, any more than self-service BI is a loophole around semantic layer governance.

### Data Lake Governance and the "Data Swamp" Anti-Pattern

**[Industry Practice, widely DAMA-referenced]** A data lake's schema-on-read flexibility is also its central governance risk: without deliberate metadata capture, classification, and access control at ingestion, a data lake can degrade into a **"data swamp"** — a large, ungoverned accumulation of raw data that is technically present but practically unusable, since nothing is findable, trusted, or understood well enough to actually use. This is the data-lake-specific instance of the same governance-gap pattern already documented as "spaghetti architecture" (`data_architecture.md`, `data_integration_and_interoperability.md`) and "data mart proliferation" (`data_warehousing_and_business_intelligence.md`) — a technically capable platform that becomes a liability without deliberate governance layered on top of it.

### Big Data and Data Science Success Metrics

**[DAMA + Industry Practice]** Echoing the demonstrable-value pattern established across this project's other operational Knowledge Areas:

- **Model accuracy/performance against defined thresholds** — whether a deployed model is actually meeting its documented accuracy target, monitored on an ongoing basis, not assumed to hold indefinitely after initial validation.
- **Data lake findability/usability rate** — a direct countermeasure to the "data swamp" risk, measuring whether users can actually locate and trust data in the lake.
- **Time from business question to actionable model/insight** — a measure of whether the data science practice is delivering value at a pace that matches business need.
- **Model governance compliance rate** — the percentage of deployed models with a documented owner, purpose, and review cadence, directly countering the "set it and forget it" risk.

### Relationships With Other DAMA Knowledge Areas

**Data Quality:** Data Preparation (Section 4) is directly downstream of the same quality dimensions established in `data_quality.md` — a model trained on inaccurate, incomplete, or inconsistent data will reliably produce unreliable predictions, the "garbage in, garbage out" principle applying with even more force to ML than to traditional reporting, since a model can obscure a data quality problem behind an apparently confident numeric prediction.

**Data Governance:** Model Governance (Section 4) is a direct, specific application of `data_governance.md`'s Owner/Steward/Custodian accountability structure to predictive models — a model needs an accountable Owner exactly as a data domain does, not a governance exemption because "it's a model, not a rule."

**Data Storage and Operations:** Big data platforms commonly rely on distributed storage and NoSQL database types already introduced in `data_storage_and_operations.md`, Section 4 — this Knowledge Area's technology choices are a direct, large-scale application of that module's database technology fit principles.

**Data Integration and Interoperability:** Streaming/real-time ingestion patterns (`data_integration_and_interoperability.md`, Section 4) are commonly how high-velocity big data sources are captured for both operational and data science use.

**Data Security:** Training data frequently contains sensitive information; anonymization or pseudonymization (`data_security.md`, Section 4) is often required before data can be used for model training or shared with a data science team, directly reusing that module's technique cluster rather than inventing a new one.

**Document and Content Management:** Unstructured content (`document_and_content_management.md`) — text, images, scanned documents — is frequently the raw input for natural language processing and other data science techniques; this Knowledge Area's classification and quality discipline directly affects the quality of any downstream analytical use of that content.

**Data Ethics** *(forthcoming module)*: Bias, fairness, and the societal impact of algorithmic decisions are surfaced here as a governance concern but are the direct, dedicated focus of `data_ethics.md` once completed — this module identifies *that* the risk exists and requires governance; that module addresses the ethical reasoning framework for evaluating it.

### Roles in Big Data and Data Science

| Role | Responsibility |
|---|---|
| **Data Owner** | Accountable for the business purpose, appropriate use, and governance of models and big data assets within their domain, exactly mirroring the structured-data Data Owner role. |
| **Data Scientist** | **[Industry Practice, DAMA-referenced]** Designs and builds predictive/analytical models; responsible for evaluating model accuracy and documenting its intended use and limitations. |
| **Data Engineer** | Builds and operates the pipelines and infrastructure (including big data/distributed platforms) that acquire, prepare, and serve data to data science work; implements approved anonymization/access controls on training data; does not unilaterally decide what data is appropriate to use for a model or approve a model for production deployment. |
| **ML Engineer** | **[Industry Practice]** Specializes in productionizing, deploying, and operating models reliably at scale, often bridging Data Science and Data Engineering responsibilities. |
| **Data Steward** | Helps classify and govern data flowing into data lakes and data science pipelines, working to prevent the "data swamp" anti-pattern through consistent metadata and classification discipline. |

---

## 5. Data Engineer Perspective

**Distributed data processing:** **[Industry Practice]** Building and operating pipelines on distributed processing frameworks (e.g., Spark-style engines) is a common technical response to Big Data's volume and velocity characteristics, extending the batch/streaming integration patterns already established in `data_integration_and_interoperability.md` to a larger scale.

**Data lake architecture and governance implementation:** Designing a data lake's zone structure (raw/landing, cleansed/trusted, curated — echoing the zone pattern already introduced in `data_governance.md`) and enforcing metadata capture at ingestion is the concrete technical countermeasure to the "data swamp" risk (Section 4) — governance intent only matters if it's actually implemented in how the platform is built and used.

**Feature pipelines:** Building the data pipelines that transform raw data into model-ready features (Feature Engineering, Section 4) is frequently a Data Engineering responsibility, done in close collaboration with Data Scientists who define what features are needed.

**Model deployment and serving infrastructure:** Operating the infrastructure that serves a trained model's predictions in production (batch scoring or real-time inference) draws directly on this project's integration and operations principles (`data_integration_and_interoperability.md`, `data_storage_and_operations.md`) applied to a model-serving context specifically.

**Model monitoring pipelines:** Implementing automated monitoring for model drift (Section 4) — tracking prediction accuracy and input data distribution over time — is a direct extension of the observability/monitoring discipline already established in `data_storage_and_operations.md` and `data_integration_and_interoperability.md`.

**Preparing training data responsibly:** Applying approved anonymization/pseudonymization techniques (`data_security.md`) to sensitive data before it's used for model training, rather than assuming a data science use case is automatically exempt from the same classification-driven protection requirements as any other use.

**How a Data Engineer contributes without owning business decisions:** As with every other Knowledge Area in this project, the Data Engineer builds and operates the infrastructure, pipelines, and monitoring that support data science work — but does not unilaterally decide what data is appropriate to use for a given model, approve a model for production deployment, or judge whether a model's fairness/bias profile is acceptable. Those are Data Owner/Data Scientist/governance decisions the engineer implements and, where something looks concerning (e.g., a model trained on data that seems to encode a protected characteristic), escalates rather than silently ships.

---

## 6. Enterprise Examples

*(Illustrative composite scenarios; named external standards/regulations are real.)*

### Banking: Credit Risk Scoring Model Governance

**Problem:** A bank (recurring from `data_governance.md`, `reference_and_master_data.md`, and `data_warehousing_and_business_intelligence.md`) uses a machine learning model to score loan applicants' credit risk, but the model was deployed without a documented owner, explainability review, or ongoing monitoring — and a regulator now asks the bank to explain why a specific applicant was denied.

**Big Data/Data Science approach:** The bank retroactively establishes Model Governance for the credit risk model — assigning an accountable Data Owner, documenting the model's features and limitations, and implementing an explainability layer that can produce a specific, defensible reason for any individual decision.

**Governance approach:** Given the direct regulatory and fairness stakes of credit decisions, Compliance and the accountable Data Owner jointly require the model to meet a higher explainability bar than a lower-stakes use case would need, directly applying the "explainability requirement scales with decision stakes" principle from Section 4.

**Business outcome:** The bank can respond to regulatory inquiries with a specific, defensible explanation for individual model decisions, rather than an opaque "the model said so."

### Healthcare: Clinical Predictive Model and Bias Risk

**Problem:** A hospital network (recurring from `reference_and_master_data.md`, `data_storage_and_operations.md`, and `data_security.md`) develops a predictive model to flag patients at high risk of readmission, but discovers during validation that the model performs meaningfully worse for certain demographic subgroups, due to those groups being underrepresented in the historical training data.

**Big Data/Data Science approach:** Before deployment, the model undergoes a fairness evaluation across demographic subgroups, and the team addresses the underrepresentation issue in the training data rather than deploying a model with a known, unaddressed performance disparity.

**Governance approach:** Clinical leadership (echoing `reference_and_master_data.md`'s Patient Data Owner) treats subgroup performance disparity as a patient-safety and fairness issue requiring resolution before deployment, not an acceptable tradeoff for faster time-to-market.

**Business outcome:** The hospital deploys a clinically validated model with documented, monitored performance across patient subgroups, rather than an unvetted model carrying undisclosed bias risk.

### Retail: Recommendation Engine on a Data Lake

**Problem:** An omnichannel retailer (recurring from `data_architecture.md`, `reference_and_master_data.md`, and `data_warehousing_and_business_intelligence.md`) wants to build a product recommendation engine using browsing, purchase, and product data — high volume, high velocity, and varied in format (structured transactions, semi-structured clickstream, unstructured product descriptions) — a textbook Big Data use case.

**Big Data/Data Science approach:** A governed data lake, with clear raw/trusted/curated zones and enforced metadata capture at ingestion, feeds the data science team's model training, avoiding the "data swamp" risk that an ungoverned lake would create at this data volume and variety.

**Governance approach:** A Data Owner for the "Customer Behavior" domain approves what browsing/purchase data can be used for recommendation modeling, consistent with the retailer's privacy commitments to customers.

**Business outcome:** The retailer builds an effective recommendation engine on a data lake that remains findable and trustworthy as it scales, rather than degrading into unusable data sprawl.

### Manufacturing: Predictive Maintenance from Sensor Data

**Problem:** A manufacturer (recurring from `data_warehousing_and_business_intelligence.md` and `data_storage_and_operations.md`) has thousands of IoT sensors generating high-velocity streaming data from production equipment, and wants to predict equipment failures before they cause costly unplanned downtime.

**Big Data/Data Science approach:** A streaming ingestion pipeline (extending the real-time integration patterns from `data_integration_and_interoperability.md`) feeds a model trained to detect early failure indicators in sensor data patterns, with automated monitoring for model drift as equipment ages and usage patterns change.

**Governance approach:** Operations and Engineering jointly own the model's deployment, with a defined process for what happens when the model flags a potential failure (a human-reviewed maintenance decision, not fully automated equipment shutdown), given the real operational cost of a false positive.

**Business outcome:** The manufacturer reduces unplanned downtime by acting on early warning signals, while keeping a human decision point in the loop for the actual maintenance action.

---

## 7. Common Mistakes

1. **Treating big data or ML as exempt from governance.** Assuming that because data is "big" or a decision is "made by a model," the usual accountability, quality, and classification requirements don't apply — directly contradicted by DMBOK2's central framing for this Knowledge Area.
2. **Building a data lake with no governance plan.** Assuming a data lake's schema-on-read flexibility means governance can be deferred indefinitely, producing the "data swamp" anti-pattern (Section 4) as data accumulates without classification or metadata.
3. **Skipping data preparation rigor because "the model will figure it out."** Underestimating how directly a model's output quality depends on the quality of its training data — the "garbage in, garbage out" principle applies with full force to machine learning.
4. **Deploying a model with no ongoing monitoring.** Treating model deployment as a one-time event rather than the start of an operational responsibility, missing model drift until its degraded predictions cause visible business harm.
5. **Evaluating a model only on aggregate accuracy, not subgroup performance.** Missing a model's disparate performance across different populations because overall accuracy looked acceptable, a documented fairness risk with real consequences (Section 6, Healthcare example).
6. **Using unprotected sensitive data for model training without appropriate anonymization.** Treating a data science use case as automatically exempt from the same classification-driven protection requirements (`data_security.md`) that would apply to any other use of the same sensitive data.
7. **Conflating Big Data and Data Science as the same thing.** Assuming every data science project requires big data infrastructure, or that having big data automatically means an organization is "doing data science" — the two are related but genuinely distinct concepts (Section 1, Section 9).

---

## 8. CDMP Exam Focus

### High-value concepts
- **The core message that governance applies to big data/ML just as it does to any other data** (Section 4, Section 7) — the single most exam-relevant theme of this Knowledge Area.
- **The 3 Vs / 5 Vs** (Section 1) — precise recall of Volume, Velocity, Variety (and Veracity, Value if extended).
- **Data Lake vs. Data Warehouse** (Section 3) — schema-on-read vs. schema-on-write, and their differing governance maturity requirements.
- **The "data swamp" anti-pattern** (Section 4) — the direct governance risk of an ungoverned data lake, and its structural similarity to "spaghetti architecture" and data mart proliferation.
- **Model Governance concepts**: explainability, model drift, bias/fairness (Section 4) — as an extension of, not exception to, established DAMA governance principles.

### Important definitions
- Big Data, Data Science, Data Lake, Schema-on-Read, Machine Learning — precise, independent definitions.
- Supervised/Unsupervised Learning, Training/Validation/Test data, Overfitting, Feature Engineering, Model Drift, Explainability — precise ML-adjacent vocabulary.

### Frequently confused concepts
- **Big Data vs. Data Science** — data characteristics vs. an analytical discipline; related but genuinely distinct concepts, frequently conflated.
- **Data Lake vs. Data Warehouse** — schema-on-read/flexible/multi-format vs. schema-on-write/structured/defined-query — not interchangeable terms, and neither is unconditionally "better."
- **Data Preparation vs. Modeling** — data preparation (the most time-consuming, quality-dependent step) is frequently underestimated relative to the more visible modeling step.
- **Explainability vs. Accuracy** — a genuine tradeoff, not a scenario where one is unconditionally more important than the other regardless of decision stakes.

---

## 9. Exam Traps

- **A question implies big data or machine learning is exempt from standard data governance principles.** DMBOK2 explicitly frames this Knowledge Area as extending, not exempting from, established governance — this is likely the single most tested idea in this Knowledge Area.
- **A question implies a Data Lake is simply a newer, universally superior replacement for a Data Warehouse.** They serve different primary uses (flexible/exploratory vs. defined/reporting) with different governance maturity requirements — neither is unconditionally better, echoing the "no single approach is unconditionally best" pattern established throughout this project.
- **A question treats "Big Data" and "Data Science" as synonyms.** Big Data describes data characteristics (volume/velocity/variety); Data Science is an analytical discipline that can be applied to data of any size — conflating them is a documented, frequently tested error.
- **A question implies a model's high aggregate accuracy is sufficient evidence it is fair and ready for deployment.** Aggregate accuracy can mask meaningfully worse performance for specific subgroups — a well-documented and increasingly tested fairness/bias concern.
- **A question implies data preparation is a minor, quick step relative to modeling.** In real data science practice, data preparation is typically the most time-consuming step, directly dependent on data quality discipline — treating it as an afterthought is a common and costly underestimation.
- **A question implies a deployed model requires no further attention once it's live.** Model drift is a well-documented risk requiring ongoing monitoring, not a "deploy and forget" capability.

---

## 10. Interview Questions

### Data Engineer level
1. **"How would you design a data lake to avoid it becoming an ungoverned 'data swamp' as it grows?"**
   *Strong answer covers:* enforcing metadata capture and classification at ingestion, defining clear zones (raw/trusted/curated), and treating governance as a design requirement from day one rather than something to retrofit later.
2. **"How would you prepare sensitive customer data for use in training a machine learning model?"**
   *Strong answer covers:* applying appropriate anonymization/pseudonymization (`data_security.md`) based on the data's classification, rather than assuming a data science use case is exempt from standard protection requirements.
3. **"What's the difference between training, validation, and test data, and why does the distinction matter?"**
   *Strong answer covers:* the purpose of each split (fitting, tuning, unbiased final evaluation) and why evaluating a model only against its own training data produces a misleadingly optimistic accuracy assessment.

### Senior Data Engineer level
4. **"A deployed model's prediction accuracy has quietly degraded over six months with no one noticing. How do you prevent this recurring?"**
   *Signal:* diagnoses this as a missing model monitoring gap (model drift going undetected) and proposes automated, ongoing accuracy/distribution monitoring with alerting, not a one-time post-deployment validation.
5. **"How would you build a feature pipeline that stays consistent between model training and production serving?"**
   *Signal:* recognizes that inconsistent feature computation between training and serving (a common, subtle bug source) undermines a model's real-world accuracy even if it performed well in training, and proposes shared, single-source feature computation logic.
6. **"A data science team asks for broad, unrestricted access to a sensitive dataset to 'see what's useful' before deciding on a project. How do you respond?"**
   *Signal:* treats this as a Least Privilege and classification-driven access question (`data_security.md`), proposing scoped access tied to an actual defined use case rather than open-ended exploratory access to sensitive raw data.

### Data Science / Model Governance level
7. **"How would you evaluate whether a model's explainability is adequate for a given use case?"**
   *Signal:* ties the required explainability level to the actual stakes of the decision the model informs (echoing Section 4's principle), rather than applying one blanket explainability standard regardless of context.
8. **"How would you design an ongoing model governance process for an organization with a growing number of deployed models and no current tracking of any of them?"**
   *Signal:* proposes an inventory of deployed models with assigned Owners, documented purpose/limitations, and a defined review cadence — treating models as governed assets requiring the same accountability structure as any other data domain.
9. **"How would you evaluate whether a data lake initiative is delivering real value versus just accumulating ungoverned data?"**
   *Signal:* proposes measuring findability/usability and actual usage of lake data (Section 4's Success Metrics), not just raw volume ingested, recognizing that volume alone is not evidence of value.

---

## 11. Practical Exercises

### Exercise 1: Diagnose a Data Swamp

**Scenario:** An organization's data lake has grown to petabyte scale over three years with no metadata standard, no classification scheme, and no documented ownership — data scientists routinely report they can't find or trust data in the lake and resort to requesting fresh extracts directly from source systems instead.

**Task:** Diagnose the problem using this Knowledge Area's terminology, and propose a remediation plan.

**Expected solution approach:** This is a textbook "data swamp" (Section 4) — the lake's technical capacity was never matched by governance discipline (metadata capture, classification, ownership). Remediation should mirror the incremental approach already established for similar sprawl problems in this project (`data_integration_and_interoperability.md`, Exercise 1; `document_and_content_management.md`, Exercise 3): prioritize metadata tagging and ownership assignment for the highest-value, most-used data first, rather than attempting to retroactively govern the entire petabyte-scale lake at once, and require metadata capture at ingestion for all new data going forward so the problem doesn't keep growing while the backlog is addressed.

### Exercise 2: Design a Model Governance Process

**Scenario:** An organization has 15 machine learning models in production, none with a documented owner, explainability review, or monitoring process. Leadership wants this remediated without halting existing model operations.

**Task:** Propose a governance process, including how to prioritize which models get attention first.

**Expected solution approach:** Establish a lightweight model inventory capturing each model's purpose, an assigned Data Owner, and its decision stakes (e.g., customer-facing/regulated decisions vs. low-stakes internal recommendations). Prioritize explainability review and monitoring implementation for the highest-stakes models first (echoing the differentiated-risk prioritization already established for RPO/RTO in `data_storage_and_operations.md`), rather than requiring an identical governance bar for every model regardless of impact, while still requiring every model to eventually have a documented owner and basic monitoring.

### Exercise 3: Evaluate a Model for Fairness Before Deployment

**Scenario:** A newly trained model shows 92% aggregate accuracy, exceeding the target threshold, and the team is ready to deploy it into a customer-facing decision process.

**Task:** Propose what additional evaluation should happen before deployment, beyond the aggregate accuracy number.

**Expected solution approach:** Before deployment, evaluate the model's performance broken down by relevant demographic or use-case subgroups, not just the aggregate figure — aggregate accuracy can mask a model that performs meaningfully worse for a specific population (Section 6, Healthcare example). If a significant disparity is found, address its root cause (often underrepresentation in training data) before deployment rather than treating 92% aggregate accuracy alone as sufficient evidence of readiness, and establish the explainability and monitoring requirements appropriate to a customer-facing decision's stakes before go-live, not as a follow-up task after launch.

---

## 12. Flashcards

| Term | Definition |
|---|---|
| Big Data | Datasets whose volume, velocity, and/or variety exceed the practical capacity of traditional data management tools. |
| Data Science | The multidisciplinary practice of extracting insight and building predictive capability from data. |
| The 3 Vs | Volume, Velocity, and Variety — the common characterization of Big Data. |
| The 5 Vs | The 3 Vs extended with Veracity (trustworthiness) and Value (usable business insight). |
| Data Lake | A large-scale repository holding raw data in its native format without a predefined schema at ingestion. |
| Schema-on-Read | An approach where structure is applied/interpreted at query time rather than enforced at storage time. |
| Schema-on-Write | An approach where structure is enforced before or during data load, the traditional warehouse approach. |
| Data Swamp | The anti-pattern of an ungoverned data lake becoming a large, unusable accumulation of unfindable, untrusted raw data. |
| Machine Learning (ML) | A data science technique in which a model learns patterns from data rather than being explicitly programmed with fixed rules. |
| Supervised Learning | Training a model on labeled historical examples to predict outcomes for new inputs. |
| Unsupervised Learning | Finding patterns or structure in data without labeled outcomes. |
| Training Data | The data subset used to fit a model. |
| Validation Data | The data subset used to tune a model during development. |
| Test Data | The data subset used only for final, unbiased model evaluation. |
| Overfitting | A model that has learned training data's specific noise rather than the general underlying pattern. |
| Feature Engineering | Transforming raw data into the specific input variables a model actually uses. |
| Model Governance | Treating a deployed model as a governed asset with an accountable owner, documented purpose, and review cadence. |
| Explainability / Interpretability | The degree to which a model's decision logic can be understood and explained, as opposed to an opaque black box. |
| Model Drift | The degradation of a deployed model's accuracy over time as real-world conditions diverge from training data. |
| Bias (in models) | A model learning and systematizing unfairness present in its training data, disproportionately affecting certain groups. |
| CRISP-DM | Cross-Industry Standard Process for Data Mining — a widely-used industry framework for the data science lifecycle. |
| Big Data and Data Science Success Metrics | Measures (e.g., model accuracy against threshold, lake findability rate, governance compliance rate) demonstrating this discipline's ongoing effectiveness. |
| Lambda Architecture | A big data processing pattern combining a batch layer (complete historical accuracy) and a speed layer (near-real-time views), merged in a serving layer. |
| Kappa Architecture | A big data processing pattern treating all data as a single continuous stream, using one processing model for both real-time and reprocessed historical views. |
| Citizen Data Science | Business analysts building models/advanced analyses using accessible tools without dedicated Data Science team involvement, carrying the same governance risks as self-service BI. |

---

## 13. Quiz Questions

1. **What is the correct relationship between Big Data and Data Science?**
   a) They are synonyms for the same concept b) Big Data describes data characteristics (volume, velocity, variety); Data Science is an analytical discipline that can be applied to data of any size c) Data Science is a subset of Big Data technology d) Big Data always requires Data Science techniques to be useful

   **Correct answer:** b) Big Data describes data characteristics (volume, velocity, variety); Data Science is an analytical discipline that can be applied to data of any size.
   **Explanation:** These are related but genuinely distinct concepts — Big Data is about the nature of the data itself, while Data Science is a methodology for extracting insight, applicable regardless of data scale.
   **Why the others are wrong:** (a) conflates two distinct concepts, a documented exam trap; (c) reverses the actual relationship — Data Science is not a technology subset of Big Data; (d) Big Data can be reported on or queried without necessarily applying data science/ML techniques.
   **Related Knowledge Area:** Big Data and Data Science (this module, Section 1, Section 9).

2. **What are the "3 Vs" commonly used to characterize Big Data?**
   a) Volume, Value, Veracity b) Volume, Velocity, Variety c) Variety, Validity, Value d) Velocity, Verification, Volume

   **Correct answer:** b) Volume, Velocity, Variety.
   **Explanation:** Volume (data quantity), Velocity (speed of arrival/processing need), and Variety (range of formats) are the classic 3 Vs characterizing Big Data.
   **Why the others are wrong:** (a), (c), and (d) all include terms not part of the core 3 Vs (Veracity and Value are the optional 5 Vs extension; Validity and Verification are not part of the standard framing at all).
   **Related Knowledge Area:** Big Data and Data Science (this module, Section 1).

3. **Which statement correctly distinguishes a Data Lake from a Data Warehouse?**
   a) A Data Lake enforces schema-on-write; a Data Warehouse uses schema-on-read b) A Data Lake stores raw data in native format with schema-on-read; a Data Warehouse enforces schema-on-write with primarily structured data c) They are interchangeable terms for the same storage pattern d) A Data Lake is always a superior, newer replacement for a Data Warehouse

   **Correct answer:** b) A Data Lake stores raw data in native format with schema-on-read; a Data Warehouse enforces schema-on-write with primarily structured data.
   **Explanation:** This is the defining distinction — a Data Lake defers structure to query time and accepts any data format; a Data Warehouse enforces structure before/during load and is primarily structured-data-focused.
   **Why the others are wrong:** (a) reverses the two approaches' actual characteristics; (c) they are genuinely distinct storage patterns serving different primary uses; (d) treating one as unconditionally superior is a documented exam trap.
   **Related Knowledge Area:** Big Data and Data Science (this module, Section 3, Section 9); relates to Data Warehousing and Business Intelligence.

4. **A data lake has grown for three years with no metadata standard, no classification, and no documented ownership, and data scientists can no longer find or trust data in it. What does this scenario best illustrate?**
   a) A well-functioning, mature data lake b) The "data swamp" anti-pattern — an ungoverned data lake becoming a large, unusable accumulation of unfindable, untrusted data c) A Recovery Point Objective (RPO) failure d) A successful application of schema-on-write

   **Correct answer:** b) The "data swamp" anti-pattern — an ungoverned data lake becoming a large, unusable accumulation of unfindable, untrusted data.
   **Explanation:** This is precisely the "data swamp" anti-pattern — the lake's technical capacity was never matched by governance discipline (metadata, classification, ownership), making it a liability rather than an asset.
   **Why the others are wrong:** (a) mischaracterizes a well-documented failure mode as healthy functioning; (c) RPO concerns data-loss tolerance during a failure, unrelated to this findability/trust problem; (d) a data lake by definition uses schema-on-read, not schema-on-write.
   **Related Knowledge Area:** Big Data and Data Science (this module, Section 4, Section 7); relates to Data Architecture, Data Integration and Interoperability.

5. **Why is a dataset typically split into training, validation, and test subsets when building a machine learning model?**
   a) To reduce the total amount of data storage required b) To allow the model to be fit, tuned, and then evaluated on data it has never seen, avoiding a misleadingly optimistic accuracy assessment c) Because DAMA requires exactly three data subsets for any model d) To satisfy Data Loss Prevention requirements

   **Correct answer:** b) To allow the model to be fit, tuned, and then evaluated on data it has never seen, avoiding a misleadingly optimistic accuracy assessment.
   **Explanation:** Evaluating a model only against data it was trained on produces an artificially optimistic accuracy picture; separate validation and test sets ensure tuning and final evaluation happen on unseen data.
   **Why the others are wrong:** (a) storage reduction is not the purpose of this split; (c) this is standard industry ML practice, not a DAMA-mandated rule; (d) DLP concerns unauthorized data movement, unrelated to model evaluation methodology.
   **Related Knowledge Area:** Big Data and Data Science (this module, Section 4).

6. **True or False: Because a decision is made by a machine learning model rather than a human-defined business rule, it is exempt from the accountability and governance principles applied to other data-driven decisions.**
   a) True b) False

   **Correct answer:** b) False.
   **Explanation:** DMBOK2 explicitly frames model governance as an extension of, not an exception to, established governance principles — an algorithmic decision requires the same accountability, ownership, and scrutiny as a human-made one.
   **Why the others are wrong:** (a) reflects the single most commonly tested misconception in this Knowledge Area.
   **Related Knowledge Area:** Big Data and Data Science (this module, Section 4, Section 7, Section 9); relates to Data Governance.

7. **A deployed credit risk model shows 94% overall accuracy but is later found to perform meaningfully worse for a specific demographic subgroup, due to underrepresentation in the training data. What does this scenario best illustrate?**
   a) The model is fully ready for deployment, since 94% exceeds most accuracy thresholds b) Aggregate accuracy can mask disparate subgroup performance — a documented fairness/bias risk requiring evaluation beyond the overall number c) This is solely a Data Storage and Operations issue d) The model's explainability is irrelevant to this finding
   
   **Correct answer:** b) Aggregate accuracy can mask disparate subgroup performance — a documented fairness/bias risk requiring evaluation beyond the overall number.
   **Explanation:** A high aggregate accuracy figure does not guarantee consistent performance across subgroups; subgroup-level evaluation is necessary to catch exactly this kind of bias risk before deployment.
   **Why the others are wrong:** (a) treats aggregate accuracy alone as sufficient evidence of readiness, a documented exam trap; (c) this is a Model Governance/fairness issue, not a storage/operations concern; (d) explainability is directly relevant to understanding and addressing why the disparity exists.
   **Related Knowledge Area:** Big Data and Data Science (this module, Section 6, Section 7, Section 9); relates to Data Ethics.

8. **Select the two items below that are examples of Model Governance practices, as distinct from the technical modeling process itself. (Select two.)**
   a) Assigning an accountable Data Owner to a deployed model b) Selecting which algorithm to use for training c) Implementing ongoing monitoring for model drift d) Choosing the programming language used to build the model
   
   **Correct answer:** a) Assigning an accountable Data Owner to a deployed model; c) Implementing ongoing monitoring for model drift.
   **Explanation:** Assigning accountable ownership and implementing drift monitoring are both governance practices treating a model as a managed, accountable asset, distinct from the technical decisions made during model development itself.
   **Why the others are wrong:** (b) and (d) are technical implementation choices made during model development, not governance practices.
   **Related Knowledge Area:** Big Data and Data Science (this module, Section 4).

9. **What is the most time-consuming step in a typical real-world data science project, according to this Knowledge Area?**
   a) Business Understanding / Problem Definition b) Data Preparation c) Deployment d) Model selection
   
   **Correct answer:** b) Data Preparation.
   **Explanation:** Data Preparation — cleaning, transforming, and structuring data for analysis — is widely recognized as typically the most time-consuming step in a real data science project, directly dependent on data quality discipline.
   **Why the others are wrong:** (a), (c), and (d) are each real, necessary steps in the data science lifecycle, but none is typically the most time-consuming relative to data preparation.
   **Related Knowledge Area:** Big Data and Data Science (this module, Section 4, Section 9).

10. **A data science team requests broad, unrestricted access to a sensitive customer dataset "to see what's useful" before defining a specific project. What is the most appropriate response, per this Knowledge Area's governance principles?**
    a) Grant full access immediately, since data science requires exploratory freedom b) Scope access to the data actually needed for a defined use case, applying the same Least Privilege and classification-driven access principles used elsewhere c) Deny all data science access to any sensitive dataset permanently d) Grant access only if the team promises not to misuse it
    
    **Correct answer:** b) Scope access to the data actually needed for a defined use case, applying the same Least Privilege and classification-driven access principles used elsewhere.
    **Explanation:** Data science use cases are not exempt from Least Privilege and classification-driven access control; open-ended exploratory access to sensitive raw data should be scoped to an actual defined need, consistent with `data_security.md`'s principles.
    **Why the others are wrong:** (a) treats data science as automatically exempt from standard access governance, a documented anti-pattern; (c) is an overcorrection that would block legitimate data science value entirely; (d) an informal promise is not a substitute for actual classification-driven access scoping.
    **Related Knowledge Area:** Big Data and Data Science (this module, Section 5, Section 7); relates to Data Security.

11. **What does 'Explainability' refer to in the context of Model Governance?**
    a) How quickly a model can be trained b) The degree to which a model's decision logic can be understood and explained, as opposed to functioning as an opaque black box c) The total volume of data used to train a model d) Whether a model was built using open-source tools
    
    **Correct answer:** b) The degree to which a model's decision logic can be understood and explained, as opposed to functioning as an opaque black box.
    **Explanation:** Explainability specifically concerns whether a model's reasoning can be understood and articulated, directly relevant to accountability for high-stakes automated decisions.
    **Why the others are wrong:** (a) training speed is an unrelated performance characteristic; (c) data volume is a Big Data characteristic (the "V" for Volume), not explainability; (d) tooling choice (open-source vs. proprietary) is unrelated to whether a model's logic can be explained.
    **Related Knowledge Area:** Big Data and Data Science (this module, Section 4); relates to Data Ethics.

12. **A manufacturer's predictive maintenance model was highly accurate at launch but has quietly become less reliable over the past year as equipment usage patterns changed. What concept does this best illustrate, and what is the appropriate response?**
    a) Overfitting; the model should never be used again b) Model Drift; the model requires ongoing monitoring and periodic retraining as conditions change c) A Data Loss Prevention failure; access controls should be tightened d) A Data Lake governance issue; the data should be reclassified
    
    **Correct answer:** b) Model Drift; the model requires ongoing monitoring and periodic retraining as conditions change.
    **Explanation:** Model Drift is exactly this phenomenon — a deployed model's accuracy degrading over time as real-world conditions diverge from training data — and the appropriate response is ongoing monitoring and retraining, not abandonment or unrelated technical fixes.
    **Why the others are wrong:** (a) Overfitting is a training-time issue about learning noise rather than general patterns, not a description of gradual real-world performance degradation after deployment; (c) DLP concerns unauthorized data movement, unrelated to gradual accuracy decline; (d) this scenario is a model performance/monitoring issue, not a data lake classification issue.
    **Related Knowledge Area:** Big Data and Data Science (this module, Section 4, Section 6); relates to Data Storage and Operations.

13. **An organization wants low-latency, near-real-time views of streaming data while also preserving the ability to reprocess complete historical data with full accuracy, and is willing to accept the complexity of maintaining two processing paths to get both. Which named architecture pattern best fits this priority?**
    a) Kappa Architecture b) Lambda Architecture c) Hub-and-spoke architecture d) Registry-style MDM

    **Correct answer:** b) Lambda Architecture.
    **Explanation:** Lambda Architecture is specifically defined by running a batch layer (for complete historical accuracy) alongside a speed layer (for near-real-time views), accepting the added complexity of two processing paths to get both benefits.
    **Why the others are wrong:** (a) Kappa Architecture uses a single stream-processing model rather than separate batch and speed layers, the opposite tradeoff described; (c) hub-and-spoke is a Data Integration and Interoperability architecture style for system connectivity, unrelated to batch/streaming processing design; (d) Registry-style is a Master Data Management implementation style, unrelated to big data processing architecture.
    **Related Knowledge Area:** Big Data and Data Science (this module, Section 4).

**Answer Key:** 1-b, 2-b, 3-b, 4-b, 5-b, 6-b, 7-b, 8-a,c, 9-b, 10-b, 11-b, 12-b, 13-b

---

## 14. References

### DAMA / Official

- DAMA-DMBOK2, 2nd Edition — Chapter 14: Big Data and Data Science (primary source for this module; paraphrased and synthesized throughout — verify exact wording, enumerated lists, and lifecycle-stage framing against your own copy)
- DAMA Dictionary of Data Management Terminology (glossary cross-reference for Big Data/Data Science terminology)
- Certification framing: `research/cdmp_exam_overview.md` — exam structure and Knowledge Area weighting

### Industry Practice

*(Real-world examples and terminology used for illustration only — not DAMA definitions; sourced per the priority rules in `research/source_map.md`, §5, which treat this tier as directional/illustrative, never authoritative for exam-fact claims.)*

- The 3 Vs / 5 Vs (Volume, Velocity, Variety, Veracity, Value) — standard industry Big Data characterization
- CRISP-DM (Cross-Industry Standard Process for Data Mining) — widely-used data science lifecycle framework
- Supervised/Unsupervised Learning, Overfitting, Feature Engineering, Model Drift — standard machine learning vocabulary
- Distributed processing frameworks and data lake platform categories — implementation categories, not DAMA concepts

### Internal

- `research/cdmp_exam_overview.md` — exam structure and Knowledge Area weighting
- `research/source_map.md` — source hierarchy and citation rules followed throughout this module
- `roadmap/four_month_plan.md` — Week 11 study plan for this module
- `knowledge_base/data_governance.md` — Owner/Steward/Custodian roles applied to Model Governance; zone pattern reused for data lake architecture
- `knowledge_base/data_quality.md` — the quality dimensions underlying Data Preparation
- `knowledge_base/data_warehousing_and_business_intelligence.md` — Data Lake vs. Data Warehouse distinction first introduced
- `knowledge_base/data_storage_and_operations.md` — distributed storage/NoSQL technology foundation for big data platforms
- `knowledge_base/data_integration_and_interoperability.md` — streaming/real-time ingestion patterns for high-velocity data
- `knowledge_base/data_security.md` — anonymization/pseudonymization for training data protection
- `knowledge_base/document_and_content_management.md` — unstructured content as data science input
- `knowledge_base/data_architecture.md` — "spaghetti architecture" anti-pattern parallel to "data swamp"
