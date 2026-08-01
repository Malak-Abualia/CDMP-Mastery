# Data Governance

**Status:** Populated — core module complete (Week 3 of `roadmap/four_month_plan.md`).
**DMBOK2 Reference:** DMBOK2 Ch.3 — Data Governance
**Exam weight:** ~11% (highest tier, tied with Data Modeling, Data Quality, Metadata Management — see `research/cdmp_exam_overview.md`)

> **Editorial note on sourcing:** Throughout this module, concepts are tagged **[DAMA]** when they reflect DMBOK2's official framing (paraphrased and synthesized from the text, not quoted verbatim — always cross-check exact wording against your own DMBOK2 copy before treating anything here as a direct quote) or **[Industry Practice]** when they reflect common real-world practice that DMBOK2 does not mandate or specify (e.g., specific tools, specific operating-model choices). Where my recall of an exact enumerated DMBOK2 list is uncertain, I've flagged it explicitly rather than presenting it as verbatim fact — verify against the book itself.

---

## 1. Overview

### Simple explanation (for beginners)

Imagine a company where every department calls the same thing by a different name — Sales calls it "client," Support calls it "account," Finance calls it "payer." Nobody agrees on what "active" means for a customer. When a report is wrong, nobody knows whose job it was to catch it. When a regulator asks "who approved sharing this data externally," there's no answer.

**Data Governance is the system of decision-making authority and accountability that prevents this.** It answers three questions for every important piece of data in an organization: *Who decides what this means? Who's accountable for its quality? Who's allowed to do what with it?* It is not a tool, not a database, and not a team that "does data quality" — it's a governance *system*: roles, rules, and decision rights.

### Professional / DAMA-level explanation

**[DAMA]** DMBOK2 defines Data Governance as the exercise of authority, control, and shared decision-making (planning, monitoring, and enforcement) over the management of data assets. Critically, DAMA draws a sharp line between **governance** and **management**:

- **Governance** = the "what" and "why" — setting direction, defining policy, assigning decision rights and accountability.
- **Management** = the "how" — the operational execution of those decisions (building pipelines, running quality checks, administering access).

This distinction is one of the most exam-relevant ideas in the entire Knowledge Area (see Section 9, Exam Traps). Data Governance doesn't do the data work — it decides who is accountable for the data work, and under what rules.

---

## 2. Why This Knowledge Area Exists

**[DAMA]** Without governance, data management activities happen, but they happen inconsistently, without coordination, and without a clear owner when something goes wrong. DMBOK2 frames governance as necessary because data is a *shared, cross-functional asset* — no single team can unilaterally decide what "customer," "revenue," or "active account" means without breaking someone else's downstream use of that same data.

### Business problems Data Governance solves

1. **Ambiguous accountability.** When a report is wrong, there's no defined chain from "the number is wrong" to "the person accountable for that data domain." Governance assigns ownership so this chain always exists.
2. **Conflicting definitions.** Different departments computing "churned customer" differently produces contradictory dashboards — and executives lose trust in data generally, not just in one report.
3. **Regulatory and legal exposure.** Regulators (financial, healthcare, privacy) increasingly require organizations to *prove* who is accountable for data, how it flows, and who approved its use. Without governance, there's no answer to "who authorized this" during an audit.
4. **Uncontrolled data quality decay.** Without an accountable owner, quality issues get discovered downstream (by an analyst or an executive) rather than caught at the source, and there's no clear escalation path to get them fixed.
5. **Inability to scale data initiatives.** Analytics, AI, and self-service BI programs stall when nobody trusts the underlying data enough to build on it — governance is what builds that trust structurally, not just technically.
6. **Duplicated and shadow effort.** Without a governance body to arbitrate, multiple teams independently build competing "customer master" datasets, wasting effort and creating reconciliation problems later.

---

## 3. DAMA Definitions and Terminology

**[DAMA]** These role and artifact definitions are foundational — the exam tests precise recall of *who does what*, and scenario questions frequently hinge on picking the correct role for a described responsibility.

