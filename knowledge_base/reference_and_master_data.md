# Reference and Master Data

**Status:** Populated — core module complete (Week 7 of `roadmap/four_month_plan.md`). Revised per `reviews/reference_and_master_data_review.md`.
**DMBOK2 Reference:** DMBOK2 Ch.10 — Reference and Master Data
**Exam weight:** ~10% (second tier, alongside Data Warehousing & Business Intelligence — see `research/cdmp_exam_overview.md`)

> **Editorial note on sourcing:** Sourced per the priority hierarchy defined in `research/source_map.md` — DAMA-DMBOK2 concepts are primary authority, official DAMA guidance is used for certification framing, and named tools/platforms are illustrative examples only, never treated as DAMA definitions. Concepts are tagged **[DAMA]** for DMBOK2's official framing (paraphrased/synthesized from the text, not quoted verbatim — verify exact wording against your own copy) or **[Industry Practice]** for real-world conventions, tools, or vendor terminology DMBOK2 references loosely or doesn't mandate. Some terms (e.g., "Golden Record," the MDM implementation style names, MDM success metrics) are tagged **[DAMA + Industry Practice]** where the underlying concept is DAMA-endorsed but the exact term or enumeration is widely-adopted practitioner vocabulary that DMBOK2 references rather than originates — cross-check exact wording against your own DMBOK2 copy. This revision follows `reviews/reference_and_master_data_review.md` and conforms to the standard 14-section template documented in `knowledge_base/README.md`. No DMBOK2 text is reproduced verbatim anywhere in this file.

---

## 1. Overview

### Simple explanation (for beginners)

Imagine a retailer with an online store, a mobile app, and physical locations. A customer named "Jonathan Smith" buys online, then walks into a store and is rung up as "Jon Smith." Are these the same person? Nothing in either system says so — each system just has its own local record, confident it's correct in isolation.

**Master Data** is the answer to "who/what is this, really, across the whole organization" — the authoritative, agreed-upon representation of the core business entities everyone depends on: customers, products, employees, suppliers, locations. It's the "nouns" of the business that show up again and again in many different processes and systems.

**Reference Data** is different, and smaller in scope: it's the standardized set of allowed *values* used to classify or categorize other data — country codes, currency codes, status codes, unit-of-measure codes. It doesn't describe a unique real-world entity the way Master Data does; it describes a controlled vocabulary that many entities share. A country code like "US" isn't *about* any one customer — it's a value any customer record can point to, and it means the same thing everywhere it's used.

**Why organizations need them:** Without governed Master Data, "how many unique customers do we have" is unanswerable with confidence — the honest answer is "it depends which system you ask, and how you define duplicate." Without governed Reference Data, one system's "Active" status might be another system's "A," and a report joining the two silently produces nonsense. Both problems look like technical inconveniences at first, but they compound into real business damage: wrong revenue numbers, marketing spend wasted on the same customer counted three times, regulatory reports that can't be reconciled.

### Professional / DAMA-level explanation

**[DAMA]** DMBOK2 treats Reference Data and Master Data as related but distinct disciplines, each requiring its own management approach:

- **Reference Data Management (RDM)** is the discipline of defining, and keeping up to date, the controlled sets of values (code sets, classification schemes) used consistently across the organization to categorize other data.
- **Master Data Management (MDM)** is the discipline of creating and maintaining a consistent, accurate, and authoritative representation of an organization's core shared business entities — the "system(s) of truth" for entities like Customer, Product, Supplier, Employee, and Location — so that every business process and system references the same understanding of "who/what" rather than independently maintained, conflicting versions.

**[DAMA]** Both disciplines exist because certain data is *shared* across many systems and processes rather than owned by any one of them — DMBOK2 frames this Knowledge Area as fundamentally about managing data that multiple parts of the organization depend on having in common. Without deliberate management, shared data doesn't stay shared; it silently forks into as many slightly different versions as there are systems that touch it.

---

## 2. Why This Knowledge Area Exists

**[DAMA]** Reference and Master Data are, by definition, shared across many systems and processes — no single application "owns" the true meaning of Customer or the true set of valid Country codes without the rest of the organization implicitly depending on that meaning being right. This Knowledge Area exists to make that shared meaning a deliberately managed, governed outcome, rather than something that emerges accidentally (and inconsistently) from whichever system happened to be built first.

### Business problems Reference and Master Data solve

