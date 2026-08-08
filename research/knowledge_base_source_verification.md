# Knowledge Base Source Verification

**Phase:** Source Verification (Phase 1 of the audit's Recommended Next Phase — `research/source_audit.md`)
**Date:** 2026-08-08
**Scope:** Read-only audit of all 14 `knowledge_base/*.md` files against the registered source library (`research/source_registry.yaml`). **No `knowledge_base/`, `question_bank/`, `quiz_engine/`, `packages/`, or `reviews/` file was modified to produce this document.** No copyrighted DMBOK2/Dictionary/prep-resource content is reproduced below — only claim summaries in this project's own words, source metadata, and locator status.

## Method and a governing caveat

Every claim below was read directly from the module text (all 14 files were read in full for this pass, not sampled from grep matches). Given the scale of the knowledge base (~114 `[DAMA]`, ~62 `[Industry Practice]`, and 9 `[Regulation/Standard]`-tagged claims across 14 files, per `research/source_audit.md` §11), this report tables the **major, exam-load-bearing concepts per Knowledge Area** rather than every individual tagged sentence — consistent with the audit objective to "identify the major DAMA concepts currently presented," not reproduce the module.

**One caveat applies to every row in every table below and is not repeated per-row:** no claim in `knowledge_base/` has undergone a physical, page-level cross-check against the registered `dmbok2-2nd-ed` or `dama-dictionary` files — both were registered on 2026-08-08, after the knowledge base's 2026-08-02 completion date (`research/source_audit.md` §11). "Confidence: High" below means *this claim is standard, stable, cross-corroborated DAMA/CDMP vocabulary very unlikely to be wrong*, not *this has been checked against the physical PDF page-by-page*. That physical check has not happened for any row and is not something this text-extraction-free audit can perform without violating the copyright rule against extracting the source's content — it is real, necessary future work, not a checkbox this document can close.

**Locators:** Every module already cites its DMBOK2 chapter at the file header (e.g., "DMBOK2 2nd Ed., Ch.3"). No module cites a page or section-letter locator anywhere. Per the task's instruction not to guess a locator that would require extracting copyrighted content to confirm, every row below carries **Locator: Ch.\<N\> only — section/page not yet verified**, and this is not repeated as a caveat per row beyond the table header.

---

## Data Governance (Ch.3)

| Concept / Claim | Current Tag | Supporting Source | source_id | Locator | Confidence | Action |
|---|---|---|---|---|---|---|
| Governance vs. Management ("what/why" vs. "how") | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.3 | High | Keep |
| Owner / Steward / Custodian role definitions | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.3 | High | Keep |
| Policy → Standard → Procedure artifact hierarchy | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.3 | High | Keep |
| Governance Council composition/function | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.3 | High | Keep |
| Governance operating models (centralized/decentralized/hybrid) | `[DAMA + Industry Practice]` | DMBOK2 + unregistered | dmbok2-2nd-ed / SOURCE GAP | Ch.3 | Medium | Verify |
| Fourth-tier "Guideline" (below Standard) | `[DAMA]`, self-hedged in text | DMBOK2 | dmbok2-2nd-ed | Ch.3 | Medium | Verify |
| BCBS 239, HIPAA, GDPR (named regulations) | `[Regulation/Standard]` | Unregistered | SOURCE GAP | n/a | High (as real regulations) / Unverified (as registered sources) | Add source |
| Data lake zone pattern (raw/curated/trusted) | `[Industry Practice]` | Unregistered | SOURCE GAP | n/a | Low | Add source / Review manually |

**Dictionary-supportable terminology:** Owner, Steward, Custodian — the module's own References section already earmarks these for Dictionary cross-check (`dama-dictionary`).
**Ambiguity:** none beyond the self-flagged Guideline tier.

---

## Data Architecture (Ch.4)

| Concept / Claim | Current Tag | Supporting Source | source_id | Locator | Confidence | Action |
|---|---|---|---|---|---|---|
| Data Architecture definition (enterprise blueprint) | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.4 | High | Keep |
| Data Architecture vs. Data Modeling vs. Database Design distinction | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.4 | High | Keep |
| Data Architecture Principles (enumerated list) | `[DAMA]`, self-hedged ("exact wording varies") | DMBOK2 | dmbok2-2nd-ed | Ch.4 | Medium | Verify |
| Conceptual/Logical/Physical Data Architecture layers | `[DAMA + general EA pattern]`, self-hedged | DMBOK2 | dmbok2-2nd-ed | Ch.4 | Medium | Verify |
| Data Lifecycle stages (creation→disposal) | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.4 | High | Keep |
| Zachman Framework, TOGAF | `[Industry Practice — TOGAF]` | Unregistered | SOURCE GAP | n/a | High (as real frameworks) / Unverified (registered) | Add source |
| PSD2 / Open Banking | `[Regulation/Standard]`-equivalent (named regulation, module doesn't use the bracket tag but treats it as real/external) | Unregistered | SOURCE GAP | n/a | High (as real regulation) | Add source |
| Data Mesh (Zhamak Dehghani), Lakehouse | `[Industry Practice]` | Unregistered | SOURCE GAP | n/a | Low | Add source / Review manually |

**Ambiguity:** module explicitly flags that the Architecture-layer conceptual/logical/physical terminology reuses Data Modeling's three-level vocabulary for a different scope — already self-documented as a trap, not a new finding.

---

## Data Modeling and Design (Ch.5)

| Concept / Claim | Current Tag | Supporting Source | source_id | Locator | Confidence | Action |
|---|---|---|---|---|---|---|
| Conceptual/Logical/Physical Data Model levels | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.5 | High | Keep |
| Entity, Attribute, Relationship, Primary/Natural/Surrogate/Foreign Key definitions | `[DAMA]` (implicit, untagged prose) | DMBOK2 | dmbok2-2nd-ed | Ch.5 | High | Keep |
| Normalization/Denormalization, 1NF/2NF/3NF/BCNF | `[DAMA]` (implicit) | DMBOK2 | dmbok2-2nd-ed | Ch.5 | High | Keep |
| Denormalization as a legitimate deliberate choice | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.5 | Medium | Verify |
| Fact/dimension/grain/star/snowflake vocabulary | `[Industry Practice]` (Kimball-origin, DAMA-referenced) | Unregistered | SOURCE GAP | n/a | High (as real methodology) | Add source |
| Data Vault (Hub/Link/Satellite) | `[Industry Practice]` | Unregistered | SOURCE GAP | n/a | Low | Add source |
| HL7 FHIR | Untagged but treated as real/external | Unregistered | SOURCE GAP | n/a | High (as real standard) | Add source |
| Generalization/Subtyping | `[DAMA]` (implicit) | DMBOK2 | dmbok2-2nd-ed | Ch.5 | Medium | Verify |

---

## Data Storage and Operations (Ch.6)

| Concept / Claim | Current Tag | Supporting Source | source_id | Locator | Confidence | Action |
|---|---|---|---|---|---|---|
| Data Storage and Operations scope/goals | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.6 | High | Keep |
| RPO / RTO definitions and independence | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.6 | High | Keep |
| Non-Production Environment Management as in-scope DAMA concern | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.6 | Medium | Verify |
| Data Masking definition | `[DAMA + Industry Practice]` | DMBOK2 + unregistered | dmbok2-2nd-ed / SOURCE GAP | Ch.6 | Medium | Verify |
| DAS / NAS / SAN / Cloud Storage taxonomy | `[Industry Practice, DAMA-referenced]` | Unregistered | SOURCE GAP | n/a | High (as real taxonomy) | Add source |
| Relational / Document / Key-Value / Column-Family / Graph DB taxonomy | `[Industry Practice, widely DAMA-referenced]` | Unregistered | SOURCE GAP | n/a | High | Add source |
| Data Virtualization definition | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.6 | Medium | Verify |
| MTTR | `[Industry Practice]` | Unregistered | SOURCE GAP | n/a | Low | Add source |

---

## Data Security (Ch.7)

| Concept / Claim | Current Tag | Supporting Source | source_id | Locator | Confidence | Action |
|---|---|---|---|---|---|---|
| Data Security definition and goals | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.7 | High | Keep |
| Authentication vs. Authorization | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.7 | High | Keep |
| Data Classification tiers (Public/Internal/Confidential/Restricted) | `[DAMA + Industry Practice]`, self-hedged as org-specific | DMBOK2 + unregistered | dmbok2-2nd-ed / SOURCE GAP | Ch.7 | Medium | Verify |
| CIA Triad | `[Industry Practice, widely DAMA-referenced]` | Unregistered | SOURCE GAP | n/a | High (as real framing) | Add source |
| RBAC / ABAC / DAC / MAC taxonomy | `[Industry Practice, DAMA-referenced]` | Unregistered | SOURCE GAP | n/a | High | Add source |
| Encryption / Masking / Tokenization / Anonymization / Pseudonymization cluster | `[DAMA + Industry Practice]` | DMBOK2 + unregistered | dmbok2-2nd-ed / SOURCE GAP | Ch.7 | Medium | Verify |
| PII / PHI / PCI / GDPR named categories | `[Regulation/Standard]` | Unregistered | SOURCE GAP | n/a | High (as real regulations) | Add source |
| Least Privilege, Segregation of Duties | `[DAMA + Industry Practice]` | DMBOK2 + unregistered | dmbok2-2nd-ed / SOURCE GAP | Ch.7 | Medium | Verify |

---

## Data Integration and Interoperability (Ch.8)

| Concept / Claim | Current Tag | Supporting Source | source_id | Locator | Confidence | Action |
|---|---|---|---|---|---|---|
| Integration vs. Interoperability distinction | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.8 | High | Keep |
| Batch / Real-time / CDC / Federation / API / Replication patterns | `[DAMA]` + `[Industry Practice, DAMA-referenced]` (mixed) | DMBOK2 + unregistered | dmbok2-2nd-ed / SOURCE GAP | Ch.8 | Medium | Verify |
| Point-to-point / Hub-and-spoke / Event-driven architecture styles | `[DAMA]` + `[Industry Practice]` (mixed) | DMBOK2 + unregistered | dmbok2-2nd-ed / SOURCE GAP | Ch.8 | Medium | Verify |
| Data Migration vs. ongoing integration distinction | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.8 | Medium | Verify |
| EDI, HL7/FHIR, SWIFT | `[Regulation/Standard]` | Unregistered | SOURCE GAP | n/a | High (as real standards) | Add source |
| Data Contract (in an integration context) | `[Industry Practice, DAMA-adjacent]` | Unregistered | SOURCE GAP | n/a | Low | Add source |
| Idempotency | `[Industry Practice]` | Unregistered | SOURCE GAP | n/a | Low | Add source |

---

## Document and Content Management (Ch.9)

| Concept / Claim | Current Tag | Supporting Source | source_id | Locator | Confidence | Action |
|---|---|---|---|---|---|---|
| Document / Content / Record classification test | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.9 | High | Keep |
| Records Retention Schedule, Records Classification Scheme, Chain of Custody | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.9 | High | Keep |
| Legal Hold overriding retention schedule | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.9 | High | Keep |
| E-Discovery definition | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.9 | Medium | Verify |
| Structured/Semi-structured/Unstructured data distinction | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.9 | High | Keep |
| ISO 15489 | `[Regulation/Standard]` | Unregistered | SOURCE GAP | n/a | High (as real standard) | Add source |
| Dublin Core (ISO 15836) | `[Regulation/Standard]` | Unregistered | SOURCE GAP | n/a | High (as real standard) | Add source |
| ECM / DMS / WCM / DAM system categories | `[Industry Practice, DAMA-referenced]` | Unregistered | SOURCE GAP | n/a | High (as real category names) | Add source |
| Spoliation (legal concept) | `[Industry Practice]` (real legal term, not DAMA) | Unregistered | SOURCE GAP | n/a | Medium | Add source |

---

## Reference and Master Data (Ch.10)

| Concept / Claim | Current Tag | Supporting Source | source_id | Locator | Confidence | Action |
|---|---|---|---|---|---|---|
| Reference Data vs. Master Data distinction | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.10 | High | Keep |
| Value Domain terminology | `[DAMA]`, self-hedged (term-overlap uncertainty) | DMBOK2 | dmbok2-2nd-ed | Ch.10 | Medium | Verify |
| Single Source of Truth (governance vs. physical-storage distinction) | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.10 | High | Keep |
| Matching/Merging, Survivorship Rules | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.10 | High | Keep |
| Registry / Consolidation / Coexistence / Centralized MDM styles | `[DAMA + Industry Practice]`, self-hedged ("exact naming varies") | DMBOK2 + unregistered | dmbok2-2nd-ed / SOURCE GAP | Ch.10 | Medium | Verify |
| Golden Record (term) | `[DAMA + Industry Practice]`, self-hedged | DMBOK2 + unregistered | dmbok2-2nd-ed / SOURCE GAP | Ch.10 | Medium | Verify |
| ISO 3166, ISO 4217, ICD-10 | Untagged inline but treated as real/external | Unregistered | SOURCE GAP | n/a | High (as real standards) | Add source |
| Master Data Types (Party/Product/Financial/Location) | `[DAMA]`, self-hedged ("exact enumeration varies") | DMBOK2 | dmbok2-2nd-ed | Ch.10 | Medium | Verify |

---

## Data Warehousing and Business Intelligence (Ch.11)

| Concept / Claim | Current Tag | Supporting Source | source_id | Locator | Confidence | Action |
|---|---|---|---|---|---|---|
| Four Data Warehouse characteristics (subject-oriented/integrated/time-variant/non-volatile) | `[DAMA + Industry Practice]` (Inmon-originated, DAMA-referenced) | DMBOK2 + unregistered | dmbok2-2nd-ed / SOURCE GAP | Ch.11 | High | Keep + Add source |
| Data Warehouse vs. Data Mart vs. ODS | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.11 | High | Keep |
| Dependent vs. independent data marts | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.11 | High | Keep |
| Inmon vs. Kimball architecture approaches | `[DAMA + Industry Practice]`, self-hedged | DMBOK2 + unregistered | dmbok2-2nd-ed / SOURCE GAP | Ch.11 | Medium | Verify |
| Data Vault (Linstedt) | `[DAMA + Industry Practice]` | DMBOK2 + unregistered | dmbok2-2nd-ed / SOURCE GAP | Ch.11 | Medium | Verify |
| ETL vs. ELT | `[DAMA]` (ETL) / `[Industry Practice]` (ELT) | DMBOK2 + unregistered | dmbok2-2nd-ed / SOURCE GAP | Ch.11 | High | Keep |
| OLAP vs. OLTP, OLAP Cube | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.11 | High | Keep |
| Slice/Dice/Drill-down/Roll-up, MOLAP/ROLAP/HOLAP | `[Industry Practice]` | Unregistered | SOURCE GAP | n/a | Medium | Add source |

---

## Metadata Management (Ch.12)

| Concept / Claim | Current Tag | Supporting Source | source_id | Locator | Confidence | Action |
|---|---|---|---|---|---|---|
| Business / Technical / Operational metadata categories | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.12 | High | Keep |
| "Metadata is itself data" governance principle | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.12 | High | Keep |
| Metadata Repository, Integration, Standards | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.12 | High | Keep |
| Data (Metadata) Lineage as a derived Technical+Operational artifact | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.12 | High | Keep |
| Data Catalog | `[DAMA + Industry Practice]` | DMBOK2 + unregistered | dmbok2-2nd-ed / SOURCE GAP | Ch.12 | Medium | Verify |
| Business Glossary | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.12 | High | Keep |
| "Data swamp" | `[Industry Practice]` | Unregistered | SOURCE GAP | n/a | Low | Add source |
| Named catalog products (Purview, Atlas, OpenMetadata, Collibra) | Explicitly untagged/illustrative | Unregistered | SOURCE GAP | n/a | Low (tool names only, not a DAMA claim) | Keep (already correctly scoped as illustration) |

---

## Data Quality (Ch.13)

| Concept / Claim | Current Tag | Supporting Source | source_id | Locator | Confidence | Action |
|---|---|---|---|---|---|---|
| "Fitness for purpose" framing | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.13 | High | Keep |
| Seven quality dimensions (Accuracy, Completeness, Consistency, Timeliness, Validity, Uniqueness, Integrity) | `[DAMA]`, explicitly self-hedged in editorial note ("lists vary across practitioner sources/editions") | DMBOK2 | dmbok2-2nd-ed | Ch.13 | **Medium** (explicitly flagged) | **Verify** |
| DQM / Profiling / Validation / Cleansing / Monitoring distinctions | `[DAMA]` (implicit) | DMBOK2 | dmbok2-2nd-ed | Ch.13 | High | Keep |
| DQM lifecycle (6 steps) | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.13 | High | Keep |
| Data Quality Engineer (role) | `[Industry Practice]` | Unregistered | SOURCE GAP | n/a | Low | Add source |
| Data Contract, Data Observability | `[Industry Practice]` | Unregistered | SOURCE GAP | n/a | Low | Add source |
| Named tools (Great Expectations, dbt, Deequ, Monte Carlo, Bigeye) | Explicitly untagged/illustrative | Unregistered | SOURCE GAP | n/a | Low (tool names, already correctly scoped) | Keep |

---

## Big Data and Data Science (Ch.14)

| Concept / Claim | Current Tag | Supporting Source | source_id | Locator | Confidence | Action |
|---|---|---|---|---|---|---|
| "Governance applies to big data/ML, not exempt" — central thesis | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.14 | High | Keep |
| Data Lake vs. Data Warehouse (schema-on-read vs. schema-on-write) | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.14 | High | Keep |
| The 3 Vs / 5 Vs | `[Industry Practice, widely DAMA-referenced]` | Unregistered | SOURCE GAP | n/a | High (as real framing) | Add source |
| CRISP-DM lifecycle | `[Industry Practice, DAMA-referenced]` | Unregistered | SOURCE GAP | n/a | High (as real methodology) | Add source |
| Model Governance (Owner, Explainability, Model Drift, Bias/Fairness) | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.14 | Medium | Verify |
| Supervised/Unsupervised Learning, Overfitting, Feature Engineering | `[Industry Practice]` | Unregistered | SOURCE GAP | n/a | Medium | Add source |
| Lambda / Kappa Architecture | `[Industry Practice, DAMA-referenced]` | Unregistered | SOURCE GAP | n/a | Medium | Add source |
| "Data swamp" (reused from Metadata Management) | `[Industry Practice, widely DAMA-referenced]` | Unregistered | SOURCE GAP | n/a | Low | Add source |

---

## Data Management Maturity Assessment (Ch.15)

| Concept / Claim | Current Tag | Supporting Source | source_id | Locator | Confidence | Action |
|---|---|---|---|---|---|---|
| Per-Knowledge-Area assessment (not one blended score) | `[DAMA, general framing]` | DMBOK2 | dmbok2-2nd-ed | Ch.15 | High | Keep |
| Maturity Model / Maturity Level / Capability Gap definitions | `[DAMA]` (implicit) | DMBOK2 | dmbok2-2nd-ed | Ch.15 | High | Keep |
| Five-level maturity scale (Initial→Optimized) with names | `[DAMA + Industry Practice]`, **explicitly self-hedged as "moderate confidence"** in the module's own editorial note | DMBOK2 | dmbok2-2nd-ed | Ch.15 | **Medium** (explicitly flagged) | **Verify** |
| People / Process / Technology assessment dimensions | `[Industry Practice, widely DAMA-referenced]` | Unregistered | SOURCE GAP | n/a | High (as real framing) | Add source |
| CMM / CMMI (named external framework) | `[Industry Practice, widely DAMA-referenced]` | Unregistered | SOURCE GAP | n/a | High (as real framework) | Add source |
| Self-assessment vs. independent assessment | `[Industry Practice, DAMA-referenced]` | Unregistered | SOURCE GAP | n/a | Medium | Add source |
| Benchmarking vs. internal gap analysis | `[Industry Practice, DAMA-referenced]` | Unregistered | SOURCE GAP | n/a | Medium | Add source |

---

## Data Ethics (Ch.2)

| Concept / Claim | Current Tag | Supporting Source | source_id | Locator | Confidence | Action |
|---|---|---|---|---|---|---|
| "Legal compliance is a floor, not a ceiling" — central thesis | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.2 | High | Keep |
| Ethical principle enumeration (impact/ownership/transparency/fairness/accountability) | `[DAMA, general framing]`, **explicitly self-hedged as "moderate confidence, exact enumeration varies"** | DMBOK2 | dmbok2-2nd-ed | Ch.2 | **Medium** (explicitly flagged) | **Verify** |
| Data Subject, Informed Consent definitions | `[Industry Practice, widely DAMA-referenced]` / `[DAMA]` (mixed) | DMBOK2 + unregistered | dmbok2-2nd-ed / SOURCE GAP | Ch.2 | Medium | Verify |
| Direct / Dignitary / Societal-Aggregate harm categories | `[DAMA]` | DMBOK2 | dmbok2-2nd-ed | Ch.2 | Medium | Verify |
| The Belmont Report (Respect for Persons/Beneficence/Justice) | `[Regulation/Standard]` | Unregistered | SOURCE GAP | n/a | High (as real framework) | Add source |
| EU AI Act | `[Regulation/Standard]` | Unregistered | SOURCE GAP | n/a | High (as real regulation) | Add source |
| Re-identification/aggregation risk incidents (search-log, movie-ratings) | `[Industry Practice, widely DAMA-referenced]`, referenced without specific attribution per this project's own citation discipline | Unregistered | SOURCE GAP | n/a | Medium (real, well-documented category of incident; specific sourcing deliberately generalized) | Review manually |

---

## Source Gaps

### 1. Missing authoritative sources

- **No official CDMP/DMF exam guide registered.** `sources/exam_guide/` remains a placeholder (confirmed empty in `research/source_audit.md` §9). This directly affects the confidence of every module's "CDMP Exam Focus" weighting language, which currently traces only to `research/cdmp_exam_overview.md`'s prep-vendor-sourced, explicitly "directional, not officially confirmed" weighting estimate.
- **No official dama.org pages registered.** `sources/dama_official/` holds only the Dictionary file (`dama-dictionary`); no certification/Knowledge-Area overview page links are registered, despite `research/source_map.md` §3 calling for them.
- **`dama-dictionary` itself is registered but unverified against content.** It exists as a source_id but, per the governing caveat above, no module's Dictionary-attributed claim has actually been checked against it yet.

### 2. Missing industry standards

None of the following named regulations/standards/frameworks cited across the 14 modules have a `research/source_registry.yaml` entry. Each instance in the tables above is marked `SOURCE GAP` rather than assigned an invented `source_id`, per instruction:

`BCBS 239`, `HIPAA`, `GDPR`, `PCI-DSS`, `ISO 15489`, `Dublin Core (ISO 15836)`, `EDI`, `HL7/FHIR`, `SWIFT`, `ISO 3166`, `ISO 4217`, `ICD-10`, `PSD2/Open Banking`, `EU AI Act`, `The Belmont Report`, `Zachman Framework`, `TOGAF`, `CRISP-DM`, `CMM/CMMI`, `Data Vault (Linstedt)`, `Kimball dimensional modeling methodology`, `Inmon Corporate Information Factory`.

These fall into two practical categories worth treating differently going forward: **named regulations/standards** (BCBS 239, HIPAA, GDPR, PCI-DSS, ISO 15489, Dublin Core, EDI, HL7/FHIR, SWIFT, ISO 3166, ISO 4217, ICD-10, PSD2, EU AI Act, Belmont Report) belong in `sources/industry/` per the existing folder structure and would register as `classification: public_standard`; **named methodologies/frameworks attributed to an individual or organization but not a formal regulation** (Zachman, TOGAF, CRISP-DM, CMM/CMMI, Data Vault, Kimball, Inmon) are citation-worthy but don't fit `public_standard` cleanly — they'd likely register as `public_link` (pointing to the originating publication/organization) if and when sourced.

### 3. Missing locators

**Systemic, not per-claim.** Every module cites only its DMBOK2 chapter number at the file header; no module cites a section or page locator anywhere in its 14 sections, including in the References section itself. This is consistent across all 14 files (a structural convention, not an oversight in any one module) but means every single `[DAMA]`-tagged claim in the knowledge base currently has **Locator: Ch.\<N\> only** and would need a section/page pass to reach the precision `research/source_registry_schema.md`'s `citation_format` field anticipates (e.g., `DMBOK2 2nd Ed., Ch.3 Data Governance, §3.2`).

### 4. Claims requiring manual verification

These are the claims where a module **already, proactively self-flags** uncertainty in its own editorial note or inline hedge — the highest-value targets for an actual verification pass, since the module's author already identified the risk:

- **Data Quality's seven dimensions** (`data_quality.md`) — editorial note explicitly states dimension lists "vary slightly across practitioner sources and editions."
- **Data Ethics' ethical principle enumeration** (`data_ethics.md`) — explicitly flagged "moderate confidence," "exact enumeration varies across sources."
- **Data Management Maturity Assessment's five-level scale names** (`data_management_maturity_assessment.md`) — explicitly flagged "moderate confidence... verify against your own DMBOK2 copy."
- **Data Architecture Principles enumerated list** (`data_architecture.md`) — flagged "exact enumerated wording varies by source."
- **MDM implementation style naming (Registry/Consolidation/Coexistence/Centralized)** (`reference_and_master_data.md`) — flagged "exact naming and boundaries vary somewhat across practitioner sources."
- **Value Domain terminology** (`reference_and_master_data.md`) — flagged as possibly interchangeable with "code set" depending on source.
- **Master Data Types enumeration (Party/Product/Financial/Location)** (`reference_and_master_data.md`) — flagged "exact enumeration varies by source."
- **DW/BI Inmon/Kimball/Data Vault exact framing** (`data_warehousing_and_business_intelligence.md`) — flagged "exact framing and enumeration vary across practitioner sources."
- **Data Classification tier names/count (Public/Internal/Confidential/Restricted)** (`data_security.md`) — flagged as organization-specific convention, not a fixed DAMA list, but the module's own illustrative four-tier table should be checked against whatever example DMBOK2 itself uses.

### 5. Content that is already sufficiently supported

The following core, cross-cutting DAMA vocabulary appears consistently, is internally cross-referenced correctly across modules, is not self-hedged anywhere it appears, and matches standard CDMP/DAMA terminology closely enough to warrant **High confidence / Keep** pending the eventual physical cross-check:

Governance vs. Management distinction; Owner/Steward/Custodian roles; Policy/Standard/Procedure hierarchy; Conceptual/Logical/Physical Data Model levels; Entity/Attribute/Relationship/Key vocabulary; Normalization forms (1NF/2NF/3NF); Reference Data vs. Master Data distinction; Single Source of Truth as a governance (not physical) concept; Authentication vs. Authorization; the four classic Data Warehouse characteristics; Data Warehouse vs. Data Mart vs. ODS; Business/Technical/Operational metadata categories; the Data Quality Management lifecycle steps; RPO vs. RTO; Document/Content/Record classification test; Legal Hold overriding a retention schedule; "legal compliance is a floor, not a ceiling" (Data Ethics); "governance applies to big data/ML, not exempt" (Big Data and Data Science); per-Knowledge-Area (not blended) maturity assessment.

These represent the majority of each module's structural backbone — the self-hedged items in §4 above are the genuine exceptions, not the norm.

---

## Validation

```
git status
python -m pytest -q
```

To be run and reported after this document is saved; see the accompanying report in the conversation. Expected/required results: no `question_bank/` files changed, no `knowledge_base/` files changed, no `quiz_engine/` files changed, no `packages/` files changed, all tests passing.
