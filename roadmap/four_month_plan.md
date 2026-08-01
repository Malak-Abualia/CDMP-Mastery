# CDMP Fundamentals — 4-Month Preparation Roadmap

**Profile:** Data Engineer, ~3 years experience, targeting CDMP Fundamentals (scoring for Practitioner-level ≥70% where possible), then Practitioner Specialist exams later.
**Cadence:** 6 study days/week, 1–1.5 hours/day (~7–9 hours/week).
**Duration:** 16 study weeks (a 4-month calendar window has ~17.4 weeks — the extra ~1.5 weeks is intentional slack for sick days, busy work weeks, or re-study, not a scheduling gap).
**Rest:** 1 day off per week, every week, no exceptions. Sustainability beats intensity.

This roadmap sequences *what* to study and *when*. It does not contain lesson content — that will be built KA by KA in `knowledge_base/` as each week is reached, per `CLAUDE.md`.

---

## How Knowledge Areas Were Prioritized

Three factors, weighted in this order:

1. **Exam weight** (from `research/cdmp_exam_overview.md`): Data Governance, Data Modeling & Design, Data Quality, and Metadata Management (~11% each) are the heaviest; Reference & Master Data and Data Warehousing/BI (~10% each) are next.
2. **Data Engineering gap risk**: Governance, Ethics, Maturity Assessment, Document & Content Management, and the *formal frameworks* inside Metadata Management and Data Quality are where engineers typically have the thinnest exposure — these get dedicated time rather than being rushed.
3. **Existing strength as leverage**: Data Modeling, Data Architecture, Data Storage & Operations, Data Integration & Interoperability, and Big Data & Data Science overlap heavily with day-to-day DE work — these move faster, spending time on DMBOK2's specific terminology and framing rather than re-teaching concepts already known.

Net effect: governance-adjacent and "soft" knowledge areas are front-loaded and given real space; technical knowledge areas are compressed and pointed at *translation into DMBOK2 vocabulary* rather than first-time learning.

---

## Phase Summary

| Phase | Weeks | Focus | Knowledge Areas |
|---|---|---|---|
| 1 — Foundation & DAMA Mindset | 1–2 | DMBOK2 framework, roles, ethics, maturity | Data Management overview, Data Ethics, Data Mgmt Maturity Assessment |
| 2 — Deep Study of Knowledge Areas | 3–11 | All 12 remaining KAs, prioritized by weight & gap risk | Governance → Modeling → Quality → Metadata → Ref/Master Data → DW/BI → Architecture → Storage/Ops+Security → Integration+Document/Content+Big Data |
| 3 — Application, Scenarios & Exam Practice | 12–14 | Cross-KA integration, full timed practice exams, error analysis | All 14, integrated |
| 4 — Final Revision & Exam Readiness | 15–16 | Weighted rapid review, mock exam, logistics, exam sitting | All 14, weighted by score gaps |

---

# Phase 1 — Foundation and DAMA Mindset (Weeks 1–2)

**Purpose:** Before going deep on any single Knowledge Area, build the mental model DAMA uses — the DMBOK2 "wheel," the vocabulary, the idea of data as a managed organizational asset rather than a pipeline output — plus the two most "mindset-shaping" chapters (Ethics, Maturity Assessment), which are light on volume but easy to under-value as an engineer.

## Week 1 — Orientation: The DAMA Wheel and Data Management Mindset

**Objective:** Understand what DMBOK2 is, how the 14 Knowledge Areas relate to each other via the wheel, and how DAMA's data-as-asset framing differs from a pipeline/engineering framing.

**Knowledge Areas covered:** Data Management (DMBOK2 Ch.1 — foundational, not a scored KA itself but the lens for all others).

