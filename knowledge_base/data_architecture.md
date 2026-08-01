# Data Architecture

**Status:** Populated — core module complete (Week 9 of `roadmap/four_month_plan.md`).
**DMBOK2 Reference:** DMBOK2 Ch.4 — Data Architecture
**Exam weight:** Moderate (below the ~11% top tier, but frequently tested indirectly through its confusion with Data Modeling — see Sections 4, 8, 9)

> **Editorial note on sourcing:** As in prior modules, concepts are tagged **[DAMA]** for DMBOK2's official framing (paraphrased/synthesized from the text — verify exact wording against your own copy) or **[Industry Practice]** for real-world conventions, external frameworks, or terminology DMBOK2 references, overlaps with, or doesn't use at all but which you'll encounter professionally (e.g., TOGAF, the Zachman Framework, data mesh, lakehouse architecture, "data engineering architecture" as a job-scope term). Anywhere my recall of an exact DMBOK2 enumerated list is uncertain, it's flagged explicitly rather than presented as verbatim fact.

---

## 1. Overview

### Simple explanation (for beginners)

If Data Modeling is the floor plan for one room, **Data Architecture is the blueprint for the entire building** — how all the rooms connect, where the plumbing and electrical run between floors, which rooms can be added later without tearing down a wall. It's not the wiring itself (that's implementation) and it's not any single room's floor plan (that's a data model) — it's the enterprise-wide plan that makes sure a hundred separately-built rooms turn into one coherent, livable building instead of a hundred incompatible rooms bolted together.

**Why organizations need it:** without a blueprint, every team designs its own "room" independently. Each team's design is locally reasonable, but the building as a whole becomes an unmaintainable maze — duplicated pipes, walls that don't line up, no way to add a new floor without demolishing existing ones. Data Architecture exists so that individually reasonable local decisions (a new pipeline here, a new database there) add up to something coherent at the organizational scale, instead of accumulating into integration chaos.

### Professional / DAMA-level explanation

**[DAMA]** DMBOK2 defines Data Architecture as identifying the data needs of the enterprise (regardless of structure) and designing and maintaining the master blueprints to meet those needs — an integrated set of specifications, models, and standards that govern how data assets, flows, and platforms fit together, aligned to business strategy. Data Architecture produces two categories of deliverable:

1. **Architecture artifacts** — diagrams, models, roadmaps, and inventories describing the current state and desired future state of the organization's data landscape.
2. **Standards** — enterprise-level rules governing how data is structured, stored, integrated, and used, so that individual projects don't each reinvent (and diverge on) these decisions independently.

Critically, DAMA does not treat Data Architecture as its own invented framework in competition with established enterprise architecture practice — it explicitly positions Data Architecture as one domain *within* broader Enterprise Architecture, meant to align with and be informed by established frameworks (see Section 3).

---

## 2. Why This Knowledge Area Exists

**[DAMA]** Without a deliberate Data Architecture function, individual teams and projects make locally-optimal data decisions with no visibility into how those decisions interact across the organization. Data Architecture exists to make the *shape of the whole system* an explicit, governed decision — not an emergent accident of whichever team built which pipeline first.

### Business problems Data Architecture solves

1. **Integration chaos ("spaghetti architecture").** Without an architectural reference, every new integration is built point-to-point, and the number of connections grows combinatorially as systems are added — a well-known, expensive failure mode that a defined integration architecture (hub-and-spoke, event bus, canonical model) prevents.
2. **Duplicated systems of record.** Without an enterprise view of where each data domain authoritatively lives, multiple teams build competing "the real Customer database," each convinced theirs is the source of truth.
3. **Misalignment with business strategy.** Data investments (a new platform, a migration) made without reference to business architecture risk solving yesterday's problem or building capability the business doesn't actually need.
4. **Inability to plan for change.** Without a roadmap-level view, technology decisions (a database, a messaging platform) get made project-by-project, making a coordinated shift (e.g., cloud migration) far harder because there's no shared picture of what exists and how it connects.
5. **Inconsistent standards across teams.** Without enterprise-level standards, one team names dates as `date`, another as `dt`, another as `event_ts` — multiplying the integration and semantic-reconciliation cost of every future project.
6. **No accountable view of the full data lifecycle.** Individual projects tend to think about data only through go-live; Data Architecture is where the *organization* plans for a domain's data across its entire lifecycle, including retirement — a stage individual project teams rarely think about.

---

## 3. DAMA Definitions and Terminology

### Enterprise Data Architecture
**[DAMA]** The subset of enterprise architecture concerned specifically with data: a coherent set of models, policies, rules, and standards governing how data is collected, stored, arranged, integrated, and used across the whole organization. It functions as an integrating layer between business strategy and technology execution — translating "what the business needs to be able to do with data" into a structure technology delivery teams can actually build against.

### Data Architecture Principles
**[DAMA, general framing — exact enumerated wording varies by source; verify against your DMBOK2 copy]** Commonly emphasized principles include: data is a shared organizational asset (not owned by whichever system happens to store it first); business needs should drive architecture decisions, not the reverse; architecture should *enable* delivery rather than exist purely as constraint; standards and common vocabulary reduce long-term integration cost; and architecture is iterative — it documents and guides an evolving current-state-to-future-state journey, not a single fixed end-state diagram.

### Data Architecture Framework
**[DAMA + Industry Practice]** DMBOK2 does not mandate a single proprietary DAMA framework for structuring Data Architecture work. Instead, it references and is compatible with established **Enterprise Architecture frameworks**, most notably:
- **The Zachman Framework** — a matrix-based framework (originated by John Zachman) organizing architecture artifacts by perspective (e.g., planner, owner, designer) and by question (what, how, where, who, when, why).
- **TOGAF** (The Open Group Architecture Framework) — a widely adopted enterprise architecture methodology whose Architecture Development Method (ADM) explicitly includes a Data Architecture phase alongside Business, Application, and Technology Architecture phases (see Section 6).

**Exam-relevant point:** these are external, industry-standard frameworks that DAMA references as compatible tools — not DAMA inventions. A question implying DAMA created Zachman or TOGAF is testing whether you know this distinction.

### Data Domains
**[DAMA]** Logical groupings of data by subject area (e.g., Customer, Product, Finance, Employee), used to organize architecture, assign ownership, and scope governance. Data domains are the architecture-level unit that Data Governance ownership (see `data_governance.md`) and Data Modeling scope (see `data_modeling_and_design.md`) both attach to — the domain boundary is an architectural decision that both other Knowledge Areas depend on.

### Data Flows
**[DAMA]** Documented paths showing how data moves between systems, applications, and processes across the enterprise — captured as data flow diagrams, one of the core Data Architecture artifacts. Data flows make integration dependencies visible before they become production incidents.

### Data Lifecycle
**[DAMA]** The full set of stages data passes through: **creation/capture → processing/use → maintenance → archival → disposal/retirement**. Data Architecture is responsible for planning across this *entire* lifecycle — including the stages (archival, disposal) that individual project teams routinely under-plan for.

### Data Architecture Components
**[DAMA, general framing]** Typical architecture deliverables include: an enterprise (or domain-level) data model showing how core subject areas relate; data flow / integration diagrams; a technology and platform inventory; a data architecture roadmap sequencing future-state initiatives; and the standards described below.

### Data Architecture Standards
**[DAMA]** Enterprise-level rules distinct from (but related to) Data Governance's Policy/Standard/Procedure hierarchy — specifically scoped to architecture decisions: approved technology/platform choices, approved integration patterns (e.g., "cross-domain integration must use the event bus, not direct database access"), and naming/design conventions applied across all data models enterprise-wide.

---

## 4. Core Concepts

### Data Architecture vs. Data Modeling vs. Database Design vs. Data Engineering Architecture

This four-way distinction is one of the most practically important — and most exam-confused — clarifications in this Knowledge Area.

| Discipline | Scope | Typical Deliverable | Example Decision |
|---|---|---|---|
| **Data Architecture** | Enterprise-wide: how data domains, flows, and platforms fit together, aligned to business strategy | Enterprise/domain data models, data flow diagrams, standards, roadmap | "Customer data will be mastered in one MDM hub and distributed to all consuming systems via event streaming." |
| **Data Modeling** | One subject area/dataset, at conceptual/logical/physical levels of detail (see `data_modeling_and_design.md`) | ER diagrams, dimensional models | "The Customer entity has these attributes, this primary key, and these relationships to Order." |
| **Database Design** | The concrete technical implementation of a physical model on a specific database engine — indexing, partitioning, storage engine, performance tuning | DDL, index strategy, partitioning scheme | "Partition the Customer table by region; add a composite index on (last_name, signup_date) for the support-lookup query." |
| **Data Engineering Architecture** *(industry term, not DAMA-defined)* | **[Industry Practice]** The technical architecture of pipelines, orchestration, storage/compute engines, and tooling used to move and transform data | Pipeline/orchestration diagrams, tool selection (e.g., Airflow + Spark + Kafka), platform layer design | "We'll use Kafka for change-data-capture ingestion, land raw events in object storage, and orchestrate transformations with Airflow into the warehouse." |

**Key takeaway:** Data Architecture decides *what should exist and how it should connect at the enterprise level*; Data Modeling decides *the structure of one piece of it*; Database Design decides *how that structure is physically implemented and tuned on a specific engine*; and "Data Engineering Architecture" — a real, commonly used industry phrase, but not a DMBOK2 term — describes the concrete pipeline/platform tooling that operationalizes the enterprise architecture's Physical layer within a specific technology stack. If an exam question uses the phrase "data engineering architecture," treat it as informal/industry language layered on top of DAMA's actual framework, not a fifth official Knowledge Area.

### Architecture Layers: Conceptual, Logical, Physical

**[DAMA + general EA pattern — DMBOK2 applies a similar three-level pattern to architecture as it does to modeling; verify exact chapter wording]** Just as a data *model* has conceptual/logical/physical levels, Data *Architecture* work product is often organized the same way, but answering architecture-scoped questions rather than single-entity structure questions:

| Layer | Decisions that belong here | Example |
|---|---|---|
| **Conceptual Data Architecture** | High-level domains/subject areas and their relationships, independent of systems or technology; what data domains exist and roughly how they relate | "The enterprise has Customer, Product, Order, and Finance domains; Orders relate to both Customer and Product." |
| **Logical Data Architecture** | Technology-independent data flows, canonical structures, and integration relationships between domains and systems | "Customer data flows from the CRM (system of record) to the warehouse and to the support platform via a canonical Customer event schema." |
| **Physical Data Architecture** | The actual technology stack, specific platforms, network/infrastructure placement, and concrete integration mechanisms | "Customer events are published to a Kafka topic hosted in AWS region X; the warehouse is Snowflake; the support platform consumes via a Kafka connector." |

**This is a different three-level split than Data Modeling's conceptual/logical/physical** (which describes *one entity's structure* at increasing detail) — here, the same three-level pattern describes *the whole system's shape* at increasing technical concreteness. Conflating the two is a common and exam-relevant mistake (see Section 9).

