# Data Modeling and Design

**Status:** Populated — core module complete (Week 4 of `roadmap/four_month_plan.md`).
**DMBOK2 Reference:** DMBOK2 Ch.5 — Data Modeling and Design
**Exam weight:** ~11% (highest tier, tied with Data Governance, Data Quality, Metadata Management — see `research/cdmp_exam_overview.md`)

> **Editorial note on sourcing:** As in `data_governance.md`, concepts are tagged **[DAMA]** for DMBOK2's official framing (paraphrased/synthesized, not verbatim — verify exact wording against your own copy) or **[Industry Practice]** for real-world conventions DMBOK2 references but doesn't mandate (e.g., specific notations, specific vendor patterns like Data Vault or the medallion architecture). Uncertain exact enumerations are flagged rather than stated as verbatim fact.

---

## 1. Overview

### Simple explanation (for beginners)

You wouldn't build a house by pouring concrete before agreeing on a floor plan. A **data model** is that floor plan for data: a precise picture of what things exist (Customer, Order, Product), what they're called, how they relate to each other, and — eventually — exactly how they're stored. Skipping straight to "just create the tables" is like skipping the floor plan and hoping the plumbing lines up later. Sometimes it does. Often it doesn't, and you find out during a renovation (a schema migration) that would have been cheap to avoid at design time.

### Professional / DAMA-level explanation

**[DAMA]** Data Modeling and Design is the process of discovering, analyzing, and scoping data requirements, and then representing and communicating those requirements precisely in the form of a **data model** — at increasing levels of technical detail. DMBOK2 frames this as a discipline with three distinct **levels of abstraction**, each serving a different audience and purpose:

- **Conceptual Data Model (CDM)** — business-level, technology-agnostic, communicates *what matters* to business stakeholders.
- **Logical Data Model (LDM)** — fully detailed (attributes, keys, relationships, normalization) but still technology-independent.
- **Physical Data Model (PDM)** — the technology-specific implementation: actual tables, columns, data types, indexes, partitioning, on a specific platform.

The discipline exists precisely *because* these three levels serve different purposes and different audiences — collapsing them into one (usually "just the physical model") is the single most common mistake this Knowledge Area exists to prevent.

---

## 2. Why This Knowledge Area Exists

**[DAMA]** Data structures that are never formally modeled tend to accrete ad hoc — every team names things differently, encodes the same concept inconsistently, and builds structures that reflect whatever the first engineer assumed rather than what the business actually means. Data Modeling and Design exists to make data structure a deliberate, reviewable, communicable decision rather than an implicit byproduct of whoever wrote the `CREATE TABLE` statement first.

### Business problems Data Modeling and Design solves

1. **Miscommunication between business and technical stakeholders.** A conceptual model lets a business stakeholder validate "yes, this is what we mean by Customer and Order" *before* a single table is built — catching misunderstandings when they're cheap to fix.
2. **Redundant and inconsistent data structures.** Without a logical model as a shared reference, different systems independently invent slightly different representations of the same entity (three different "Customer" tables with three different definitions of "active").
3. **Costly rework from structural mistakes.** A structural flaw discovered after a system is in production (e.g., a relationship that should have been many-to-many but was built as one-to-many) is far more expensive to fix than one caught at the logical modeling stage.
4. **Poor data quality baked into structure.** Some data quality problems aren't quality-check failures — they're modeling failures (e.g., no constraint preventing a duplicate primary key, an attribute that should have been broken into two, an ambiguous relationship).
5. **Inability to integrate across systems.** Integration (a separate Knowledge Area) depends heavily on shared or at least reconcilable data models — without them, every integration becomes bespoke translation logic.
6. **Loss of institutional knowledge.** An undocumented physical schema is only interpretable by whoever built it. A maintained logical model (tied to a business glossary — see `data_governance.md`) survives staff turnover.

---

## 3. DAMA Definitions and Terminology

### The Three Levels of Abstraction

| Level | Audience | Contains | Technology-bound? |
|---|---|---|---|
| **Conceptual Data Model (CDM)** | Business stakeholders | Entities and relationships only — no attributes, no keys | No |
| **Logical Data Model (LDM)** | Business + technical analysts | Entities, full attributes, primary/foreign keys, relationships, normalization | No — still platform-independent |
| **Physical Data Model (PDM)** | Engineers/DBAs | Tables, columns, data types, indexes, partitioning, constraints | Yes — specific to a database/platform |