1. **Fragmented view of core entities.** The same customer, product, or supplier exists as multiple, disconnected records across systems, making a true enterprise-wide count or view impossible without heavy manual reconciliation.
2. **Inconsistent categorization.** Different systems using different code values for the same concept (e.g., "USA" vs. "US" vs. "United States") break every attempt to join, aggregate, or compare data across those systems.
3. **Duplicate effort and conflicting "truth."** Multiple teams each build their own "authoritative" customer or product list, each convinced theirs is correct, with no way to reconcile them.
4. **Poor customer/business experience.** A customer who updates their address in one channel but sees it unreflected in another (because there's no shared, synchronized master record) experiences the organization as disjointed rather than unified.
5. **Regulatory and reporting risk.** Regulatory reporting (e.g., consolidated risk exposure in banking) requires a single, defensible view of entities like "customer" or "counterparty" — fragmented master data makes this legally risky, not just operationally messy.
6. **Wasted integration effort.** Without shared reference/master data as a common reference point, every system-to-system integration must independently build (and maintain) its own translation/mapping logic.

---

## 3. DAMA Definitions and Terminology: Reference Data vs. Master Data

This is one of the most heavily tested distinctions in this Knowledge Area — candidates who understand MDM conceptually still lose points by misclassifying a specific example.

| Dimension | Reference Data | Master Data |
|---|---|---|
| **Definition** | A controlled, standardized set of permissible values used to classify or categorize other data | The authoritative, agreed representation of an organization's core shared business entities |
| **Purpose** | Ensures consistent classification/categorization across systems | Ensures a single, trusted, shared understanding of "who/what" for entities every process depends on |
| **Characteristics** | Small, relatively static value sets; low rate of change; often externally defined (industry/regulatory standards) or internally defined (business-specific codes) | Complex entities with many attributes and relationships; changes more frequently (a customer moves, a product is discontinued); often larger volume than reference data |
| **Examples** | Country codes, currency codes, status codes ("Active"/"Inactive"), unit-of-measure codes, industry classification codes (e.g., NAICS/SIC) | Customer, Product, Employee, Supplier/Vendor, Location/Site, Chart of Accounts entity in some framings |
| **Ownership** | Often a Data Steward for a narrow domain, sometimes inherited directly from an external standards body (e.g., ISO defines country codes; the org doesn't invent them) | A business-side Data Owner per entity/domain (e.g., a "Customer Data Owner"), typically with more organizational weight given the entity's broad usage |
| **Management approach** | A managed, versioned code list/registry; changes are infrequent and tightly controlled since many systems reference the same values | An ongoing MDM program: matching, merging, survivorship, synchronization, and distribution to consuming systems (see Section 4) |
| **Governance requirements** | Lighter-weight but still governed — an unauthorized new "status code" invented by one team breaks every downstream system expecting the standard set | Heavier — requires explicit stewardship, a defined system (or process) of record, and an operating model for keeping consumers synchronized as the entity changes |

### Terminology clarification

- **"Is this Reference Data or Master Data?"** questions hinge on one test: *does the item describe a controlled value used to classify something else (Reference Data), or does it describe a unique real-world business entity with its own identity and attributes (Master Data)?* A "Customer Status" **code** ("Active") is Reference Data; the **Customer** entity itself is Master Data.
- **Overlap cases.** Some data blurs the line — e.g., a "Product Category" list functions as Reference Data (a controlled classification), while the **Product** entity itself (with its own SKU, price, description) is Master Data. A single domain can contain both kinds of data simultaneously.

*(See Section 9, Exam Traps, for common incorrect assumptions built on top of this distinction.)*

---

## 4. Core Concepts

### Master Data Management (MDM)

**[DAMA]** MDM is the function that creates and maintains the organization's authoritative version of shared, core business entities, and makes that authoritative version available consistently to every system and process that needs it.

- **Purpose:** Provide a single, trusted, consistent representation of core entities (Customer, Product, Supplier, etc.) so that every consuming system and process operates against the same understanding rather than independently maintained, diverging copies.
- **Benefits:** A unified enterprise view of key entities (e.g., a true customer count, a true product catalog); reduced integration cost (systems synchronize against one authoritative source rather than each other); improved data quality at the source, since matching/deduplication happens once centrally rather than being re-solved by every downstream consumer; better regulatory defensibility (a demonstrable, governed "customer" or "counterparty" definition).
- **Challenges:** Matching and deduplication is genuinely hard at scale (see Matching and Merging below) — no algorithm gets it perfectly right, and false matches/non-matches both carry real cost; organizational resistance, since MDM typically requires source systems to give up local autonomy over "their" version of an entity; the technical complexity of keeping many downstream systems synchronized as the master record changes; and sustaining executive sponsorship, since MDM is infrastructure-like — its value is diffuse and easy to underfund relative to a feature with a visible, immediate payoff (see MDM Success Metrics, below, for the countermeasure).
- **Governance requirements:** MDM cannot succeed as a purely technical initiative — it requires an accountable business Data Owner per master entity domain, Data Stewards to define and enforce matching/survivorship rules, and a governed change process for how the "golden" definition of an entity evolves (directly inheriting the Owner/Steward/Council structure from `data_governance.md`).

### Reference Data Management

**[DAMA]** Reference Data Management is the discipline of defining, maintaining, and distributing controlled value sets ("code sets" or "classification schemes") that other data references to ensure consistent meaning across the organization.

- **Controlled values:** A defined, finite (or slowly-growing) list of permitted values for a given classification — e.g., the exact set of allowable "Order Status" values. Systems should not be free to invent new values outside this controlled set without a governed change process.
- **Value Domain:** **[DAMA]** The precise term for the bounded, permitted set of values a Reference Data code set defines — e.g., the Value Domain for "Order Status" is {Pending, Shipped, Delivered, Cancelled}. Some practitioner sources use "code set" and "Value Domain" interchangeably; verify exact DMBOK2 usage against your own copy.
- **Standards:** Reference Data frequently maps to external standards bodies rather than being internally invented — e.g., ISO 3166 (country codes), ISO 4217 (currency codes). Using an external standard, where one exists, avoids reinventing a classification scheme the rest of the industry already agrees on.
- **Codes:** The literal permitted values themselves (e.g., "US," "CA," "MX" for country) plus their authoritative descriptions/definitions — a code with no governed definition is just as prone to misinterpretation as an ungoverned business term in a glossary (see `data_governance.md`, Business Glossary).
- **Classifications:** Reference Data is often hierarchical or grouped (e.g., a "Product Category" scheme with parent/child levels) — this is a lighter-weight cousin of the Hierarchies concept discussed below for Master Data.

### Golden Record

**[DAMA + Industry Practice]** The concept of producing a single, trusted, authoritative version of a master entity once candidate records have been matched and reconciled is DAMA-endorsed; the specific term **"Golden Record"** is near-universal practitioner vocabulary for it, comparable to how `data_modeling_and_design.md`, Section 3 notes that Kimball-originated dimensional-modeling terms are industry vocabulary DMBOK2 references rather than invents.

- **What it means:** Not necessarily an exact copy of any single source system's record — it's often a *synthesized* record, built by selecting the best available value for each attribute from among the matched source records (see Survivorship Rules below).
- **Why it matters:** It's the concrete deliverable that makes "a single view of the customer" more than a slogan — without a golden record, "single view" remains an aspiration with no artifact anyone can actually query.
- **How it is created:** Through the MDM pipeline: candidate source records are identified, matched (Matching and Merging), and then the surviving/winning values for each attribute are selected according to governed Survivorship Rules — producing one record trusted as authoritative and made available for distribution back to consuming systems.

### Single Source of Truth

**[DAMA]** "Single Source of Truth" is a business/governance concept — it describes a single **trusted, authoritative definition** of an entity or fact that the organization agrees to treat as correct, regardless of how many physical copies of that data actually exist in different systems.

- **Business meaning:** It's an agreement about *authority*, not a claim about physical storage — the organization has decided which record (or which process for producing a record) is the one to trust when values disagree.
- **Difference between physical storage and trusted data source:** A Single Source of Truth does **not** require all data to live in one physical database. In a **Registry-style** MDM implementation (below), the golden record might be a virtual, computed view referencing data still physically stored in multiple source systems — the "single source of truth" is the governed *process and resulting authoritative view*, not necessarily a single physical repository. Conflating "single source of truth" with "one physical database" is a common and costly architectural misconception (see Section 9, Exam Traps).

### Matching and Merging

**[DAMA]** The technical and procedural process of determining which records across (or within) source systems represent the *same* real-world entity, and combining them into one.

- **Duplicate detection:** Identifying candidate records that likely represent the same entity, using deterministic rules (exact match on a strong identifier like a national ID or email) and/or probabilistic techniques (fuzzy matching on name/address combinations, weighted scoring across multiple attributes) when no reliable shared identifier exists.
- **Identity resolution:** The broader process of establishing "these N records across systems are the same real-world entity" — matching is the mechanism; identity resolution is the outcome.
- **Record consolidation:** Once records are matched, consolidating them into a single golden record — the point where Survivorship Rules become necessary, since matched records rarely agree on every attribute value.

**[Industry Practice]** Matching quality is usually measured along two error types with an inherent tradeoff: **false positives** (incorrectly merging two different real-world entities into one) and **false negatives** (failing to merge records that really are the same entity, leaving duplicates). Tuning matching aggressiveness one direction worsens the other — this tradeoff is not a DMBOK2-defined term, but the underlying tension is a direct extension of the DAMA point that MDM is inherently imperfect and requires ongoing tuning and human review, not a "solve once" algorithm.

### Survivorship Rules

**[DAMA]** The governed business rules that determine, when matched source records disagree on an attribute's value, which value "survives" into the golden record.

- **Source priority:** A common approach — rank source systems by trustworthiness for a given attribute (e.g., the billing system is authoritative for legal name; the CRM is authoritative for marketing preferences) and take that source's value when records conflict.
- **Conflict resolution:** Beyond simple source priority, rules may consider recency (most recently updated value wins), completeness (a populated value beats a null), or explicit manual stewardship review for high-stakes conflicts that automated rules can't confidently resolve.
- **Business rules:** Survivorship logic is not a technical default — it must be defined and approved by the accountable Data Owner/Steward for that entity, since "which value is correct" is fundamentally a business judgment about source trustworthiness, not an engineering decision to be made unilaterally (directly echoing the Owner/Custodian boundary from `data_governance.md`).

### Hierarchies

**[DAMA]** Master Data frequently isn't flat — entities relate to each other in structured, often multi-level ways that must themselves be managed as part of the master data.

- **Organizational hierarchies:** Reporting structures, cost centers, legal entity structures (e.g., which subsidiary rolls up to which parent company) — critical for consolidated financial and regulatory reporting.
- **Product hierarchies:** Category → subcategory → product → SKU relationships — needed for consistent sales reporting and analysis at different levels of aggregation.
- **Customer relationships:** Household groupings, corporate parent/subsidiary relationships between business customers, or account hierarchies (e.g., which individual accounts belong to which corporate customer) — needed to answer questions like "what is our total exposure/revenue for this customer *including* all its subsidiaries," which a flat customer list cannot answer alone.

**Why hierarchies matter for MDM specifically:** A hierarchy is itself master data that must be matched, governed, and kept current — a stale or incorrect hierarchy (a subsidiary still mapped to its former parent after a corporate restructuring) silently corrupts every roll-up report built on top of it, even if every individual entity record is perfectly accurate.

### Master Data Types

**[DAMA, general framing — exact enumeration varies by source; verify against your DMBOK2 copy]** Master Data is commonly discussed in terms of broad entity-type categories:

- **Party** — people and organizations the enterprise has relationships with (customers, employees, suppliers, partners). Frequently modeled with a **"Party" supertype** and **"Person"/"Organization" subtypes** — this is the exact Generalization/Subtyping pattern already introduced in `data_modeling_and_design.md`, Section 3, applied directly to Master Data's most common entity type.
- **Product** — the goods/services the enterprise sells or produces.
- **Financial** — accounts, cost centers, and chart-of-accounts entities needed for consistent financial reporting.
- **Location** — physical or logical places relevant to the business (sites, stores, warehouses, addresses).

Recognizing that "Customer" and "Supplier" are typically both instances of a **Party** entity type (rather than two unrelated entities independently invented) is a direct, practical application of data modeling discipline to Master Data design — and a natural bridge between this Knowledge Area and `data_modeling_and_design.md`.

### Data Sharing Agreements

**[DAMA]** A **Data Sharing Agreement** is a governance artifact — a documented, approved agreement between a master data provider and its consumers specifying what data is shared, under what terms, at what quality/freshness level, and under what usage restrictions. It is the MDM-specific counterpart to the Policy/Standard/Procedure hierarchy from `data_governance.md`, formalizing the terms under which a golden record (or any shared master/reference dataset) is distributed. Without one, consuming systems can develop undocumented assumptions about freshness, completeness, or permitted use that the source was never actually committed to.

**[Industry Practice]** A Data Sharing Agreement is conceptually adjacent to the **Data Contract** pattern already introduced in `data_quality.md` and `data_modeling_and_design.md` — a Data Sharing Agreement tends to be the business/governance-oriented agreement, while a Data Contract is typically its technical, enforced instantiation (schema and quality expectations encoded and checked in the pipeline itself).

### MDM Success Metrics

**[DAMA + Industry Practice]** Echoing Data Governance's emphasis on demonstrating value (`data_governance.md`, Section 4), sustaining MDM investment requires measurable success indicators, since MDM's value is diffuse and easy to underfund without proof of impact (see the Challenges bullet under Master Data Management, above). Commonly used measures include:

- **Match rate** — the percentage of candidate records successfully matched/consolidated.
- **Duplicate reduction rate** — the decline in known duplicate entities over time.
- **Golden record adoption** — the number or percentage of consuming systems actually using the golden record rather than maintaining a local copy.
- **Downstream data quality improvement** attributable to consuming governed master data (tying back to the Uniqueness dimension in `data_quality.md`).

**[Industry Practice]** These specific metric names are practitioner convention rather than a DMBOK2-mandated list — DMBOK2 discusses the general need for demonstrable program value without necessarily prescribing this exact metric set; verify framing against your own copy.

### MDM Implementation Styles

**[DAMA + Industry Practice]** DMBOK2 discusses several architectural approaches for implementing MDM; the four styles below are the commonly-taught set (exact naming and boundaries vary somewhat across practitioner sources — verify framing against your own DMBOK2 copy).

**Registry Style**
- **Description:** A thin, virtual layer. The registry doesn't store full master records itself — it stores just enough identifying information (cross-reference keys) to know that Record A in System 1 and Record B in System 2 represent the same entity. The "golden view" is computed on demand by referencing data that stays physically in the source systems.
- **Advantages:** Fast and relatively cheap to implement; minimal disruption to existing source systems, since they keep ownership of their own data; lower risk for an initial MDM effort.
- **Challenges:** Limited data quality improvement — since the data isn't actually consolidated or cleansed, underlying inconsistencies in source systems persist; performance can suffer since the "golden view" is assembled at query time from multiple live systems; not well suited when consumers need a single, physically consistent record to act against.
- **When to use:** A good starting point for organizations new to MDM, or where full consolidation is politically or technically infeasible in the near term, and the primary need is simply *knowing* which records match, not necessarily unifying them physically.

**Consolidation Style**
- **Description:** Master data is physically extracted from multiple source systems into a separate, centralized store where matching, merging, and golden-record creation happen. The golden record is typically used for reporting/analytics but source systems continue operating and updating their own local copies independently — the consolidated store is not (yet) the system those source systems write back to.
- **Advantages:** Produces an actual, physical, queryable golden record; supports enterprise reporting and analytics needs well; less organizationally disruptive than centralizing operational write authority, since source systems keep their normal write patterns.
- **Challenges:** The golden record can drift out of sync with source systems between consolidation cycles, since it's typically built via periodic batch extraction rather than continuously synchronized in real time; doesn't solve the root problem of source systems still independently creating and diverging on new records.
- **When to use:** When the primary driver is trustworthy, unified reporting/analytics (e.g., an accurate enterprise customer count) rather than needing operational systems to transact against the golden record directly.

**Coexistence Style**
- **Description:** Similar to Consolidation — a centralized golden record is built and maintained — but here it actively synchronizes *back* to source systems, so local systems' data is kept updated in near-real time (or on a defined cadence) to reflect changes made to the golden record elsewhere. Source systems retain some local autonomy but participate in bidirectional synchronization rather than being purely read from.
- **Advantages:** Improves consistency across source systems over time without requiring them to fully give up local operational control; a practical middle ground between Registry's minimal intervention and Centralized's full control.
- **Challenges:** Bidirectional synchronization is technically complex — conflict handling (what happens if a source system and the golden record are updated simultaneously) must be explicitly designed; still leaves multiple physical copies of the same entity in existence, which is itself an ongoing consistency risk.
- **When to use:** When both operational systems and enterprise reporting need reasonably consistent data, but a full "rip and replace" of source systems' operational data ownership isn't feasible or desired.

**Centralized Style**
- **Description:** Also called a transaction hub — the golden record becomes the **single system of record**, and source/consuming applications read and write directly against the central master data hub rather than maintaining their own local master copies at all.
- **Advantages:** The strongest consistency guarantee of the four styles — there's structurally only one place the authoritative data lives, eliminating the synchronization-lag and conflict problems the other three styles must manage; new source systems onboard against one clear integration point rather than a web of peer synchronization.
- **Challenges:** The most organizationally and technically disruptive style — requires source applications to be re-architected to depend on the central hub, which is a major undertaking for legacy systems; the hub becomes a critical single point of failure/bottleneck if not architected for the availability and latency needs of every dependent system.
- **When to use:** For organizations with the maturity, executive sponsorship, and technical runway to fully re-architect around a central master data platform — typically a later-stage MDM maturity outcome rather than a realistic starting point.

**Progression note [Industry Practice]:** Organizations commonly progress from Registry → Consolidation/Coexistence → Centralized as MDM maturity and organizational buy-in grow, rather than starting with a Centralized implementation — DMBOK2 doesn't mandate this progression, but it's the practical pattern most MDM programs follow given the disruption cost of the more centralized styles.

### Relationships With Other DAMA Knowledge Areas

**Data Governance:** Reference and Master Data is one of the clearest illustrations of Governance's role, because MDM *cannot* function as a purely technical initiative. The Data Owner (see `data_governance.md`) for a master entity domain (e.g., "Customer Data Owner") makes the accountable calls that MDM depends on: which source system is authoritative for which attribute (feeding Survivorship Rules), how matching conflicts get escalated, and what the entity's governed definition even is. Data Stewards translate that authority into concrete matching and survivorship rules. Without this governance layer, an MDM *tool* can be deployed, but there's no one accountable for the business decisions the tool's matching/merge logic actually depends on — a direct parallel to the "buying a tool isn't governance" lesson from `data_governance.md`, Section 7.

**Data Quality:** Master Data Management and Data Quality Management are tightly linked but distinct: MDM's matching/merging process directly addresses the **Uniqueness** dimension (see `data_quality.md`) at its structural root, rather than leaving downstream teams to independently detect and manage the same duplicates repeatedly. Poor source-data **Accuracy** and **Completeness** going into the matching process degrade match quality (garbage attributes make it harder to confidently determine two records represent the same entity), so MDM is *downstream* of basic data quality discipline, not a substitute for it. Conversely, a well-run MDM program becomes a quality *enabler* for every consuming system, since they inherit a pre-deduplicated, reconciled entity rather than needing to solve uniqueness themselves.

**Metadata Management:** Both Reference and Master Data depend heavily on Metadata Management (see `metadata_management.md`) to function: Business Metadata provides the governed definition of what a "Customer" or a "Country Code" means; Technical Metadata documents each source system's schema so matching logic knows what it's comparing; and Lineage is what lets someone trace a suspicious golden-record value back to which source system and survivorship rule produced it. A Business Glossary entry for "Active Customer" and an MDM golden record are complementary artifacts answering related but distinct questions: the glossary defines the *concept*; the golden record is the *authoritative instance data* for it. **Despite the near-identical names, Master Data Management and Metadata Management are distinct disciplines** — MDM manages authoritative entity/instance data, Metadata Management manages data *about* data (see Section 9, Exam Traps, for this common point of confusion).

**Data Architecture:** Master and Reference Data domains are a natural fit for the **Data Domain** concept from `data_architecture.md` — architecture decides domain boundaries (what counts as "Customer" vs. "Contact" as separate or combined domains) and which MDM implementation style (above) fits the organization's integration architecture. The choice between Registry, Consolidation, Coexistence, and Centralized styles is fundamentally a **Physical Data Architecture** decision, informed by the Logical Data Architecture's data flow requirements (does the golden record need to be queried live, or is periodic batch synchronization sufficient?).

**Data Modeling:** A Master Data entity needs the same conceptual → logical → physical modeling discipline as any other entity (see `data_modeling_and_design.md`) — but with extra weight given how many systems depend on getting the model right, since a structural mistake in a widely-shared Customer or Product model propagates its cost across every consuming system rather than staying contained to one. Reference Data code sets are frequently modeled as small, well-normalized lookup tables at the physical level, with foreign-key relationships from every table that uses that classification — a direct, everyday application of the Primary Key/Foreign Key relationship pattern from `data_modeling_and_design.md`, Section 3. The **Party/Person/Organization** generalization pattern (above) is the clearest single link between the two Knowledge Areas.

### Roles in Reference and Master Data Management

| Role | Reference & Master Data Responsibility |
|---|---|
| **Data Owner** | Accountable for the business definition of a master entity domain (e.g., "what is a Customer") and for approving source-priority/survivorship rules; the escalation point for unresolved matching conflicts with real business consequences. |
| **Data Steward** | Defines and maintains concrete matching rules, survivorship logic, and reference data code sets on the Owner's behalf; reviews ambiguous or low-confidence matches that automated rules can't resolve; maintains the accuracy of hierarchies. |
| **Data Engineer** | Builds and operates the matching/merge/survivorship pipeline and the distribution mechanism to consuming systems (Custodian role); surfaces match-quality metrics and flags ambiguous cases for Steward review; does not unilaterally decide business-level matching or survivorship logic. |
| **Data Architect** | Decides which MDM implementation style fits the organization's integration architecture and maturity; defines Data Domain boundaries (see `data_architecture.md`) that Master Data entities map onto; plans how the golden record is distributed across the broader data architecture. |
| **Application teams (source system owners)** | Own the day-to-day data entry and local operational use of their system's records; in more centralized MDM styles (Coexistence, Centralized), must adapt their applications to read/write against the golden record rather than maintaining fully independent local copies — often the primary source of organizational resistance to MDM maturity. |

---

## 5. Data Engineer Perspective

**ETL/ELT pipelines:** Building the matching, merging, and survivorship logic that produces a golden record is often literally a data engineering pipeline — but the *rules* the pipeline encodes (which source wins, what similarity threshold counts as a match) must trace back to Steward/Owner-approved business decisions, exactly as with quality rules in `data_quality.md`. An engineer should not be silently deciding, for example, that "the CRM always wins" without that being an approved survivorship rule.

**Data integration:** MDM is inherently an integration-heavy discipline — pulling candidate records from multiple source systems, applying matching logic, and distributing the resulting golden record back out. The choice of integration pattern (batch extraction for a Consolidation-style implementation vs. near-real-time event-driven sync for Coexistence) is exactly the kind of decision `data_architecture.md` frames as an architecture-level integration-pattern choice, not a per-pipeline preference.

**Customer 360 solutions:** **[Industry Practice]** "Customer 360" is a common industry term for the practical outcome of Customer Master Data Management — a unified, queryable view of everything the organization knows about a customer across channels. As a Data Engineer, building a Customer 360 pipeline *is* implementing MDM (matching, merging, survivorship) for the Customer domain specifically, whether or not the project is formally labeled "MDM."

**Data warehouses:** Master Data most commonly shows up in a warehouse as **conformed dimensions** (Customer, Product, Location) — the golden record becomes the dimension table's source, ensuring every fact table that joins to "Customer" is joining against the same authoritative entity rather than a locally-reconciled approximation (a direct link to the conformed-dimension concept in `data_governance.md` and dimensional modeling in `data_modeling_and_design.md`).

**Data lakes / lakehouse platforms:** Master and Reference Data are natural candidates for a **trusted/gold zone** dataset (see the zone pattern in `data_governance.md`) — raw customer records from many source systems land in lower zones, and the matched/merged golden record is what gets promoted to the trusted zone for broad consumption, since it's specifically been through the governance and quality process that zone implies.

**APIs:** A **Registry** or **Centralized** MDM implementation is typically exposed to consuming applications via an API (a "get golden Customer record by ID" service) rather than direct database access — this is the same API-vs-direct-access architectural pattern discussed in `data_architecture.md`, applied specifically to master data distribution.

**CDC (Change Data Capture) pipelines:** CDC is a common mechanism for keeping a **Coexistence**-style MDM implementation synchronized — capturing changes in source systems in near-real time and propagating them into the matching/merge process, and propagating resulting golden-record updates back out, rather than relying on slower, less current batch reconciliation.

**Data synchronization:** Whichever MDM style is chosen, someone has to solve "how does an update to the golden record reach every consuming system, and how are conflicting simultaneous updates handled" — a genuinely hard distributed-systems problem that's easy to underestimate when an MDM initiative is scoped as "just matching and merging."

**Dimensional modeling:** As noted above, Master Data entities become dimension tables; Reference Data code sets frequently become small, well-governed lookup/reference dimensions — the direct technical destination for both disciplines' output in an analytics context.

**How a Data Engineer contributes without owning business decisions:** The Data Engineer's role in MDM mirrors the Custodian role from `data_governance.md` — building and operating the matching/merge/survivorship pipeline, surfacing match-quality metrics and ambiguous cases for Steward review, and implementing the distribution mechanism to consuming systems. The Data Engineer should **not** unilaterally decide what counts as a duplicate, which source system is authoritative for a given attribute, or what a "Customer" even means in the first place — those are Owner/Steward decisions the engineer implements, escalates ambiguous cases into, and should never quietly default on.

---

## 6. Enterprise Examples

*(Illustrative composite scenarios; named external standards/regulations are real.)*

### Government: Citizen Master Data Platform

**Problem:** A government agency serving citizens across tax, health, and benefits programs has each agency maintaining its own citizen record, with no reliable way to confirm "this tax filer and this benefit recipient are the same person" — leading to both fraud risk (undetected duplicate claims under slightly different name spellings) and service failure (a citizen denied a benefit because their case history is split across unmatched records).

**Master/reference data involved:** Citizen (Master Data — name, date of birth, national ID, address); Case Status, Benefit Type, Program Eligibility Category (Reference Data — controlled classification codes shared across agencies).

**Governance approach:** A cross-agency governance council (echoing `data_governance.md`'s government example) must agree on a shared Citizen definition and a national identifier as the primary matching key, with clear source-priority rules for conflicting demographic data across agencies.

**Technical implementation:** Given the political and technical difficulty of forcing every agency onto one operational system, a **Registry**-style implementation is a realistic starting point — a cross-reference layer confirming "these records across agencies are the same citizen" without requiring any agency to give up its own system, potentially maturing toward Coexistence as trust and integration capability grow.

### Banking: Customer Master and Regulatory Reporting

**Problem:** A bank's retail banking, lending, and wealth management divisions each maintain separate customer records; regulators require a single, defensible view of total exposure per customer (and per corporate customer group, via hierarchy) for risk reporting.

**Master/reference data involved:** Customer/Counterparty (Master Data, including a Customer Hierarchy for corporate parent/subsidiary relationships — Section 4); Currency Code, Country Code, Risk Rating Category (Reference Data, several drawn from real external standards like ISO 4217 for currency).

**Governance approach:** Directly serves the BCBS 239 requirement (introduced in `data_governance.md`) for demonstrable, traceable risk-data aggregation — a Customer Data Owner accountable for the golden Customer definition, with Stewards defining survivorship rules prioritizing the system of record for legally significant attributes (e.g., legal entity name from the core banking system over a marketing-sourced nickname).

**Technical implementation:** Given the regulatory stakes, banks commonly invest in **Consolidation** or **Coexistence**-style MDM specifically for the Customer/Counterparty domain, feeding both a physically consolidated golden record for regulatory reporting and synchronized updates back to operational systems.

### Healthcare: Patient Identity Management

**Problem:** A hospital network's billing, clinical (EHR), and scheduling systems each maintain their own patient record; without reliable matching, a patient's care history can be split across unmatched records — a genuine patient-safety risk, not just a reporting inconvenience.

**Master/reference data involved:** Patient (Master Data, matched via a **Master Patient Index**, or MPI — introduced in `data_governance.md`); Encounter Type, Diagnosis Code Classification (Reference Data, frequently drawn from real external standards like ICD-10).

**Governance approach:** A Patient Data Owner role (often clinical leadership, per `data_governance.md`'s healthcare example) approves matching confidence thresholds — critically, false-positive matches (incorrectly merging two different patients) are a direct clinical safety risk, so survivorship and matching rules here are typically far more conservative than in, say, marketing use cases.

**Technical implementation:** MPI systems are frequently implemented in a **Coexistence** or **Centralized** style precisely because clinical staff need to query and act on an up-to-date, trustworthy patient identity at the point of care — a stale Registry-style cross-reference isn't sufficient when a clinician needs to know *right now* whether they're looking at the complete patient history.

### Retail: Product Master and Customer Master

**Problem:** An omnichannel retailer (recurring from `data_architecture.md`) has separate product catalogs for its online store, in-store POS, and supplier/procurement systems, plus separate customer records across online, in-store, and loyalty channels — undermining both consistent product information for customers and a unified view of customer behavior for marketing/personalization.

**Master/reference data involved:** Product (Master Data, with a Product Hierarchy — category → subcategory → SKU); Customer (Master Data, matched across channels — a direct "Customer 360" use case); Product Category, Unit of Measure (Reference Data).

**Governance approach:** Separate Data Owners for Product (often merchandising) and Customer (often marketing/CRM) domains, each with their own Stewards defining domain-specific survivorship rules — e.g., pricing data sourced authoritatively from the pricing system regardless of what a stale POS cache shows.

**Technical implementation:** Retailers commonly start with a **Consolidation**-style golden Customer record feeding analytics/personalization, while moving toward **Coexistence** for Product data so that a price or description change propagates back out to all channels rather than only existing in a reporting copy.

---

## 7. Common Mistakes

1. **Confusing Reference Data with Master Data.** Treating a controlled classification value set (Reference Data) and a shared business entity (Master Data) as the same kind of problem leads to applying the wrong management approach — e.g., trying to run full matching/merging/survivorship logic on a small, largely static code list, which is unnecessary overhead, or conversely treating Customer data as "just another lookup table" and under-investing in the matching discipline it actually needs.
2. **Treating MDM as only a software tool.** **[Industry Practice observation]** Purchasing an MDM platform and expecting it to resolve organizational disagreement about what "Customer" means, or which source system is authoritative, mistakes the tool for the governance decisions it depends on — directly mirroring the same tool-vs-discipline mistake covered in `data_governance.md` and `metadata_management.md`.
3. **No business ownership.** Without an accountable Data Owner, there's no one to approve survivorship rules, resolve matching disputes, or be answerable when a bad golden-record decision causes real business harm (e.g., a healthcare false-positive match) — the same accountability gap pattern seen across every Knowledge Area so far.
4. **Poor matching rules.** Overly loose matching thresholds create false-positive merges (two different real people incorrectly combined); overly strict thresholds leave duplicates undetected — and matching rules set once and never revisited tend to drift out of tune as source data patterns change over time.
5. **Ignoring data quality.** Feeding poor-quality source data (inconsistent formatting, missing key attributes) directly into matching logic degrades match confidence — MDM cannot compensate for source data quality it was never given the inputs to work with; it can only get systematically worse decisions from worse inputs.
6. **Creating multiple conflicting "sources of truth."** Multiple teams independently building their own "authoritative" customer or product list — often because no single, trusted, accessible golden record existed yet — recreates the exact fragmentation problem MDM exists to solve, just with more infrastructure built around each fragment.
7. **Solving symptoms instead of root causes.** Repeatedly, manually de-duplicating the same recurring set of records rather than fixing the upstream process (e.g., a poorly-designed intake form with no duplicate-check) that keeps creating new duplicates — the MDM-specific instance of the root-cause discipline covered generally in `data_quality.md`, Section 4.

---

## 8. CDMP Exam Focus

### High-value concepts
- **The Reference Data vs. Master Data distinction** (Section 3) — precisely, with the ability to correctly classify a described example, not just recite the definitions.
- **The four MDM implementation styles** (Registry, Consolidation, Coexistence, Centralized) — know their descriptions, tradeoffs, and which is appropriate for a given scenario.
- **Golden Record and Survivorship Rules** — how a golden record is produced from conflicting source data, and that survivorship logic is a governed business decision, not a technical default.
- **Single Source of Truth as a governance/authority concept**, distinct from physical data consolidation — this distinction is frequently tested indirectly through Registry-style scenario questions.
- **Matching and Merging (identity resolution)** as the technical core of MDM, and its inherent tradeoff between false positives and false negatives.

### Important definitions
- Master Data, Reference Data, Master Data Management (MDM), Reference Data Management (RDM), Golden Record, Survivorship Rules, Matching/Merging, Value Domain, Data Sharing Agreement — precise, independent definitions.
- Registry / Consolidation / Coexistence / Centralized MDM styles; Master Data Types (Party, Product, Financial, Location); Hierarchy (organizational, product, customer).

### Frequently confused concepts
- **Reference Data vs. Master Data** — a controlled classification *value* vs. a unique real-world business *entity*; the single most commonly tested distinction in this Knowledge Area.
- **Matching vs. Merging vs. Survivorship** — matching identifies likely-duplicate candidates; merging (record consolidation) combines them; survivorship rules decide which attribute values win — three distinct steps often conflated as one.
- **Single Source of Truth vs. single physical database** — an authority/governance concept, not an implementation requirement; a Registry-style MDM implementation achieves the former without the latter.
- **Master Data Management (MDM) vs. Metadata Management** — despite near-identical names, MDM manages authoritative *instance/entity data*; Metadata Management manages *data about data* (schemas, definitions, lineage). See Section 9 for this trap in detail.
- **MDM implementation styles** — Registry vs. Consolidation vs. Coexistence vs. Centralized are frequently tested by scenario ("which style does this description match"), not by name recall alone.

---

## 9. Exam Traps

- **A scenario describes correctly-formatted, low-complexity data (like a status code) and implies it's therefore unimportant or ungoverned.** Reference Data's low complexity is not the same as low impact — an uncontrolled, duplicate, or inconsistently-applied code value can silently break every downstream system relying on the standard set. Don't mistake simplicity for low stakes.
- **A question treats "Reference Data" and "lookup table" as automatically synonymous.** Many technical lookup tables are indeed Reference Data implementations, but the DAMA concept is the *governance and standardization discipline*, not merely the physical table pattern — a badly-governed lookup table with inconsistent, unowned values is a technical implementation of Reference Data without actually being *managed* Reference Data.
- **A question assumes Master Data always means "big" or "complex" data.** The defining trait isn't size or complexity — it's that the data represents a *shared core business entity* multiple systems and processes depend on referencing consistently. A large, complex dataset used by only one system in isolation isn't Master Data in DAMA's sense.
- **A question implies "Single Source of Truth" requires one physical database.** As established in Section 4, Single Source of Truth is a governance/authority concept — a Registry-style MDM implementation is a direct counterexample, since it achieves a single source of truth without physically consolidating any data. An answer requiring physical consolidation by definition is incorrect.
- **A question (or a candidate's own assumption) treats "Master Data Management" and "Metadata Management" as interchangeable, or confuses one for the other because of how similar the names sound.** They are distinct Knowledge Areas: MDM manages the authoritative *instance data* for shared entities (a Customer's actual attributes); Metadata Management manages *data about data* (schemas, definitions, lineage — see `metadata_management.md`). A golden Customer record is Master Data; the catalog entry describing what a "Customer" field means is Metadata. Don't let vocabulary similarity substitute for checking which discipline a scenario actually describes.
- **A question implies more centralized MDM styles are always "better."** DMBOK2 presents the four styles as tradeoffs suited to different organizational contexts and maturity levels, not a strict quality ladder where Centralized is unconditionally the right answer (see the same anti-pattern applied to governance operating models in `data_governance.md`, Section 9).
- **A question treats Reference Data governance and Master Data governance as needing identical weight/investment.** Reference Data's governance is real but typically lighter-weight (a smaller, more static value set) than the ongoing matching/merging/survivorship discipline Master Data requires.
- **A question treats deduplication (Data Quality's Uniqueness dimension) as synonymous with MDM.** Deduplication is a necessary *component* of MDM, but MDM is the broader discipline including survivorship, distribution, and governance — not simply a synonym for "removing duplicates."

---

## 10. Interview Questions

### Data Engineer level
1. **"How would you detect that two customer records from different systems likely represent the same person?"**
   *Strong answer covers:* deterministic matching on strong identifiers (email, national ID) where available, probabilistic/fuzzy matching (name + address similarity scoring) where not, and acknowledges the false-positive/false-negative tradeoff rather than presenting matching as a solved, binary problem.
2. **"What's the difference between how you'd handle a Reference Data table (like country codes) versus a Master Data entity (like Customer) in a pipeline?"**
   *Strong answer covers:* Reference Data as a small, versioned, infrequently-changing lookup table enforced via foreign-key/referential integrity; Master Data as requiring an ongoing matching/merge/survivorship process, not a static lookup.
3. **"How would you build a pipeline that keeps a golden Customer record synchronized with multiple source systems?"**
   *Strong answer covers:* choosing an appropriate synchronization pattern (batch consolidation vs. CDC-based near-real-time sync) tied to actual business latency requirements, not defaulting to real-time without justification.

### Senior Data Engineer level
4. **"A false-positive customer match incorrectly merged two different people's purchase histories. How do you prevent this class of bug from recurring?"**
   *Signal:* proposes tightening/reviewing matching confidence thresholds with Steward input, adding a human-review step for low-confidence matches, and treats this as a governed-rule tuning problem, not just a code bug to patch silently.
5. **"How would you design survivorship logic so business rule changes don't require an engineering deploy every time?"**
   *Signal:* externalizes survivorship rules (source priority, recency, completeness logic) into a Steward-editable configuration rather than hardcoding them into pipeline code — directly mirroring the data-quality-rule externalization pattern from `data_quality.md`.
6. **"How do you decide whether to implement MDM as a Registry, Consolidation, or Coexistence style for a given organization?"**
   *Signal:* frames the decision around organizational readiness, whether consumers need a physically consolidated record vs. just cross-reference confirmation, and latency/synchronization requirements — not a default preference for the most sophisticated option.

### Data Architect level
7. **"How would you define Master Data domain boundaries for a newly merged organization with overlapping customer and product systems?"**
   *Signal:* starts from business capability and entity definition (echoing the Data Architecture domain-definition question from `data_architecture.md`), and has a process for resolving domain overlap through governance escalation rather than a unilateral technical call.
8. **"How would you evaluate moving an organization from a Registry-style MDM implementation toward a Centralized model?"**
   *Signal:* weighs the disruption cost to source applications against the consistency benefit, and frames this as a maturity progression justified by business need — not change for its own sake.
9. **"How do you architect golden-record distribution so dozens of consuming systems stay reasonably in sync without building a fragile web of point-to-point integrations?"**
   *Signal:* proposes a hub-style distribution pattern (API or event-driven) consistent with the integration-architecture principles in `data_architecture.md`, avoiding the "spaghetti architecture" failure mode described there.

---

## 11. Practical Exercises

### Exercise 1: Design a Customer Master Solution

**Scenario:** A company has Customer records fragmented across a CRM, an e-commerce platform, and a support ticketing system, with no shared identifier.

**Task:** Propose (a) which MDM implementation style (Section 4) you'd start with and why; (b) what attributes would be used for matching, and whether deterministic or probabilistic matching (or both) is appropriate for each; (c) who should be the accountable Data Owner and why; (d) how the golden record would be distributed back to the three source systems.

**Expected solution approach:** A Registry or Consolidation start (lower disruption, given no existing shared identifier or prior MDM maturity) is more defensible than jumping straight to Centralized. Matching should combine a strong deterministic identifier where available (e.g., verified email) with probabilistic fallback (name + address) for records lacking it — and should explicitly acknowledge that some records will remain ambiguous and require Steward review rather than fully automated resolution. The Data Owner should be a business-side role tied to customer relationship accountability (e.g., a CRM/marketing leader), not IT/Engineering by default. Distribution should be justified against actual consumer needs (e.g., an API for on-demand lookups vs. batch sync for reporting), not assumed to require real-time sync everywhere.

### Exercise 2: Define Survivorship Rules for Conflicting Customer Records

**Scenario:** Three matched source records disagree: the CRM shows "Jonathan Smith," the e-commerce platform shows "Jon Smith," and the support system shows "J. Smith" for what has been confirmed to be the same person. Similarly, phone numbers differ across all three, with the e-commerce platform's being the most recently updated.

**Task:** Propose concrete survivorship rules for the Name and Phone Number attributes, specifying source priority, recency, or another rule for each, and justify each choice.

**Expected solution approach:** For Name, a source-priority rule is likely more defensible than pure recency — e.g., the CRM (often the system where sales/account teams maintain a verified legal or preferred name) might be designated authoritative, rather than assuming whichever system was updated last has the correct value. For Phone Number, a recency-based rule may be more appropriate, since contact information genuinely does change over time and the most recently confirmed value is often the most likely to be current — but this should still be a Steward-approved default, with a fallback to source priority if recency data is unreliable or missing. The key deliverable is not a single "correct" answer but demonstrating that each rule choice is justified by the attribute's actual behavior (identity attributes vs. contact attributes behave differently) rather than applying one blanket rule to every field.

### Exercise 3: Design Governance for Reference Data Values

**Scenario:** Multiple teams have started independently adding new "Order Status" values (e.g., one team added "Pending Review," another added "Awaiting Approval" for what is functionally the same status) without any central coordination.

**Task:** Propose a governance process that prevents uncontrolled growth of the Order Status code set going forward, including who approves new values and how existing near-duplicate values would be consolidated.

**Expected solution approach:** Assign a Data Steward accountable for the Order Status reference data domain, with a lightweight but mandatory approval process for any new code value (a new value cannot go live in any consuming system until reviewed and approved, preventing the ad hoc proliferation described in the scenario). Existing near-duplicates ("Pending Review" / "Awaiting Approval") should be consolidated into one canonical value with the other formally deprecated, following a governed change process that accounts for updating all downstream consumers rather than silently breaking systems still expecting the deprecated value. The solution should explicitly note that this governance overhead is proportionally lighter than Master Data governance (see Section 9, Exam Traps, on the risk of treating them as equally heavy), since Reference Data code sets are smaller and slower-changing by nature.

---

## 12. Flashcards

| Term | Definition |
|---|---|
| Reference Data | A controlled, standardized set of permissible values used to classify or categorize other data. |
| Master Data | The authoritative, agreed representation of an organization's core shared business entities. |
| Master Data Management (MDM) | The discipline of creating and maintaining a consistent, authoritative representation of core shared business entities. |
| Reference Data Management (RDM) | The discipline of defining and maintaining controlled value/code sets used consistently across the organization. |
| Golden Record | The single, agreed, authoritative version of a master data entity's attributes, produced via matching and survivorship. |
| Single Source of Truth | The governed, trusted authoritative source for an entity or fact — an authority concept, not necessarily a single physical database. |
| Matching | The process of identifying candidate records that likely represent the same real-world entity. |
| Identity Resolution | The broader outcome of confirming multiple records across systems represent the same real-world entity. |
| Record Consolidation | Combining matched records into a single golden record. |
| Survivorship Rules | Governed business rules determining which attribute value "wins" when matched source records disagree. |
| Source Priority | A survivorship approach ranking source systems by trustworthiness for a given attribute. |
| Registry Style (MDM) | An MDM implementation storing only cross-reference keys; the golden view is computed virtually from source systems. |
| Consolidation Style (MDM) | An MDM implementation physically extracting and merging master data into a centralized store, typically for reporting. |
| Coexistence Style (MDM) | An MDM implementation with a centralized golden record that synchronizes bidirectionally with source systems. |
| Centralized Style (MDM) | An MDM implementation where the golden record is the single system of record that applications read/write directly. |
| Data Domain | A logical grouping of data by subject area, used to scope Master Data entities and architecture/ownership (cross-referenced from Data Architecture). |
| Hierarchy (Master Data) | A structured, often multi-level relationship between master entities (organizational, product, or customer hierarchies). |
| Customer 360 | Industry-practice term for a unified, cross-channel customer view — the practical outcome of Customer MDM. |
| False Positive (matching) | An incorrect match that merges two different real-world entities into one golden record. |
| False Negative (matching) | A failure to match records that actually represent the same real-world entity, leaving duplicates unresolved. |
| Value Domain | The bounded, permitted set of values a Reference Data code set defines. |
| Master Data Types (Party/Product/Financial/Location) | Common categorization of Master Data by entity type; "Party" unifies Person/Organization via generalization/subtyping. |
| Data Sharing Agreement | A governance artifact documenting the terms (freshness, quality, usage) under which shared master/reference data is distributed to consumers. |
| MDM Success Metrics | Measures (e.g., match rate, duplicate reduction, golden record adoption) used to demonstrate an MDM program's ongoing business value. |

---

## 13. Quiz Questions

1. **A company maintains a controlled list of "Order Status" values (Pending, Shipped, Delivered, Cancelled) used across all its systems. What kind of data is this?**
   a) Master Data b) Reference Data c) Metadata d) Transactional Data

   **Correct answer:** b) Reference Data.
   **Explanation:** A controlled, standardized set of permitted classification values is the defining characteristic of Reference Data — it doesn't represent a unique real-world entity, it classifies other data.
   **Why the others are wrong:** (a) Master Data represents a unique shared business entity (like Customer), not a value list; (c) Metadata describes data's structure/meaning, but this is the actual controlled value set itself, not data *about* it; (d) Transactional Data records business events/activity, not classification values.
   **Related Knowledge Area:** Reference and Master Data (this module, Section 3).

