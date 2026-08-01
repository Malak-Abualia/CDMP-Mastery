# Data Quality

**Status:** Populated — core module complete (Week 5 of `roadmap/four_month_plan.md`).
**DMBOK2 Reference:** DMBOK2 Ch.13 — Data Quality
**Exam weight:** ~11% (highest tier, tied with Data Governance, Data Modeling, Metadata Management — see `research/cdmp_exam_overview.md`)

> **Editorial note on sourcing:** As in prior modules, concepts are tagged **[DAMA]** for DMBOK2's official framing (paraphrased/synthesized — verify exact wording against your own copy) or **[Industry Practice]** for real-world tools, terms, or conventions DMBOK2 doesn't define but you'll encounter professionally (e.g., data observability, data contracts, specific vendor tools). Note also that published "data quality dimension" lists vary slightly across practitioner sources and editions — the seven used here (Accuracy, Completeness, Consistency, Timeliness, Validity, Uniqueness, Integrity) are the commonly-taught core set; cross-check exact wording and any additional dimensions against your own DMBOK2 copy.

---

## 1. Overview

### Simple explanation (for beginners)

**What is Data Quality?** Data Quality is how well data reflects the real-world thing it's supposed to represent, and how well it serves the purpose someone needs it for. A customer's phone number that's correctly formatted but belongs to the wrong customer is "valid" but not "accurate." A sales report that's 100% accurate but arrives three days after the decision it was meant to inform is useless despite being correct — timeliness matters as much as correctness.

**Why it matters:** Every downstream decision, report, machine learning model, and automated process is only as trustworthy as the data feeding it — "garbage in, garbage out" isn't a cliché, it's the entire reason this Knowledge Area exists. Bad data doesn't just produce wrong answers; over time it destroys trust in *all* data, even the correct parts, because consumers can no longer tell which is which.

### Professional / DAMA-level explanation

**[DAMA]** DMBOK2 frames Data Quality Management around the concept of data being **"fit for purpose"** — quality isn't an abstract, universal property of data; it's measured against the specific requirements of the people and processes consuming it. Data that's perfectly adequate for an internal dashboard might be entirely unfit for a regulatory filing. This is why Data Quality Management is a *management discipline* (define requirements, measure against them, improve, monitor) rather than a one-time technical cleanup activity — fitness for purpose changes as purposes multiply and evolve.

---

## 2. Why This Knowledge Area Exists

**[DAMA]** Without a deliberate Data Quality Management discipline, quality issues are discovered accidentally — usually by whoever is most harmed by them (an executive acting on a wrong number, a customer receiving a duplicate bill) — rather than caught systematically before they cause damage. This Knowledge Area exists to make "how good is our data, and is it good enough for what we're using it for" a measured, managed, and continuously improved question rather than an assumption.

### Business problems Data Quality Management solves

- **Untrustworthy decision-making.** Executives and analysts lose confidence in *all* data once one high-visibility quality failure occurs, even in unrelated datasets.
- **Compounding downstream cost.** A quality issue caught at the source costs far less to fix than the same issue discovered after it has propagated through ten downstream reports, models, and integrations.
- **Regulatory and financial exposure.** Inaccurate risk, financial, or patient data can produce direct legal, financial, or safety consequences — not just an internal inconvenience.
- **Wasted remediation effort with no lasting fix.** Without root-cause discipline, the same data quality issue gets manually "cleaned" repeatedly because the process that creates it was never fixed.
- **Inability to scale AI/analytics investment.** Machine learning and self-service analytics amplify the cost of poor quality data enormously — a model trained on flawed data doesn't just report wrong numbers, it makes systematically wrong decisions at scale.

---

## 3. DAMA Definitions and Terminology: The Core Data Quality Dimensions

**[DAMA]** Each dimension below is a distinct, independently measurable property of data. Precisely distinguishing them — not just recognizing the buzzwords — is the highest-value exam skill in this Knowledge Area.

### Accuracy
- **Definition:** The degree to which data correctly describes the real-world object or event it represents.
- **Example:** A customer's address on file matches their actual current residence.
- **How to measure:** Sample audit against a trusted, independent reference source (e.g., match rate against a verified postal or government registry).
- **How organizations improve it:** Validate at the point of capture (e.g., address-verification APIs), periodic re-verification against authoritative sources, and root-causing why inaccurate data entered the system in the first place (not just correcting the record found wrong).