**Exam-critical distinction:** the *presence of data types, indexes, or partitioning* is what signals a **Physical** model. A model with full attributes and keys but no data types or storage details is still **Logical**.

### Core Structural Terms
- **Entity** — a distinct business "thing" the organization needs to hold data about (e.g., Customer, Order).
- **Attribute** — a property of an entity (e.g., Customer.email).
- **Relationship** — an association between entities, with **cardinality** (one-to-one, one-to-many, many-to-many) describing how instances relate.
- **Primary Key** — the attribute(s) that uniquely identify an entity instance.
- **Natural Key** — a real-world, business-meaningful identifier (e.g., a national ID number, an email address).
- **Surrogate Key** — a system-generated, meaningless identifier (e.g., an auto-incrementing integer or UUID) used instead of, or alongside, a natural key — especially common in warehouse dimensions where natural keys can change or be reused.
- **Foreign Key** — an attribute referencing another entity's primary key, implementing a relationship physically.

### Normalization / Denormalization
- **Normalization** — the process of structuring a logical model to eliminate redundancy and update anomalies, typically expressed as **normal forms**: **1NF** (atomic values, no repeating groups), **2NF** (no partial dependency on a composite key), **3NF** (no transitive dependency — non-key attributes depend only on the key). **BCNF** is a stricter refinement of 3NF.
- **Denormalization** — deliberately introducing redundancy (usually at the physical level) to optimize read performance, most commonly in analytical/warehouse models. **[DAMA]** DMBOK2 treats denormalization as a legitimate, deliberate physical-modeling decision, not a mistake — the mistake is denormalizing *without knowing* you're trading write-integrity/redundancy-control for read performance.

### Dimensional Modeling
- **Fact table** — holds measurable, numeric events (e.g., a sale), typically with foreign keys to dimensions and a defined **grain** (the level of detail one row represents).
- **Dimension table** — holds descriptive context for facts (e.g., Customer, Product, Date).
- **Star schema** — a fact table directly connected to denormalized dimension tables.
- **Snowflake schema** — a star schema where dimensions are further normalized into sub-dimensions.

**[Industry Practice]** Dimensional modeling terminology (fact, dimension, grain, star/snowflake) originates largely from Ralph Kimball's warehouse methodology. DMBOK2 references and endorses these concepts within its Data Modeling and Data Warehousing chapters, but the *methodology itself* (Kimball vs. Inmon vs. Data Vault) is industry practice, not a DAMA invention — DMBOK2 presents modeling techniques neutrally rather than prescribing one methodology.

### Other Key Terms
- **Canonical Data Model** — a single, shared, standardized model used as a common reference point for integration across systems, reducing point-to-point translation logic.
- **Generalization / Subtyping** — modeling a general entity (e.g., "Party") with specialized subtypes (e.g., "Person," "Organization") that share common attributes but also have distinct ones — a precise term for something engineers often do informally without naming it.
- **Data Vault** — **[Industry Practice]** a modeling approach (Hub/Link/Satellite) designed for auditability and flexibility to source-system change, popular in modern warehouse architectures; DMBOK2 mentions modeling approaches like this but does not mandate any specific one.

---

## 4. Core Concepts

**[DAMA]** Beyond terminology, DMBOK2's Data Modeling and Design chapter emphasizes:

- **Modeling as an iterative, not strictly waterfall, process.** Conceptual → logical → physical is a progression of *detail*, not necessarily three separate sequential projects — models get revisited as understanding deepens.
- **Modeling is a communication tool as much as a technical artifact.** A model's value is partly in the conversations it forces (does this relationship actually hold? is this really one entity or two?) as much as in the resulting schema.
- **Model governance.** Naming standards, a review/approval process, and version control for shared models — DMBOK2 treats data models as governed artifacts, directly linking this Knowledge Area back to Data Governance (see `data_governance.md`): someone needs to be accountable for approving changes to a shared logical model, the same way someone owns a business glossary term.
- **Data Modeling vs. Data Architecture — the classic adjacent-KA confusion.** A **data model** describes the structure of a *specific* dataset/subject area. **Data Architecture** (a separate Knowledge Area, DMBOK2 Ch.4) describes the *overall blueprint* — how data assets, models, and flows fit together across the organization, aligned to enterprise strategy. Rule of thumb: if it describes one subject area's entities/attributes, it's a model; if it describes how many subject areas and systems fit together, it's architecture.
- **Model quality dimensions.** DMBOK2 discusses evaluating a model itself for completeness, correctness of relationships, and adherence to naming/structure standards — modeling quality is a precursor to (and distinct from) data quality of the *instances* stored in that structure.