2. **A retailer wants a single, trusted view of "Customer" across its online, in-store, and loyalty systems. This is primarily a:**
   a) Reference Data Management problem b) Data Architecture problem only c) Master Data Management problem d) Data Warehousing problem

   **Correct answer:** c) Master Data Management problem.
   **Explanation:** Unifying a shared core business entity (Customer) across multiple systems into one authoritative representation is the definition of MDM's purpose.
   **Why the others are wrong:** (a) Reference Data concerns controlled classification values, not core entity unification; (b) Data Architecture would inform the *implementation style* but the core problem being solved is MDM; (d) Data Warehousing is a potential *consumer* of the resulting golden record, not the discipline that produces it.
   **Related Knowledge Area:** Reference and Master Data (this module, Section 4).

3. **An MDM implementation stores only cross-reference keys and computes the "golden view" on demand from data still physically located in source systems. This is the:**
   a) Centralized style b) Consolidation style c) Coexistence style d) Registry style

   **Correct answer:** d) Registry style.
   **Explanation:** The Registry style is defined by its minimal footprint — it doesn't physically consolidate data, only maintains the cross-references needed to compute a virtual golden view.
   **Why the others are wrong:** (a) Centralized physically hosts the golden record as the single system of record; (b) Consolidation physically extracts and merges data into a centralized store; (c) Coexistence also physically maintains a centralized golden record, with bidirectional sync back to sources.
   **Related Knowledge Area:** Reference and Master Data (this module, Section 4).