### Completeness
- **Definition:** The degree to which all data required for a given purpose is present — no missing values where a value is required.
- **Example:** A customer record missing a phone number despite the field being mandatory for the SMS-notification service that depends on it.
- **How to measure:** Percentage of null/missing values in fields defined as mandatory for a given use case.
- **How organizations improve it:** Enforce mandatory-field validation at entry, run targeted backfill campaigns for existing gaps, and require upstream source systems to enforce the same constraint rather than patching downstream.

### Consistency
- **Definition:** The degree to which data values for the same entity are the same, or at least reconcilable, across different datasets, systems, or points in time.
- **Example:** A customer's status shows "Active" in the CRM but "Churned" in the billing system at the same point in time.
- **How to measure:** Cross-system reconciliation checks — the discrepancy rate for the same entity's attribute across systems that should agree.
- **How organizations improve it:** Establish a single authoritative source (tied to Master Data Management and a governed canonical definition — see `data_governance.md` and `data_modeling_and_design.md`), synchronize updates via event-driven propagation rather than independent batch updates, and eliminate silent local overrides.

### Timeliness
- **Definition:** The degree to which data is available and current enough for its intended use, within an expected time window.
- **Example:** A daily sales report that must reflect the prior day's transactions by 6 a.m. — if it's stale, decisions get made on outdated numbers without anyone realizing it.
- **How to measure:** Latency between data creation/event occurrence and its availability for consumption, measured against a defined freshness SLA.
- **How organizations improve it:** Define explicit freshness SLAs per dataset, monitor pipeline latency against those SLAs, and adopt streaming or micro-batch ingestion where batch latency no longer meets the business need.

### Validity
- **Definition:** The degree to which data conforms to the required syntax, format, type, range, or business rule defined for it.
- **Example:** An "email" field containing a string with no `@` symbol, or an "age" field containing a negative number.
- **How to measure:** Percentage of records failing defined format/business-rule validation checks.
- **How organizations improve it:** Enforce schema and constraint validation at ingestion (reject or quarantine invalid records), add input-level validation at the point of capture (form/UI constraints), and version business rules explicitly as they evolve.

### Uniqueness
- **Definition:** The degree to which no entity is represented more than once within a dataset when it shouldn't be — the absence of unintended duplication.
- **Example:** The same customer represented as three separate records due to minor name/address variations ("Jon Smith" / "Jonathan Smith" / "J. Smith").
- **How to measure:** Duplicate rate detected via entity-matching/deduplication logic against a defined matching rule.
- **How organizations improve it:** Implement entity-resolution/matching rules, enforce uniqueness constraints where a true natural key exists, and apply Master Data Management "golden record" processes for domains prone to duplication (see `data_modeling_and_design.md` on Reference & Master Data).

### Integrity
- **Definition:** The degree to which relationships between data elements (referential integrity) and the data's overall structure remain intact and reliable.
- **Example:** An Order record referencing a Customer ID that doesn't exist in the Customer table — an "orphaned" record.
- **How to measure:** Count of referential-integrity violations (orphaned foreign keys, broken relationship links) detected across related datasets.
- **How organizations improve it:** Enforce foreign-key/referential constraints where technically feasible, apply transactional integrity controls across related writes, and include integration testing that specifically checks cross-table/cross-system relationships.

---

## 4. Core Concepts

### Distinguishing the Core Activities: DQM, Profiling, Validation, Cleansing, Monitoring

These five terms are frequently used loosely and interchangeably in casual conversation — DAMA treats them as distinct activities within one overarching discipline. This is a high-value distinction for both the exam and real practice.