### Relationships Between Business, Application, Technology, and Data Architecture

**[Industry Practice — TOGAF]** TOGAF (The Open Group Architecture Framework) formally decomposes Enterprise Architecture into four domains, and DMBOK2's Data Architecture chapter positions itself as compatible with this decomposition:

- **Business Architecture** — business strategy, capabilities, processes, and organizational structure. Defines *why* data is needed: which business capabilities require which data.
- **Data Architecture** — the structures, flows, and integration of data assets needed to support those business capabilities.
- **Application Architecture** — the blueprint of applications/systems that create, process, and consume data. Depends on Data Architecture to know what data structures and flows applications must support.
- **Technology Architecture** — the infrastructure (hardware, network, cloud, platforms) that hosts both applications and data. Provides the physical substrate on which Data and Application Architecture are realized.

**How they interact:** Business Architecture drives Data Architecture requirements (a new business capability requires new data domains or flows); Data Architecture in turn drives Application Architecture requirements (systems must be built or adapted to produce/consume the required data structures); Technology Architecture constrains and enables both (a new cloud platform can unlock a new data flow pattern that wasn't previously feasible, e.g., real-time streaming replacing nightly batch). Changes cascade in both directions — a technology change (e.g., cloud migration) can force a Data Architecture rethink, just as a business strategy change (e.g., entering a new market) can force new data domains into existence.

---

## 5. Data Engineer Perspective

As a Data Engineer, you operate mostly at the **Physical Data Architecture** layer and within the **Application/Technology Architecture** domains — but nearly every technical decision you make either follows an architectural standard someone else defined, or *becomes* an architectural precedent if no one else has defined one yet.

**ETL/ELT pipelines:** Architecture decides the overall integration *pattern* your pipelines must conform to — batch vs. streaming, point-to-point vs. hub-and-spoke, direct database access vs. API/event-based access. An individual pipeline's design is the execution of an architectural decision, not a decision made fresh each time — when no such decision exists yet, you are implicitly setting precedent for the next team's pipeline.

**Data platforms:** Architecture defines the reference layers a "data platform" is expected to have (ingestion, storage, processing, serving) — this reference shape is what guides tool selection, rather than each team independently choosing its own stack for the same layer.

**Data warehouses:** Whether the organization has one centralized enterprise warehouse, federated domain-specific marts, or a warehouse layered on top of a lake is a **Physical Data Architecture** decision, informed by Conceptual/Logical requirements about which domains need integrated cross-domain reporting.

**Data lakes:** Architecture decides zone structure (raw/curated/trusted — see `data_governance.md` Section 5), governance boundaries per zone, and — critically — whether the lake is a staging area feeding a separate warehouse, or the primary serving layer itself.

**Lakehouse architecture:** **[Industry Practice]** A modern pattern (e.g., Delta Lake, Apache Iceberg) merging lake-style flexible/cheap storage with warehouse-style transactional and query guarantees. This is a **Physical/Technology Architecture** decision — a good illustration that while specific technology patterns evolve rapidly, the underlying DAMA architecture principles (align to business need, plan for the full lifecycle, apply consistent standards) don't change with the tooling.

**Cloud migration:** Often the single event that forces an organization to *finally* document its Data Architecture formally — because migration requires answering "what do we actually have, and how does it all connect" before you can safely move it. Cloud migration is fundamentally a Technology Architecture initiative with major cascading Data Architecture consequences (data residency, latency, and security-zone constraints reshape feasible data flows).

**APIs:** Choosing API-based data exposure (vs. batch file transfer or direct database access) is an architectural integration-pattern decision, not a per-project style preference — architecture governs which pattern is the enterprise standard for which situation.

**Streaming platforms (e.g., Kafka):** Represent a **Logical/Physical Data Architecture** decision about how data flows near-real-time across domains — adopting a streaming platform is an architecture-level commitment to an event-driven integration pattern, not just a tool choice for one pipeline.

**Data integration patterns generally (ETL, ELT, CDC, event streaming, API-based, data virtualization):** Architecture is the layer that decides which pattern(s) are the enterprise standard for which use cases — the Data Engineer's job is largely to implement correctly *within* that decided pattern, and to escalate (rather than silently improvise) when a genuinely new use case doesn't fit any existing approved pattern.

---

## 6. Enterprise Case Studies

*(Illustrative composite scenarios; named external frameworks/regulations — TOGAF, PSD2/Open Banking, HL7 FHIR — are real.)*

### Government Digital Platforms
A government building a "digital government" citizen services platform must integrate data across previously siloed agencies (tax, health, identity, benefits). Getting this right requires a **Conceptual Data Architecture** defining shared domains (Citizen, Case, Service, Benefit) recognized across all agencies; a **Logical Data Architecture** defining a canonical citizen identifier and standard data-exchange flows between agencies; and a **Physical Data Architecture** implementing this via a government-operated cloud platform and standardized API gateway. Without this enterprise-level alignment, each agency's independently reasonable system becomes yet another incompatible island — this is precisely the "spaghetti architecture" failure mode Data Architecture exists to prevent, at national scale.

### Banking
Modern banking regulation has directly forced Data Architecture maturity: **PSD2 / Open Banking** (a real EU/UK regulatory framework) mandates that banks expose customer account data to authorized third parties via standardized APIs — effectively a regulator dictating a specific **Physical Data Architecture** integration pattern (API-based access) enterprise-wide. Internally, a bank's Data Architecture must also reconcile retail banking, lending, and risk-reporting systems (often built on different eras of technology) into a coherent whole — commonly requiring a Data Architecture roadmap phasing a move from siloed core-banking systems toward a centralized lakehouse or data-mesh-style domain-oriented platform (see Section 14 for Data Mesh as an industry-practice reference).

### Healthcare
A hospital network's Data Architecture must define how clinical, billing, and operational domains integrate — Conceptual domains like Patient, Encounter, Provider, and Claims need to be consistently defined across systems that historically evolved independently (an EHR system, a billing system, a scheduling system). **HL7 FHIR** (introduced in `data_modeling_and_design.md` as a real interoperability standard) operates at the intersection of Data Modeling and Data Architecture: it standardizes not just entity structure but the *exchange pattern* (a defined API-based integration approach) between systems — illustrating how a real industry standard can simultaneously answer a modeling question ("what does a Patient resource look like") and an architecture question ("how do systems exchange it").

### Retail
An omnichannel retailer running separate online, in-store POS, and inventory systems needs a Data Architecture unifying them around common Customer, Product, and Inventory domains so a customer's online cart and in-store purchase history can be reconciled, and inventory can be reported accurately across channels in near-real-time. This typically requires a **Logical Data Architecture** decision to introduce a canonical Customer/Product model and a **Physical Data Architecture** decision to adopt a streaming platform for real-time inventory updates — replacing what was historically a batch, end-of-day reconciliation process inadequate for real-time omnichannel expectations.

---

## 7. Common Mistakes

Focused specifically on mistakes Data Engineers make when architecture thinking is skipped:

1. **Building pipelines without architecture thinking.** Each new integration is designed in isolation, optimized for the immediate task, with no reference to an existing (or any) integration standard — the direct cause of point-to-point "spaghetti architecture" that becomes unmaintainable as the number of systems grows.
2. **Ignoring data ownership when building shared/canonical datasets.** An engineer builds a dataset multiple teams start relying on, but no business Owner (see `data_governance.md`) was ever assigned — so there's no one accountable for its definition evolving safely, and it silently becomes a de facto system of record nobody formally decided should be one.
3. **Ignoring enterprise standards.** Choosing a different message broker, naming convention, or integration pattern than the rest of the organization because it wasn't known, or was inconvenient to look up — multiplying long-term integration and operational cost even when the local decision was technically reasonable.
4. **Creating inconsistent data models across systems.** Without architecture-level domain definitions to anchor to, each team's data model for "Customer" or "Product" independently diverges, recreating the exact reconciliation problem `data_modeling_and_design.md` describes — but at enterprise scale, and after significant investment has already been sunk into each divergent version.
5. **Treating a static diagram as "the architecture."** Producing an architecture diagram once, then never updating it as systems evolve — the diagram stops reflecting reality within months, and "the architecture" becomes documentation theater rather than something that actually functions as decisions get made.
6. **Assuming building pipelines is the same as defining architecture.** Because engineers implement the physical layer daily, it's easy to assume architecture *is* whatever engineering happens to build — losing the enterprise, business-aligned, cross-team perspective that makes Data Architecture a distinct discipline from Data Engineering execution.
7. **Not planning for the full data lifecycle.** Building a pipeline and a storage layer with no plan for archival or disposal — data accumulates indefinitely because "we'll deal with retention later" was never revisited at the architecture level.

---

## 8. CDMP Exam Preparation

### High-value concepts
- The **definition of Data Architecture** as an enterprise-wide blueprint aligning data investments to business strategy — distinct from any single deliverable.
- **Data Architecture vs. Data Modeling** — the single most commonly tested distinction in this Knowledge Area (see Section 4 and Section 9).
- **Data Architecture components**: artifacts (models, flow diagrams, roadmap) vs. standards (naming, technology, integration pattern rules).
- **Data lifecycle stages**: creation/capture → processing/use → maintenance → archival → disposal — including the frequently-forgotten later stages.
- DAMA's positioning of Data Architecture as **one domain within Enterprise Architecture**, compatible with (not a replacement for) frameworks like Zachman and TOGAF.

### Important definitions
- Enterprise Data Architecture, Data Domain, Data Flow, Data Architecture Standard — precise recall of each, and the ability to distinguish "artifact" from "standard" as deliverable types.

### Frequently tested areas
- Distinguishing Conceptual/Logical/Physical **Data Architecture** (system-wide shape) from Conceptual/Logical/Physical **Data Modeling** (single-entity structure) — these are easy to conflate because they reuse the same three words for a different scope.
- Recognizing that Zachman and TOGAF are **external, industry-standard frameworks**, not DAMA inventions.

### Confusing concepts
- **Data Architecture vs. Database Design** — enterprise blueprint vs. concrete technical implementation on a specific engine.
- **Data Architecture vs. Data Engineering "Architecture"** — the latter is informal industry language for the technical pipeline/platform layer, not a DMBOK2-defined term.
- **Business/Application/Technology/Data Architecture** as TOGAF's four domains — know the relationships (Business drives Data, Data informs Application, Technology hosts both), not just the four names.

---

## 9. Exam Traps

- **A question conflates "Data Architecture" with "Data Model."** If a scenario describes the structure of *one* entity or dataset, that's Data Modeling, even if the word "architecture" appears in the question's wording — read for scope (one subject area vs. enterprise-wide), not vocabulary.
- **A question implies DAMA invented Zachman or TOGAF.** These are external frameworks DAMA positions itself as compatible with — an answer crediting DAMA/DMBOK2 as their origin is incorrect.
- **A question uses "Conceptual/Logical/Physical" ambiguously.** Check whether the scenario is describing one entity's structure (→ Data Modeling's three levels) or the whole system's integration shape (→ Data Architecture's three levels) — the same three words mean different things depending on KA context.
- **Assuming Data Architecture is "the diagram."** DMBOK2 frames architecture as an ongoing discipline (current state → future state, standards, roadmap) — an answer option equating architecture with a single static artifact undersells the Knowledge Area.
- **Assuming Data Engineering builds the architecture by default.** A scenario showing engineers making enterprise-wide integration-pattern decisions with no business/architecture-function involvement is describing a *gap*, not a correct process — don't mistake "who executes the physical layer" for "who owns the architecture decision."
- **Treating "data mesh" or "lakehouse" as DAMA-official terms.** These are real, important, but industry-originated concepts (see Section 14) — if an exam option attributes them to DMBOK2 directly, that's a trap.