4. **Two matched customer records disagree on "Legal Name." The organization has decided the core banking system is always authoritative for this attribute. This is an example of:**
   a) Data Profiling b) A survivorship rule based on source priority c) Reference Data classification d) A false positive match

   **Correct answer:** b) A survivorship rule based on source priority.
   **Explanation:** Designating one source system as authoritative for a given attribute when records conflict is precisely the source-priority approach to survivorship.
   **Why the others are wrong:** (a) Data Profiling is a diagnostic activity from Data Quality, not a conflict-resolution rule; (c) Reference Data classification concerns controlled value sets, not resolving conflicting master data attributes; (d) A false positive is an incorrect *match* between different entities, not a rule for resolving an attribute conflict on an already-confirmed match.
   **Related Knowledge Area:** Reference and Master Data (this module, Section 4).

5. **A "Single Source of Truth" for Customer data necessarily requires that all customer data physically reside in one database.**
   a) True — by definition it must be one physical database b) False — it describes governed authority, and can be implemented as a virtual/computed view c) True, but only in Centralized MDM implementations d) False — the concept doesn't apply to Master Data at all

   **Correct answer:** b) False — it describes governed authority, and can be implemented as a virtual/computed view.
   **Explanation:** Single Source of Truth is a governance/authority concept about which data is *trusted*, not a mandate about physical storage — a Registry-style implementation demonstrates this directly.
   **Why the others are wrong:** (a) and (c) both incorrectly assume physical consolidation is required — Registry-style MDM is a direct counterexample; (d) is wrong because Single Source of Truth is a core concept specifically discussed in the context of Master Data.
   **Related Knowledge Area:** Reference and Master Data (this module, Section 4).