---

## 5. Data Engineer Perspective

Data Modeling is one of the Knowledge Areas where your existing skill is closest to DAMA's content — the risk is not lacking the skill, but **skipping levels of abstraction** because tooling makes it easy to jump straight to physical implementation, and **not knowing DAMA's precise vocabulary** for things you already do intuitively.

**Warehouse modeling:** Star/snowflake schema design, fact tables, and dimension tables are direct, daily territory (see also `data_warehousing_and_business_intelligence.md`, Week 8). The DAMA-specific value-add here is discipline: does a conceptual/logical model exist and get reviewed *before* the dbt model is built, or does the dbt model *become* the only model that ever existed? The latter means business stakeholders never validated the structure — only engineers did.

**ELT tooling (e.g., dbt) and schema-first shortcuts:** Modern ELT patterns encourage writing a SQL transformation and letting the resulting table *be* the schema. This is efficient but silently collapses all three modeling levels into one physical artifact with no separate logical review — a common and easy-to-miss version of the "skipping levels" mistake (Section 7).

**Canonical/domain event schemas:** In event-driven and microservices architectures, a schema registry entry (Avro, Protobuf, JSON Schema) *is* a physical model — often built with no preceding logical model, meaning breaking changes are only caught by consumers failing at runtime rather than by a reviewed model change. A **canonical data model** for shared domain events (e.g., a standardized "Order" event schema used across services) is exactly the integration-simplifying artifact DMBOK2 describes.

**Data contracts:** **[Industry Practice]** The emerging "data contract" pattern (a formal, versioned agreement between a data producer and consumer about schema and semantics) is a modern, tooling-enforced instantiation of the logical model concept — DMBOK2 doesn't use this term, but the underlying idea (a documented, agreed structure that changes require negotiation to break) is the same discipline the chapter describes.

**Schema evolution:** Every schema migration is a physical-model change. DAMA's framing suggests the discipline is not the migration tooling itself, but whether a change to a widely-used entity's structure goes through a review process proportional to its blast radius — the same "model as governed artifact" idea from Section 4.

**Normalization/denormalization tradeoffs:** OLTP systems favor normalized (3NF) structures for write integrity; warehouses deliberately denormalize (star schemas) for read performance. You likely already make this tradeoff instinctively — DAMA's contribution is naming it precisely and treating it as a conscious physical-modeling decision to be documented, not just "how the query got fast."

---

## 6. Enterprise Examples

*(Illustrative composite scenarios; named external standards like HL7 FHIR are real.)*

### Banking
A bank's "Loan" concept looks different across origination, servicing, and risk-reporting systems. A **conceptual model** for "Lending" agreed across all three business lines (Loan, Borrower, Collateral, as shared entities) lets each system's physical model differ in implementation while staying reconcilable at the logical level — critical for the same BCBS 239 risk-aggregation regulation discussed in `data_governance.md`, which requires the bank to demonstrate its risk data is consistently and traceably defined, not just consistently *stored*.

### Healthcare
**HL7 FHIR** (Fast Healthcare Interoperability Resources) is a real, widely adopted industry standard that is essentially a published canonical logical/physical model for healthcare data — "Patient," "Encounter," "Observation," and other resources are precisely defined so that different hospital systems can exchange data without bespoke point-to-point translation for every integration. It's a strong real-world illustration of what a well-governed canonical model achieves at industry scale, not just within one organization.