**Daily study tasks:**
- **Day 1 (75 min):** Read DMBOK2 Ch.1 sections on the definition of data management and its goals. Sketch the DMBOK2 wheel from memory after reading; label all 14 Knowledge Areas.
- **Day 2 (60 min):** Continue Ch.1 — data management principles (data as an asset, quality, ethics, no one-size-fits-all, etc.). Write a 5-sentence reflection: which principles does my current DE work already embody, and which does it ignore?
- **Day 3 (60 min):** Read the "Roles and Responsibilities" concepts referenced in Ch.1 (data steward vs. data owner vs. data custodian). Build a 1-page comparison table — this distinction reappears in nearly every later KA.
- **Day 4 (60 min):** Re-read `research/cdmp_exam_overview.md` in full. Set up a personal exam-mechanics cheat sheet: format, timing, scoring thresholds, what "Practitioner-level score" requires.
- **Day 5 (60 min):** Start a running glossary (in `notes/`) of DAMA terminology as you encounter unfamiliar terms. Populate it with ~15 terms from this week's reading.
- **Day 6 (60 min):** Review — re-draw the wheel unaided, compare to the book's diagram, correct gaps. Take a short self-check quiz (survey-level, ~10 questions) covering wheel structure and role definitions.

**Recommended resources:**
- DAMA-DMBOK2, 2nd Edition — Chapter 1
- DAMA Dictionary of Data Management (glossary reference)
- `research/cdmp_exam_overview.md` (this project)

**Practical exercises:**
- Map your current team's roles (e.g., platform engineer, analytics engineer, data owner-by-default) onto steward/owner/custodian definitions. Note mismatches.

**Review activities:**
- End-of-week wheel redraw from memory (active recall, not re-reading).

**Quiz plan:**
- One low-stakes ~10-question self-check on wheel structure + role definitions. Goal is calibration, not scoring pressure.

**Expected outcome:**
- Can draw and explain the DMBOK2 wheel unaided, define data steward/owner/custodian, and articulate why DAMA treats data as an organizational asset rather than a technical byproduct.

---

## Week 2 — Data Ethics and Data Management Maturity Assessment

**Objective:** Cover the two "framework" Knowledge Areas that are conceptually light but easy to under-study — both show up on the exam and both are unfamiliar territory for most engineers.

**Knowledge Areas covered:** Data Ethics, Data Management Maturity Assessment.

**Daily study tasks:**
- **Day 1 (60 min):** Read DMBOK2 Data Ethics chapter — core principles (impact, transparency, accountability, fairness in data use).
- **Day 2 (60 min):** Continue Data Ethics — bias, privacy, and consent concepts as DAMA frames them (not GDPR-specific, but overlapping). Add new terms to glossary.
- **Day 3 (60 min):** Read DMBOK2 Data Management Maturity Assessment chapter — purpose of maturity models, common maturity levels, how assessments drive governance investment.
- **Day 4 (60 min):** Continue Maturity Assessment — components typically assessed (people, process, technology) across Knowledge Areas.
- **Day 5 (75 min):** Practical exercise (below) + glossary consolidation for both KAs.
- **Day 6 (60 min):** Quiz + review of Week 1 material (interleaved recall) to start building retention habits before Phase 2's heavier load.

**Recommended resources:**
- DAMA-DMBOK2, 2nd Edition — Data Handling Ethics chapter; Data Management Maturity Assessment chapter
- Any reputable data ethics primer (e.g., a short article on algorithmic bias) for real-world grounding — optional, DMBOK2 text is sufficient for exam purposes

**Practical exercises:**
- Informally score your current team/organization against a simplified maturity model (1–5) for two or three Knowledge Areas you already know well (e.g., Data Quality, Metadata). Note what evidence you used to justify each score — this is the muscle the exam tests.

**Review activities:**
- 10-minute flashcard review of Week 1 glossary terms before starting new content each day (light spaced repetition, continues every week from here on).

**Quiz plan:**
- One ~15-question quiz combining Data Ethics + Maturity Assessment.
- One ~5-question interleaved review quiz pulling from Week 1.

**Expected outcome:**
- Can explain DAMA's ethical principles for data handling and describe the purpose/structure of a data management maturity assessment, including why maturity is typically assessed per-Knowledge-Area rather than organization-wide.

---

# Phase 2 — Deep Study of DMBOK2 Knowledge Areas (Weeks 3–11)

**Purpose:** Go deep on each remaining Knowledge Area, in priority order. Heavier-weighted and higher-gap-risk areas get a full week each; technical areas you already have strong intuition for are compressed and combined, with study time redirected toward DMBOK2-specific vocabulary and framing rather than re-learning fundamentals.

## Week 3 — Data Governance

**Objective:** Master Data Governance deeply — it is the highest-weighted KA, sits at the center of the wheel, and is the area with the largest gap for most Data Engineers.

**Knowledge Areas covered:** Data Governance.