6. **A hospital's MDM program sets an unusually conservative (strict) matching threshold for patient records. What tradeoff does this reflect?**
   a) Prioritizing fewer false positives (incorrect merges) at the cost of more false negatives (missed duplicates) b) Prioritizing fewer false negatives at the cost of more false positives c) Eliminating both false positives and false negatives entirely d) No tradeoff exists in matching logic

   **Correct answer:** a) Prioritizing fewer false positives (incorrect merges) at the cost of more false negatives (missed duplicates).
   **Explanation:** A stricter matching threshold requires more confidence before merging, reducing the risk of incorrectly combining two different patients (a serious clinical safety risk) at the cost of leaving more genuine duplicates unmerged.
   **Why the others are wrong:** (b) describes the opposite tradeoff (a looser threshold); (c) is incorrect — matching inherently involves an unavoidable tradeoff between the two error types, not a way to eliminate both; (d) is incorrect — the false-positive/false-negative tradeoff is a fundamental characteristic of matching/identity resolution.
   **Related Knowledge Area:** Reference and Master Data (this module, Section 4).

7. **A "Product Category" hierarchy (Category → Subcategory → SKU) used to support consistent sales roll-up reporting is an example of:**
   a) Reference Data only b) Master Data hierarchy management c) Data Lineage d) A survivorship rule

   **Correct answer:** b) Master Data hierarchy management.
   **Explanation:** Product hierarchies structure relationships between master data entities (Product/SKU) and must themselves be governed and kept current, as described in Section 4's Hierarchies concept.
   **Why the others are wrong:** (a) is a partial trap — while category values may function as Reference Data classification, the *hierarchy relationship itself*, tied to master Product entities, is a Master Data hierarchy concern; (c) Data Lineage traces data's origin and transformation history, unrelated to structuring category relationships; (d) Survivorship rules resolve conflicting attribute values, not hierarchy structure.
   **Related Knowledge Area:** Reference and Master Data (this module, Section 4).

