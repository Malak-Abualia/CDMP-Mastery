# Metadata Management

**Status:** Populated — core module complete (Week 6 of `roadmap/four_month_plan.md`).
**DMBOK2 Reference:** DMBOK2 Ch.12 — Metadata Management
**Exam weight:** ~11% (highest tier, tied with Data Governance, Data Modeling, Data Quality — see `research/cdmp_exam_overview.md`)

> **Editorial note on sourcing:** As in prior modules, concepts are tagged **[DAMA]** for DMBOK2's official framing (paraphrased/synthesized — verify exact wording against your own copy) or **[Industry Practice]** for real-world tools, terms, or conventions DMBOK2 doesn't define but you'll encounter professionally (e.g., "data swamp," lakehouse-embedded metadata, and specific catalog products). Uncertain exact enumerations are flagged rather than presented as verbatim fact.

---

## 1. Overview

### Simple explanation (for beginners)

**What is metadata?** Metadata is "data about data" — but the more useful way to think about it is as the *label on the can*. The can's contents (the data) might be perfectly good, but without a label telling you what's inside, when it was made, and what it's safe to use for, you'd have to open and taste every single can to find out — which doesn't scale past a handful of cans, let alone an enterprise with thousands of tables. Metadata is what lets you know what a dataset is, where it came from, whether it's trustworthy, and who's allowed to use it — without having to inspect the raw data itself every time.

**Why it matters:** Without metadata, organizational knowledge about data lives only in people's heads — "ask Sarah, she built that pipeline" — which doesn't survive staff turnover, doesn't scale as data volume grows, and makes both self-service analytics and compliance audits nearly impossible. Metadata is the mechanism that turns tribal knowledge into a durable, searchable, organizational asset.

### Professional / DAMA-level explanation

**[DAMA]** DMBOK2 defines Metadata Management as the set of processes that ensure metadata is created, stored, integrated, and controlled to support both business and technical requirements throughout the data lifecycle. A subtle but important point DMBOK2 makes: **metadata is itself data**, and must be governed with the same discipline as any other data asset — it needs quality management, ownership, and standards, not just a place to be stored. Treating a metadata repository as a "set it and forget it" system is the same mistake as treating any other ungoverned dataset as reliable by default.

---

## 2. Why This Knowledge Area Exists

**[DAMA]** Without deliberate metadata management, an organization's understanding of its own data assets is fragmented, informal, and person-dependent. This Knowledge Area exists to make "what data do we have, what does it mean, where did it come from, and can I trust it" answerable systematically — not by asking around.

### Business problems Metadata Management solves

- **Undiscoverable data.** Without a searchable inventory, teams don't know what data already exists, so they duplicate collection and analysis effort that could have been reused.
- **Tribal knowledge dependency.** Institutional understanding of "what this table actually means" lives only with the engineer who built it — and leaves the organization when they do.
- **Inability to assess impact of change.** Without lineage (a form of metadata), no one can confidently answer "what breaks if I change this schema" without manual investigation or trial and error in production.
- **Compliance and audit exposure.** Regulators increasingly require organizations to *prove* where data came from and how it was transformed — impossible without maintained lineage and operational metadata.
- **Eroded trust in self-service analytics.** Business users given direct access to raw data without business metadata (definitions, ownership, quality signals) can't tell trustworthy datasets from stale or deprecated ones — undermining the entire point of self-service.

---

## 3. DAMA Definitions and Terminology: The Three Metadata Categories

**[DAMA]** DMBOK2 organizes metadata into three categories. Correctly classifying a described piece of metadata into the right category is one of the most frequently tested skills in this Knowledge Area.