### Retail / E-commerce
A single "Customer" concept needs a **conceptual model** shared across marketing, sales, and support; a **logical model** capturing the full normalized attribute set (contact info, addresses, preferences, relationships to orders); and multiple **physical models** — a normalized OLTP schema for the transactional order system, and a denormalized star schema (Customer as a dimension) for the analytics warehouse. The same logical concept intentionally has different physical shapes for different purposes — a clean illustration of why the three levels are kept distinct rather than collapsed into one "true" schema.

---

## 7. Common Mistakes

1. **Skipping conceptual and logical modeling entirely.** Going straight from a requirements conversation to a physical `CREATE TABLE` (or dbt model) means no one validated the structure at a business level — errors surface only after data starts flowing.
2. **Confusing Data Modeling with Data Architecture.** Producing a single "data model" document and calling it the organization's data architecture (or vice versa) — they answer different questions at different scope.
3. **Over-normalizing analytical models.** Applying strict 3NF discipline to a warehouse fact/dimension design because "normalization is best practice" — in an analytical context this often just adds unnecessary joins and hurts query performance without a corresponding integrity benefit.
4. **Denormalizing without documenting the tradeoff.** Denormalizing OLTP structures for convenience without recognizing (or documenting) that you've traded away update-anomaly protection.
5. **No naming standards.** The same entity (Customer) ending up as `cust`, `customer`, `client`, and `Customers` across different systems because no governed naming standard exists — this is a Data Modeling problem with a Data Governance solution (naming standards are typically approved as governance Standards, see `data_governance.md`).
6. **Cryptic physical models with no link back to business meaning.** A physical schema with columns like `cst_typ_cd` and no documented mapping to a business glossary term makes the model unreadable to anyone but its original author.
7. **Treating the ORM-generated or dbt-generated schema as the only model.** Tooling that auto-generates physical schemas from code (ORMs) or transformation logic (dbt) is convenient, but if it's never reviewed against a logical model or business definitions, structural mistakes ship silently.
8. **No version control or change process for shared models.** A widely-used canonical or warehouse model changing without a review process breaks downstream consumers who had no visibility into the change.

---

## 8. CDMP Exam Focus

**High-value concepts:**
- The **conceptual / logical / physical** distinction — by far the most-tested aspect of this Knowledge Area. Expect questions that describe a model's contents and ask you to identify its level.
- **Normalization forms (1NF/2NF/3NF)** — know what each form eliminates (repeating groups → partial dependency → transitive dependency), not just the buzzwords.
- **Key types** — primary, foreign, natural, surrogate — and when a surrogate key is preferred (warehouse dimensions, natural keys that can change or be reused).
- **Dimensional modeling vocabulary** — fact, dimension, grain, star vs. snowflake schema.
- **Generalization/subtyping** as a named technique, not just an intuitive pattern.

**Frequently confused concepts:**
- **Data Modeling vs. Data Architecture** — the single most commonly confused KA pair per the roadmap (see Week 9). A model = one subject area's structure; architecture = the enterprise-wide blueprint of how models, systems, and flows relate.
- **Logical vs. Physical model** — both can have full attributes and keys; the presence of data types/indexes/partitioning is what makes it Physical, not the level of detail alone.
- **Normalization vs. Denormalization** — normalization reduces redundancy for integrity (favored in OLTP); denormalization deliberately introduces redundancy for read performance (favored in analytics) — neither is universally "correct."

**Exam Traps:** see Section 9 below.

---

## 9. Exam Traps

- **A question describes a model with only entities and relationships, no attributes.** This is **Conceptual**, even if the entities sound technical — the deciding factor is the *absence of attributes/keys*, not subject matter.
- **A question describes a model with full attributes, primary/foreign keys, and normalization — but no data types or indexes.** This is still **Logical**, not Physical. Don't assume "detailed = physical."
- **"Which model should a business stakeholder validate?"** → the **Conceptual** model (sometimes Logical for detail review), never the Physical model — business stakeholders generally can't (and shouldn't need to) validate index strategy or data types.
- **Assuming denormalization is always a mistake.** DMBOK2 treats it as a legitimate, deliberate physical-design choice for analytical workloads — an answer option framing all denormalization as an error is a trap.
- **Data Architecture vs. Data Modeling scenario questions.** If a question describes "how data flows and is organized across multiple systems enterprise-wide," that's Architecture; if it describes "the structure of the Customer entity," that's Modeling — even though both chapters use overlapping vocabulary.
- **Assuming a surrogate key is always superior.** DMBOK2 presents surrogate vs. natural key as a tradeoff (surrogate keys avoid instability from changing natural keys, but lose inherent business meaning) — not a rule that surrogate keys are unconditionally correct.