8. **Who should typically be accountable for approving survivorship rules for the Customer Master domain?**
   a) The Data Engineer building the pipeline b) The Data Owner for the Customer domain c) The MDM software vendor d) Whichever system was implemented first

   **Correct answer:** b) The Data Owner for the Customer domain.
   **Explanation:** Survivorship rules encode business judgments about source trustworthiness — an accountability decision that belongs to the business-side Data Owner, consistent with the Owner/Custodian boundary established in Data Governance.
   **Why the others are wrong:** (a) The Data Engineer implements approved rules but should not unilaterally decide business-level survivorship logic; (c) A vendor's tool provides mechanism, not the accountable business decision; (d) Implementation order has no bearing on data authority or accountability.
   **Related Knowledge Area:** Reference and Master Data (this module, Section 4); relates to Data Governance.

9. **A bank must demonstrate a consolidated, traceable view of total customer exposure across retail, lending, and wealth divisions for a regulator. This most directly relies on:**
   a) Reference Data Management alone b) A well-governed Customer Master (including hierarchy) and its lineage c) Data Architecture without any MDM component d) A Registry-style implementation exclusively

   **Correct answer:** b) A well-governed Customer Master (including hierarchy) and its lineage.
   **Explanation:** Consolidated, defensible exposure reporting requires an authoritative Customer/Counterparty master entity (including hierarchy for related accounts) and traceable lineage back to source systems — directly serving BCBS 239-style regulatory requirements.
   **Why the others are wrong:** (a) Reference Data classification alone can't unify a fragmented customer view; (c) Data Architecture informs the implementation but doesn't itself produce the consolidated, traceable customer view; (d) A Registry style is one possible implementation choice, not a requirement — other styles (Consolidation/Coexistence) may better suit regulatory reporting depending on organizational needs.
   **Related Knowledge Area:** Reference and Master Data (this module, Section 6); relates to Data Governance (BCBS 239).