**Daily study tasks:**
- **Day 1 (75 min):** Read DMBOK2 Data Governance — business drivers, goals, and principles.
- **Day 2 (75 min):** Governance organization structures — councils, committees, stewardship models.
- **Day 3 (75 min):** Governance activities — policy development, issue management, communication.
- **Day 4 (75 min):** Tools & techniques for governance; metrics used to demonstrate governance value.
- **Day 5 (75 min):** Practical exercise (below).
- **Day 6 (60 min):** Quiz + interleaved review of Weeks 1–2.

**Recommended resources:**
- DAMA-DMBOK2, 2nd Edition — Data Governance chapter (primary, read in full — do not skim this one)
- A CDMP-focused practice question set for Data Governance (per `research/cdmp_exam_overview.md` prep providers) once available

**Practical exercises:**
- Pick a real data governance gap you've observed at work (e.g., no clear data owner for a critical table, undocumented access policy). Write a one-page mini "governance proposal" using DMBOK2 terminology (policy, steward, council, issue escalation).

**Review activities:**
- Flashcard pass on Weeks 1–2 glossary before each day's new reading.

**Quiz plan:**
- One ~20-question deep quiz on Data Governance (highest question volume of any week so far, matching its exam weight).

**Expected outcome:**
- Can explain the purpose of a data governance program, describe common organizational structures for it, and connect governance to every other Knowledge Area as the "center of the wheel."

---

## Week 4 — Data Modeling and Design

**Objective:** Reframe existing modeling skill (schemas, normalization, dimensional modeling) into DMBOK2's formal vocabulary and lifecycle (conceptual → logical → physical).

**Knowledge Areas covered:** Data Modeling and Design.

**Daily study tasks:**
- **Day 1 (60 min):** Read DMBOK2 Data Modeling — goals, conceptual/logical/physical model definitions. Note where these map to work you already do (ERDs, dbt models, warehouse schemas).
- **Day 2 (60 min):** Modeling techniques — normalization, dimensional modeling (star/snowflake), canonical modeling.
- **Day 3 (60 min):** Naming standards, model governance, and the role of a data model as a governance artifact (not just a technical one).
- **Day 4 (75 min):** Practical exercise (below).
- **Day 5 (60 min):** Terminology drill — DMBOK2 often uses precise terms (e.g., "generalization," "subtyping") for things engineers do informally. Build a translation table: my term → DMBOK2 term.
- **Day 6 (60 min):** Quiz + interleaved review (Governance + this week).

**Recommended resources:**
- DAMA-DMBOK2, 2nd Edition — Data Modeling and Design chapter
- Existing personal familiarity with dimensional modeling (Kimball-style) as a comparison point — read critically for where DMBOK2's framing differs from what you already practice

**Practical exercises:**
- Take a real schema you've designed (a warehouse fact table or a service's data model) and produce a one-page conceptual and logical model for it in DMBOK2 style, distinct from the physical implementation you actually built.

**Review activities:**
- Flashcard pass on Governance terms; add Modeling terms to the same deck.