### Business Metadata
- **Definition:** Metadata that describes data in business terms — definitions, business rules, ownership, and classification — focused on *meaning* for business consumers rather than technical implementation.
- **Examples:** A business glossary entry defining "Active Customer"; a documented business rule ("Revenue excludes refunds issued within 30 days"); a data ownership record; a sensitivity/classification label ("PII — Restricted").
- **Who uses it:** Business analysts, Data Stewards, executives, compliance/legal teams, self-service BI users.
- **Why it matters:** It's what lets a non-technical stakeholder understand and trust a dataset without needing an engineer to explain it — and it's the anchor that ties a Governance-approved definition (see `data_governance.md`) to an actual physical data asset.

### Technical Metadata
- **Definition:** Metadata describing the technical structure and characteristics of data — schemas, data types, and the technical mechanics of how data is produced and transformed.
- **Examples:** Table and column names and data types; schema version history; ETL/ELT transformation logic and source-to-target mappings; database constraints; file formats and partitioning schemes.
- **Who uses it:** Data Engineers, DBAs, Data Architects, application developers.
- **Why it matters:** It's what makes technical implementation, integration, and impact analysis for schema changes possible — and it's the layer that must be correctly mapped back to Business Metadata for a data asset to be both usable *and* understandable.

### Operational Metadata
- **Definition:** Metadata describing the execution and runtime characteristics of data processes — not what the data structurally *is*, but what has actually *happened* to it during processing.
- **Examples:** ETL job start/end times and success/failure status; row counts processed, rejected, or quarantined; data freshness/latency timestamps; access audit logs (who queried what, and when).
- **Who uses it:** Data Engineers and operations/platform teams, data observability tooling, auditors and compliance teams.
- **Why it matters:** It's the foundation for monitoring, troubleshooting, SLA verification, and audit trails — and it's the category most often neglected by organizations that think of "metadata" purely as static documentation (see Common Mistakes, Section 7).

---

## 4. Core Concepts

### Key Metadata Concepts

- **Metadata Repository [DAMA]** — A managed store (centralized or federated) holding metadata records; the technical home where metadata is actually captured and organized, whether a dedicated tool or embedded within a broader catalog platform.
- **Metadata Management Strategy [DAMA]** — A defined plan for how the organization will collect, integrate, store, and govern metadata: which systems/domains are in scope, whether the approach is centralized/federated/hybrid (mirroring the governance operating-model tradeoffs in `data_governance.md`), and who is responsible for what.
- **Metadata Integration [DAMA]** — The process of collecting and harmonizing metadata from many disparate source systems (databases, pipelines, BI tools) into one coherent, cross-referenced view — technically difficult because each source system exposes metadata differently, or not at all, requiring connectors or scanners to extract it consistently.
- **Metadata Standards [DAMA]** — Enterprise rules governing how metadata itself must be structured, named, and classified (e.g., "every new dataset must have an assigned Owner and at least one classification tag before it can be published to the catalog") — the metadata-specific counterpart to the Data Architecture standards in `data_architecture.md`.
- **Metadata (Data) Lineage [DAMA]** — The traceable record of data's origin, movement, and transformation history: where it came from, what happened to it, and where it went. Lineage is itself a *form of metadata* — typically a combination of Technical (what transformation ran) and Operational (when it ran, on what data) metadata — and is the artifact that makes impact analysis and audit proof possible.
- **Data Catalog [DAMA + Industry Practice]** — A searchable inventory of an organization's data assets that brings Business, Technical, and Operational metadata together into a single discoverable interface. DMBOK2 discusses the catalog as a key metadata management deliverable; specific catalog *products* (Section 14) are industry implementations of this concept, not DAMA inventions.
- **Business Glossary [DAMA]** — A governed collection of business term definitions — a specific Business Metadata artifact, and the same governance-sponsored artifact introduced in `data_governance.md`. The glossary is what a catalog's business-metadata layer is typically built from.

### Relationships: Metadata Management, Governance, Quality, Architecture, and Catalogs

