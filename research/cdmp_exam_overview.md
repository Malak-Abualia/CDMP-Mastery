# CDMP Exam Overview

Source: DAMA International official pages ([Exam Information & Pricing](https://dama.org/certification/exam-information-and-pricing/), [CDMP Certification Levels](https://dama.org/certification/cdmp-certification-levels/)), cross-checked against secondary prep resources. Last verified: 2026-08-01.

## 1. Certification Levels

CDMP is a single credential earned at different tiers of rigor. Every level starts with the **same** Data Management Fundamentals (DMF) exam — the tier you earn depends on your score (and, for Master, your experience and CV).

| Level | Requirement | Experience Needed | Target Audience |
|---|---|---|---|
| **Associate** | Pass DMF exam ≥ 60% | None required | Newcomers, students, early-career professionals building foundational knowledge |
| **Practitioner** | Pass DMF exam ≥ 70% **+ 2 Specialist exams** ≥ 70% each | None required formally; typically 2–10 years in data roles | Active practitioners in governance, quality, metadata, architecture, modeling, or stewardship roles |
| **Master** | Pass DMF exam ≥ 80% **+ 2 Specialist exams** ≥ 80% each | 10+ years relevant experience; CV submission required | Senior professionals who lead or significantly influence data management capability |
| **Fellow** | Additional recognition tier above Master (peer/industry recognition) | Extensive experience | Highest tier of the program |

**Key implication for my path:** I take the exact same Fundamentals exam whether I'm aiming for Associate or Practitioner-level scoring — the score threshold is what changes. Scoring ≥ 70% on the Fundamentals exam now sets up the eventual Practitioner credential once I later pass 2 Specialist exams.

## 2. Data Management Fundamentals (DMF) Exam Structure

- **Format:** 100 multiple-choice questions
- **Time limit:** 90 minutes (ESL candidates may purchase a version with +20 minutes)
- **Delivery:** Online, proctored (Honorlock), available on-demand — no fixed test center or date
- **Cost:** USD $311 per exam (same price for Fundamentals and each Specialist exam)
- **Passing scores:** 60% (Associate) / 70% (Practitioner) / 80% (Master) — see table above

### Specialist Exams (needed later for Practitioner/Master, not for Associate)

Same format as Fundamentals (100 questions, 90 minutes, same pricing). Choose 2 from:
- Data Quality
- Data Governance
- Metadata Management
- Data Modeling and Design
- Data Warehousing & Business Intelligence
- Reference & Master Data Management
- Data Integration & Interoperability

*(Not needed for my current Fundamentals-first phase — noted here for later Practitioner planning.)*

## 3. Knowledge Areas Covered (DMBOK2)

The Fundamentals exam draws from all 14 Knowledge Areas of the DAMA-DMBOK2 "wheel":

1. Data Governance
2. Data Architecture
3. Data Modeling and Design
4. Data Storage and Operations
5. Data Security
6. Data Integration and Interoperability
7. Document and Content Management
8. Reference and Master Data
9. Data Warehousing and Business Intelligence
10. Metadata Management
11. Data Quality
12. Big Data and Data Science
13. Data Management Maturity Assessment
14. Data Ethics (Data Handling Ethics)

### Approximate Exam Weighting

Based on published prep-provider breakdowns of the DMBOK2 wheel (not an official DAMA-published percentage table, so treat as directional rather than exact):

- **~11% each (heaviest):** Data Governance, Data Modeling and Design, Data Quality, Metadata Management
- **~10% each:** Reference & Master Data, Data Warehousing & Business Intelligence
- **Remaining weight spread** across Data Architecture, Data Storage and Operations, Data Security, Data Integration and Interoperability, Document and Content Management, Big Data and Data Science, Data Management Maturity Assessment, and Data Ethics

**Implication:** Data Governance, Data Modeling, Data Quality, and Metadata Management deserve the deepest study given they're both heavily weighted *and* (per my Data Engineering background) the areas most likely to contain unfamiliar governance/business-process framing rather than pure technical content.

## 4. Exam Expectations

- Questions are definitional and conceptual, drawn directly from DMBOK2 terminology, principles, and frameworks — not scenario-based coding or tool-specific questions.
- Expect emphasis on: DMBOK2 definitions, the purpose/goals of each Knowledge Area, roles and responsibilities (e.g., data steward vs. data owner), governance frameworks, and the relationships between Knowledge Areas (the "wheel" concept).
- No calculators, external references, or notes permitted (closed-book, proctored).
- Because it's multiple-choice and broad rather than deep on any one topic, breadth of coverage across all 14 Knowledge Areas matters more than mastering one area extremely well.

## 5. Recommended Preparation Approach

1. **Read DMBOK2 cover-to-cover once** for overall context — don't skip chapters, since the exam samples from all 14 Knowledge Areas.
2. **Study by Knowledge Area, weighted by exam emphasis** — spend proportionally more time on Data Governance, Data Modeling, Data Quality, and Metadata Management.
3. **Translate each Knowledge Area into Data Engineering terms** — for each DMBOK2 concept, identify the technical analogue I already know (e.g., Metadata Management ↔ data catalogs/lineage tools; Reference & Master Data ↔ dimension tables/golden records; Data Integration ↔ ETL/ELT pipelines) to anchor new theory to existing intuition.
4. **Actively target weak spots** — governance, stewardship roles, ethics, and maturity assessment are commonly the least intuitive areas for engineers and deserve deliberate extra attention rather than passive reading.
5. **Test retention continuously** — use practice quizzes per Knowledge Area rather than one big test at the end, and revisit missed concepts before moving on.
6. **Aim for the Practitioner threshold (≥70%) while studying for Fundamentals**, even though Associate only requires 60%, since the same exam sitting can support the eventual Practitioner path if scored high enough now (Practitioner status itself still requires the 2 Specialist exams later, but there's no reason to under-shoot the score).

## Open Questions / To Confirm Later

- Exact current DAMA-recommended DMBOK2 edition/errata to study from.
- Whether DAMA publishes an official (vs. third-party-estimated) percentage weighting per Knowledge Area — current weighting above is sourced from prep vendors, not confirmed on dama.org.