---

## 10. Interview Preparation

### Data Engineer level (execution-focused)
1. "How do you decide whether a new data source should land in the lake or go directly into the warehouse?"
2. "Walk me through implementing a pipeline that must conform to an existing integration standard you didn't design yourself."
3. "What's different about how you'd design a batch ETL job vs. a streaming pipeline for the same underlying data?"

### Senior Data Engineer level (design and tradeoff-focused)
4. "How would you evaluate whether to adopt a lakehouse architecture versus keeping a separate lake and warehouse?"
   *Signal:* weighs consistency/transactional guarantees vs. flexibility and cost, and ties the decision back to actual business query/latency requirements rather than technology trend-following.
5. "Describe a time you pushed back on a proposed pipeline design because it violated an existing architectural standard."
   *Signal:* demonstrates recognizing architecture as a constraint they respect and escalate around, not something they route around unilaterally.
6. "How would you plan a cloud migration for an existing on-prem data platform without breaking downstream consumers?"
   *Signal:* mentions mapping current data flows first (Logical Architecture work) before touching Physical implementation, and phased/parallel-run migration rather than a single cutover.

### Data Architect level (enterprise and strategic-focused)
7. "How would you define data domains for a newly merged organization with overlapping systems?"
   *Signal:* starts from business capabilities (Business Architecture) rather than existing system boundaries, and has a process for resolving domain overlap/conflict (tying back to Governance escalation).