**Quiz plan:**
- One ~15-question quiz on Data Modeling, weighted toward terminology precision (this is where engineers lose easy points — knowing the concept but not DAMA's exact term for it).

**Expected outcome:**
- Can name and distinguish conceptual/logical/physical models, describe normalization and dimensional modeling in DMBOK2 terms, and translate personal modeling experience into the exam's vocabulary.

---

## Week 5 — Data Quality

**Objective:** Move from "I write data quality checks" to understanding DAMA's formal data quality dimensions, management process, and the idea of quality as an ongoing program rather than a set of checks.

**Knowledge Areas covered:** Data Quality.

**Daily study tasks:**
- **Day 1 (60 min):** Read DMBOK2 Data Quality — definition of quality, business drivers.
- **Day 2 (75 min):** The data quality dimensions (accuracy, completeness, consistency, timeliness, validity, uniqueness, etc.) — memorize definitions precisely, not just intuitively.
- **Day 3 (60 min):** Data quality management process — assessment, root cause analysis, remediation, monitoring.
- **Day 4 (60 min):** Roles in data quality management and the relationship between DQ and Governance/Stewardship.
- **Day 5 (75 min):** Practical exercise (below).
- **Day 6 (60 min):** Quiz + interleaved review (Governance, Modeling, this week).

**Recommended resources:**
- DAMA-DMBOK2, 2nd Edition — Data Quality chapter
- Any existing data quality tooling documentation you use at work (e.g., Great Expectations, dbt tests) as a contrast point for "what DAMA calls this dimension vs. what my tool calls its check type"

**Practical exercises:**
- Map every automated data quality check in a pipeline you own to one of DAMA's formal quality dimensions. Identify which dimensions your current checks *don't* cover.

**Review activities:**
- Flashcard pass covering Governance + Modeling terms; add DQ dimension definitions.

**Quiz plan:**
- One ~20-question quiz on Data Quality (matches its exam weight), with a sub-section specifically testing dimension *definitions* verbatim.

**Expected outcome:**
- Can list and precisely define the core DAMA data quality dimensions, describe the DQ management lifecycle, and map real technical checks to formal DQ concepts.

---

## Week 6 — Metadata Management

**Objective:** Formalize catalog/lineage intuition into DAMA's metadata types (business, technical, operational) and metadata management lifecycle.

**Knowledge Areas covered:** Metadata Management.

**Daily study tasks:**
- **Day 1 (60 min):** Read DMBOK2 Metadata Management — definition and business drivers.
- **Day 2 (60 min):** The three metadata types (business, technical, operational) — build a table with examples from your own stack for each.
- **Day 3 (60 min):** Metadata architecture patterns (centralized, distributed, hybrid repositories) and metadata governance.
- **Day 4 (75 min):** Practical exercise (below).
- **Day 5 (60 min):** Terminology drill + glossary consolidation.
- **Day 6 (60 min):** Quiz + interleaved review (Governance, Modeling, DQ, this week).

**Recommended resources:**
- DAMA-DMBOK2, 2nd Edition — Metadata Management chapter
- Documentation for whatever data catalog / lineage tool you use professionally, as a real-world anchor

**Practical exercises:**
- Classify the metadata your organization's data catalog (or lack thereof) actually captures into business/technical/operational buckets. Identify the biggest gap.

**Review activities:**
- Flashcard pass on all prior weeks' terms (deck is growing — start timing this review to keep it under 10–15 minutes).

**Quiz plan:**
- One ~20-question quiz on Metadata Management (matches exam weight), emphasizing the three-type classification.

**Expected outcome:**
- Can classify any given piece of metadata into business/technical/operational, describe common metadata architectures, and explain why metadata management is treated as a distinct discipline from data modeling.

---

## Week 7 — Reference and Master Data Management

**Objective:** Formalize "dimension tables" and "golden record" intuition into DAMA's reference vs. master data distinction and MDM architecture styles.

**Knowledge Areas covered:** Reference and Master Data.

**Daily study tasks:**
- **Day 1 (60 min):** Read DMBOK2 Reference & Master Data — definitions and the distinction between reference data and master data (this distinction is a common exam trap).
- **Day 2 (60 min):** MDM architecture styles (registry, consolidation, coexistence, centralized) — compare to any MDM/golden-record system you've encountered at work.
- **Day 3 (60 min):** Master data governance and stewardship considerations specific to this KA.
- **Day 4 (60 min):** Practical exercise (below).
- **Day 5 (60 min):** Terminology drill + glossary consolidation.
- **Day 6 (60 min):** Quiz + interleaved review (add this week, keep rotating oldest weeks less frequently).

**Recommended resources:**
- DAMA-DMBOK2, 2nd Edition — Reference and Master Data chapter

**Practical exercises:**
- Identify one reference dataset (e.g., country codes, status enums) and one master data entity (e.g., customer, product) in a system you work on. Justify the classification using DAMA's definitions, and name which MDM architecture style (if any) your organization implicitly uses.

**Review activities:**
- Flashcard pass, rotating full deck.

**Quiz plan:**
- One ~15-question quiz on Reference & Master Data, with several questions specifically testing reference-vs-master classification.

**Expected outcome:**
- Can correctly classify data as reference vs. master, name the four common MDM architecture styles, and describe stewardship considerations unique to master data.

---

## Week 8 — Data Warehousing and Business Intelligence

**Objective:** Reframe warehouse/BI experience into DMBOK2's vocabulary, including where it deliberately differs from a single vendor's or methodology's (e.g., Kimball-only) framing.

**Knowledge Areas covered:** Data Warehousing and Business Intelligence.

**Daily study tasks:**
- **Day 1 (60 min):** Read DMBOK2 DW/BI — definitions, business drivers, and how DAMA frames the DW/BI lifecycle.
- **Day 2 (60 min):** Architecture approaches (Inmon vs. Kimball vs. hybrid) as DMBOK2 presents them — note this is likely familiar territory, focus on exact terminology.
- **Day 3 (60 min):** BI delivery concepts (reporting, dashboards, self-service) and their governance implications.
- **Day 4 (60 min):** Practical exercise (below).
- **Day 5 (60 min):** Terminology drill.
- **Day 6 (60 min):** Quiz + interleaved review.

**Recommended resources:**
- DAMA-DMBOK2, 2nd Edition — Data Warehousing and Business Intelligence chapter

**Practical exercises:**
- Diagram a warehouse you've built or maintained, labeling each layer using DMBOK2's terms rather than your team's internal jargon (e.g., "staging," "conformed dimensions," "presentation layer").

**Review activities:**
- Flashcard pass, full deck.

**Quiz plan:**
- One ~15-question quiz on DW/BI (matches exam weight).

**Expected outcome:**
- Can describe DW/BI architecture approaches in DMBOK2 terms and explain how governance and metadata concepts from earlier weeks apply specifically to warehousing.

---

## Week 9 — Data Architecture

**Objective:** Formalize architectural intuition into DAMA's data architecture principles, deliverables, and its relationship to enterprise architecture more broadly.

**Knowledge Areas covered:** Data Architecture.

**Daily study tasks:**
- **Day 1 (60 min):** Read DMBOK2 Data Architecture — definition, goals, relationship to enterprise architecture.
- **Day 2 (60 min):** Architecture deliverables (data architecture models, roadmaps, standards) and how they differ from data models (Week 4).
- **Day 3 (60 min):** Architecture principles and patterns referenced by DMBOK2.
- **Day 4 (60 min):** Practical exercise (below).
- **Day 5 (60 min):** Terminology drill, with explicit compare/contrast against Week 4 (Data Modeling) — these two KAs are the most commonly confused pair on the exam.
- **Day 6 (60 min):** Quiz + interleaved review.

**Recommended resources:**
- DAMA-DMBOK2, 2nd Edition — Data Architecture chapter

**Practical exercises:**
- Write a short comparison: for a system you know well, what would count as a "data architecture" artifact vs. a "data model" artifact under DAMA's definitions? Most engineers conflate these — resolving the distinction is the point of this exercise.

**Review activities:**
- Flashcard pass, full deck.

**Quiz plan:**
- One ~15-question quiz on Data Architecture, including several Architecture-vs-Modeling discrimination questions.

**Expected outcome:**
- Can distinguish Data Architecture from Data Modeling precisely, and describe how architecture artifacts guide (but don't replace) individual data models.

---

## Week 10 — Data Storage and Operations + Data Security

**Objective:** Cover two technically-familiar Knowledge Areas efficiently, focusing on DMBOK2's operational governance framing (backup/recovery policy, access control policy) rather than the technical mechanics you already know.

**Knowledge Areas covered:** Data Storage and Operations; Data Security.

**Daily study tasks:**
- **Day 1 (60 min):** Read DMBOK2 Data Storage and Operations — storage architecture, database operations concepts, DBA role framing.
- **Day 2 (60 min):** Continue Storage and Operations — performance, availability, and recovery concepts as DAMA frames them (SLAs, RPO/RTO framing).
- **Day 3 (60 min):** Read DMBOK2 Data Security — goals, classification schemes, and access control principles.
- **Day 4 (60 min):** Continue Data Security — security roles, monitoring, and the relationship between security and governance.
- **Day 5 (75 min):** Practical exercise (below), covering both KAs.
- **Day 6 (60 min):** Quiz (both KAs) + interleaved review.

**Recommended resources:**
- DAMA-DMBOK2, 2nd Edition — Data Storage and Operations chapter; Data Security chapter

**Practical exercises:**
- Write down your organization's actual data classification scheme (public/internal/confidential/restricted or equivalent) and access control model. Compare it against DMBOK2's security framework and note any gaps in formal policy vs. actual practice.

**Review activities:**
- Flashcard pass, full deck.

**Quiz plan:**
- One combined ~20-question quiz split across both KAs (10 each), reflecting their moderate individual exam weight but efficient combined coverage.

**Expected outcome:**
- Can describe storage/operations concepts and security classification/access principles in DMBOK2 terms, translating operational experience into formal policy language.

---

## Week 11 — Data Integration & Interoperability + Document & Content Management + Big Data & Data Science

**Objective:** Close out Phase 2 by covering the three remaining, lower-weighted Knowledge Areas — one a strong overlap with DE work, two genuinely less familiar.

**Knowledge Areas covered:** Data Integration and Interoperability; Document and Content Management; Big Data and Data Science.

**Daily study tasks:**
- **Day 1 (60 min):** Read DMBOK2 Data Integration and Interoperability — patterns (ETL/ELT, messaging, APIs, replication) framed in DAMA terms. This should move fast given daily pipeline experience.
- **Day 2 (60 min):** Continue Integration — data integration architecture and governance touchpoints (data contracts, SLAs between systems).
- **Day 3 (60 min):** Read DMBOK2 Document and Content Management — unstructured/semi-structured content, retention, and lifecycle concepts. This is likely the least familiar material this week — slow down here.
- **Day 4 (60 min):** Read DMBOK2 Big Data and Data Science — how DAMA frames big data characteristics, data science lifecycle, and its governance implications.
- **Day 5 (75 min):** Practical exercise (below), covering all three.
- **Day 6 (60 min):** Quiz (all three KAs) + interleaved review — this is the last new-content day of Phase 2, so review coverage should span the full Phase 2 glossary deck.

**Recommended resources:**
- DAMA-DMBOK2, 2nd Edition — Data Integration and Interoperability chapter; Document and Content Management chapter; Big Data and Data Science chapter

**Practical exercises:**
- For Integration: diagram one real integration pattern you've built (e.g., CDC pipeline, event stream) in DMBOK2 terms.
- For Document/Content Management: list any unstructured content your organization manages (contracts, support tickets, logs-as-content) and note whether any formal retention policy exists.
- For Big Data/Data Science: describe how a data science project you've supported as an engineer would be governed under DMBOK2's framing.

**Review activities:**
- Full glossary deck review — by this point it should span all 14 Knowledge Areas at least at a definitional level.

**Quiz plan:**
- One ~15-question quiz split across the three KAs.
- **End-of-Phase-2 checkpoint:** one longer ~30-question mixed quiz pulling from all 12 KAs studied in Weeks 3–11, to confirm readiness for Phase 3.

**Expected outcome:**
- All 14 Knowledge Areas have now been studied at least once. Can describe integration patterns, document/content lifecycle basics, and big data/data science governance considerations in DMBOK2 terms — and the Phase 2 checkpoint quiz identifies which KAs need reinforcement in Phase 3.

---

# Phase 3 — Application, Scenarios, and Exam Practice (Weeks 12–14)

**Purpose:** Shift from learning individual Knowledge Areas to answering exam-style questions that mix them — and from open-ended study to timed, scored practice with structured error analysis.

## Week 12 — Cross-Knowledge-Area Integration

**Objective:** Practice reasoning across Knowledge Areas the way the exam and real governance work actually requires — most real scenarios touch Governance, Quality, and Metadata simultaneously, for example.

**Knowledge Areas covered:** All 14, in combination.

**Daily study tasks:**
- **Day 1 (60 min):** Revisit the DMBOK2 wheel; for each spoke, write one sentence on how it depends on Data Governance (the center). This cements the "wheel" as a system, not a list.
- **Day 2 (60 min):** Work through 2–3 scenario-style questions (e.g., "a company wants to launch a new customer 360 initiative — which KAs are involved and how") and map out every relevant KA.
- **Day 3 (60 min):** Repeat with a scenario more familiar to your DE background (e.g., "a new data pipeline is failing quality checks downstream — trace the governance, quality, and metadata implications").
- **Day 4 (60 min):** Mixed-topic quiz (below), then review every wrong answer by tracing it back to its source KA and re-reading the specific DMBOK2 passage.
- **Day 5 (60 min):** Second mixed-topic quiz, same review process.
- **Day 6 (60 min):** Consolidate a personal "weak KA list" ranked by quiz error rate — this list drives Phase 3–4 prioritization from here on.

**Recommended resources:**
- DAMA-DMBOK2, 2nd Edition — the wheel diagram and cross-references between chapters
- CDMP-style practice question banks (per prep providers noted in `research/cdmp_exam_overview.md`)

**Practical exercises:**
- Take one real, moderately complex initiative from your own work (a migration, a new pipeline, a platform change) and write a half-page "data management impact analysis" touching at least 5 Knowledge Areas.

**Review activities:**
- Error-tracing (above) is the primary review activity this week — treat every wrong quiz answer as a pointer back to a specific chapter section.

**Quiz plan:**
- Two ~20-question mixed-topic quizzes (Day 4 and Day 5), scored and logged in `progress/`.

**Expected outcome:**
- Comfortable answering scenario-style questions spanning multiple Knowledge Areas, and has a concrete, evidence-based list of weakest KAs to prioritize.

---

## Week 13 — First Full-Length Practice Exam + Targeted Re-Study

**Objective:** Simulate real exam conditions once, then use the result diagnostically rather than as a final verdict.

**Knowledge Areas covered:** All 14.

**Daily study tasks:**
- **Day 1 (90 min):** Full-length timed practice exam — 100 questions, 90 minutes, no notes, no interruptions. Treat conditions as seriously as the real exam.
- **Day 2 (60 min):** Score the exam. Break results down by Knowledge Area (not just overall %). Update the weak-KA list from Week 12 with real exam-condition data.
- **Day 3 (75 min):** Re-study the single weakest KA from the breakdown — full re-read of that DMBOK2 chapter section, focused on missed question topics.
- **Day 4 (75 min):** Re-study the second-weakest KA the same way.
- **Day 5 (60 min):** Retake a shorter (~20-question) quiz covering only those two re-studied KAs to confirm improvement.
- **Day 6 (60 min):** Interleaved review across all 14 KAs (light touch — flashcard deck), plus rest/buffer if the week ran long.

**Recommended resources:**
- A full-length CDMP-style practice exam (100 questions) from a reputable prep provider
- DMBOK2 chapters corresponding to identified weak areas

**Practical exercises:**
- None new this week — the practice exam itself is the exercise. Time is better spent on review depth than new application work.

**Review activities:**
- Per-KA score breakdown logged in `progress/` to track improvement over Weeks 13–15.

**Quiz plan:**
- 1 full-length (100Q/90min) practice exam.
- 1 short (~20Q) targeted retake on the two weakest KAs.

**Expected outcome:**
- A concrete, scored baseline against the real exam format, with the two weakest Knowledge Areas already reinforced.

---

## Week 14 — Second Full-Length Practice Exam + Continued Targeted Re-Study

**Objective:** Confirm improvement from Week 13 and continue narrowing weak spots — by now, no Knowledge Area should be a complete unknown, only relatively weaker.

**Knowledge Areas covered:** All 14.

**Daily study tasks:**
- **Day 1 (90 min):** Second full-length timed practice exam (different question set than Week 13 if possible).
- **Day 2 (60 min):** Score and compare per-KA breakdown against Week 13's results. Confirm the previously weakest KAs improved; identify any new/remaining weak spots.
- **Day 3 (75 min):** Re-study the current weakest KA.
- **Day 4 (75 min):** Re-study the second-weakest KA.
- **Day 5 (60 min):** Mixed-topic quiz (~20 questions) across all 14 KAs, weighted slightly toward whatever remains weakest.
- **Day 6 (60 min):** Update `progress/` with a clear before/after comparison; plan Phase 4 priorities based on remaining gaps.

**Recommended resources:**
- A second full-length CDMP-style practice exam, distinct from Week 13's
- DMBOK2 chapters for any remaining weak areas

**Practical exercises:**
- None new — consolidation week.

**Review activities:**
- Full glossary deck review, timed to under 15 minutes (by now this should be fast — a sign of real retention).

**Quiz plan:**
- 1 full-length (100Q/90min) practice exam.
- 1 mixed-topic ~20-question quiz.

**Expected outcome:**
- Two full practice-exam data points showing an upward trend, and a short, specific list (ideally 1–3 KAs) of what still needs reinforcement heading into final revision.

---

# Phase 4 — Final Revision and Exam Readiness (Weeks 15–16)

**Purpose:** Convert the accumulated weak-spot list into a final, weighted revision pass, confirm readiness with one last full-length mock under strict conditions, and handle exam-day logistics — without last-minute cramming of new material.

## Week 15 — Weighted Revision Pass

**Objective:** Revise all 14 Knowledge Areas one more time, allocating time proportionally to both exam weight and remaining personal weakness — no new material introduced this week.

**Knowledge Areas covered:** All 14, weighted revision only.

**Daily study tasks:**
- **Day 1 (60 min):** Rapid review of the 4 heaviest-weighted KAs (Governance, Modeling, Quality, Metadata) — summary notes and glossary only, not full chapter re-reads.
- **Day 2 (60 min):** Rapid review of the next tier (Reference & Master Data, DW/BI, Architecture).
- **Day 3 (60 min):** Rapid review of remaining technical KAs (Storage/Ops, Security, Integration).
- **Day 4 (60 min):** Rapid review of the lighter KAs (Document/Content, Big Data/DS, Ethics, Maturity Assessment).
- **Day 5 (90 min):** Third full-length timed practice exam under strict conditions.
- **Day 6 (60 min):** Score and review Day 5's exam — this result is the clearest readiness signal so far. If any KA is still notably weak, flag it for a short Week 16 refresh.

**Recommended resources:**
- Personal glossary/flashcard deck (built since Week 1) — this is the primary resource this week, not the raw DMBOK2 text
- A third full-length CDMP-style practice exam

**Practical exercises:**
- None — pure revision and assessment week.

**Review activities:**
- The daily rapid reviews above ARE the review activity — this entire week is structured review by design.

**Quiz plan:**
- 1 full-length (100Q/90min) practice exam (Day 5).

**Expected outcome:**
- All 14 Knowledge Areas refreshed in memory within the last 7 days, and a third practice-exam score confirming (or flagging exceptions to) exam readiness.

---

## Week 16 — Final Mock Exam and Exam Logistics

**Objective:** One last confidence-confirming mock exam, light targeted touch-ups only, and all exam-day logistics handled well before sitting the real exam.

**Knowledge Areas covered:** All 14 — light touch-up only, driven by Week 15's results.

**Daily study tasks:**
- **Day 1 (60 min):** If Week 15's practice exam flagged a specific weak KA, do one final focused review of it. If not, do a light full-deck flashcard pass instead.
- **Day 2 (90 min):** Fourth and final full-length timed practice exam, under conditions as close to the real exam as possible (same time of day, same environment, proctoring-style quiet room).
- **Day 3 (60 min):** Score and review — at this point, review should be quick since most misses will be familiar patterns, not new gaps.
- **Day 4 (45 min):** Exam logistics: confirm Honorlock/proctoring system requirements, test your device/webcam/connection, confirm ID requirements, re-read `research/cdmp_exam_overview.md` exam-mechanics section once more.
- **Day 5 (45 min):** Light glossary skim only — no new studying, no last-minute cramming. Confidence-building review of your own notes, not the textbook.
- **Day 6:** Rest day, or move the exam sitting itself here if scheduled — no new studying immediately before the exam.

**Recommended resources:**
- Personal notes and glossary deck only
- DAMA/proctoring platform technical requirements page (system check before exam day)

**Practical exercises:**
- None — this is a consolidation and logistics week, not a learning week.

**Review activities:**
- Final flashcard/glossary pass, self-paced and low-pressure.

**Quiz plan:**
- 1 full-length (100Q/90min) practice exam (Day 2) — the final readiness checkpoint.

**Expected outcome:**
- A fourth practice-exam score at or above the target threshold (≥70% for Practitioner-level scoring), all exam logistics confirmed in advance, and the exam sat with no last-minute new material introduced.

---

## Sustainability Notes

- **1 rest day every week is non-negotiable.** A missed study day is not a failure — shift that day's tasks into the built-in calendar slack (the ~1.5-week buffer between 16 planned weeks and a real 4-month calendar span) rather than compressing later weeks.
- **Interleaved review (light flashcard passes) starts in Week 2 and never stops** — this is what prevents Week 3's content from being forgotten by Week 11.
- **No new material is introduced after Week 14.** Phases 3–4 are deliberately about practice and consolidation, not content — cramming new Knowledge Areas in the final two weeks is a common and avoidable failure mode.
- **Practice exam scores are diagnostic, not verdicts.** Each of the four full-length practice exams (Weeks 13, 14, 15, 16) exists to redirect study time, not to create pass/fail anxiety.