### Data Owner
The individual (almost always a **business-side** role, not IT) formally accountable for a specific data domain — its quality, definition, and appropriate use. The Owner has **decision-making authority**: they approve definitions, approve access policy exceptions, and are ultimately answerable for that data domain's state. Ownership is about *accountability*, not day-to-day hands-on work.

### Data Steward
The person (or role) responsible for the **day-to-day oversight** of a data domain on the Owner's behalf: defining and maintaining business definitions, enforcing data standards, resolving data issues, and representing stakeholder interests. DAMA distinguishes several steward types:
- **Business/Subject-area Stewards** — domain experts (e.g., a "Customer Data Steward") who own definitions and rules for their subject area.
- **Technical Stewards** — bridge business rules into technical implementation (e.g., ensuring a business rule is correctly reflected in a schema or transformation).
- **Coordinating/Chief Stewards** — coordinate across subject-area stewards, often chairing stewardship committees.

**Owner vs. Steward, in one line:** the Owner is accountable; the Steward is responsible for doing the accountability's legwork day-to-day. (An Owner can delegate execution to a Steward but cannot delegate accountability.)

### Data Custodian
The **technical** role responsible for the safe storage, technical maintenance, and secure handling of data — typically a DBA, platform engineer, or (very often) a **Data Engineer**. Custodians implement the controls that Owners and Stewards decide are necessary (encryption, backups, access provisioning) but do **not** have decision-making authority over what the data means or who should be allowed to see it — they execute those decisions.

### Governance Council (Data Governance Council / Board)
A cross-functional, senior decision-making body — typically composed of business unit leaders, the Chief Data Officer (or equivalent), compliance/legal, and senior IT/data leadership. **[DAMA]** Its functions include: approving governance policy, resolving escalated data issues/disputes between domains or stewards, sponsoring governance initiatives, and holding the overall program accountable to the business. It is the top of the escalation chain when Stewards or Owners can't resolve a conflict themselves (e.g., two departments disagreeing on a shared definition).

### Policy → Standard → Procedure (the governance artifact hierarchy)
This hierarchy is a classic exam distinction:

| Artifact | Defines | Nature | Example |
|---|---|---|---|
| **Policy** | The **intent and direction** — what must be true and why | High-level, mandatory, rarely changes | "All customer PII must be classified and access-controlled." |
| **Standard** | The **specific, measurable requirement** that satisfies the policy | Mandatory, more detailed, moderately stable | "PII fields must be encrypted at rest using AES-256; access requires role X." |
| **Procedure** | The **step-by-step instructions** for how to comply with the standard | Operational, most frequently updated | "To request access to a PII-classified table, submit ticket type Y, get Owner approval, provisioning applied within 2 business days." |