8. "How do you align a proposed data architecture with the organization's business architecture and strategy?"
   *Signal:* can articulate a concrete link — "this business goal requires this capability, which requires this data domain to exist and flow this way" — not just general alignment language.
9. "What framework(s) would you use to structure an enterprise's data architecture, and why?"
   *Signal:* can discuss Zachman/TOGAF (or a reasoned alternative) as a structuring tool, correctly attributing them as external frameworks rather than DAMA content.
10. "How do you govern architectural standards across autonomous teams without becoming a bottleneck?"
    *Signal:* discusses federated/hybrid governance models (see `data_governance.md`) applied to architecture specifically — enabling guardrails rather than centralized approval for every decision.
11. "How would you design a 3-year data architecture roadmap moving an organization from legacy on-prem systems to a modern cloud data platform?"
    *Signal:* sequences by business risk/value rather than technical convenience, and explicitly addresses the full data lifecycle (including what happens to legacy/retired data), not just the shiny new-platform build-out.

---

## 11. Practical Exercise

### Enterprise Scenario: Unifying an Omnichannel Retailer's Data Architecture

**Scenario:** A retail company operates three previously independent channels: an online store, physical stores with local POS systems, and a third-party-run loyalty program. Each has its own database and no integration exists between them. Leadership has set a strategic goal: a unified customer view and near-real-time inventory visibility across all channels within 18 months.

