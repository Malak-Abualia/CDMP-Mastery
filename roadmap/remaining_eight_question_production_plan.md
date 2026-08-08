# Question Production Plan — Remaining 8 Knowledge Areas

**Date:** 2026-08-08
**Status:** Planning only. No question was generated, and no existing content was modified, to produce this document.
**Scope:** Big Data and Data Science (BIGDATA), Data Ethics (ETH), Data Integration and Interoperability (INTEG), Data Management Maturity Assessment (MAT), Data Security (SEC), Data Storage and Operations (STOR), Data Warehousing and Business Intelligence (DWBI), Document and Content Management (DOC).

## Method

Each KA below was inspected against: its `knowledge_base/*.md` module (full content, previously read in this session), its module review (`reviews/<module>_review.md`), its existing question set (`question_bank/questions/<module>/*.yaml`, inventoried field-by-field), its question-bank review where one exists (`reviews/questions_<module>_review.md`), its `taxonomy.md` topic/subtopic table, and the source-coverage findings already established in `research/source_audit.md`. **No new per-concept source-verification pass** (of the depth `research/knowledge_base_source_verification.md` gave the first six KAs) has been done for these eight yet — that remains a gap, noted per KA below, not something this planning pass fabricates.

Six of these eight KAs already carry a cross-KA hook to the six-KA batch just completed, established from the *other* KA's side (e.g., `MASTER-026` already tests "golden record as the source for a DW/BI conformed dimension" from Reference and Master Data's primary-KA angle). Where that's true, it's named explicitly below — the recommendation is to author the *complementary*, DWBI-primary (or SEC-primary, etc.) version of the same relationship, mirroring the two-sided-reinforcement pattern already validated and accepted in the six-KA audit, not to re-test the same fact redundantly.

---

## 1. Data Management Maturity Assessment (MAT)