10. **A team decides "since Reference Data is just simple code values, it doesn't need any governance." What is the risk in this reasoning?**
    a) There is no risk — Reference Data genuinely needs no governance b) Uncontrolled, duplicate, or inconsistent code values can silently break every downstream system relying on the standard set, despite low individual complexity c) Reference Data automatically self-governs through database constraints d) This reasoning is correct as long as the values are stored in a lookup table

    **Correct answer:** b) Uncontrolled, duplicate, or inconsistent code values can silently break every downstream system relying on the standard set, despite low individual complexity.
    **Explanation:** Reference Data's low complexity is not the same as low impact — an ungoverned, inconsistently-applied code value corrupts every downstream aggregation or join relying on that controlled set, exactly the exam-trap pattern noted in Section 9.
    **Why the others are wrong:** (a) and (d) both underestimate the real governance need, mistaking simplicity for unimportance; (c) is incorrect — a database constraint (like a foreign key) can enforce that a value exists in a lookup table, but cannot on its own guarantee the lookup table's values are correctly defined, non-duplicative, or consistently used across systems in the first place.
    **Related Knowledge Area:** Reference and Master Data (this module, Section 3, Section 9).

11. **The bounded set of permitted values that a Reference Data code set defines (e.g., {Pending, Shipped, Delivered, Cancelled} for Order Status) is precisely termed:**
    a) A Golden Record b) A Value Domain c) A Survivorship Rule d) A Data Sharing Agreement

    **Correct answer:** b) A Value Domain.
    **Explanation:** Value Domain is the precise DAMA-adjacent term for a Reference Data code set's bounded, permitted values.
    **Why the others are wrong:** (a) A Golden Record is a Master Data concept — the authoritative merged entity record — unrelated to a code set's value boundaries; (c) A Survivorship Rule resolves conflicting attribute values during matching, not a value boundary; (d) A Data Sharing Agreement governs distribution terms, not the value set itself.
    **Related Knowledge Area:** Reference and Master Data (this module, Section 4).