**Deliverables to produce (write these out in `notes/` as you work through it):**

1. **Conceptual Data Architecture:** Identify the core data domains involved (e.g., Customer, Product, Order, Inventory, Loyalty) and which existing system currently owns each — note any domain with no clear current owner.
2. **Logical Data Architecture:** Design a data flow diagram showing how data should move between systems to achieve a unified customer view (e.g., a canonical Customer model integrating identity across online/in-store/loyalty). Decide which integration pattern fits which flow (e.g., streaming for real-time inventory, batch or API for less time-sensitive loyalty data) and justify each choice.
3. **Physical Data Architecture:** Choose concrete technology for the platform (e.g., a specific cloud provider's data platform, a streaming technology, a warehouse/lakehouse) and justify the choice against the Logical requirements you just defined — don't pick technology first and rationalize it after.
4. **Standards to establish:** Define at least 3 enterprise-level Data Architecture standards this initiative should set (e.g., a canonical Customer identifier standard, an approved integration pattern for new channel integrations, a naming convention for shared domain events).
5. **Roadmap:** Sequence the work into 3 phases across the 18-month window, ordering by business risk/value rather than technical convenience. Explicitly state what happens to the legacy loyalty-program data relationship (part of full lifecycle planning) once the new architecture is live.
6. **Alignment check:** Write 2–3 sentences explicitly tracing how this Data Architecture serves the stated Business Architecture goal (omnichannel customer experience), and note where Technology Architecture choices (e.g., cloud platform selection) constrain or enable your Logical design.

**Self-check:** Could you defend, to a skeptical CTO, *why* each domain's data flows the way you designed — not just *that* it does?

---

## 12. Flashcards

| Term | Definition |
|---|---|
| Data Architecture | Enterprise-wide blueprint identifying data needs and designing/maintaining specifications, models, and standards to meet them, aligned to business strategy. |
| Enterprise Data Architecture | The coherent set of models, policies, rules, and standards governing data across the whole organization. |
| Data Architecture Artifact | A deliverable describing current/future data landscape state — models, flow diagrams, roadmaps. |
| Data Architecture Standard | An enterprise-level rule governing technology choice, integration pattern, or design convention. |
| Data Domain | A logical grouping of data by subject area (e.g., Customer, Product, Finance), used to scope ownership and architecture. |
| Data Flow | A documented path showing how data moves between systems, applications, and processes. |
| Data Lifecycle | The stages data passes through: creation/capture → processing/use → maintenance → archival → disposal. |
| Zachman Framework | An external (non-DAMA) matrix-based enterprise architecture framework organizing artifacts by perspective and question. |
| TOGAF | The Open Group Architecture Framework — an external, widely adopted EA methodology whose ADM includes a Data Architecture phase. |
| Conceptual Data Architecture | High-level domains and their relationships, independent of systems/technology. |
| Logical Data Architecture | Technology-independent data flows and integration relationships between domains/systems. |
| Physical Data Architecture | The actual technology stack and concrete integration mechanisms implementing the architecture. |
| Business Architecture | TOGAF domain describing business strategy, capabilities, and processes — drives Data Architecture requirements. |
| Application Architecture | TOGAF domain describing the application/system landscape; depends on Data Architecture for required structures/flows. |
| Technology Architecture | TOGAF domain describing infrastructure hosting applications and data. |
| Database Design | The concrete technical implementation of a physical data model on a specific engine (indexing, partitioning, tuning). |
| Data Engineering Architecture | Industry term (not DAMA-defined) for the technical pipeline/platform/tooling architecture that operationalizes Physical Data Architecture. |
| Lakehouse | Industry-practice architecture pattern merging data lake flexibility with data warehouse transactional/query guarantees. |
| Data Mesh | Industry-practice concept (Zhamak Dehghani) for domain-oriented, decentralized data architecture and ownership. |

---

## 13. Quiz Questions

1. What is the primary distinguishing scope difference between Data Architecture and Data Modeling?
   a) Architecture is technical, Modeling is business-only b) Architecture is enterprise-wide; Modeling describes one subject area's structure c) They are the same discipline with different names d) Modeling only applies to warehouses