- **Current question count:** 6 (5 Beginner, 1 Intermediate; 0 Advanced) — by far the thinnest of the 14 KAs.
- **Knowledge-base approval status:** Approved, 92/100 (`reviews/data_management_maturity_assessment_review.md`).
- **Existing topic/subtopic coverage (`taxonomy.md`):** Core Distinction; Maturity Levels; Assessment Dimensions; Assessment Methods; Roadmap and Benchmarking — 5 topics defined, only the first two have *any* question, and only barely.
- **Existing question coverage:** Definitions only — Data Management Maturity Assessment, Maturity Model, Capability Gap, Level 1 (Initial/Ad Hoc), CMM/CMMI, plus one Intermediate scenario on per-KA-vs-blended scoring. **No question-bank review exists for this KA** (`reviews/questions_data_management_maturity_assessment_review.md` is absent — confirmed by directory listing).
- **Missing concepts:** Levels 2–5 individually (Repeatable, Defined, Quantitatively Managed, Optimized); the People/Process/Technology assessment dimensions (the module's own stated highest-value concept); Self-Assessment vs. Independent/External Assessment; evidence-gathering techniques; Benchmarking vs. internal gap analysis; gap-times-impact prioritization; the "documented (Level 3) ≠ actually followed" trap; the "technology-only maturity illusion" pattern (a full Enterprise Example in the module, untested).
- **Missing scenario coverage:** Zero Advanced-tier content, zero Multiple Select, zero cross-KA tagging — despite the module explicitly cross-referencing Data Governance (Council as sponsor), Data Ethics (as an assessable KA), Data Storage and Operations (RPO/RTO prioritization pattern reused), and Big Data and Data Science (Model Governance's differentiated-review pattern reused).
- **Recommended additional question count:** **+11** (bringing the set to 17 — the largest single addition of the eight, proportional to the largest gap).
- **Recommended difficulty distribution (of the +11):** 2 Beginner (round out Level definitions), 5 Intermediate, 4 Advanced.
- **Recommended question-type distribution:** 5 Multiple Choice, 4 Scenario-Based, 2 Multiple Select.
- **Source availability:** `dmbok2-2nd-ed` (primary), `dama-dictionary` (terminology). No named regulation/standard is specific to this KA beyond `CMM/CMMI` (already `SOURCE GAP`, unregistered).
- **Source gaps:** CMM/CMMI unregistered (`SOURCE GAP`); module's own maturity-level enumeration is explicitly self-hedged as "moderate confidence" (per `research/knowledge_base_source_verification.md`'s §4 finding for the six-KA batch — the same hedge applies here even though this KA wasn't in that batch's scope).
- **Highest-value CDMP concepts:** per-Knowledge-Area (not blended) assessment; People/Process/Technology dimensions; the technology-only-maturity-illusion trap.
- **Recommended real-world domains:** insurance, telecom, government/public sector (none used yet for this KA — the module's own examples are banking, healthcare, retail, manufacturing).

## 2. Data Warehousing and Business Intelligence (DWBI)

- **Current question count:** 20 (5/10/5).
- **Knowledge-base approval status:** Approved, 93/100 (`reviews/data_warehousing_and_business_intelligence_review.md`).
- **Existing topic/subtopic coverage:** Store Types; DW/BI Architecture Approaches; Data Movement; Analytical Processing; BI Delivery and Value — all five topics have coverage.
- **Existing question coverage:** Solid across all five topics — DW/BI/Mart/ETL/OLAP definitions; dependent-vs-independent mart, ODS-vs-DW, Inmon-vs-Kimball, ETL-vs-ELT, OLAP-vs-OLTP scenarios; conformed dimension purpose; BI delivery mechanisms; semantic layer; self-service governance risk; architecture-selection-under-regulation, independent-mart-proliferation, success metrics, retention/archival governance at Advanced tier.
- **Missing concepts:** Data Vault (Hub/Link/Satellite) has no *dedicated* question (only touched indirectly via Inmon/Kimball); Slice/Dice/Drill-down/Roll-up OLAP operations; MOLAP/ROLAP/HOLAP variants.
- **Missing scenario coverage:** Two specific cross-KA mirror opportunities are open, both already validated from the *other* side in the six-KA batch: conformed dimension sourced from an MDM golden record (already tested as `MASTER-026`, no DWBI-primary counterpart yet) and semantic layer as a Business Metadata application (already tested as `META-025`, no DWBI-primary counterpart yet).
- **Recommended additional question count:** **+7** — the largest addition among the seven KAs that already have a full 20, reflecting this KA's ~10% exam-weight tier (second-highest among all 14, per `research/cdmp_exam_overview.md`).
- **Recommended difficulty distribution:** 1 Beginner (Data Vault dedicated), 3 Intermediate, 3 Advanced.
- **Recommended question-type distribution:** 3 Multiple Choice, 3 Scenario-Based, 1 Multiple Select.
- **Source availability:** `dmbok2-2nd-ed`, `dama-dictionary`. Kimball, Inmon, and Data Vault (Linstedt) attributions are `industry_practice_concept`-tagged, unregistered (`SOURCE GAP`).
- **Source gaps:** Kimball, Inmon, Data Vault/Linstedt named-methodology attributions unregistered.
- **Highest-value CDMP concepts:** the four classic DW characteristics; Inmon vs. Kimball tradeoffs; conformed dimensions as the cross-mart consistency mechanism.
- **Recommended real-world domains:** telecom, insurance, government/public sector (module's existing examples are retail, banking, healthcare, manufacturing).

## 3. Data Ethics (ETH)

- **Current question count:** 20 (5/10/5).
- **Knowledge-base approval status:** Approved, 91/100 (`reviews/data_ethics_review.md`).
- **Existing topic/subtopic coverage:** Core Distinction; Impact and Harm; Ethical Principles; Data Ethics in Practice; Named Frameworks and Regulation — all five covered.
- **Existing question coverage:** Ethics-vs-compliance (definition and scenario); informed consent; Belmont Report (definition and principle-identification); data minimization; harm-category classification; re-identification risk; transparency; proxy discrimination; consent quality; Ethics-vs-Security distinction; ownership/control; fairness-vs-aggregate-accuracy; multi-factor evaluation; legitimate-vs-illegitimate consent; quality's compounding ethical risk; regulation-vs-ethics reasoning; success metrics.
- **Missing concepts:** EU AI Act — no *dedicated* named-regulation question (the flagship current-regulation example in this module); Data Subject as a standalone term; the three harm categories (Direct/Dignitary/Societal-Aggregate) tested together as a discrimination set, not just classification of one.
- **Missing scenario coverage:** No question yet tests the Governance-Council-as-ethics-review-venue relationship from Data Ethics' own primary-KA side (the module explicitly extends `data_governance.md`'s Council authority to ethical review).
- **Recommended additional question count:** **+6**.
- **Recommended difficulty distribution:** 1 Beginner (EU AI Act dedicated), 3 Intermediate, 2 Advanced.
- **Recommended question-type distribution:** 2 Multiple Choice, 3 Scenario-Based, 1 Multiple Select.
- **Source availability:** `dmbok2-2nd-ed`. The Belmont Report and EU AI Act are `[Regulation/Standard]`-tagged in-module but unregistered.
- **Source gaps:** Belmont Report, EU AI Act — both `SOURCE GAP`. This KA has the highest `[Regulation/Standard]` tag density (3) of any of the eight, per `research/source_audit.md`, making it the strongest candidate for registering `public_standard` sources next.
- **Highest-value CDMP concepts:** "legal compliance is a floor, not a ceiling" (the module's central, most-tested thesis); anonymization-as-risk-reduction-not-guarantee; proxy discrimination.
- **Recommended real-world domains:** government/public sector, insurance, telecom — none used yet (module's existing examples are retail, banking, healthcare, and an unnamed "technology company").

## 4. Data Security (SEC)

- **Current question count:** 20 (5/10/5).
- **Knowledge-base approval status:** Approved, 93/100 (`reviews/data_security_review.md`).
- **Existing topic/subtopic coverage:** Access Fundamentals; Access Control; Data Protection Techniques; Sensitive Data and Regulation; Security Operations — all five covered.
- **Existing question coverage:** Authentication/Authorization/Classification/CIA Triad/Encryption definitions; Auth-vs-Authz, RBAC-vs-ABAC, masking-vs-tokenization, anonymization-vs-pseudonymization scenarios; Least Privilege and Segregation of Duties violations; reversible-technique identification; PII/PHI/PCI classification; DLP purpose; classification governance accountability; RBAC-vs-ABAC tradeoff; over-restriction failure; key management; PCI-DSS scope reduction; classification-metadata-propagation failure (already the SEC-primary complement to the six-KA batch's `META-024` — a good existing mirror, not a gap).
- **Missing concepts:** Security Risk Assessment as a named, structured process — no dedicated question; Access Logging / Anomaly Detection dedicated question; MAC/DAC (only RBAC/ABAC well-covered).
- **Missing scenario coverage:** The Security-vs-Ethics/Privacy distinction is already tested from Data Ethics' side (`ETH-013`); no SEC-primary complementary version exists yet.
- **Recommended additional question count:** **+6**.
- **Recommended difficulty distribution:** 1 Beginner (Security Risk Assessment / MAC-DAC), 3 Intermediate, 2 Advanced.
- **Recommended question-type distribution:** 3 Multiple Choice, 2 Scenario-Based, 1 Multiple Select.
- **Source availability:** `dmbok2-2nd-ed`, `dama-dictionary`. HIPAA, GDPR, PCI-DSS all `[Regulation/Standard]`-tagged, unregistered.
- **Source gaps:** HIPAA, GDPR, PCI-DSS — all `SOURCE GAP`, three of the highest-value named regulations across the whole project, still unregistered.
- **Highest-value CDMP concepts:** Authentication vs. Authorization (the module's single most-tested distinction); the Encryption/Masking/Tokenization/Anonymization/Pseudonymization cluster; Least Privilege.
- **Recommended real-world domains:** telecom, insurance, government/public sector — none used yet (module's existing examples are banking, healthcare, retail, manufacturing).

## 5. Data Storage and Operations (STOR)

- **Current question count:** 20 (5/10/5).
- **Knowledge-base approval status:** Approved, 92/100 (`reviews/data_storage_and_operations_review.md`).
- **Existing topic/subtopic coverage:** Storage and Database Technology; Database Operations; Availability and Recovery; Performance Management; Data Lifecycle and Environments — all five covered, though Performance Management thinly.
- **Existing question coverage:** RPO/RTO/DBA/Data Masking/Availability definitions; RPO-vs-RTO reasoning; storage-architecture and database-technology-fit classification; HA-vs-DR/BCP; untested-backup risk; non-production environment risk; Database Operations components; cloud shared responsibility; tiering-vs-archival; retention governance; differentiated recovery targets; NoSQL-vs-relational tradeoffs; unilateral retention diagnosis; Data Virtualization tradeoffs; proactive-vs-reactive capacity planning.
- **Missing concepts:** Performance Management's own named techniques (Indexing, Partitioning, Query Optimization, Caching) have no *dedicated* question — only touched glancingly; MTTR as a named metric has no dedicated question.
- **Missing scenario coverage:** No question yet tests database/storage technology selection as a Physical Data Architecture decision from Storage and Operations' own primary-KA side (the module explicitly cross-references `data_architecture.md` for this).
- **Recommended additional question count:** **+5**.
- **Recommended difficulty distribution:** 1 Beginner (Indexing/Partitioning/Caching), 2 Intermediate, 2 Advanced.
- **Recommended question-type distribution:** 2 Multiple Choice, 2 Scenario-Based, 1 Multiple Select.
- **Source availability:** `dmbok2-2nd-ed`, `dama-dictionary`. Highest `[DAMA]`-tag density (12) of any module per `research/source_audit.md` — a strong, well-grounded content base.
- **Source gaps:** No named regulation/standard specific to this KA; MTTR (industry-practice) unregistered.
- **Highest-value CDMP concepts:** RPO vs. RTO (the module's single most-tested distinction); the Backup/HA/DR-BCP distinction; Non-Production Environment Management and Data Masking as a named DAMA-scoped concern (not just an engineering habit).
- **Recommended real-world domains:** telecom, insurance, government/public sector, cloud/data platform — none used yet (module's existing examples are banking, healthcare, retail, manufacturing).

## 6. Data Integration and Interoperability (INTEG)

- **Current question count:** 20 (5/10/5).
- **Knowledge-base approval status:** Approved, 92/100 (`reviews/data_integration_and_interoperability_review.md`).
- **Existing topic/subtopic coverage:** Core Distinction; Integration Patterns; Integration Architecture; Interoperability and Contracts; Integration Governance and Projects — all five covered.
- **Existing question coverage:** Integration/Interoperability/Orchestration/Data Contract/CDC definitions; Integration-vs-Interoperability, batch-vs-real-time, point-to-point-vs-hub-and-spoke scenarios; federation-vs-replication; named-standards classification; idempotency; integration-pattern identification; migration-vs-ongoing-integration; missing-contract consequence; Data Sharing Agreement accountability; spaghetti-architecture remediation; hub-and-spoke tradeoff; migration cutover risk; real-time-vs-batch tradeoff; success metrics.
- **Missing concepts:** Event-driven architecture as its own distinctly-tested style (currently folded into pattern-identification content rather than dedicated).
- **Missing scenario coverage:** Two open cross-KA mirrors, both already validated from the *other* side in the six-KA batch: integration pattern as an architecture-governed decision (already tested as `ARCH-025`, no INTEG-primary counterpart) and MDM implementation style as fundamentally an integration-pattern choice (the `reference_and_master_data.md` module makes this connection explicitly; no INTEG-primary question tests it).
- **Recommended additional question count:** **+6**.
- **Recommended difficulty distribution:** 1 Beginner (Event-Driven Architecture dedicated), 3 Intermediate, 2 Advanced.
- **Recommended question-type distribution:** 2 Multiple Choice, 3 Scenario-Based, 1 Multiple Select.
- **Source availability:** `dmbok2-2nd-ed`, `dama-dictionary`. EDI, HL7/FHIR, SWIFT all `[Regulation/Standard]`-tagged, unregistered.
- **Source gaps:** EDI, HL7/FHIR, SWIFT — all `SOURCE GAP`.
- **Highest-value CDMP concepts:** Integration vs. Interoperability (the module's single most-tested distinction — movement vs. meaning); Point-to-point vs. Hub-and-Spoke vs. Event-Driven; Data Contracts as the interoperability-enforcement mechanism.
- **Recommended real-world domains:** telecom, government/public sector — not yet used (module's existing examples are retail, banking, healthcare, manufacturing).

## 7. Big Data and Data Science (BIGDATA)

- **Current question count:** 20 (5/10/5).
- **Knowledge-base approval status:** Approved, 92/100 (`reviews/big_data_and_data_science_review.md`).
- **Existing topic/subtopic coverage:** Core Distinction; Storage and Processing; Data Science Lifecycle; Machine Learning Fundamentals; Model Governance — all five covered.
- **Existing question coverage:** Big Data/Data Science/Data Lake/Model Drift/Overfitting definitions; Big-Data-vs-Data-Science, Lake-vs-Warehouse, data-swamp-diagnosis scenarios; train/validation/test purpose; supervised-vs-unsupervised classification; explainability stakes; the 3 Vs; citizen data science governance risk; Lambda-vs-Kappa classification; data-preparation time investment; subgroup fairness evaluation; governance-practices-vs-technical-choices; data-swamp remediation; governance-exemption fallacy; success metrics.
- **Missing concepts:** CRISP-DM's full 8-stage lifecycle sequence has no *dedicated* question (only "data preparation time" touches one stage); Feature Engineering as a named term has no dedicated question.
- **Missing scenario coverage:** The data-quality-as-precondition-for-model-reliability relationship is already tested from Data Quality's primary-KA side (`QUAL-026`, six-KA batch); no BIGDATA-primary complementary version exists yet.
- **Recommended additional question count:** **+6**.
- **Recommended difficulty distribution:** 1 Beginner (Feature Engineering dedicated), 3 Intermediate, 2 Advanced.
- **Recommended question-type distribution:** 2 Multiple Choice, 3 Scenario-Based, 1 Multiple Select.
- **Source availability:** `dmbok2-2nd-ed`, `dama-dictionary`. The 3/5 Vs and CRISP-DM are `industry_practice_concept`-tagged, unregistered.
- **Source gaps:** CRISP-DM, the 3/5 Vs framing — both `SOURCE GAP`.
- **Highest-value CDMP concepts:** "governance applies to big data/ML, not exempt" (the module's central, most-tested thesis); Data Lake vs. Data Warehouse; the data-swamp anti-pattern.
- **Recommended real-world domains:** insurance, government/public sector, cloud/data platform — none used yet (module's existing examples are banking, healthcare, retail, manufacturing).

## 8. Document and Content Management (DOC)

- **Current question count:** 20 (5/10/5).
- **Knowledge-base approval status:** Approved, 92/100 (`reviews/document_and_content_management_review.md`).
- **Existing topic/subtopic coverage:** Core Distinction; Content Lifecycle; Records Management; Legal and Compliance; Content Systems and Metadata — all five covered.
- **Existing question coverage:** Document/Content/Record/Legal Hold/Records Retention Schedule definitions; Document-Content-Record classification scenario; records-management-vs-general-content-management; e-discovery dependency; structured-vs-semi-vs-unstructured classification; taxonomy purpose; content-system-category classification; content-lifecycle-stage identification; chain of custody; Records Manager accountability; ISO 15489-vs-Dublin-Core distinction; spoliation risk; legitimate-vs-illegitimate retention; taxonomy backlog remediation; legal-hold-and-retention-schedule interaction; success metrics.
- **Missing concepts:** Records Classification Scheme (Records Series) has no *dedicated* question (only touched via the broader records-management questions).
- **Missing scenario coverage:** Three open cross-KA mirrors this module explicitly sets up but no DOC-primary question yet tests: Information Governance as `data_governance.md`'s Owner/Steward/Custodian structure extended to unstructured content; classification-driven access control (`data_security.md`) applied to a sensitive document; descriptive metadata (`metadata_management.md`) as what makes content findable.
- **Recommended additional question count:** **+5**.
- **Recommended difficulty distribution:** 1 Beginner (Records Classification Scheme dedicated), 2 Intermediate, 2 Advanced.
- **Recommended question-type distribution:** 2 Multiple Choice, 2 Scenario-Based, 1 Multiple Select.
- **Source availability:** `dmbok2-2nd-ed`, `dama-dictionary`. ISO 15489 and Dublin Core `[Regulation/Standard]`-tagged, unregistered.
- **Source gaps:** ISO 15489, Dublin Core — both `SOURCE GAP`.
- **Highest-value CDMP concepts:** Document vs. Content vs. Record (the module's single most-tested distinction); Legal Hold overriding the normal Retention Schedule; the "tool vs. discipline" trap applied to content management platforms.
- **Recommended real-world domains:** government/public sector, insurance, telecom, cloud/data platform — none used yet (module's existing examples are banking, healthcare, retail, manufacturing).

---

## Aggregate Summary

| KA | Current | Planned New | Projected Total | Exam-Weight Tier |
|---|---|---|---|---|
| MAT | 6 | +11 | 17 | Remaining spread |
| DWBI | 20 | +7 | 27 | **~10% (higher)** |
| ETH | 20 | +6 | 26 | Remaining spread |
| SEC | 20 | +6 | 26 | Remaining spread |
| INTEG | 20 | +6 | 26 | Remaining spread |
| BIGDATA | 20 | +6 | 26 | Remaining spread |
| STOR | 20 | +5 | 25 | Remaining spread |
| DOC | 20 | +5 | 25 | Remaining spread |
| **Total** | **126** | **+52** | **178** | — |

Combined with the 161 already produced across the first six KAs, the full 14-KA bank would reach **339** questions once this plan is executed (against the original 266 baseline). This is a planning projection, not a commitment to hit an exact number — per this project's standing instruction, actual production should prioritize quality and genuine gap-closure over hitting these counts precisely; a KA may reasonably end with slightly more or fewer than planned once real drafting surfaces additional or fewer defensible gaps.

## Recommended Production Order

**1. MAT, standalone.**
The single most severe, unambiguous gap of the eight (6 questions vs. every other KA's 20) — and MAT is the meta-discipline that evaluates every other Knowledge Area (`data_management_maturity_assessment.md` explicitly frames itself as "the evaluative lens applied *to* every other Knowledge Area's practices"), so establishing its own content properly first, before the other seven, keeps the production sequence internally consistent rather than building seven KAs' worth of content before circling back to fix the smallest one last.

**2. DWBI, standalone.**
Highest exam-weight tier (~10%) of the remaining eight — directly following `research/cdmp_exam_overview.md`'s own weighting guidance for where study (and by extension, question-bank) investment should concentrate first. It also has the most cross-KA mirror opportunities immediately available from the six-KA batch (golden-record-as-conformed-dimension, semantic-layer-as-Business-Metadata), which are cheapest to author correctly while that context is freshest.

**3. ETH + DOC, paired batch.**
Both are explicitly named in `CLAUDE.md`'s mentor-role guidance as governance/business-facing areas where "Data Engineers often have weak spots... call these out explicitly and spend extra care there" — pairing them keeps that deliberate-extra-care framing front and center for both at once, rather than letting it get diluted across a larger, more technical batch. Both also share a similar authoring pattern (a core three/four-way classification test — Document/Content/Record; Direct/Dignitary/Societal harm) that benefits from being drafted with the same reviewer mindset back to back.

**4. SEC + STOR, paired batch.**
These two are the most tightly cross-referenced pair among the remaining eight — encryption at rest, non-production data masking, classification-driven access control, and RPO/RTO-as-governed-decision all span both modules' own explicit cross-references to each other. Producing them together, with both modules freshly in view, minimizes the risk of authoring a cross-KA question that's subtly inconsistent with the sibling module's actual framing (the specific failure mode this project's own quality audit already caught once in `QUAL-022`).

**5. INTEG + BIGDATA, paired batch, last.**
Both need the smallest top-ups (+6 each, no severe individual gap), both are lower exam-weight, and both have their remaining cross-KA mirror opportunities pointing *back* at already-completed content (ARCH, MASTER for INTEG; QUAL, ETH for BIGDATA) rather than at each other or at anything still unproduced — the natural closing batch that ties off loose threads without needing anything from a KA not yet done.

---

## Validation

```
python -m pytest -q
```
Run after this planning document was created; see the accompanying report. No `question_bank/`, `knowledge_base/`, `quiz_engine/`, or `packages/` file was modified to produce this plan.