*(Some frameworks add a fourth tier, a **Guideline** — a recommended-but-not-mandatory practice. DMBOK2 references this tier in places; if your practice exam distinguishes "mandatory" vs. "recommended," that's the Standard/Procedure vs. Guideline distinction.)*

---

## 4. Core Concepts

**[DAMA]** Beyond roles and artifacts, DMBOK2's Data Governance chapter centers on these ideas:

- **Governance as a program, not a project.** Governance has a defined lifecycle and operates continuously — it is never "done."
- **Decision rights and accountability framework.** A core governance deliverable is a clear map of *who decides what* — frequently implemented as a RACI-style matrix per data domain (who is Responsible, Accountable, Consulted, Informed for a given decision, e.g., "approve a new definition of 'active customer'").
- **Governance organizational models [DAMA + Industry Practice]:**
  - **Centralized** — one team/council owns governance decisions for the whole organization. Consistent, but can be slow and disconnected from domain nuance.
  - **Decentralized/Federated** — each business unit or domain governs its own data, coordinated loosely (or not) at the top. Fast and domain-aware, but risks inconsistency across the organization.
  - **Hybrid** — a central council sets enterprise-wide policy and standards; domain-level stewards implement and adapt within that frame. **[Industry Practice]** This hybrid model (and the related "federated" pattern popularized by data mesh thinking) is the most common real-world compromise, though DMBOK2 itself presents the three models neutrally rather than recommending one.
- **Issue management and escalation.** A named, repeatable process for raising a data conflict (e.g., "Sales and Finance disagree on what counts as 'revenue'") through Steward → Owner → Council, with a decision that becomes binding once made.
- **Business Glossary as a governance artifact.** A governed, single source of truth for business term definitions, sponsored and maintained through the governance structure (this is also central to Metadata Management — the two Knowledge Areas deliberately overlap here).
- **Regulatory and compliance oversight.** Governance is frequently the structure through which regulatory obligations (privacy law, financial reporting rules, healthcare privacy rules) get translated into concrete organizational policy.
- **Value and metrics.** DMBOK2 stresses that governance programs need to demonstrate measurable value (e.g., reduced data incidents, faster issue resolution, audit readiness) to sustain executive sponsorship — governance programs that can't show value tend to get defunded.

---

## 5. Data Engineer Perspective

As a Data Engineer, you are almost always a **Data Custodian**, occasionally a **Technical Steward**, and — critically — you are the person who suffers most when governance is *absent*, because ungoverned ambiguity lands on you as an implementation problem (e.g., you must guess what "active customer" means because no one defined it). Understanding governance is partly about understanding your own role's boundaries: you *implement* decisions; you should not be *making* business decisions by default, even when no one else is available to make them.

**ETL/ELT pipelines:**
Governance determines what a pipeline is *allowed* to do before you write a line of code: which source systems are approved for extraction, what transformations require sign-off (e.g., "any change to how 'active customer' is calculated needs Steward approval before deploying"), and what lineage/audit trail must exist for regulators. Without governance, business logic silently drifts across pipelines maintained by different teams, each with a slightly different interpretation of the same rule.

**Data warehouses:**
Conformed dimensions (customer, product, date) are inherently governance artifacts — someone has to be the accountable Owner for "what a customer record looks like enterprise-wide." Schema changes to shared warehouse models should go through a change-control process rooted in governance, not just a pull request review, because a schema change to a shared dimension can silently break definitions relied on by other teams.

**Data lakes:**
Lakes are harder to govern than warehouses because schema-on-read and low-friction ingestion make it easy to dump ungoverned data. **[Industry Practice]** A common pattern is zone-based governance — raw/bronze (minimal governance, ingestion-only), curated/silver (schema enforced, quality-checked, some governance), and trusted/gold (fully governed, business-approved for consumption) — with governance requirements increasing at each zone boundary. DMBOK2 doesn't prescribe this exact zone terminology (that's largely a modern lakehouse-era convention), but the underlying principle — that governance rigor should increase as data moves toward broader consumption — is consistent with DAMA's framing.

**Data quality checks:**
Governance defines *what quality means* for a data domain (the acceptable definition of "complete," "valid," "timely" for a given dataset, often via a Steward-approved rule) — the Data Engineer implements the *check* that enforces that rule. When a check fails, governance defines the *escalation path* (who gets notified, who decides whether to block the pipeline vs. let it through with a flag). Without this, engineers end up unilaterally deciding quality thresholds that are really business decisions.

**Metadata:**
Data Engineers are usually the primary producers of **technical metadata** (schemas, lineage, job run stats) — governance is what connects that technical metadata to **business metadata** (the glossary term it represents, its Owner, its sensitivity classification) so that a data consumer can trust and understand a dataset without asking an engineer directly. A data catalog is the common technical home for this, but the catalog is a tool — governance is the process that keeps its content accurate and accountable.

**Access control:**
Governance (via policy and classification standards) decides *what* needs to be protected and at what level (e.g., "PII fields require role-based access + audit logging"). The Data Engineer, as Custodian, *implements* that decision technically — IAM roles, row/column-level security, masking, tokenization. A common failure mode is engineers making classification decisions themselves by default ("I'll just restrict this table because it looks sensitive") — technically reasonable, but it's a governance decision being made without governance, which creates inconsistency once someone else's judgment differs from yours.

---

## 6. Enterprise Examples