- **Metadata Management ↔ Data Governance:** Governance *decides* what metadata must exist, who owns it, and the standards for approving business definitions (Policy/Standard, per `data_governance.md`). Metadata Management provides the *mechanism* — repository, integration, catalog — to actually capture, maintain, and surface that metadata. Governance without metadata management has no way to prove its decisions are reflected in reality; metadata management without governance produces a catalog full of unowned, unreliable entries (see Section 7).
- **Metadata Management ↔ Data Quality:** Technical metadata (a field's defined type/format) is what makes a Validity check possible in the first place (see `data_quality.md`); lineage metadata is what makes root-cause analysis possible when a quality issue is found downstream. Conversely, quality signals themselves (a "last validated" timestamp, a quality score) are metadata that a catalog should surface so consumers can judge a dataset's trustworthiness before using it.
- **Metadata Management ↔ Data Architecture:** Architecture's data flow diagrams (see `data_architecture.md`) describe the *intended*, high-level shape of how data should move. Metadata lineage, by contrast, captures the *actual, as-built* record of how data really moved and transformed — and the two can drift apart over time. A mature metadata management practice is often what reveals when the real system has diverged from its documented architecture.
- **Metadata Management ↔ Data Catalogs:** A catalog is the primary *tool* that operationalizes metadata management by bringing all three metadata categories into one discoverable place — but, echoing the governance module's "tool vs. discipline" theme, a catalog is not metadata management itself. Deploying a catalog without the underlying strategy, standards, and ownership behind it is a specific, common failure mode (Section 7).

### Roles in Metadata Management

| Role | Metadata Responsibility |
|---|---|
| **Data Owner** | Accountable for the accuracy of business metadata (definitions, classification) in their domain; approves what gets published to the catalog for that domain. |
| **Data Steward** | The primary hands-on curator of business metadata — maintains glossary term definitions and classification tags, and works with technical teams to ensure metadata matches reality. |
| **Data Engineer** | The primary *producer* of technical and operational metadata — responsible for instrumenting pipelines to reliably emit schema information, lineage events, and execution metrics; also a *consumer* of business metadata (the glossary) to correctly interpret what they're building against. |
| **Data Architect** | Uses metadata — especially lineage and the as-built catalog inventory — to compare the actual current state of systems against the intended architectural blueprint; defines metadata standards at the architecture level (what must be captured for any new system). |

---

## 5. Data Engineer Perspective

**ETL/ELT pipelines:** Pipelines are prime producers of both Technical metadata (transformation logic, source-to-target mappings) and Operational metadata (run status, row counts, latency). The discipline point: pipelines should be designed to *emit* this metadata as a first-class output, not as an afterthought bolted on after something breaks.

**SQL schemas:** A schema is technical metadata by definition. Column and table comments are an easy, frequently neglected way to embed *business* metadata directly at the source — reducing reliance on a separate, easily-outdated external glossary entry that no one remembers to check.

**Data warehouses:** Business definitions attached to conformed warehouse objects (fact/dimension tables) are precisely what lets self-service BI users trust and correctly use those tables without asking an engineer to explain every column.

**Data lakes:** Schema-on-read makes metadata *more* critical than in a warehouse, not less — structure isn't self-evident from the storage layer alone. **[Industry Practice]** A lake with no catalog or metadata discipline is commonly called a **"data swamp"** — technically holding data, but practically undiscoverable and untrustworthy.

**Lakehouse platforms:** **[Industry Practice]** Modern lakehouse formats (e.g., Delta Lake, Apache Iceberg) embed technical metadata (schema versions, transaction logs) directly in the storage layer itself — an architectural evolution that blurs the line between "the data" and "the metadata describing it." Engineers should treat this built-in metadata layer as a first-class platform concern, not solely an external catalog's job.

**Pipeline monitoring:** Operational metadata (run status, latency, error/rejection rates) is exactly what pipeline monitoring and observability tooling exists to capture and act on — a direct, daily connection between this Knowledge Area and standard DE tooling.

**Data lineage:** Lineage doesn't appear automatically — engineers typically must instrument pipelines deliberately (via lineage-emission APIs, or tools that parse pipeline/SQL code) to actually capture it. Assuming lineage "just exists" because a pipeline runs is a common and costly misconception.

**Schema evolution:** Every schema change is a metadata event. Without metadata management tracking schema versions and known consumers, an engineer cannot confidently answer "what will this change break" — this is the same schema-evolution challenge from `data_modeling_and_design.md`, reframed here as fundamentally a metadata capture and impact-analysis problem.

**Data contracts:** A data contract (introduced in `data_quality.md`) is, from a metadata lens, formalized and *enforced* Technical + Business metadata — schema and semantic expectations made contractually binding between producer and consumer, rather than merely descriptive documentation that can silently go stale.

**CI/CD for data:** Metadata (schema definitions, validation rules, lineage annotations) should be version-controlled alongside pipeline code, so metadata evolves in lockstep with the pipeline itself — rather than drifting out of sync in a separately, manually maintained catalog entry that nobody remembers to update after a deploy.

---

## 6. Enterprise Examples

*(Illustrative composite scenarios, continuing entities from earlier modules for continuity.)*

### Government Data Platforms
A cross-agency metadata catalog lets one agency discover what data another agency already holds *before* launching a redundant collection effort — directly reducing the duplicated-effort problem described in Section 2. A shared business glossary keeps terms like "resident" (recurring from `data_governance.md` and `data_architecture.md`) aligned across agencies. Lineage becomes essential when a citizen disputes an automated decision (e.g., benefit eligibility) — the agency must be able to trace exactly which source data and transformation logic produced that decision.

### Banking
Operational and technical metadata are what make the BCBS 239 lineage-proof requirement (recurring from `data_governance.md` and `data_quality.md`) actually achievable — a regulator asking "prove where this risk figure came from" is, in metadata terms, asking for lineage. A data catalog lets risk analysts discover which system holds the authoritative version of exposure data instead of manually surveying every IT team. A standardized business glossary for risk terminology prevents the same term meaning different things in different risk models.

### Healthcare
HL7 FHIR resource definitions (introduced in `data_modeling_and_design.md` and `data_architecture.md`) function simultaneously as technical metadata (the structural schema of a "Patient" resource) and business metadata (its clinical meaning) — a useful illustration that the two categories aren't always cleanly separable in practice. A clinical data catalog helps researchers discover relevant, appropriately de-identified datasets without violating access policy. Operational metadata (access logs — who viewed which patient record, and when) is a direct HIPAA audit requirement, not an optional nicety.

### Retail
A data catalog lets analysts and data scientists discover customer and product datasets across the omnichannel platform (recurring from `data_architecture.md`) without manually asking each channel team what exists. Lineage lets an engineer trace a bad personalization-model recommendation back to the specific upstream dataset and transformation that produced it — turning "the recommendation engine is acting strange" from a mystery into a traceable, debuggable problem.

---

## 7. Common Mistakes

1. **Treating metadata as documentation only.** Viewing metadata as static, write-once documentation rather than an actively maintained, machine-usable asset that should power real functionality — search, lineage-driven impact analysis, automated quality checks — means it goes stale immediately and is trusted by no one within a year.
2. **Ignoring operational metadata.** Investing catalog effort entirely into business and technical metadata while operational metadata (freshness, run health, error rates) sits disconnected in a separate monitoring tool — severing the link between "what is this dataset" and "can I trust it *right now*."
3. **No lineage.** Without lineage, both impact analysis (what breaks if I change this) and root-cause analysis (where did this bad value come from) become manual archaeology instead of a traceable lookup.
4. **No business glossary.** Technical metadata alone (column names and types) doesn't tell anyone what a field *means* to the business — this directly recreates the multiple-conflicting-definitions problem `data_governance.md` describes, just one layer removed.
5. **Building catalogs without governance.** Deploying a catalog tool and assuming metadata will become accurate on its own, with no assigned ownership or stewardship reviewing what's in it — the catalog fills with stale, unapproved, or simply wrong metadata, which actively undermines the trust it was supposed to create (a catalog people learn not to trust is worse than no catalog at all).
6. **Assuming lineage happens automatically.** **[Industry Practice observation]** Believing that because a pipeline runs, lineage is somehow being captured passively — in reality, most lineage requires deliberate instrumentation or dedicated scanning tooling; it does not appear for free.

---

## 8. CDMP Exam Preparation

### High-value concepts
- **Precise classification into Business / Technical / Operational metadata** — the exam frequently describes a specific piece of metadata and asks which category it belongs to; this is the single highest-value skill in this Knowledge Area.
- **The relationship between Metadata Management and Data Governance** — Governance decides what must be captured and who owns it; Metadata Management provides the mechanism.
- **Metadata Management vs. Data Architecture** — architecture describes the *intended* data flow; lineage (a metadata artifact) captures the *actual, as-built* record, and the two can diverge.
- **Lineage as a specific, named artifact** combining Technical and Operational metadata — not a fourth metadata category, but a cross-cutting product of the other two.
- **A data catalog as a tool implementing metadata management**, not the discipline itself.

### Important definitions
- Business Metadata, Technical Metadata, Operational Metadata — precise, independent definitions.
- Metadata Repository, Metadata Integration, Metadata Standards, Data Lineage, Data Catalog, Business Glossary.

### Frequently confused concepts
- **Business vs. Technical metadata edge cases** — e.g., a data ownership record is Business Metadata even though it might be stored inside a technical system; classify by *what it describes* (meaning/accountability vs. structure), not by *where it's stored*.
- **Data Catalog vs. Metadata Repository** — a repository is the underlying store; a catalog is typically the searchable, often business-facing interface built on top of one or more repositories. The terms are often used loosely as synonyms in casual conversation, but DAMA treats them as distinct layers.
- **Lineage vs. Data Flow Diagram** — lineage is a detailed, actual, element-level trace of what happened to specific data; a data flow diagram (an Architecture artifact) is a higher-level, intended-state diagram of how systems should exchange data.
- **Metadata Management vs. Data Governance** — governance is decision rights and policy; metadata management is the operational mechanism that makes those decisions visible and enforceable in practice.

---

## 9. Exam Traps

- **A question describes a data ownership or classification field and asks its metadata category.** This is **Business Metadata**, even if it's technically stored as a column in a database table — classify by meaning, not storage location.
- **A question describes ETL job run times or row counts and calls it "technical" metadata.** This is actually **Operational** metadata — schema/structure (Technical) is not the same as execution/runtime facts (Operational); don't conflate the two just because both sound "engineering-related."
- **A question implies a data catalog and a metadata repository are the same thing.** They're related but distinct — a repository is a store; a catalog is a (often business-facing) interface/product built on metadata from one or more repositories.
- **A question implies lineage is a separate, fourth metadata category.** Lineage is a *derived artifact* combining Technical and Operational metadata, not an independent category alongside Business/Technical/Operational.
- **Assuming a well-populated catalog implies good governance.** A catalog can be full of entries and still be untrustworthy if no ownership/stewardship process maintains accuracy — an exam option equating catalog adoption with governance maturity is a trap.
- **Assuming metadata management is purely a technical/IT initiative.** Business Metadata specifically requires business-side involvement (Owners/Stewards) — a scenario framing metadata management as IT-only is inconsistent with DAMA's cross-functional framing (the same trap pattern as Data Governance in `data_governance.md`).

---

## 10. Interview Preparation

### Data Engineer level
1. "How would you capture technical metadata automatically as part of your ETL pipeline, rather than documenting it manually after the fact?"
2. "What's the practical difference between a data catalog and a metadata repository, in your own words?"
3. "How would you document a new table so a business analyst could understand and trust it without asking you directly?"

### Senior Data Engineer level
4. "How would you design pipelines to automatically emit lineage metadata, rather than relying on someone manually documenting it later?"
   *Signal:* discusses either lineage-emission APIs/hooks built into the pipeline framework, or automated parsing/scanning of transformation code — not a manual, easily-outdated wiki page.
5. "A schema change broke three downstream dashboards that nobody realized depended on that table. How would you prevent that going forward?"
   *Signal:* proposes maintaining lineage/dependency metadata specifically so impact analysis is a lookup, not a surprise — and treats the incident as a metadata-capture gap, not just bad luck.
6. "How do you decide what operational metadata is worth capturing versus what's just noise?"
   *Signal:* ties the decision back to what actually supports monitoring/SLA verification and audit needs, rather than capturing everything indiscriminately or nothing at all.

### Data Architect level
7. "How would you design an enterprise metadata management strategy for an organization with dozens of disconnected systems and no existing catalog?"
   *Signal:* starts with scope and prioritization (which domains/systems first, based on risk/value — echoing the governance "don't govern everything at once" lesson), not a big-bang, all-systems-at-once rollout.
8. "How do you keep a data catalog's content from drifting out of sync with the actual current state of systems?"
   *Signal:* discusses automated metadata integration/scanning over manual entry wherever feasible, plus an ownership/review cadence for what can't be automated.
9. "How would you evaluate build-vs-buy for a metadata/catalog platform — for example, open-source options like Apache Atlas or OpenMetadata versus a commercial platform like Microsoft Purview or Collibra?"
   *Signal:* frames the decision around integration breadth with existing systems, governance workflow support, and total ownership cost — not just feature checklists, and correctly treats all of these as *tools implementing* metadata management, not the strategy itself.

---

## 11. Practical Exercises

### Exercise A: Design a Metadata Strategy for a Data Platform
Using the omnichannel retail platform from `data_architecture.md`'s practical exercise (or a platform of your choice), define: (1) scope — which systems/domains are included first; (2) architecture — centralized, federated, or hybrid metadata repository approach, and why; (3) minimum required metadata standard — what fields (owner, classification, definition, freshness SLA) must exist before any new dataset can be published to the catalog; (4) roles — who is responsible for business vs. technical vs. operational metadata, using the Section 4 roles table.

### Exercise B: Build a Simple Data Lineage Example
Take this pipeline: `raw_orders` (ingested from an operational database) → `cleaned_orders` (deduplicated and validated) → `daily_sales_summary` (aggregated) → a BI dashboard. Diagram the lineage from source to dashboard, and for each hop, specify: what technical metadata should be captured (the transformation logic/mapping) and what operational metadata should be captured (run time, row counts in/out, rejected records). Then answer: if `cleaned_orders`' deduplication logic changes, what would lineage let you instantly know that you couldn't otherwise?

### Exercise C: Create a Business Glossary
Pick 5 terms relevant to a domain of your choice (e.g., "Active Customer," "Churned Customer," "Net Revenue," "Order," "Return"). For each, write a proper glossary entry including: a precise business definition, the accountable Owner role, the related technical field(s) it maps to (e.g., which table/column implements it), and one common misinterpretation the definition is meant to prevent.

---

## 12. Flashcards

| Term | Definition |
|---|---|
| Metadata | Data that describes and provides context for other data. |
| Business Metadata | Metadata describing data in business terms — definitions, rules, ownership, classification. |
| Technical Metadata | Metadata describing technical structure — schemas, data types, transformation logic. |
| Operational Metadata | Metadata describing execution/runtime facts — job status, row counts, freshness, access logs. |
| Metadata Repository | A managed store holding metadata records, centralized or federated. |
| Metadata Management Strategy | A defined plan for how metadata will be collected, integrated, stored, and governed. |
| Metadata Integration | Harmonizing metadata from many disparate source systems into one coherent view. |
| Metadata Standards | Enterprise rules governing how metadata itself must be structured and classified. |
| Data Lineage | Traceable record of data's origin, movement, and transformation history. |
| Data Catalog | A searchable inventory bringing business, technical, and operational metadata into one discoverable interface. |
| Business Glossary | A governed collection of business term definitions. |
| Data Swamp | Industry-practice term for an ungoverned, undiscoverable data lake lacking metadata discipline. |
| Metadata-as-data | DAMA's point that metadata must itself be governed and quality-managed, not assumed reliable by default. |

---

## 13. Quiz Questions

1. A record showing an ETL job ran for 12 minutes and processed 40,000 rows is an example of:
   a) Business Metadata b) Technical Metadata c) Operational Metadata d) A business glossary entry