| Term | What it is | Timing | Relationship to the others |
|---|---|---|---|
| **Data Quality Management (DQM)** | The overarching, ongoing management discipline: define requirements, measure, improve, monitor | Continuous program | The umbrella — all the others are activities *within* it |
| **Data Profiling** | Analyzing data's structure, content, and statistical characteristics (distributions, null rates, patterns, outliers) to understand its current state | Diagnostic, typically upfront and periodic | Produces the evidence that feeds "identify issues" in the DQM lifecycle (below) — profiling doesn't fix anything, it reveals |
| **Data Validation** | Checking data against defined rules/constraints at a specific point (e.g., ingestion) to confirm it meets expected criteria | Point-in-time gate | The enforcement mechanism for Validity (and often Completeness) — a pass/fail check, not a diagnostic exploration |
| **Data Cleansing** (a.k.a. scrubbing) | Correcting, standardizing, deduplicating, or removing identified bad data | Remediation, reactive | Fixes *symptoms* — DAMA is explicit that cleansing without root-cause correction (Section 7) just creates a recurring cleanup cycle |
| **Data Monitoring** | Continuous, ongoing measurement of quality metrics over time, with trend detection and alerting | Continuous, ongoing | Closes the loop — confirms whether DQM improvements hold, and detects regression before it reaches consumers |

**Key takeaway:** profiling tells you what's wrong; validation catches new bad data at the door; cleansing repairs what's already inside; monitoring watches continuously so you find out about regressions before your data consumers do. None of these alone constitutes "doing data quality" — DQM is the discipline that ties them into a coherent, ongoing program.

### The Data Quality Management Lifecycle

**[DAMA]** DMBOK2 frames Data Quality Management as a repeating cycle, not a linear one-time project:

1. **Define quality requirements** — engage business stakeholders (Owners/Stewards) to define which dimensions matter for a given data domain and what thresholds constitute "good enough," tied to governed standards (see `data_governance.md`).
2. **Profile data** — analyze the current state of the data to establish a factual baseline (see Data Profiling above).
3. **Identify issues** — compare profiling results against the defined requirements to surface concrete, quantified quality gaps.
4. **Analyze root causes** — investigate *why* an issue occurs (a broken source system, a missing validation step, an ambiguous manual process, human error) rather than stopping at describing *what* is wrong.
5. **Improve processes** — fix the root cause: a system change, a process change, a new validation rule, training — sustainable improvement targets the cause, not just the symptom.
6. **Monitor continuously** — implement ongoing measurement to confirm the improvement holds and to catch new regressions early, feeding back into Step 1 as requirements evolve.

This cycle repeats indefinitely — a data domain is never "done" with quality management, the same way a codebase is never "done" with testing.

### Roles in Data Quality Management

**[DAMA, applying the role definitions from `data_governance.md` specifically to Data Quality]**

| Role | Data Quality Responsibility |
|---|---|
| **Data Owner** | Accountable for the overall quality outcome of their data domain; approves *what* quality means and what thresholds are acceptable; the ultimate escalation point when quality failures have business consequences. |
| **Data Steward** | Translates the Owner's intent into concrete, specific quality rules and thresholds per dimension; coordinates root-cause analysis; day-to-day owner of the "identify issues → analyze root causes" steps of the lifecycle. |
| **Data Custodian** | Implements the technical controls (validation checks, monitoring dashboards, cleansing jobs) that Owners/Stewards decide are necessary — executes decisions, doesn't make them. |
| **Data Engineer** | In practice, most often **is** the Custodian for quality: builds and maintains the pipelines, validation frameworks, and monitoring that enforce Steward-defined rules, and surfaces detected issues through the defined escalation path — should not unilaterally decide business-level quality thresholds. |

**[Industry Practice]** Many organizations now also have a dedicated **Data Quality Engineer** — a specialized role (not a DMBOK2-defined term) focused specifically on building and operating quality tooling and frameworks, sitting close to Data Engineering but with a mandate closer to the Steward/Custodian boundary described above.

---

## 5. Data Engineer Perspective

**ETL/ELT pipelines:** The pipeline is the primary enforcement point for Steward-defined quality rules — pre-load validation (reject or quarantine bad records before they reach a trusted layer) versus post-load checks (flagging issues after data has already landed) is itself an architectural quality decision with real tradeoffs in latency and blast radius.

**Data validation frameworks:** **[Industry Practice]** Tools like Great Expectations, dbt's built-in `tests`, and AWS Deequ are the technical implementation layer for Validity, Completeness, and Uniqueness checks. The critical discipline point: the *rules* these tools encode should trace back to Steward/Owner-approved definitions, not be invented ad hoc by whichever engineer wrote the pipeline — otherwise "quality" quietly becomes whatever an individual engineer assumed it should be.