2. Which of the following is an external framework DAMA references as compatible with Data Architecture, not a DAMA invention?
   a) The DMBOK2 Wheel b) TOGAF c) The Business Glossary d) The Data Quality Dimensions

3. What does "Conceptual Data Architecture" describe?
   a) Specific technology and infrastructure choices b) High-level data domains and their relationships, independent of technology c) Index and partitioning strategy d) A single entity's attributes and keys

4. Which TOGAF domain is primarily responsible for defining *why* certain data is needed?
   a) Technology Architecture b) Application Architecture c) Business Architecture d) Data Architecture

5. What distinguishes Database Design from Data Architecture?
   a) They are identical disciplines b) Database Design is the concrete technical implementation on a specific engine; Data Architecture is the enterprise-wide blueprint c) Database Design only applies to NoSQL systems d) Data Architecture is not concerned with technology at all

6. Is "Data Engineering Architecture" an official DMBOK2-defined Knowledge Area?
   a) Yes, it's Chapter 4 b) Yes, it's part of Data Storage and Operations c) No, it's an informal industry term for pipeline/platform tooling architecture d) No such concept exists in practice

7. What are the stages of the Data Lifecycle per DAMA's framing?
   a) Extract, Transform, Load b) Creation/capture, processing/use, maintenance, archival, disposal c) Conceptual, Logical, Physical d) Plan, Build, Run

