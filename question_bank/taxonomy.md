# Question Bank — Taxonomy

## Purpose

This document defines the **subject classification structure** every question is filed under: Knowledge Area → Topic → Subtopic. It answers "where does this question live," not "how hard is it" (see `difficulty_framework.md`) or "what cognitive skill does it test" (Bloom's Taxonomy, also in `difficulty_framework.md`). These are three genuinely different axes that happen to share the word "taxonomy" in common usage — keep them distinct. A question has exactly one Knowledge Area/Topic/Subtopic classification but is independently assigned a Difficulty and a Bloom's level.

## Design Principle: 1:1 Traceability to the Knowledge Base

Every Knowledge Area in this taxonomy corresponds exactly to one `knowledge_base/*.md` file and one DMBOK2 chapter — there is no separate content hierarchy invented for the Question Bank. Every Topic below corresponds to a named subsection of that file's **Core Concepts** (or **DAMA Definitions and Terminology**) section. This is deliberate: it means a question's `related_knowledge_areas` metadata field (see `metadata_schema.md`) can always resolve to a real, citable location, and a learner missing a question can be pointed to the exact paragraph that teaches it.

## Knowledge Area Index

| Code | Knowledge Area | DMBOK2 Ch. | `knowledge_base/` file | Content status |
|---|---|---|---|---|
| GOV | Data Governance | 3 | `data_governance.md` | Approved |
| ARCH | Data Architecture | 4 | `data_architecture.md` | Approved |
| MODEL | Data Modeling and Design | 5 | `data_modeling_and_design.md` | Approved |
| STOR | Data Storage and Operations | 6 | `data_storage_and_operations.md` | Template only |
| SEC | Data Security | 7 | `data_security.md` | Template only |
| INTEG | Data Integration and Interoperability | 8 | `data_integration_and_interoperability.md` | Template only |
| DOC | Document and Content Management | 9 | `document_and_content_management.md` | Template only |
| MASTER | Reference and Master Data | 10 | `reference_and_master_data.md` | Approved |
| DWBI | Data Warehousing and Business Intelligence | 11 | `data_warehousing_and_business_intelligence.md` | Template only |
| META | Metadata Management | 12 | `metadata_management.md` | Approved |
| QUAL | Data Quality | 13 | `data_quality.md` | Approved |
| BIGDATA | Big Data and Data Science | 14 | `big_data_and_data_science.md` | Template only |
| MAT | Data Management Maturity Assessment | 15 | `data_management_maturity_assessment.md` | Template only |
| ETH | Data Ethics | 2 | `data_ethics.md` | Template only |

*(Codes match `naming_conventions.md` exactly — this table is the single source of truth for both documents; if they ever diverge, `naming_conventions.md` governs the ID format and this table governs content scope.)*

A Knowledge Area only receives question-authoring attention once its `knowledge_base/` module reaches **Approved** status per `CLAUDE.md`'s Approval Workflow — see `authoring_guidelines.md` and `roadmap.md` for how this gates the bank's growth.

## Topic / Subtopic Breakdown — Approved Knowledge Areas

The six Approved modules already have real, reviewed content to classify against. Topics below are drawn directly from each module's existing section structure.

### GOV — Data Governance
| Topic | Subtopics |
|---|---|
| Roles and Accountability | Data Owner; Data Steward (Business/Technical/Coordinating); Data Custodian; Governance Council |
| Governance Artifacts | Policy; Standard; Procedure; Guideline; Business Glossary |
| Governance Operating Models | Centralized; Decentralized/Federated; Hybrid |
| Governance Program Mechanics | Issue management and escalation; Regulatory/compliance oversight; Value and metrics |
| Governance in Practice | Governance vs. Management distinction; Governance zone patterns (lake/warehouse) |

### ARCH — Data Architecture
| Topic | Subtopics |
|---|---|
| Enterprise Data Architecture | Definition and scope; Data Architecture Principles; Data Domains; Data Flows; Data Lifecycle |
| Architecture Frameworks | Zachman Framework; TOGAF; Business/Application/Technology/Data Architecture relationships |
| Architecture Layers | Conceptual; Logical; Physical Data Architecture |
| Discipline Boundaries | Data Architecture vs. Data Modeling vs. Database Design vs. Data Engineering Architecture |
| Standards | Data Architecture Standards vs. Governance Policy/Standard/Procedure |

### MODEL — Data Modeling and Design
| Topic | Subtopics |
|---|---|
| Levels of Abstraction | Conceptual Data Model; Logical Data Model; Physical Data Model |
| Structural Terms | Entity; Attribute; Relationship/Cardinality; Primary/Natural/Surrogate/Foreign Key |
| Normalization | 1NF/2NF/3NF/BCNF; Denormalization tradeoffs |
| Dimensional Modeling | Fact table; Dimension table; Grain; Star schema; Snowflake schema |
| Advanced Modeling Patterns | Canonical Data Model; Generalization/Subtyping; Data Vault |

### MASTER — Reference and Master Data
| Topic | Subtopics |
|---|---|
| Core Distinction | Reference Data vs. Master Data classification |
| MDM Concepts | Golden Record; Single Source of Truth; Matching and Merging; Survivorship Rules; Hierarchies |
| Master Data Types | Party (Person/Organization); Product; Financial; Location |
| MDM Implementation | Registry; Consolidation; Coexistence; Centralized styles |
| MDM Governance | Data Sharing Agreements; MDM Success Metrics; Roles in MDM |

### META — Metadata Management
| Topic | Subtopics |
|---|---|
| Metadata Categories | Business Metadata; Technical Metadata; Operational Metadata |
| Metadata Infrastructure | Metadata Repository; Metadata Integration; Metadata Standards |
| Metadata Artifacts | Data Lineage; Data Catalog; Business Glossary |
| Cross-KA Relationships | Metadata vs. Governance; Metadata vs. Data Quality; Metadata vs. Architecture (lineage vs. data flow diagrams) |

### QUAL — Data Quality
| Topic | Subtopics |
|---|---|
| Quality Dimensions | Accuracy; Completeness; Consistency; Timeliness; Validity; Uniqueness; Integrity |
| Quality Activities | Data Quality Management (DQM); Profiling; Validation; Cleansing; Monitoring |
| DQM Lifecycle | Define requirements; Profile; Identify issues; Root cause analysis; Improve; Monitor |
| Roles in Quality | Owner/Steward/Custodian/Engineer responsibilities for quality |

## Topic / Subtopic Breakdown — Pending Knowledge Areas

STOR, SEC, INTEG, DOC, DWBI, BIGDATA, MAT, and ETH have no topic/subtopic breakdown yet — their `knowledge_base/` modules are template-only (see the Index above). Per `authoring_guidelines.md`, this table will be populated for each Knowledge Area **immediately after** that module reaches Approved status, using the same method applied above: topics are lifted directly from the module's own section structure, not invented independently.

## Cross-Knowledge-Area Tagging

A question's primary classification is always exactly one Knowledge Area/Topic/Subtopic. However, many real DMBOK2 concepts are inherently cross-cutting (e.g., a Master Data survivorship-rule question is squarely MASTER, but it directly depends on GOV's Owner/Steward roles). The `related_knowledge_areas` metadata field (see `metadata_schema.md`) captures this secondary relevance without diluting the primary classification — this mirrors the "Related Knowledge Area" pattern already used in every completed module's Quiz Questions section (e.g., `reference_and_master_data.md`'s Q8: *"Related Knowledge Area: Reference and Master Data... relates to Data Governance"*). **Mini Case Study** questions (see `question_lifecycle.md` and the question types defined in `authoring_guidelines.md`) are the question type most likely to carry several `related_knowledge_areas` values, since they are explicitly designed to test cross-KA integration — directly mirroring the "cross-KA integration" study approach already planned in `roadmap/four_month_plan.md`, Week 12.