*(Illustrative composite scenarios, not case studies of specific named organizations, unless a named law/regulation is cited — those are real.)*

### Government data platforms
A national statistics or open-data agency publishes datasets from dozens of source agencies (tax, health, transport). Without governance, each agency exports data with its own definitions, formats, and update cadence, and there's no accountable party when published data conflicts with another agency's numbers on the same topic. A governance council spanning the contributing agencies typically owns: data classification (public / restricted / confidential), a shared glossary for cross-agency terms (e.g., "resident" meaning differs between tax and health authorities), and data-sharing agreements that define who is accountable when shared data is misused. Interoperability standards (so agency B can consume agency A's data reliably) are a governance-driven output, not just a technical integration detail.

### Banking
Banking is one of the most heavily governance-regulated industries, driven by real regulatory frameworks:
- **BCBS 239** (Basel Committee's *Principles for Effective Risk Data Aggregation and Risk Reporting*) explicitly requires banks to demonstrate data lineage, accountability, and quality controls for risk-reporting data — this is essentially a regulator mandating DAMA-style governance by law for a specific data domain.
- **KYC/AML (Know Your Customer / Anti-Money-Laundering)** data requires a single, trusted "customer" definition across product lines — a governance Owner for the Customer domain, with Stewards enforcing consistent identity-resolution rules, is what makes a defensible "single customer view" possible.
- A **Data Governance Council** in a bank typically includes the Chief Risk Officer's team, compliance/legal, and business unit heads — because a data governance failure in banking has direct regulatory and financial consequences, not just an inconvenient dashboard.

### Healthcare
Healthcare data governance is shaped by patient safety and privacy law:
- **HIPAA** (U.S. Health Insurance Portability and Accountability Act) legally mandates controls over Protected Health Information (PHI) — access control, audit trails, and accountable data stewardship for patient data are not optional; they are compliance requirements with legal penalties for failure.
- A **Master Patient Index (MPI)** is a governance-critical artifact: multiple systems (billing, clinical, scheduling) must agree on "this is the same patient," which requires a Data Owner for patient identity, Stewards defining matching/merge rules, and Custodians (often Data Engineers) implementing identity-resolution pipelines under those rules.
- Governance councils in healthcare typically include clinical leadership (not just IT/compliance) because data quality issues in clinical data can directly affect patient care decisions — this is a good illustration of DAMA's point that governance is fundamentally a *business* function, not a technical one.

---

## 7. Common Mistakes

1. **Treating governance as a one-time project.** A governance "rollout" that isn't followed by ongoing operation (issue management, policy maintenance, steward onboarding) decays within a year.
2. **Naming a Steward without giving them authority or time.** A common anti-pattern: someone is told "you're the Customer Data Steward" as an added responsibility with no time allocation and no real authority to enforce decisions — the role exists on paper only.
3. **Letting Data Engineers become de facto Owners by default.** Because engineers are the ones who touch the data daily, business decisions (what counts as "valid," what a field means) quietly become *engineering* decisions simply because no one else is available. This is efficient short-term and corrosive long-term — those decisions won't be discoverable, documented, or defensible later.
4. **Confusing Custodian responsibility with Owner accountability.** "IT owns the data" is a common but incorrect framing — IT/Data Engineering are typically Custodians, not Owners, even when they're the only ones who understand the data technically.
5. **Over-engineering governance bureaucracy.** Requiring heavyweight sign-off for every minor change causes teams to route around governance entirely (shadow IT, unsanctioned spreadsheets, unofficial pipelines) — which produces *less* governance, not more.
6. **Buying a governance tool before defining roles and processes.** **[Industry Practice observation]** Purchasing a data catalog or governance platform is often mistaken for "implementing governance." The tool is a home for governance artifacts (glossary, lineage, ownership records) — it does not create accountability by itself.
7. **Trying to govern everything at once.** Attempting enterprise-wide governance across all data simultaneously stalls under its own scope. DAMA-aligned practice favors starting with high-risk/high-value domains (e.g., customer, financial reporting data) and expanding.
8. **No metrics tied to business value.** Governance programs that can't show "this reduced incidents by X" or "this cut audit prep time by Y" lose executive sponsorship and funding over time.

---

## 8. CDMP Exam Focus

**High-value concepts (study these first — they carry the most question weight in this Knowledge Area):**
- The **Governance vs. Management** distinction (what/why vs. how) — this framing recurs across nearly every DMBOK2 chapter, not just this one.
- Precise role definitions: **Owner, Steward, Custodian** — and correctly assigning a described real-world responsibility to the right role.
- The **Policy → Standard → Procedure** hierarchy, including which is mandatory vs. which is more operationally detailed.
- The purpose and composition of a **Governance Council**, especially its role in **escalation and dispute resolution**.
- Governance operating models (centralized / decentralized / federated / hybrid) and their tradeoffs.
- The idea that Data Governance sits conceptually at the **center of the DMBOK2 wheel** — nearly every other Knowledge Area (Quality, Metadata, Security, Master Data) has a governance dependency, and the exam likes to test that relationship indirectly through other KAs' questions.

**Frequently confused concepts:**
- **Steward vs. Owner** — accountability (Owner) vs. day-to-day responsibility (Steward). The exam often describes a scenario ("resolves data definition disputes for a domain, reports to the Owner") and expects you to identify it as the Steward, not the Owner.
- **Custodian vs. Steward** — technical execution (Custodian) vs. business rule ownership (Steward). A DBA implementing an access control list is a Custodian action; deciding *who should* have access is a Steward/Owner decision.
- **Governance vs. Data Quality Management** — Governance *decides* what quality standards should be; Data Quality Management (a separate Knowledge Area) *measures and improves* against those standards. They're tightly linked but distinct KAs.
- **Policy vs. Standard** — a policy states intent ("data must be protected"); a standard states the measurable requirement ("AES-256 encryption required"). Exam questions sometimes swap these to test if you notice the mismatch in specificity.

---

## 9. Exam Traps

- **"Who has final decision-making authority over X?"** → almost always the **Owner**, not the Steward, even if the Steward does the actual analysis/recommendation.
- **"Who is responsible for implementing backup, encryption, or technical access controls?"** → the **Custodian**, not the Owner or Steward — don't be misled by a scenario that makes the Custodian sound senior or influential; the *role*, not the seniority of the person, determines the answer.
- **A question describes someone doing both business rule-setting AND technical implementation** — DAMA's role model assumes separation of these; the exam may be testing whether you recognize this as a **Technical Steward** (a bridge role) rather than a pure Owner or Custodian.
- **Assuming "governance = IT function."** Any answer option that frames governance as primarily a technology or IT department responsibility is very likely the *wrong* answer — DMBOK2 is explicit that governance is business-led, cross-functional, and IT-supported, not IT-owned.
- **Treating "Guideline" and "Standard" as interchangeable.** A Guideline is recommended; a Standard is mandatory. If a question hinges on "must" vs. "should," this distinction is what's being tested.
- **Assuming there is one universally correct governance operating model.** DMBOK2 presents centralized/decentralized/federated neutrally, as tradeoffs depending on organizational context — an exam option claiming one model is "always best" is a trap.

---

## 10. Interview Questions (Senior Data Engineer Level)

Each includes a note on what a strong answer demonstrates.

1. **"Who should own the definition of 'active customer' — engineering or the business, and why?"**
   *Strong answer signal:* recognizes this as a business/Owner decision, explains why engineering shouldn't unilaterally decide it, and describes how they'd escalate an undefined term rather than guessing.

2. **"How would you design an ETL pipeline to comply with your organization's data governance policies?"**
   *Signal:* mentions approved source registration, documented transformation logic tied to Steward-approved business rules, lineage capture, and a change-control path for altering business logic.

3. **"What's the practical difference between your role as a Data Engineer and a Data Steward's role, when you both touch the same dataset daily?"**
   *Signal:* clearly separates "I implement and maintain the technical pipeline (Custodian)" from "they define what the data should mean and enforce business rules (Steward)," and can give a concrete example of where that line matters.

4. **"A business team wants to bypass the governed warehouse and query directly from the raw lake zone. How do you respond?"**
   *Signal:* doesn't just say "no" — explains the governance/quality risk of consuming ungoverned data, and proposes an escalation or exception process rather than a unilateral technical block.

5. **"How would you implement column-level access control for PII to satisfy a governance policy you didn't write?"**
   *Signal:* separates the *policy decision* (which fields are PII, who should access them — not their call) from the *technical implementation* (masking, RBAC, row/column security — their job), and asks the right people the right questions before building.

6. **"Describe how you'd prove data lineage to an auditor for a regulated dataset."**
   *Signal:* mentions capturing transformation logic, source-to-target mapping, versioning of business rules, and ties this back to why governance requires it (accountability, not just technical curiosity).

7. **"A data quality check you built is failing in production. Who decides whether to block the pipeline or let bad data through with a warning?"**
   *Signal:* recognizes this as a governance-defined escalation decision (tied to Steward/Owner-approved thresholds), not something the engineer should decide silently on their own judgment alone.

8. **"How do you balance governance/compliance overhead against delivery speed on an agile data team?"**
   *Signal:* acknowledges the real tension, proposes risk-based prioritization (heavier governance for high-risk/regulated domains, lighter for low-risk internal data) rather than either ignoring governance or applying it uniformly and slowing everything down.

---

## 11. Practical Exercises

### Exercise: Design a Governance Model for a Data Platform

**Scenario:** You're the lead Data Engineer at a mid-size company building a modern data platform: operational systems → data lake (raw/curated/trusted zones) → data warehouse → BI/reporting. The company has no existing formal data governance. Leadership has asked you to propose a starting governance model.

**Deliverables to produce (write these out in `notes/` as you work through it):**

1. **Governance Council composition** — who should sit on it (roles, not names) and why. Include at least one business, one compliance/legal, and one technical representative, and justify each seat.
2. **Ownership assignment** — pick 3 data domains (e.g., Customer, Product, Financial Transactions) and assign an Owner (business role) and a Steward (role, business or technical) for each. Justify why that role, not another, should own it.
3. **One Policy, one Standard, one Procedure** — write a real (short) example of each for a single concern, e.g., PII handling: a Policy statement, a Standard that operationalizes it, and a Procedure that tells an engineer exactly what to do to comply.
4. **Escalation path** — diagram what happens when two teams disagree on a data definition, from first disagreement to Council resolution.
5. **Classification and access tiers** — define at least 3 sensitivity classifications (e.g., Public / Internal / Restricted) and what access control each implies technically.
6. **Governance touchpoints across the pipeline** — annotate your lake → warehouse → BI architecture diagram with where governance decisions apply at each stage (ingestion approval, curated-zone quality gates, warehouse schema change control, BI-layer access control).

**Self-check:** Could you defend every assignment above to a skeptical auditor who asks "why is this person accountable, and what happens if they aren't available"? If not, revisit that assignment.

---

## 12. Flashcards

| Term | Definition |
|---|---|
| Data Governance | The exercise of authority, control, and shared decision-making over the management of data assets — the "what/why," not the "how." |
| Data Management | The execution/operational side of handling data — the "how." Distinct from, but directed by, governance. |
| Data Owner | Business-accountable individual for a data domain; holds decision authority; cannot delegate accountability. |
| Data Steward | Responsible for day-to-day oversight, definitions, and rule enforcement for a domain, on the Owner's behalf. |
| Business Steward | A Steward who is a subject-matter/domain expert on the business side. |
| Technical Steward | A Steward who bridges business rules into technical implementation. |
| Data Custodian | Technical role (often a Data Engineer/DBA) responsible for safe storage and technical handling; implements, doesn't decide. |
| Governance Council | Cross-functional senior body that sets policy, resolves escalated disputes, and sponsors governance initiatives. |
| Policy | High-level, mandatory statement of intent/direction. |
| Standard | Specific, measurable, mandatory requirement that operationalizes a policy. |
| Procedure | Step-by-step instructions for how to comply with a standard. |
| Guideline | A recommended (not mandatory) practice — distinct from a Standard. |
| Centralized governance model | One team/council makes governance decisions enterprise-wide. |
| Federated/Decentralized governance model | Each domain/business unit governs its own data with looser central coordination. |
| Issue escalation | The defined path for resolving a data conflict: Steward → Owner → Council. |
| BCBS 239 | Basel Committee banking regulation requiring provable data lineage and governance for risk-reporting data. |
| HIPAA | U.S. law mandating governance/access controls over Protected Health Information (PHI). |
| Master Patient Index (MPI) | A governed, cross-system record of "this is the same patient" — requires Owner, Stewards, and Custodian implementation. |

---

## 13. Quiz Questions

1. Who has final decision-making authority over the definition of a data domain?
   a) Data Custodian b) Data Steward c) Data Owner d) Data Engineer