---

## 10. Interview Questions (Senior Data Engineer Level)

1. **"Walk me through building a conceptual, then logical, then physical model for a new 'Subscription' domain."**
   *Signal:* actually produces three distinct artifacts of increasing detail rather than jumping straight to table DDL, and can explain what each level is for.

2. **"When would you choose a star schema over a snowflake schema, and what are you trading off?"**
   *Signal:* names query simplicity/performance (star) vs. storage/redundancy reduction and easier dimension maintenance (snowflake) as the actual tradeoff, not just a preference.

3. **"What's the difference between a data model and a data architecture diagram, concretely?"**
   *Signal:* correctly scopes a model to one subject area's structure and architecture to the cross-system, enterprise-wide blueprint — ideally with a concrete example from their own work.

4. **"Why would you use a surrogate key instead of a natural key in a warehouse dimension?"**
   *Signal:* explains natural key instability (reuse, format changes, nullability) as the real driver, not just "it's best practice."

5. **"How do you prevent a shared canonical event schema from breaking downstream consumers when it changes?"**
   *Signal:* mentions schema versioning, backward-compatibility rules, and a review/governance process for changes to widely-consumed schemas — ties back to "models as governed artifacts."

6. **"Describe a situation where you normalized or denormalized a schema, and how you decided."**
   *Signal:* frames it explicitly as integrity-vs-performance tradeoff analysis, not an unexamined default.

7. **"How would you model a many-to-many relationship at the logical level, and how does that change physically?"**
   *Signal:* correctly describes an associative/junction entity at the logical level and its corresponding join table physically.

8. **"What's generalization/subtyping, and where have you used it (even if you didn't call it that)?"**
   *Signal:* recognizes the pattern (e.g., a "Party" supertype with "Person"/"Organization" subtypes) from their own schema history, even if the formal term is new to them.

---

## 11. Practical Exercises

### Exercise: Model "Order Management" at All Three Levels

**Scenario:** Your company sells products directly to customers and needs a data model for order management, to be used both operationally (OLTP) and for warehouse analytics.

1. **Conceptual model:** Identify the core entities (e.g., Customer, Order, Order Line, Product) and their relationships only — no attributes, no keys. Validate: could a non-technical stakeholder confirm this is "what we mean" by an order?
2. **Logical model:** Add full attributes, primary/foreign keys, and normalize to at least 3NF. Explicitly identify any many-to-many relationships and how you resolved them (associative entities).
3. **Physical model (OLTP):** Translate the logical model into an actual normalized schema for a transactional database — pick real data types, define primary/foreign key constraints.
4. **Physical model (Warehouse):** Design a **star schema** for sales analytics from the same logical concepts — identify the fact table and its grain, and the dimension tables (including whether you'd use a surrogate key for the Customer dimension and why).
5. **Compare and reflect:** Write a short note on which decisions changed between the OLTP physical model and the warehouse physical model, and why — despite both tracing back to the same logical model.

**Self-check:** Could you explain to a business stakeholder why the "same" Customer data looks structurally different in the OLTP system vs. the warehouse, using the conceptual/logical/physical framework rather than just "it's optimized differently"?

---

## 12. Flashcards

| Term | Definition |
|---|---|
| Conceptual Data Model (CDM) | Business-level model: entities and relationships only, no attributes/keys, technology-agnostic. |
| Logical Data Model (LDM) | Fully detailed model with attributes, keys, relationships, and normalization — still technology-independent. |
| Physical Data Model (PDM) | Technology-specific implementation: tables, columns, data types, indexes, partitioning. |
| Entity | A distinct business "thing" the organization holds data about. |
| Attribute | A property of an entity. |
| Cardinality | The nature of a relationship between entities (one-to-one, one-to-many, many-to-many). |
| Primary Key | Attribute(s) uniquely identifying an entity instance. |
| Natural Key | A real-world, business-meaningful identifier. |
| Surrogate Key | A system-generated, meaningless identifier, often preferred in warehouse dimensions. |
| Normalization | Structuring data to eliminate redundancy and update anomalies (1NF/2NF/3NF/BCNF). |
| Denormalization | Deliberately introducing redundancy, typically for read performance in analytics. |
| Fact table | Table holding measurable, numeric events at a defined grain. |
| Dimension table | Table holding descriptive context for facts. |
| Grain | The level of detail one row in a fact table represents. |
| Star schema | Fact table directly connected to denormalized dimension tables. |
| Snowflake schema | Star schema with dimensions further normalized into sub-dimensions. |
| Canonical Data Model | A shared, standardized model used as a common reference point for integration. |
| Generalization/Subtyping | Modeling a general entity with specialized subtypes sharing common attributes. |
| Data Vault | Industry-practice modeling approach (Hub/Link/Satellite) for auditability and source-change flexibility. |

---

## 13. Quiz Questions

1. A model contains only entities and relationships, no attributes or keys. What level is it?
   a) Physical b) Logical c) Conceptual d) Canonical