2. A documented business rule stating "Revenue excludes refunds within 30 days" is:
   a) Technical Metadata b) Operational Metadata c) Business Metadata d) Data Lineage

3. What is the key relationship between a Data Catalog and a Metadata Repository?
   a) They are always the same product b) A repository is the underlying store; a catalog is typically the searchable interface built on metadata from one or more repositories c) A catalog replaces the need for governance d) A repository only stores operational metadata

4. What does Data Lineage primarily combine?
   a) Business and Governance metadata only b) Technical and Operational metadata c) A fourth, independent metadata category d) Only Business Metadata

5. What distinguishes a Data Flow Diagram (Architecture) from Data Lineage (Metadata Management)?
   a) They are identical artifacts b) A data flow diagram is the intended, high-level design; lineage is the actual, as-built trace c) Lineage is only used in banking d) Data flow diagrams are more detailed than lineage

6. Who is typically the primary curator of business glossary definitions?
   a) Data Custodian b) Data Steward c) Data Engineer d) Metadata repository vendor

7. What is a "data swamp"?
   a) A DAMA-official term for a well-governed lake b) An industry term for an ungoverned, undiscoverable data lake lacking metadata c) A type of metadata repository d) A synonym for a data catalog

8. Why is building a data catalog without governance a common mistake?
   a) Catalogs are always too expensive without governance b) Without ownership/stewardship, the catalog fills with stale or unapproved metadata, undermining trust c) Catalogs cannot technically function without governance software d) Governance is only required for operational metadata