2. Which role is most likely filled by a Data Engineer?
   a) Data Owner b) Data Steward c) Data Custodian d) Governance Council Chair

3. What is the correct order of the governance artifact hierarchy, from most general/mandatory-intent to most operational/detailed?
   a) Procedure → Standard → Policy b) Policy → Procedure → Standard c) Policy → Standard → Procedure d) Standard → Policy → Procedure

4. A governance body composed of senior cross-functional stakeholders that resolves escalated data disputes is called the:
   a) Data Quality Team b) Governance Council c) Stewardship Committee d) Data Office

5. What is the key distinction DAMA draws between Governance and Management?
   a) Governance is technical, Management is business-focused b) Governance is the "what/why," Management is the "how" c) Governance only applies to regulated industries d) There is no meaningful distinction

6. A bank must demonstrate lineage and accountability for its risk-reporting data due to which regulation?
   a) HIPAA b) GDPR c) BCBS 239 d) SOX

7. Which statement about a "Guideline" is correct?
   a) It is mandatory, like a Standard b) It is recommended but not mandatory c) It replaces the need for a Policy d) It is only used in healthcare governance

8. A Data Engineer implementing row-level security based on a policy decision they didn't make is acting as a:
   a) Data Owner b) Data Steward c) Data Custodian d) Governance Council member