12. **An organization models "Party" as a supertype with "Person" and "Organization" subtypes to represent both individual and corporate customers under one Master Data structure. This modeling technique is called:**
    a) Survivorship b) Generalization/Subtyping c) Record consolidation d) Value Domain

    **Correct answer:** b) Generalization/Subtyping.
    **Explanation:** Modeling a general entity with specialized subtypes sharing common attributes is Generalization/Subtyping, introduced in `data_modeling_and_design.md` and directly applicable to Master Data's common Party entity type.
    **Why the others are wrong:** (a) Survivorship resolves conflicting attribute values, unrelated to entity typing; (c) Record consolidation combines matched records into a golden record, not entity-type modeling; (d) Value Domain concerns Reference Data code sets, not entity structure.
    **Related Knowledge Area:** Reference and Master Data (this module, Section 4); relates to Data Modeling and Design.

13. **A new analyst says "Master Data Management and Metadata Management are basically the same thing since they sound alike." What is the correct response?**
    a) They are the same; DAMA uses the names interchangeably b) They are distinct Knowledge Areas: MDM manages authoritative instance/entity data, Metadata Management manages data about data (schemas, definitions, lineage) c) Metadata Management is a subset of MDM d) MDM only exists within Metadata Management's scope

    **Correct answer:** b) They are distinct Knowledge Areas: MDM manages authoritative instance/entity data, Metadata Management manages data about data.
    **Explanation:** Despite the similar names, the two disciplines have entirely different subject matter — MDM's output is authoritative entity data (a golden Customer record); Metadata Management's output is descriptive data about data (schemas, glossary definitions, lineage).
    **Why the others are wrong:** (a) they are never used interchangeably in DAMA framing; (c) and (d) both incorrectly subordinate one Knowledge Area to the other — they are peer, related-but-distinct disciplines.
    **Related Knowledge Area:** Reference and Master Data (this module, Section 9, Exam Traps); relates to Metadata Management.

14. **A team wants to consume the golden Customer record but has no documented understanding of its freshness guarantees or permitted uses. What artifact is missing?**
    a) A Survivorship Rule b) A Value Domain c) A Data Sharing Agreement d) A Business Glossary entry

    **Correct answer:** c) A Data Sharing Agreement.
    **Explanation:** A Data Sharing Agreement is the governance artifact documenting the terms (freshness, quality, usage restrictions) under which shared master/reference data is distributed to consumers.
    **Why the others are wrong:** (a) Survivorship rules resolve attribute conflicts during golden record creation, not distribution terms; (b) Value Domain is a Reference Data concept, unrelated to distribution terms; (d) a Business Glossary entry defines a term's meaning, not distribution terms or usage restrictions.
    **Related Knowledge Area:** Reference and Master Data (this module, Section 4); relates to Data Governance.

15. **Which metric would best demonstrate an MDM program's ongoing value to secure continued executive sponsorship?**
    a) Total lines of matching code written b) Number of Data Owners appointed on paper c) Golden record adoption rate across consuming systems d) Number of source systems that exist

    **Correct answer:** c) Golden record adoption rate across consuming systems.
    **Explanation:** Golden record adoption — how many consuming systems actually use the authoritative record rather than a local copy — is a concrete, business-relevant success measure, directly addressing MDM's diffuse value being easy to underfund without measurable proof of impact.
    **Why the others are wrong:** (a) code volume is an engineering vanity metric with no business meaning; (b) appointing Owners "on paper" without adoption evidence doesn't itself demonstrate value (echoes Common Mistake #3's "naming a steward without real authority" pattern); (d) counting source systems says nothing about whether MDM is actually improving consistency.
    **Related Knowledge Area:** Reference and Master Data (this module, Section 4); relates to Data Governance (Value and metrics).

**Answer Key:** 1-b, 2-c, 3-d, 4-b, 5-b, 6-a, 7-b, 8-b, 9-b, 10-b, 11-b, 12-b, 13-b, 14-c, 15-c

---

## 14. References

### DAMA / Official

- DAMA-DMBOK2, 2nd Edition — Chapter 10: Reference and Master Data (primary source for this module; paraphrased and synthesized throughout — verify exact wording, enumerated lists, MDM style framing, and Master Data Type categorization against your own copy)
- DAMA Dictionary of Data Management Terminology (glossary cross-reference for Reference Data / Master Data / Golden Record / Value Domain terminology)
- Certification framing: `research/cdmp_exam_overview.md` — exam structure and Knowledge Area weighting (Reference & Master Data at the ~10% tier)

### Industry Practice

*(Real-world examples and terminology used for illustration only — not DAMA definitions; sourced per the priority rules in `research/source_map.md`, §5, which treat this tier as directional/illustrative, never authoritative for exam-fact claims.)*

- "Customer 360" — widely-used industry term for a unified, cross-channel customer view (the practical product of Customer MDM)
- MDM/data management platform categories (e.g., commercial and open-source MDM/master-data platforms) — tool choice is an implementation detail, not a DAMA concept
- ISO 3166 (country codes) and ISO 4217 (currency codes) — real external standards commonly used as the basis for Reference Data code sets
- ICD-10 — real external healthcare diagnosis classification standard, cited in the healthcare enterprise example (Section 6)
- Master Patient Index (MPI) pattern — cross-referenced from `data_governance.md`'s healthcare example
- BCBS 239 — real Basel Committee banking regulation requiring demonstrable, traceable risk-data aggregation, cross-referenced from `data_governance.md`
- MDM success metric naming (match rate, duplicate reduction rate, golden record adoption) — practitioner convention illustrating DAMA's general call for demonstrable program value

### Internal

- `research/cdmp_exam_overview.md` — exam structure and Knowledge Area weighting
- `research/source_map.md` — source hierarchy and citation rules followed throughout this module
- `roadmap/four_month_plan.md` — Week 7 study plan for this module
- `reviews/reference_and_master_data_review.md` — quality review this revision addresses
- `knowledge_base/data_governance.md` — Owner/Steward/Custodian roles, BCBS 239, HIPAA, Master Patient Index, and "Value and metrics" cross-references
- `knowledge_base/data_quality.md` — Uniqueness dimension and its relationship to matching/deduplication
- `knowledge_base/metadata_management.md` — Business Glossary, Lineage, and their relationship to golden-record traceability
- `knowledge_base/data_architecture.md` — Data Domain concept and MDM implementation style as an architecture decision
- `knowledge_base/data_modeling_and_design.md` — Primary/Foreign Key patterns and the Party/Person/Organization Generalization/Subtyping example underlying Master Data typing