8. What is a "data domain" used for architecturally?
   a) Encrypting sensitive data b) Grouping data by subject area to scope ownership and architecture c) Defining SQL data types d) Naming database indexes

9. What is "data mesh," per its origin?
   a) A DAMA-official governance framework b) An industry-practice concept for domain-oriented, decentralized data architecture and ownership c) A normalization technique d) A dimensional modeling notation

10. Why is "spaghetti architecture" considered a failure mode Data Architecture aims to prevent?
    a) It refers to slow SQL queries b) It describes uncoordinated point-to-point integrations that grow unmanageably as systems are added c) It only affects data quality checks d) It is a synonym for a star schema

**Answer Key:** 1-b, 2-b, 3-b, 4-c, 5-b, 6-c, 7-b, 8-b, 9-b, 10-b

---

## 14. References

**DAMA Official:**
- DAMA-DMBOK2, 2nd Edition — Chapter 4: Data Architecture (primary source; verify exact wording and any enumerated principle/component lists against your own copy)
- DAMA Dictionary of Data Management Terminology (glossary cross-reference)

**Industry Practices (real, not DAMA-official — cited in this module):**
- The Zachman Framework — John A. Zachman's matrix-based enterprise architecture framework
- TOGAF (The Open Group Architecture Framework) — including its four-domain (Business/Data/Application/Technology) architecture decomposition and ADM
- Zhamak Dehghani — "Data Mesh" concept and domain-oriented, decentralized data architecture principles
- Lakehouse architecture pattern (e.g., Delta Lake, Apache Iceberg) as an industry-practice evolution of warehouse/lake convergence
- PSD2 / Open Banking (EU/UK) — real regulatory framework mandating standardized API-based data architecture in banking

**Additional Architecture References:**
- HL7 FHIR — real healthcare interoperability standard spanning both Data Modeling and Data Architecture concerns (cross-referenced from `data_modeling_and_design.md`)

**Internal:**
- `research/cdmp_exam_overview.md` — exam structure and Knowledge Area weighting
- `roadmap/four_month_plan.md` — Week 9 study plan for this module
- `knowledge_base/data_governance.md` — ownership and standards cross-references
- `knowledge_base/data_modeling_and_design.md` — for the parallel (but scope-distinct) conceptual/logical/physical framing