9. Which governance operating model has each business unit governing its own data with minimal central coordination?
   a) Centralized b) Decentralized/Federated c) Hybrid d) Outsourced

10. What is the most common failure mode when a governance program is treated as a one-time rollout rather than an ongoing program?
    a) It becomes too strict over time b) It decays — policies go stale and enforcement stops c) It automatically converts to a federated model d) It merges with Data Quality Management

**Answer Key:** 1-c, 2-c, 3-c, 4-b, 5-b, 6-c, 7-b, 8-c, 9-b, 10-b

---

## 14. References

**DAMA Official:**
- DAMA-DMBOK2, 2nd Edition — Chapter 3: Data Governance (primary source for this module; verify exact definitions and any enumerated lists against your own copy)
- DAMA Dictionary of Data Management Terminology (glossary cross-reference for Owner/Steward/Custodian definitions)

**Regulatory / Authoritative External Sources (real, industry-defining references cited in Section 6):**
- Basel Committee on Banking Supervision — *BCBS 239: Principles for Effective Risk Data Aggregation and Risk Reporting*
- U.S. Department of Health & Human Services — HIPAA Privacy and Security Rules
- EU General Data Protection Regulation (GDPR) — relevant where cross-border/EU personal data governance is discussed

**Industry Practice (not DAMA-official, included for real-world grounding):**
- Data lake zone patterns (raw/curated/trusted or bronze/silver/gold) — common lakehouse architecture convention, not a DMBOK2-defined term
- Data governance/catalog tooling categories (e.g., data catalogs, lineage tools) as the operational home for governance artifacts — tool choice itself is an implementation detail, not a DAMA concept

**Internal:**
- `research/cdmp_exam_overview.md` — exam structure and Knowledge Area weighting
- `roadmap/four_month_plan.md` — Week 3 study plan for this module