**Data contracts:** **[Industry Practice]** A formal, versioned agreement between a data producer and consumer defining not just schema but quality expectations (freshness SLAs, null-rate thresholds, valid value ranges). This pattern pushes quality enforcement upstream to the team that *creates* the data, rather than leaving downstream consumers to discover and absorb quality problems after the fact.

**Data observability:** **[Industry Practice]** A newer tooling category (e.g., Monte Carlo, Bigeye) that extends the DQM lifecycle's "monitor continuously" step with automated anomaly detection across freshness, volume, schema, and distribution — without requiring every check to be manually pre-defined. It's a technology-enabled evolution of Monitoring, not a replacement for defining what quality means in the first place.

**Data warehouses:** Quality gates typically sit at the boundary before data enters a trusted/conformed layer (see the zone pattern in `data_governance.md` and `data_architecture.md`) — conformed dimensions are exactly the kind of shared artifact where a quality failure has the widest blast radius, since many downstream reports depend on them.

**Data lakes:** Schema-on-read makes quality enforcement structurally harder — a common pattern is escalating quality rigor by zone (raw = minimal/no validation, curated = validated and profiled, trusted = fully governed and monitored), directly mirroring the governance zone pattern already established in earlier modules.

**Streaming pipelines:** Quality checks must happen in-flight or in short micro-batch windows rather than against a complete, stable dataset — schema/format validation is feasible in real time, but deeper checks (e.g., some Completeness or Consistency checks that depend on late-arriving or out-of-order events) often must be deferred to a windowed or downstream batch pass, a real architectural constraint that doesn't exist in traditional batch quality checking.

**CI/CD for data:** **[Industry Practice]** Treating data quality tests like unit tests in software engineering — running validation/quality checks as part of a pipeline's deployment process (e.g., `dbt test` in a CI pipeline) so that a change which would degrade data quality is caught before it reaches production, not after. Quality rules are version-controlled alongside pipeline code rather than living only as tribal knowledge or a separate, disconnected monitoring dashboard.

---

## 6. Enterprise Examples

*(Illustrative composite scenarios, continuing entities introduced in earlier modules for continuity.)*

### Government Citizen Data
Duplicate citizen records (a **Uniqueness** failure) can cause a benefit to be paid twice, or a citizen to be denied a service because their case history is split across two unmatched records. Incomplete address data (a **Completeness** failure) can mean benefit correspondence never reaches the intended recipient. When the same citizen's data is inconsistent across agencies (a tax agency and a health agency disagreeing on basic demographic facts — a **Consistency** failure), inter-agency data sharing initiatives (see `data_architecture.md`'s government example) fail even when the underlying integration technology works perfectly.

### Banking Transactions
**Accuracy** and **Integrity** are directly regulatory concerns here — the BCBS 239 risk-data-aggregation regulation (introduced in `data_governance.md`) explicitly requires demonstrable data quality controls for risk-reporting data, not just lineage. A transaction record referencing an account that doesn't exist in the account master (an **Integrity** failure) can misstate risk exposure. **Timeliness** is critical for fraud detection specifically — a fraud-detection model relying on transaction data that's even minutes stale can miss a fraud pattern that a near-real-time feed would have caught.

### Healthcare Records
**Completeness** and **Accuracy** failures in patient records directly affect patient safety, not just reporting — a missing allergy field or an inaccurate medication record is a clinical risk, not merely a data inconvenience. **Integrity** failures in the Master Patient Index (introduced in `data_modeling_and_design.md` and `data_architecture.md`) — where an Encounter record links to the wrong Patient, or fails to link at all — can result in care being documented against, or withheld from, the wrong person.

### Retail Customer Data
**Uniqueness** failures (duplicate customer profiles from inconsistent identity resolution across online/in-store/loyalty channels — see `data_architecture.md`'s omnichannel example) directly waste marketing spend and degrade personalization quality. **Consistency** failures (a customer's stated preferences differing between the e-commerce platform and the loyalty program) undermine the "unified customer view" that was the entire point of the architecture investment — a clean illustration of how a Data Architecture initiative can be technically successful while still failing its business goal if Data Quality isn't managed with equal discipline.

---

## 7. Common Mistakes