2. What distinguishes a Physical model from a Logical model, even if both have full attributes and keys?
   a) The Physical model has more entities b) The Physical model specifies data types, indexes, and platform-specific details c) The Logical model is always simpler d) There is no meaningful distinction

3. Which normal form eliminates transitive dependency on the primary key?
   a) 1NF b) 2NF c) 3NF d) None of these

4. Why might a warehouse dimension use a surrogate key instead of a natural key?
   a) Surrogate keys are required by SQL b) Natural keys can change or be reused, destabilizing history c) Surrogate keys are always shorter d) Natural keys are not allowed in dimensions

5. What is the key difference between Data Modeling and Data Architecture?
   a) They are the same thing b) Modeling describes one subject area's structure; Architecture describes the enterprise-wide blueprint c) Architecture is only for cloud systems d) Modeling is business-only, Architecture is technical-only

6. In a star schema, what does the fact table typically contain?
   a) Descriptive text attributes b) Measurable, numeric events at a defined grain c) Only foreign keys with no measures d) Business glossary terms

7. What is denormalization primarily used to optimize?
   a) Write integrity b) Storage cost c) Read/query performance d) Security

8. What is generalization/subtyping used to model?
   a) A many-to-many relationship b) A general entity with specialized subtypes sharing common attributes c) A surrogate key strategy d) A physical index

9. HL7 FHIR is an example of:
   a) A DAMA-defined governance council b) A real industry-standard canonical/logical model for healthcare interoperability c) A normalization form d) A dimensional modeling tool

10. Which statement reflects DAMA's view on denormalization?
    a) It is always a modeling mistake b) It is a legitimate, deliberate physical-design tradeoff for read performance c) It is only valid in OLTP systems d) It eliminates the need for a logical model

**Answer Key:** 1-c, 2-b, 3-c, 4-b, 5-b, 6-b, 7-c, 8-b, 9-b, 10-b

---

## 14. References

**DAMA Official:**
- DAMA-DMBOK2, 2nd Edition — Chapter 5: Data Modeling and Design (primary source; verify exact wording and any enumerated lists against your own copy)
- DAMA Dictionary of Data Management Terminology (glossary cross-reference)

**Industry Practice / External Standards (real, cited in this module):**
- Ralph Kimball — dimensional modeling methodology (star schema, fact/dimension, grain) — industry-standard terminology adopted and referenced by DMBOK2, not a DAMA invention
- Dan Linstedt — Data Vault modeling methodology (Hub/Link/Satellite)
- HL7 FHIR (Fast Healthcare Interoperability Resources) — real healthcare interoperability standard illustrating a canonical model at industry scale
- Entity-Relationship notations (Chen, Crow's Foot, IDEF1X) — industry-standard modeling notations, not DAMA-specific

**Internal:**
- `research/cdmp_exam_overview.md` — exam structure and Knowledge Area weighting
- `roadmap/four_month_plan.md` — Week 4 study plan for this module
- `knowledge_base/data_governance.md` — model governance and naming-standard cross-references
- `knowledge_base/data_architecture.md` — for resolving the Modeling-vs-Architecture distinction (once populated)