9. Column data types and table names are an example of:
   a) Operational Metadata b) Business Metadata c) Technical Metadata d) A business glossary

10. What is the primary risk of assuming lineage is captured automatically just because a pipeline runs?
    a) Pipelines will fail to execute b) Lineage typically requires deliberate instrumentation; assuming otherwise means it likely isn't being captured at all c) Lineage is only relevant for streaming pipelines d) There is no risk; lineage is always automatic

**Answer Key:** 1-c, 2-c, 3-b, 4-b, 5-b, 6-b, 7-b, 8-b, 9-c, 10-b

---

## 14. References

**DAMA Official:**
- DAMA-DMBOK2, 2nd Edition — Chapter 12: Metadata Management (primary source; verify exact wording and any enumerated lists against your own copy)
- DAMA Dictionary of Data Management Terminology (glossary cross-reference)

**Industry Practices (real, not DAMA-official — cited in this module):**
- "Data swamp" — industry term for an ungoverned, undiscoverable data lake
- Lakehouse-embedded technical metadata (e.g., Delta Lake, Apache Iceberg transaction logs) as a modern evolution of technical metadata capture
- Data contracts as enforced, formalized metadata (cross-referenced from `data_quality.md`)

**Tools/Frameworks (real, named for concreteness — tool choice is an implementation detail, not a DAMA concept):**
- Microsoft Purview — commercial data governance/catalog platform
- Apache Atlas — open-source metadata and governance framework originating in the Hadoop ecosystem
- OpenMetadata — open-source metadata catalog platform
- Collibra — commercial data governance/catalog platform

**Internal:**
- `research/cdmp_exam_overview.md` — exam structure and Knowledge Area weighting
- `roadmap/four_month_plan.md` — Week 6 study plan for this module
- `knowledge_base/data_governance.md` — business glossary, ownership, and standards cross-references
- `knowledge_base/data_architecture.md` — data flow diagrams vs. lineage distinction, and the omnichannel retail scenario used in Practical Exercise A
- `knowledge_base/data_quality.md` — data contracts and the quality/metadata relationship