1. **Treating quality as only a technical issue.** Deciding what "accurate enough" or "complete enough" means is a *business* decision (an Owner/Steward responsibility), not something an engineer should infer unilaterally from what seems reasonable — quality thresholds tied to no business input tend to be either too strict (wasting effort) or too lax (missing what actually matters).
2. **Fixing bad data without fixing root causes.** Repeatedly cleansing the same recurring issue (Section 4's Data Cleansing) without ever completing Step 4 of the DQM lifecycle (root-cause analysis) means the same manual effort repeats indefinitely — cleansing is a symptom treatment, not a cure.
3. **No ownership.** Without an accountable Owner, there's no one to decide which quality issues matter most, arbitrate disputes about acceptable thresholds, or be answerable when a quality failure has real business consequences — quality work becomes whatever individual engineers happen to prioritize.
4. **No quality metrics.** Without measured dimensions and tracked trends, quality is anecdotal — there's no way to demonstrate improvement, detect regression, or make the business case for investing further in a struggling data domain.
5. **Only checking data after failure.** Reactive quality checking — adding validation only after a production incident already caused visible harm — is a symptom of the entire DQM lifecycle being skipped in favor of ad hoc firefighting; ideally quality requirements and checks are defined and built *before* an incident forces the issue.
6. **Buying quality tooling and mistaking it for a quality program.** **[Industry Practice observation]** As with Data Governance tooling, purchasing a validation/observability platform doesn't create accountability or defined requirements by itself — the tool needs a defined DQM lifecycle wrapped around it to be effective, not the other way around.

---

## 8. CDMP Exam Preparation

### High-value concepts
- **Precise, independent definitions of all seven quality dimensions** — the exam frequently gives a scenario and asks which dimension it illustrates; you must be able to distinguish, e.g., a *format* problem (Validity) from a *factual correctness* problem (Accuracy).
- **The "fitness for purpose" framing** — quality is relative to intended use, not an absolute, universal property of a dataset.
- **The Data Quality Management lifecycle** — know the steps and their order, especially that root-cause analysis precedes sustainable process improvement, and that monitoring feeds back into requirement definition.
- **The distinction between DQM, Profiling, Validation, Cleansing, and Monitoring** as related but non-interchangeable activities.
- **The relationship between Data Governance and Data Quality** — Governance *decides* what quality standards should be (policy/standard); Data Quality Management *measures and improves* against those standards (see `data_governance.md`, Section 8).

### Important definitions
- Accuracy, Completeness, Consistency, Timeliness, Validity, Uniqueness, Integrity — each precisely, not just as buzzwords.
- Data Profiling, Data Validation, Data Cleansing, Data Monitoring, Data Quality Management.

### Frequently confused concepts
- **Validity vs. Accuracy** — a value can be perfectly well-formatted (valid) and still be factually wrong (inaccurate); e.g., a syntactically correct email address that belongs to the wrong person.
- **Consistency vs. Integrity** — Consistency concerns whether the *same fact* agrees across systems/time; Integrity concerns whether *relationships* between data elements (foreign keys, links) remain structurally intact.
- **Data Cleansing vs. Data Quality Management** — cleansing is one remediation activity; DQM is the entire ongoing discipline that cleansing sits inside.
- **Data Profiling vs. Data Monitoring** — profiling is typically a deep, periodic/upfront diagnostic pass; monitoring is continuous, ongoing measurement over time.

---

## 9. Exam Traps

- **A scenario describes correctly-formatted but factually wrong data** → this is an **Accuracy** issue, not Validity — don't default to Validity just because the data "looks like data quality."
- **A scenario describes the same entity disagreeing across two systems** → **Consistency**, not Integrity — Integrity is about broken relationships/references, not disagreeing facts.
- **A scenario describes an orphaned foreign key or broken relationship** → **Integrity**, not Consistency.
- **A scenario describes data that arrived correctly but too late to be useful** → **Timeliness**, even though "the data itself" wasn't wrong in any other dimension.
- **Assuming "cleansing" and "data quality management" are synonyms.** An exam option equating a one-time cleansing project with an ongoing DQM program is a trap — DQM is explicitly framed as continuous.
- **Assuming quality thresholds are a technical/engineering decision.** An answer implying an engineer should determine what counts as "accurate enough" without business/Steward input contradicts DAMA's governance-quality relationship.
- **Assuming profiling fixes data.** Profiling is diagnostic only — an answer suggesting profiling itself resolves a quality issue is incorrect; it *reveals* issues that then require the later lifecycle steps.

---

## 10. Interview Preparation

### Data Engineer level
1. "How would you implement a check to catch duplicate customer records in a nightly batch load?"
2. "What's the difference between rejecting a bad record at ingestion versus flagging it after it's loaded — when would you choose each?"
3. "How do you handle late-arriving events in a streaming pipeline when your completeness check assumes all data for a time window has already arrived?"

### Senior Data Engineer level
4. "How would you design a validation framework that enforces business rules defined by a Data Steward, without hardcoding those rules directly into pipeline code?"
   *Signal:* separates rule definition (externalized, ideally Steward-editable/reviewable) from pipeline execution logic, so a rule change doesn't require an engineering deploy cycle every time.
5. "A quality check has been silently failing for three months before anyone noticed. How do you prevent that from happening again?"
   *Signal:* proposes monitoring/alerting on the *health of the checks themselves*, not just on the data — a "who watches the watcher" answer, not just "we'll check more often."
6. "How do you decide whether a data quality issue should block a pipeline (fail loudly) versus pass through with a warning?"
   *Signal:* frames this as a governance-defined, business-risk-based decision (tied to Owner/Steward-approved thresholds), not something to decide unilaterally based on engineering convenience.

### Data Quality Engineer level
7. "How would you design a data quality framework that scales across dozens of pipelines without every team reinventing their own checks?"
   *Signal:* discusses centralizing shared quality rule definitions/frameworks (e.g., a shared validation library or platform) while still allowing domain-specific rule ownership by Stewards.
8. "How do you perform root cause analysis when a quality issue could originate from any of five upstream systems?"
   *Signal:* describes a systematic elimination/lineage-tracing approach (tying back to Metadata Management) rather than guessing, and emphasizes collaborating with source-system owners rather than only patching downstream.
9. "How would you measure and report data quality trends to non-technical stakeholders?"
   *Signal:* proposes concrete, dimension-based metrics with clear business framing (e.g., "% of customer records missing a required field, trending over time") rather than raw technical error counts.

---

## 11. Practical Exercises

### Exercise A: Define Quality Rules for a Data Warehouse
Take a Customer dimension and a Sales fact table (from the star schema you designed in `data_modeling_and_design.md`'s practical exercise, if completed). For each, define at least one concrete rule per relevant quality dimension — e.g., a Completeness rule for a mandatory Customer attribute, a Validity rule for an email format, a Uniqueness rule preventing duplicate Customer surrogate keys, an Integrity rule ensuring every fact row's foreign keys resolve to an existing dimension row. Specify, for each rule, who would need to approve it (Owner/Steward) before it goes live.

### Exercise B: Design a Quality Monitoring Framework
Sketch a monitoring framework for the same warehouse: which metrics get tracked per dimension, what thresholds trigger an alert versus a hard pipeline failure, who gets notified (tie to the roles table in Section 4), and how the framework would detect a *regression* (a previously-passing check that starts failing) versus a known, accepted data limitation.

### Exercise C: Analyze a Bad Dataset Scenario
**Scenario:** A retail company's daily customer export contains: 12% of records with a missing phone number (required for SMS marketing), 340 customer records that appear to be duplicates of 150 unique people, 40 orders referencing customer IDs that don't exist in the customer table, and a report that historically arrives by 5 a.m. now arriving at 11 a.m. For each issue: (1) name the specific quality dimension violated, (2) propose a plausible root cause (not just a symptom description), and (3) propose both an immediate remediation and a longer-term process fix.

---

## 12. Flashcards

| Term | Definition |
|---|---|
| Data Quality Management (DQM) | The ongoing discipline of defining requirements, measuring, improving, and monitoring data's fitness for purpose. |
| Fitness for purpose | DAMA's framing that quality is relative to the specific use the data serves, not an absolute property. |
| Accuracy | Degree to which data correctly describes the real-world object/event it represents. |
| Completeness | Degree to which all required data is present. |
| Consistency | Degree to which the same fact agrees across systems, datasets, or time. |
| Timeliness | Degree to which data is available and current enough for its intended use. |
| Validity | Degree to which data conforms to required format, type, range, or business rule. |
| Uniqueness | Degree to which no entity is unintentionally duplicated within a dataset. |
| Integrity | Degree to which relationships/references between data elements remain structurally intact. |
| Data Profiling | Diagnostic analysis of data's structure and characteristics to establish a baseline. |
| Data Validation | Point-in-time check of data against defined rules/constraints. |
| Data Cleansing | Corrective activity: fixing, standardizing, deduplicating, or removing bad data. |
| Data Monitoring | Continuous, ongoing measurement of quality metrics with trend detection and alerting. |
| Root cause analysis | Investigating *why* a quality issue occurs, not just describing what is wrong. |
| Data Contract | Industry-practice formal agreement between producer and consumer on schema and quality expectations. |
| Data Observability | Industry-practice automated anomaly detection across freshness, volume, schema, and distribution. |

---

## 13. Quiz Questions

1. A customer's email address is correctly formatted but belongs to the wrong customer. Which dimension is violated?
   a) Validity b) Accuracy c) Completeness d) Uniqueness

2. A report that is factually correct but arrives too late to inform the decision it was meant for violates:
   a) Accuracy b) Integrity c) Timeliness d) Consistency

3. An Order record references a Customer ID that does not exist. This is a violation of:
   a) Consistency b) Integrity c) Validity d) Uniqueness

4. What is the correct relationship between Data Cleansing and Data Quality Management?
   a) They are synonyms b) Cleansing is one remediation activity within the broader DQM discipline c) DQM is a subset of cleansing d) Cleansing replaces the need for DQM

5. What does Data Profiling primarily produce?
   a) A fixed dataset b) A diagnostic understanding of data's current structure and characteristics c) A business glossary d) A governance policy

6. In the DQM lifecycle, what should happen immediately after identifying a quality issue?
   a) Deploy a monitoring dashboard b) Analyze root causes c) Cleanse the data d) Notify the Governance Council only

7. Who is typically accountable for deciding what quality threshold is "good enough" for a data domain?
   a) Data Custodian b) Data Engineer c) Data Owner d) Data Quality tooling vendor

8. Two systems disagree on a customer's status ("Active" vs. "Churned") at the same point in time. This is a:
   a) Validity issue b) Consistency issue c) Integrity issue d) Timeliness issue

9. What is the primary limitation of Data Cleansing performed without root cause analysis?
   a) It's too expensive to automate b) The same issue recurs because the underlying cause was never fixed c) It violates data governance policy by definition d) It always introduces new duplicates

10. What best describes "fitness for purpose" in DAMA's data quality framing?
    a) Data quality is an absolute, universal property b) Data quality is measured relative to the specific use the data serves c) Only regulated industries need to consider fitness for purpose d) Fitness for purpose only applies to warehouse data

**Answer Key:** 1-b, 2-c, 3-b, 4-b, 5-b, 6-b, 7-c, 8-b, 9-b, 10-b

---

## 14. References

**DAMA Official:**
- DAMA-DMBOK2, 2nd Edition — Chapter 13: Data Quality (primary source; verify exact dimension definitions and any enumerated lists against your own copy)
- DAMA Dictionary of Data Management Terminology (glossary cross-reference)

**Industry Practices (real, not DAMA-official — cited in this module):**
- Data Contracts — producer/consumer schema-and-quality agreement pattern
- Data Observability — automated, continuous anomaly detection across data pipelines
- CI/CD for data — applying software-engineering deployment/testing discipline to data pipeline quality checks
- Data Quality Engineer — an industry role specialization, not a DMBOK2-defined title

**Tools/Frameworks (real, named for concreteness — tool choice is an implementation detail, not a DAMA concept):**
- Great Expectations — open-source data validation framework
- dbt tests — built-in data testing feature of the dbt transformation tool
- AWS Deequ — data quality library for large-scale (Spark) datasets
- Monte Carlo, Bigeye — commercial data observability platforms

**Internal:**
- `research/cdmp_exam_overview.md` — exam structure and Knowledge Area weighting
- `roadmap/four_month_plan.md` — Week 5 study plan for this module
- `knowledge_base/data_governance.md` — role definitions and the governance/quality relationship
- `knowledge_base/data_modeling_and_design.md` — referenced star schema used in Practical Exercise A
- `knowledge_base/data_architecture.md` — referenced omnichannel retail scenario in Section 6
