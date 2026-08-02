# Data Security

**Status:** Populated — core module complete. Revised per `reviews/data_security_review.md`.
**DMBOK2 Reference:** DMBOK2 2nd Ed., Ch.7 — Data Security
**Exam weight:** Part of the "remaining weight spread" tier alongside Data Architecture, Data Storage and Operations, Data Integration and Interoperability, Document and Content Management, Big Data and Data Science, Data Management Maturity Assessment, and Data Ethics — see `research/cdmp_exam_overview.md`.

> **Editorial note on sourcing:** Sourced per the priority hierarchy defined in `research/source_map.md` — DAMA-DMBOK2 concepts are primary authority, official DAMA guidance is used for certification framing, named regulations are real and independently verifiable, and named tools/platforms are illustrative examples only, never treated as DAMA definitions. Concepts are tagged **[DAMA]** for DMBOK2's official framing, **[Industry Practice]** for real-world conventions DMBOK2 references loosely or doesn't mandate, or **[Regulation/Standard]** for named external regulations (GDPR, HIPAA, PCI-DSS) cited because DMBOK2 references them or they directly ground a concept. This module follows the standard 14-section template documented in `knowledge_base/README.md`. No DMBOK2 text is reproduced verbatim anywhere in this file.

---

## 1. Overview

### Simple explanation (for beginners)

Every organization holds data that could cause real harm if the wrong person saw it, changed it, or leaked it — customer payment details, employee records, trade secrets, health information. **Data Security** is the discipline of making sure the right people (and systems) can access the right data for the right reasons, while everyone else can't, and being able to prove that after the fact.

It's tempting to think of this as purely a technical problem (firewalls, passwords, encryption), but DAMA treats it as a governed business discipline: deciding *how sensitive* a piece of data is and *who should be allowed to see it* are business/risk decisions, not something the security team invents unilaterally. The technology enforces the decision; it doesn't make it.

### Professional / DAMA-level explanation

**[DAMA]** DMBOK2 defines Data Security as the planning, development, and execution of security policies and procedures to provide proper authentication, authorization, access, and auditing of data and information assets. DMBOK2 frames this Knowledge Area's goals as: enabling appropriate access to, and preventing inappropriate access to, enterprise data; understanding and complying with relevant regulations and standards for privacy, protection, and confidentiality; and ensuring the security requirements of stakeholders (customers, employees, regulators) are met.

**[Industry Practice, widely DAMA-referenced]** A foundational framing underlying most data security work is the **CIA Triad**: **Confidentiality** (only authorized parties can access data), **Integrity** (data cannot be improperly altered without detection), and **Availability** (data is accessible to authorized parties when needed). This triad is not DAMA-original terminology, but DMBOK2's security goals map closely onto it and it's the standard vocabulary the security field uses to describe what security is protecting.

---

## 2. Why This Knowledge Area Exists

**[DAMA]** Data has value precisely because it's useful — and the same properties that make it useful to the organization (identifiability, detail, connectivity across systems) make it valuable and dangerous if exposed to the wrong party. This Knowledge Area exists because access to data cannot be left to informal trust or ad hoc technical convenience; it requires deliberate classification, policy, and enforcement.

### Business problems Data Security solves

1. **Unauthorized access and data breaches.** Without deliberate access control, sensitive data is exposed to more people (internal and external) than the business ever intended, creating direct financial, legal, and reputational risk.
2. **Regulatory and legal exposure.** Regulations governing personal, health, and financial data (Section 4) impose real legal consequences for inadequate protection — "we didn't think about it" is not a defense.
3. **Inconsistent protection across systems.** Without a shared classification scheme, one system might rigorously protect a field another system exposes freely, undermining protection everywhere the data flows.
4. **Insider risk and lack of accountability.** Without access logging and least-privilege practices, there's no way to know who accessed sensitive data, or to limit unnecessary broad access "just in case," both of which increase the blast radius of an eventual incident.
5. **Blocked legitimate use.** Overly blunt, undifferentiated security (e.g., locking down everything equally) frustrates legitimate business use of data just as much as under-protection creates risk — this Knowledge Area exists to calibrate protection to actual sensitivity, not maximize restriction indiscriminately.
6. **Inability to demonstrate compliance.** Without documented classification, policy, and access history, an organization cannot credibly answer a regulator's or auditor's "prove that only authorized parties could access this."

---

## 3. DAMA Definitions and Terminology

| Term | Definition |
|---|---|
| **Data Security** | The planning, development, and execution of security policies and procedures providing proper authentication, authorization, access, and auditing of data and information assets. |
| **Authentication** | The process of verifying that a party (user or system) is who/what it claims to be. |
| **Authorization** | The process of determining what an authenticated party is permitted to do. |
| **Data Classification** | The categorization of data according to its sensitivity, criticality, or regulatory requirements, used to determine the level of protection required. |
| **Confidentiality** | The property that data is accessible only to authorized parties. |
| **Data Security Policy** | A governance artifact (per the Policy/Standard/Procedure hierarchy in `data_governance.md`) stating the organization's mandatory direction for protecting data, from which specific standards and procedures are derived. |

### Authentication vs. Authorization

**[DAMA]** These two terms are among the most frequently confused in this Knowledge Area, despite answering genuinely different questions:

- **Authentication answers:** "Are you who you claim to be?" — verifying identity (e.g., a password, a certificate, multi-factor verification).
- **Authorization answers:** "Now that we know who you are, what are you allowed to do?" — determining permitted actions on specific resources.

A user can be successfully **authenticated** (the system correctly confirms their identity) and still be correctly **denied** access to a specific resource because they are not **authorized** for it — the two checks are sequential and independent, and a system that conflates them (assuming "logged in" automatically means "allowed to see everything") has a real security design flaw.

### Data Classification Levels

**[DAMA + Industry Practice]** DMBOK2 discusses classifying data by sensitivity to drive differentiated protection; the specific tier names below are common industry convention for expressing that scheme (exact naming varies by organization; verify framing against your own DMBOK2 copy):

| Tier | Typical meaning | Example |
|---|---|---|
| **Public** | No restriction; disclosure causes no harm | Published marketing materials |
| **Internal** | Not for external release, but broadly accessible inside the organization | Internal process documentation |
| **Confidential** | Restricted to those with a legitimate business need | Unreleased financial results, contract terms |
| **Restricted** (sometimes "Highly Confidential") | Tightly restricted, often regulated; highest protection tier | Customer PII, health records, payment card data |

*(See Section 9, Exam Traps, for the common mistake of treating classification tier count/names as a fixed DAMA-mandated list rather than an organization-specific scheme.)*

---

## 4. Core Concepts

### Sensitive Data Categories

**[Regulation/Standard]** Several named categories of sensitive data carry specific external regulatory obligations, distinct from an organization's internal classification tiers above:

- **PII (Personally Identifiable Information)** — data that can identify a specific individual (name, national ID, email), broadly regulated across jurisdictions.
- **PHI (Protected Health Information)** — health-related data tied to an identifiable individual, specifically regulated in the U.S. under **HIPAA**.
- **PCI (Payment Card data)** — cardholder data subject to the **PCI-DSS** (Payment Card Industry Data Security Standard), an industry-mandated standard (not a government regulation) for any organization handling card payments.
- **GDPR-regulated personal data** — the EU's **GDPR** (General Data Protection Regulation) defines a broad category of "personal data" with specific rights (access, erasure, portability) and obligations (lawful basis for processing, breach notification) attached.

These are named, independently verifiable regulations/standards (per `research/source_map.md`'s tier 4), used here to ground DAMA's general classification and protection concepts in real external obligations — not DAMA-authored content themselves.

### Access Control Models

**[Industry Practice, DAMA-referenced]** Different mechanisms for implementing authorization decisions:

- **Role-Based Access Control (RBAC)** — access is granted based on a user's assigned role (e.g., "Analyst," "Finance Manager"), with permissions attached to the role rather than the individual — the most common model for managing access at organizational scale, since permissions are administered per role rather than per person.
- **Attribute-Based Access Control (ABAC)** — access decisions are computed dynamically from attributes of the user, the data, and the context (e.g., "Finance staff can access this record only during business hours from a company device") — more flexible than RBAC but more complex to design and audit.
- **Discretionary Access Control (DAC)** — the data's owner/creator controls who else can access it, common in file-sharing contexts but weaker for enterprise-wide consistency.
- **Mandatory Access Control (MAC)** — access is governed by a central authority's fixed policy that individual users cannot override, common in high-security/government contexts.

**Choosing an access control model is an architecture and governance decision**, not a default — RBAC's administrative simplicity makes it the common enterprise default, while ABAC's added flexibility is typically reserved for genuinely context-sensitive access needs that role alone can't express.

### Least Privilege and Segregation of Duties

**[DAMA + Industry Practice]** Two foundational access-design principles:

- **Least Privilege** — granting a user or system only the minimum access actually needed to perform its function, not broad access "in case it's useful later." This directly limits the blast radius of both accidental misuse and a compromised account.
- **Segregation of Duties** — structuring access so that no single individual holds enough combined permissions to both perform and approve/conceal a sensitive action alone (e.g., the person who can create a vendor record should not also be the sole approver of payments to that vendor) — a control against both error and fraud.

### Encryption, Masking, Tokenization, Anonymization, and Pseudonymization

**[DAMA + Industry Practice]** These five terms are frequently confused, despite protecting data through genuinely different mechanisms with different reversibility properties:

| Technique | Mechanism | Reversible? |
|---|---|---|
| **Encryption** | Data is mathematically transformed using a key; unreadable without the correct decryption key. Applied **at rest** (stored data) and **in transit** (data moving across a network). | Yes, with the correct key |
| **Data Masking** | Sensitive values are obscured or substituted with realistic-but-fake values, typically for non-production environments (see `data_storage_and_operations.md`, Section 4). | Typically no (one-way substitution for the masked copy) |
| **Tokenization** | A sensitive value is replaced with a non-sensitive token; the mapping back to the real value is kept in a separate, tightly secured lookup (a "vault"). | Yes, but only via the secured token vault |
| **Anonymization** | Identifying information is removed or altered such that the individual cannot be re-identified, even by the organization itself, typically by processes robust to re-identification attacks. | No — irreversible by design |
| **Pseudonymization** | **[Regulation/Standard]** Identifying fields are replaced with pseudonyms; re-identification is possible only using additional information kept separately and securely — a technique explicitly named and encouraged by GDPR as a risk-reduction measure, while still treating pseudonymized data as personal data subject to its protections. | Yes, via securely separated additional information |

**Why the distinction matters for the exam:** "Anonymized" and "pseudonymized" are often used loosely in casual conversation as synonyms, but they carry materially different regulatory consequences — genuinely anonymized data typically falls outside many personal-data regulatory obligations (since no one can re-identify it), while pseudonymized data generally does not, because re-identification remains possible.

### Encryption Key Management

**[DAMA + Industry Practice]** Encryption (Section 4, above) is only as protective as the discipline around the keys that unlock it — a well-encrypted dataset with poorly controlled key access provides far less real protection than it appears to (Section 7, Common Mistake 3). Key management is the named practice covering:

- **Key generation and storage** — creating keys with sufficient strength and storing them separately from the data they protect, typically in a dedicated, access-restricted key management system rather than alongside the encrypted data itself.
- **Key rotation** — periodically replacing keys on a defined schedule, limiting how much data any single compromised key could expose.
- **Key access control** — applying the same Least Privilege and Segregation of Duties principles (above) to *who can access the keys themselves*, not only to who can access the encrypted data — since anyone with unrestricted key access can bypass the encryption's protection entirely.

### Data Loss Prevention (DLP)

**[Industry Practice, widely DAMA-referenced]** A category of monitoring and control technique — complementing Access Logging and Anomaly Detection, below — specifically focused on detecting and blocking unauthorized movement of sensitive data out of an organization's control (e.g., a bulk export of Restricted-classified records to an unapproved external destination). DLP tooling typically inspects data in motion or at egress points against classification rules, so a policy violation can be blocked or flagged in real time rather than discovered only after the fact.

### Data Security in the Data Lifecycle

**[DAMA]** DMBOK2 frames security as a concern spanning the entire data lifecycle, not a one-time control applied at creation:

- **Creation/Acquisition** — classifying data appropriately as soon as it's created or ingested, not retroactively after exposure has already occurred.
- **Use** — enforcing authentication/authorization at every point of access, including analytical and reporting use, not only primary operational systems.
- **Sharing** — applying appropriate controls (encryption, contractual terms, access restriction) when data moves to another system, team, or external party.
- **Archival** — maintaining appropriate protection even for infrequently accessed, archived data — sensitivity does not decay simply because access frequency does (a direct link to `data_storage_and_operations.md`'s archival concept, which preserves data but must preserve its protection level too).
- **Destruction** — ensuring destruction itself is secure and verifiable, so data isn't recoverable from improperly wiped media after its retention period ends.

### Security Monitoring and Auditing

**[DAMA]** Ongoing verification that access controls are actually working as designed, not just documented:

- **Access logging** — recording who accessed what data, when, providing the evidence needed to investigate an incident or demonstrate compliance.
- **Anomaly detection** — **[Industry Practice]** identifying unusual access patterns (e.g., a bulk export from an account that normally performs small, routine queries) that may indicate compromise or misuse.
- **Periodic access review** — regularly re-validating that granted access still matches actual need (echoing Least Privilege), since access rights tend to accumulate over time as people change roles unless deliberately reviewed and revoked.

### Security Risk Assessment

**[DAMA]** A structured process for identifying, evaluating, and prioritizing data security risks — considering the likelihood and impact of a given threat against a given data asset's classification, and directing protection investment toward the highest-risk combinations rather than spreading effort evenly regardless of actual risk.

### Data Security Success Metrics

**[DAMA + Industry Practice]** Echoing the same demonstrable-value pattern established across this project's other operational Knowledge Areas, security program health is typically evidenced through concrete, monitorable measures:

- **Time to detect and time to respond** to a security incident.
- **Access review completion rate** — whether periodic access reviews (above) are actually happening on schedule, not just documented as a policy.
- **Percentage of sensitive data classified and inventoried** — an organization cannot protect what it hasn't identified as sensitive in the first place.
- **Audit/compliance finding trend** — whether external or internal audits show improving or worsening security posture over time.

### Relationships With Other DAMA Knowledge Areas

**Data Governance:** Data classification and access policy are governed decisions requiring an accountable Data Owner (`data_governance.md`) — Data Security defines and enforces the technical/procedural controls, but the Owner decides what sensitivity level applies to their domain and who has a legitimate business need, the same Owner/Custodian boundary established throughout this project.

**Data Storage and Operations:** Encryption at rest, non-production data masking, and access provisioning are the operational, technical enforcement point where Data Security policy becomes an actually-configured control (`data_storage_and_operations.md`, Section 4) — Data Security defines the classification-driven requirement; Storage and Operations implements it.

**Metadata Management:** Classification level is itself a piece of Technical/Business Metadata (`metadata_management.md`) — without capturing and propagating classification as metadata, downstream systems have no reliable way to know a field needs protection as it moves through pipelines.

**Data Quality:** Integrity, one leg of the CIA Triad, directly overlaps with the Integrity/Accuracy-adjacent dimensions covered in `data_quality.md` — unauthorized or undetected alteration of data is both a security failure and a data quality failure viewed from two angles of the same underlying concern.

**Data Ethics** *(forthcoming module)*: Security and privacy are related but distinct — security protects data from unauthorized access; privacy concerns whether collecting and using the data at all (even by authorized parties) is appropriate and consented to. This module focuses on the security side; the ethical and consent dimensions are the specific focus of `data_ethics.md` once completed.

### Roles in Data Security

| Role | Data Security Responsibility |
|---|---|
| **Data Owner** | Approves the classification level for their data domain and defines who has a legitimate business need for access. |
| **Data Security Officer / Administrator** | **[DAMA + Industry Practice]** Designs and implements the technical and procedural security controls (access models, encryption standards, monitoring) enforcing classification-driven policy. |
| **Data Steward** | Helps classify data within their domain accurately and consistently, and flags data that doesn't fit existing classification tiers cleanly. |
| **Data Engineer** | Implements access controls, encryption, masking, and tokenization in pipelines and storage; propagates classification metadata through transformations; does not unilaterally decide classification or grant exceptions to approved access policy. |
| **Chief Information Security Officer (CISO)** | **[Industry Practice]** Senior executive accountable for the organization's overall security posture and program, typically the escalation point above individual Data Security Officers for cross-domain risk decisions. |

---

## 5. Data Engineer Perspective

**Pipeline-level access control:** Enforcing authentication and authorization at every stage a pipeline touches sensitive data — not only at the final storage layer — since a pipeline's intermediate stages (staging areas, logs, temporary files) can just as easily leak sensitive data if left unprotected.

**Encryption in practice:** Implementing encryption at rest (for stored data) and in transit (for data moving between systems) as a default engineering practice for sensitive data, not an optional add-on applied only after an incident.

**Classification-aware pipeline design:** Propagating classification metadata alongside the data itself as it moves through transformations, so a downstream consumer (or an automated policy engine) can enforce the correct protection level without needing to independently re-derive sensitivity from scratch.

**Tokenization and masking implementation:** Building the actual pipelines that tokenize sensitive fields for downstream analytical use, or mask them for non-production environments (directly extending `data_storage_and_operations.md`, Section 4's Non-Production Environment Management into a concrete engineering deliverable).

**IAM (Identity and Access Management) integration:** **[Industry Practice]** Connecting pipeline and platform access to a centralized identity provider and role/attribute-based access system, rather than maintaining separate, inconsistent access lists per tool or dataset.

**Secrets management:** **[Industry Practice]** Storing credentials, API keys, and encryption keys in a dedicated, access-controlled secrets management system rather than embedding them in code or configuration files — a common, high-impact real-world security failure this Knowledge Area's principles directly address.

**Audit logging for pipelines:** Ensuring pipeline access to sensitive sources and outputs is logged in a way that supports the access review and anomaly detection practices in Section 4, not just application-level user access.

**How a Data Engineer contributes without owning business decisions:** As with every other Knowledge Area in this project, the Data Engineer implements approved classification-driven controls (encryption, masking, RBAC/ABAC configuration) but does not unilaterally decide what classification a dataset should carry or grant an access exception because it's operationally convenient — those are Owner/Data Security Officer decisions the engineer implements and, where a request seems misaligned with policy, escalates rather than quietly grants.

---

## 6. Enterprise Examples

*(Illustrative composite scenarios; named external standards/regulations are real.)*

### Banking: Segregation of Duties in Payment Processing

**Problem:** A bank (recurring from `data_governance.md`, `reference_and_master_data.md`, and `data_warehousing_and_business_intelligence.md`) discovers that a single employee role can both create a new vendor record and approve payments to that vendor — a fraud risk regulators specifically flag during audit.

**Data Security approach:** Access is redesigned around Segregation of Duties: vendor creation and payment approval are split into distinct roles under RBAC, with no individual permitted to hold both simultaneously without a documented, time-limited exception requiring senior sign-off.

**Governance approach:** The Data Owner for vendor/payment data, in consultation with compliance, approves the new role design, and periodic access reviews confirm the separation is maintained as staff change roles over time.

**Business outcome:** The bank closes a real fraud vector and can demonstrate to regulators that the control is actively enforced and reviewed, not merely documented.

### Healthcare: PHI Access Control and Auditing

**Problem:** A hospital network (recurring from `reference_and_master_data.md` and `data_storage_and_operations.md`) must ensure clinical staff can access patient records needed for direct care while preventing broader, unnecessary access to PHI — and must be able to prove, after the fact, exactly who accessed a given patient's record.

**Data Security approach:** RBAC scoped to clinical assignment (a nurse can access records for patients on their current unit, not the entire hospital's patient population by default) combined with comprehensive access logging, satisfying HIPAA's access control and audit requirements.

**Governance approach:** The clinical Data Owner (echoing `reference_and_master_data.md`'s Patient Data Owner) defines what counts as legitimate "need to know" access per role, balancing care-delivery speed against over-broad default access.

**Business outcome:** The hospital can both support fast, unblocked clinical care and produce a defensible access audit trail if a patient privacy concern is ever raised.

### Retail: PCI-DSS Compliance for Payment Data

**Problem:** An omnichannel retailer (recurring from `data_architecture.md`, `reference_and_master_data.md`, and `data_warehousing_and_business_intelligence.md`) processes card payments across online, in-store, and marketplace channels, and must protect cardholder data to PCI-DSS's mandated standard across all of them.

**Data Security approach:** Tokenization replaces raw card numbers with non-sensitive tokens immediately at capture, so downstream systems (order processing, analytics, customer service tools) never handle raw card data at all — dramatically shrinking the scope of systems that must meet PCI-DSS's strictest requirements.

**Governance approach:** A named Data Security Officer role owns PCI-DSS compliance specifically, since it is an externally audited, industry-mandated standard with real consequences (including loss of card processing privileges) for non-compliance.

**Business outcome:** The retailer reduces both breach risk and compliance audit scope by minimizing how many systems ever touch raw sensitive payment data at all.

### Manufacturing: Classification and Access for Trade Secrets

**Problem:** A manufacturer (recurring from `data_warehousing_and_business_intelligence.md` and `data_storage_and_operations.md`) has proprietary product formulas and supplier contract terms stored in the same systems as ordinary operational data, with no differentiated protection — anyone with general system access can see trade secrets alongside routine production data.

**Data Security approach:** A formal classification pass identifies formulas and contract terms as "Restricted," with ABAC rules restricting access to specific named roles and requiring additional authentication, distinct from the "Internal" classification applied to routine production metrics.

**Governance approach:** R&D and Legal jointly serve as Data Owners for their respective Restricted categories, since the business impact of exposure (competitive loss, contractual breach) is severe enough to warrant dedicated accountability beyond general IT oversight.

**Business outcome:** The organization protects its most competitively sensitive data without over-restricting the much larger volume of routine operational data that legitimately needs broad internal access.

---

## 7. Common Mistakes

1. **Conflating authentication with authorization.** Assuming that because a user successfully logged in, they should be able to see everything the system contains, rather than enforcing a separate, deliberate authorization check per resource.
2. **Applying uniform protection regardless of sensitivity.** Either over-restricting routine, low-sensitivity data (frustrating legitimate use) or under-protecting genuinely sensitive data because classification was never actually performed — both are failures of the same missing step.
3. **Treating encryption as a complete security solution.** Encrypting data at rest while leaving broad, poorly audited access to the decrypted data (or the decryption keys themselves) provides far less real protection than it appears to.
4. **Letting access rights accumulate without review.** Granting access when a legitimate need exists but never revoking it when that need ends (a role change, a completed project), silently violating Least Privilege over time.
5. **Confusing masking, tokenization, anonymization, and pseudonymization.** Using the wrong technique for the actual requirement — e.g., using masking (typically irreversible, for non-production use) where tokenization (reversible, for production analytical use) was actually needed, or calling data "anonymized" when it's genuinely only pseudonymized and still subject to personal-data regulation.
6. **Treating security as solely IT's responsibility.** Assuming a security or IT team can unilaterally decide classification and access policy without business Data Owner input, recreating the same accountability gap pattern this project has documented across every other Knowledge Area.
7. **Storing secrets and credentials insecurely.** Embedding API keys or database credentials directly in code or configuration files rather than in a dedicated secrets management system — a common, high-impact, and entirely preventable real-world failure mode.

---

## 8. CDMP Exam Focus

### High-value concepts
- **Authentication vs. Authorization** (Section 3) — precise, independent definitions and the ability to reason about scenarios where a user is authenticated but correctly denied authorization.
- **Data Classification** (Section 3, Section 4) — the concept of tiered sensitivity driving differentiated protection, and that specific tier names/counts are organization-specific, not a fixed DAMA enumeration.
- **Encryption vs. Masking vs. Tokenization vs. Anonymization vs. Pseudonymization** (Section 4) — the single most commonly tested cluster of related-but-distinct techniques in this Knowledge Area, including their differing reversibility.
- **Least Privilege and Segregation of Duties** (Section 4) — precise definitions and the ability to identify a violation in a described scenario.
- **The CIA Triad** (Section 1) as the underlying framing for what security protects.

### Important definitions
- Data Security, Authentication, Authorization, Data Classification, Confidentiality — precise, independent definitions.
- RBAC, ABAC, DAC, MAC; Least Privilege; Segregation of Duties; Encryption (at rest/in transit); Data Masking; Tokenization; Anonymization; Pseudonymization.
- PII, PHI, PCI, GDPR — named categories/regulations and what each specifically governs.

### Frequently confused concepts
- **Authentication vs. Authorization** — identity verification vs. permission determination; the single most commonly tested distinction in this Knowledge Area.
- **Anonymization vs. Pseudonymization** — irreversible vs. reversible-with-separately-secured-information; carries real regulatory consequence differences.
- **Data Masking vs. Tokenization** — masking is typically one-way and for non-production use; tokenization is reversible via a secured vault and commonly used in production to reduce sensitive-data footprint.
- **Data Security vs. Data Privacy/Ethics** — security protects data from unauthorized access; privacy/ethics concerns whether collecting and using data is appropriate in the first place, even by authorized parties (see `data_ethics.md` once completed).
- **Data Classification tiers as fixed DAMA terminology** — the concept of tiered classification is DAMA-endorsed; specific tier names (Public/Internal/Confidential/Restricted) are common industry convention, not a fixed, universally-mandated DAMA list.

---

## 9. Exam Traps

- **A question implies authentication alone is sufficient for access.** A successfully authenticated (logged-in) user must still pass a separate authorization check for each specific resource — conflating the two is a documented, frequently-tested error.
- **A question treats "anonymized" and "pseudonymized" as interchangeable.** They carry materially different reversibility and regulatory implications (Section 4) — an answer treating pseudonymized data as no longer personal/regulated data is very likely wrong.
- **A question implies encryption alone fully secures data.** Encryption protects data confidentiality specifically; it does not substitute for access control, monitoring, or key management — a well-encrypted dataset with poorly controlled access to its decryption key or its decrypted form is not actually well protected (Section 7, Common Mistake 3).
- **A question implies more restrictive access is always the safer, "more correct" choice.** Over-restricting legitimate access is also a documented failure mode (Section 2, Section 7) — the goal is calibrated protection matching actual sensitivity and need, not maximum restriction indiscriminately.
- **A question assumes data classification tier names are DAMA-fixed and universal.** The concept of classification is DAMA-endorsed; the specific tier names/count are organization-specific convention (Section 3).
- **A question treats Data Security and Data Privacy/Ethics as synonymous.** Security is about unauthorized access; privacy/ethics is about whether the use itself (even by authorized parties) is appropriate — related but genuinely distinct concerns (Section 8).
- **A question implies IT/Security can set classification and access policy unilaterally, without business input.** Classification and "legitimate business need" determinations are governed, Data Owner-accountable decisions, not a purely technical judgment call (Section 7, Common Mistake 6).

---

## 10. Interview Questions

### Data Engineer level
1. **"What's the difference between how you'd implement authentication versus authorization in a data platform?"**
   *Strong answer covers:* authentication as identity verification (e.g., integrating with a centralized identity provider) versus authorization as a separate, resource-specific permission check (e.g., role/attribute-based rules), and explicitly does not conflate "logged in" with "allowed to see everything."
2. **"How would you decide between masking and tokenization for a dataset containing customer PII?"**
   *Strong answer covers:* masking for non-production/test environments where the real value is never needed again, versus tokenization for production analytical use where reversibility via a secured vault may genuinely be required — tied to the actual requirement, not a default habit.
3. **"How do you handle secrets like database credentials and API keys in your pipelines?"**
   *Strong answer covers:* using a dedicated secrets management system rather than embedding credentials in code or config files, and rotating credentials rather than treating them as permanent.

### Senior Data Engineer level
4. **"An access review reveals a team member still has access to a sensitive dataset from a project that ended eight months ago. How do you address this, and how do you prevent recurrence?"**
   *Signal:* treats this as a Least Privilege violation requiring immediate revocation, and proposes a systematic periodic access review process (Section 4) rather than a one-off manual fix.
5. **"How would you design a pipeline so that classification/sensitivity information travels with the data through every transformation stage?"**
   *Signal:* proposes propagating classification as metadata alongside the data (tying to `metadata_management.md`) so downstream consumers and automated policy engines can enforce protection without re-deriving sensitivity independently.
6. **"A business team requests broad access to a Restricted-classified dataset because it would be 'convenient' for an upcoming analysis. How do you respond?"**
   *Signal:* escalates to the accountable Data Owner rather than granting the exception directly, and asks for the specific legitimate business need rather than treating convenience alone as sufficient justification.

### Data Security Officer / Architect level
7. **"How would you evaluate whether RBAC or ABAC is the right access control model for a given system?"**
   *Signal:* weighs RBAC's administrative simplicity against ABAC's context-sensitivity, recognizing this as a genuine tradeoff (echoing the "no single approach is unconditionally best" pattern established across this project) rather than defaulting to whichever is currently trending.
8. **"How would you design a classification scheme for an organization that currently has none?"**
   *Signal:* proposes starting from actual regulatory/business-impact-driven tiers (not an arbitrary number of levels), assigns Data Owner accountability per domain for applying it, and plans for it to be enforced via metadata propagation, not a one-time manual exercise.
9. **"How would you reduce PCI-DSS audit scope for an organization handling a high volume of card payments?"**
   *Signal:* proposes tokenizing cardholder data immediately at capture so the fewest possible downstream systems ever handle raw sensitive data, directly minimizing the systems subject to the standard's strictest requirements.

---

## 11. Practical Exercises

### Exercise 1: Design an Access Control Model for a New System

**Scenario:** A new internal analytics platform will be used by Finance, Marketing, and Customer Support teams, each needing access to different, overlapping subsets of customer and financial data.

**Task:** Propose (a) which access control model (RBAC, ABAC, or a hybrid) best fits this scenario and why; (b) how Least Privilege would be applied to each team's access; (c) how you would prevent access rights from silently accumulating over time.

**Expected solution approach:** RBAC is a reasonable starting point given three well-defined organizational roles, with ABAC-style refinements (e.g., context like "only during business hours" or "only aggregated, not row-level, financial data for Marketing") layered on top where role alone is too coarse. Least Privilege means each team's role is scoped to only the specific data subsets their function actually requires — Marketing should not default to raw financial detail just because it exists in the same platform. Preventing accumulation requires a scheduled, mandatory periodic access review (Section 4) with an owner accountable for actually completing it, not just a documented policy.

### Exercise 2: Choose the Right Data Protection Technique

**Scenario:** An organization needs to (a) let its QA team test against realistic customer data without real customer PII, (b) let its fraud-analytics team occasionally look up a real customer's details after a hit on a suspicious-activity flag, and (c) publish an aggregated statistical report for external researchers with no possibility of any individual being identified.

**Task:** Recommend the correct technique (masking, tokenization, or anonymization) for each of the three needs, and justify why the other two would be a worse fit for each.

**Expected solution approach:** (a) Data Masking — QA needs realistic-looking data but never needs to recover the real value, matching masking's typically one-way substitution. (b) Tokenization — the fraud-analytics team genuinely needs reversibility for specific, justified lookups, which only tokenization's secured vault mechanism supports; masking would make the real value permanently unrecoverable, and anonymization would remove the linkage needed to investigate a specific customer at all. (c) Anonymization — external publication with zero re-identification risk requires irreversible removal of identifying information; pseudonymization or tokenization would still leave the data classified as personal/regulated, which is unacceptable for this use case.

### Exercise 3: Diagnose a Segregation of Duties Gap

**Scenario:** An internal audit finds that a single "AP Clerk" role can both create new vendor records and approve payments to those vendors, with no secondary review required.

**Task:** Diagnose the risk using this Knowledge Area's terminology, and propose a remediation that doesn't create unreasonable operational friction.

**Expected solution approach:** This is a Segregation of Duties gap (Section 4) — combining vendor creation and payment approval in one role creates a fraud vector (a malicious or compromised account could create a fake vendor and approve payment to it with no independent check). Remediation: split the permissions into two distinct roles under RBAC, requiring a second person to approve any payment to a newly created vendor, with a documented, time-limited exception process (requiring senior sign-off) for genuinely urgent cases rather than a blanket, permanent combined-role default.

---

## 12. Flashcards

| Term | Definition |
|---|---|
| Data Security | The planning, development, and execution of security policies and procedures providing authentication, authorization, access, and auditing of data assets. |
| Authentication | The process of verifying that a party is who/what it claims to be. |
| Authorization | The process of determining what an authenticated party is permitted to do. |
| Data Classification | Categorizing data by sensitivity/criticality/regulatory requirement to determine required protection level. |
| Confidentiality | The property that data is accessible only to authorized parties (one leg of the CIA Triad). |
| CIA Triad | Confidentiality, Integrity, and Availability — the foundational framing of what data security protects. |
| Role-Based Access Control (RBAC) | Access granted based on a user's assigned role rather than individually. |
| Attribute-Based Access Control (ABAC) | Access decisions computed dynamically from attributes of the user, data, and context. |
| Least Privilege | Granting only the minimum access actually needed to perform a function. |
| Segregation of Duties | Structuring access so no single individual can both perform and approve/conceal a sensitive action alone. |
| Encryption | Mathematically transforming data using a key so it is unreadable without the correct decryption key. |
| Data Masking | Obscuring or substituting sensitive values, typically irreversibly, for non-production use. |
| Tokenization | Replacing a sensitive value with a non-sensitive token, reversible via a securely separated lookup vault. |
| Anonymization | Irreversibly removing identifying information so an individual cannot be re-identified. |
| Pseudonymization | Replacing identifying fields with pseudonyms, reversible only via securely separated additional information. |
| PII | Personally Identifiable Information — data that can identify a specific individual. |
| PHI | Protected Health Information — health-related data tied to an identifiable individual, regulated under HIPAA. |
| PCI | Payment card data, subject to the PCI-DSS industry standard. |
| GDPR | The EU's General Data Protection Regulation, governing personal data rights and obligations. |
| Access Logging | Recording who accessed what data and when, supporting investigation and compliance evidence. |
| Security Risk Assessment | A structured process for identifying, evaluating, and prioritizing data security risks. |
| Data Security Success Metrics | Measures (e.g., time to detect/respond, access review completion rate) demonstrating a security program's ongoing effectiveness. |
| Encryption Key Management | The practice of generating, storing, rotating, and access-controlling encryption keys, without which encryption alone provides limited real protection. |
| Data Loss Prevention (DLP) | Monitoring and control techniques that detect and block unauthorized movement of sensitive data out of an organization's control. |

---

## 13. Quiz Questions

1. **What is the primary difference between Authentication and Authorization?**
   a) They are the same process under different names b) Authentication verifies identity; Authorization determines what an authenticated party is permitted to do c) Authentication only applies to systems; Authorization only applies to human users d) Authorization always occurs before Authentication

   **Correct answer:** b) Authentication verifies identity; Authorization determines what an authenticated party is permitted to do.
   **Explanation:** These are sequential, independent checks — authentication answers "who are you," authorization answers "what are you allowed to do now that we know."
   **Why the others are wrong:** (a) conflates two genuinely distinct processes, a documented exam trap; (c) both concepts apply equally to human users and systems; (d) authorization logically requires a known, authenticated identity first, not the reverse order.
   **Related Knowledge Area:** Data Security (this module, Section 3, Section 9).

2. **A user successfully logs into a data platform but is denied access to a specific Restricted-classified table. What does this best illustrate?**
   a) A system error, since a logged-in user should see everything b) Correct behavior — successful authentication does not automatically grant authorization to every resource c) A failure of the CIA Triad's Availability principle d) A Segregation of Duties violation

   **Correct answer:** b) Correct behavior — successful authentication does not automatically grant authorization to every resource.
   **Explanation:** This is the expected, correct behavior of a properly designed system — authentication and authorization are separate checks, and being authenticated does not imply blanket authorization.
   **Why the others are wrong:** (a) incorrectly assumes login should grant full access, the exact conflation this Knowledge Area warns against; (c) Availability concerns whether authorized parties can access data when needed, not this scenario; (d) Segregation of Duties concerns combined permissions enabling fraud, unrelated to a single denied access attempt.
   **Related Knowledge Area:** Data Security (this module, Section 3, Section 9).

3. **Which technique irreversibly removes identifying information so that an individual cannot be re-identified, even by the organization itself?**
   a) Tokenization b) Pseudonymization c) Anonymization d) Data Masking for non-production environments

   **Correct answer:** c) Anonymization.
   **Explanation:** Anonymization is specifically defined by irreversibility — identifying information is removed such that re-identification is not possible by design, even by the organization that performed it.
   **Why the others are wrong:** (a) Tokenization is reversible via a secured token vault; (b) Pseudonymization is reversible using separately secured additional information; (d) Data Masking is typically one-way for the masked copy, but the concept and its typical use case (realistic non-production test data) is distinct from Anonymization's regulatory-driven, irreversible re-identification prevention.
   **Related Knowledge Area:** Data Security (this module, Section 4, Section 9).

4. **A payment processor replaces raw card numbers with non-sensitive tokens immediately at capture, keeping the mapping back to real card numbers in a separate, tightly secured vault. This technique is:**
   a) Anonymization b) Tokenization c) Data Masking d) Least Privilege

   **Correct answer:** b) Tokenization.
   **Explanation:** Tokenization is defined by replacing a sensitive value with a non-sensitive token while keeping the reversible mapping in a separately secured vault — exactly as described.
   **Why the others are wrong:** (a) Anonymization is irreversible by design, unlike this scenario's explicit reversible vault mapping; (c) Data Masking is typically one-way and used for non-production environments, not this production reversible-substitution use case; (d) Least Privilege is an access-scoping principle, unrelated to value substitution techniques.
   **Related Knowledge Area:** Data Security (this module, Section 4); relates to Data Storage and Operations.

5. **What is the core purpose of Segregation of Duties?**
   a) To ensure only one person understands each business process b) To structure access so no single individual can both perform and approve/conceal a sensitive action alone c) To reduce the total number of user accounts in a system d) To guarantee data is encrypted at rest

   **Correct answer:** b) To structure access so no single individual can both perform and approve/conceal a sensitive action alone.
   **Explanation:** Segregation of Duties is specifically a control against error and fraud, ensuring sensitive actions require more than one person's combined authority.
   **Why the others are wrong:** (a) describes a knowledge-concentration risk, the opposite of good practice, and unrelated to Segregation of Duties' actual purpose; (c) reducing account count is an unrelated administrative concern; (d) encryption is a distinct protection technique, unrelated to duty separation.
   **Related Knowledge Area:** Data Security (this module, Section 4).

6. **Select the two items below that are named external regulations/standards governing specific categories of sensitive data. (Select two.)**
   a) HIPAA b) Role-Based Access Control (RBAC) c) PCI-DSS d) Least Privilege

   **Correct answer:** a) HIPAA; c) PCI-DSS.
   **Explanation:** HIPAA (U.S. health information regulation) and PCI-DSS (payment card industry standard) are both real, named, externally-defined regulations/standards governing specific sensitive data categories.
   **Why the others are wrong:** (b) RBAC is an access control model/mechanism, not a named external regulation; (d) Least Privilege is a general access-design principle, not a named external regulation.
   **Related Knowledge Area:** Data Security (this module, Section 4).

7. **True or False: Encrypting a dataset at rest is, by itself, sufficient to consider that dataset fully secured.**
   a) True b) False

   **Correct answer:** b) False.
   **Explanation:** Encryption protects confidentiality specifically, but does not substitute for access control, monitoring, or key management — poorly controlled access to the decrypted data or the decryption key itself undermines the protection encryption alone provides.
   **Why the others are wrong:** (a) treats encryption as a complete solution, a documented exam trap and Common Mistake in this Knowledge Area.
   **Related Knowledge Area:** Data Security (this module, Section 7, Section 9).

8. **An organization grants a project team broad access to a sensitive dataset for a six-month initiative, but never revokes that access after the project ends. Eight months later, this unrevoked access is discovered. What principle was violated?**
   a) Segregation of Duties b) Least Privilege c) The CIA Triad's Availability principle d) Data Classification
   
   **Correct answer:** b) Least Privilege.
   **Explanation:** Least Privilege requires access to be limited to actual, current need; failing to revoke access once the legitimate need ends is a direct violation of this principle, even if the original grant was appropriate.
   **Why the others are wrong:** (a) Segregation of Duties concerns combined permissions enabling fraud, not access retention after need ends; (c) Availability concerns whether authorized parties can access data when needed, unrelated to over-retained access; (d) Data Classification concerns sensitivity categorization, not access lifecycle management.
   **Related Knowledge Area:** Data Security (this module, Section 4, Section 7).

9. **A retailer tokenizes cardholder data immediately at capture so that downstream systems never handle raw card numbers. What is the most direct business benefit of this approach?**
   a) It eliminates the need for any access control on downstream systems b) It reduces the number of systems subject to the strictest PCI-DSS compliance requirements, since they never touch raw sensitive data c) It makes the data permanently unrecoverable, improving privacy d) It replaces the need for a Data Security Officer role
   
   **Correct answer:** b) It reduces the number of systems subject to the strictest PCI-DSS compliance requirements, since they never touch raw sensitive data.
   **Explanation:** By minimizing which systems ever handle raw cardholder data, tokenization directly shrinks the scope of systems subject to PCI-DSS's most stringent requirements, reducing both breach risk and audit burden.
   **Why the others are wrong:** (a) tokenized data still requires appropriate access control; tokenization reduces risk, it does not eliminate the need for controls; (c) tokenization is reversible via the secured vault, unlike anonymization's permanent irreversibility; (d) a Data Security Officer role remains necessary regardless of tokenization to own the broader compliance and security program.
   **Related Knowledge Area:** Data Security (this module, Section 6); relates to Data Governance.

10. **A Data Engineer receives a request from a business team to grant broad access to a Restricted-classified dataset because it would be "convenient" for an upcoming analysis. What is the most appropriate response?**
    a) Grant the access immediately, since data should generally be as accessible as possible b) Deny all future requests from that team as a precaution c) Escalate to the accountable Data Owner and request the specific legitimate business need, rather than granting or denying the exception unilaterally d) Grant the access, but only for one week
    
    **Correct answer:** c) Escalate to the accountable Data Owner and request the specific legitimate business need, rather than granting or denying the exception unilaterally.
    **Explanation:** Classification and access exceptions for Restricted data are governed, Data Owner-accountable decisions; a Data Engineer should escalate rather than unilaterally grant or deny convenience-driven requests.
    **Why the others are wrong:** (a) treats convenience as sufficient justification, contradicting the Least Privilege and Owner-accountability principles established in this Knowledge Area; (b) is an overcorrection with no basis in the scenario and doesn't resolve the actual governance question; (d) still constitutes the Data Engineer unilaterally granting an access exception, only with an arbitrary time limit rather than proper Owner approval.
    **Related Knowledge Area:** Data Security (this module, Section 5, Section 7); relates to Data Governance.

11. **A hospital scopes clinical staff access so a nurse can view records only for patients on their currently assigned unit, rather than the entire hospital's patient population. This is a direct application of which two principles? (Select two.)**
    a) Role-Based Access Control (RBAC) b) Anonymization c) Least Privilege d) Tokenization
    
    **Correct answer:** a) Role-Based Access Control (RBAC); c) Least Privilege.
    **Explanation:** Scoping access by clinical role/assignment is an RBAC implementation, and limiting that access to only the specific patients a nurse currently needs (rather than the full population) is a direct application of Least Privilege.
    **Why the others are wrong:** (b) Anonymization would prevent identifying any patient at all, which would defeat the purpose of clinical care access; (d) Tokenization substitutes sensitive values with tokens, unrelated to scoping which records a role can view.
    **Related Knowledge Area:** Data Security (this module, Section 4, Section 6).

12. **An organization treats "Public," "Internal," "Confidential," and "Restricted" as the one universally DAMA-mandated classification scheme that every organization must use verbatim. What is the flaw in this assumption?**
    a) There is no flaw; DAMA mandates this exact four-tier scheme b) The concept of tiered classification is DAMA-endorsed, but the specific tier names and count are common industry convention, not a fixed, universally-mandated DAMA list c) DAMA mandates a minimum of six classification tiers d) Classification schemes are only relevant to government organizations
    
    **Correct answer:** b) The concept of tiered classification is DAMA-endorsed, but the specific tier names and count are common industry convention, not a fixed, universally-mandated DAMA list.
    **Explanation:** DMBOK2 endorses the general practice of sensitivity-driven classification; the specific tier names/count shown in this module are illustrative industry convention, and organizations commonly adapt the exact scheme to their own needs.
    **Why the others are wrong:** (a) and (c) both incorrectly assert a fixed, universal DAMA-mandated scheme that does not exist; (d) classification is relevant to any organization handling sensitive data, not government-specific.
    **Related Knowledge Area:** Data Security (this module, Section 3, Section 9).

13. **A dataset is fully encrypted at rest, but the encryption key is stored in the same unrestricted-access location as the encrypted data itself, with no rotation policy. What is the most accurate assessment?**
    a) The dataset is fully secured, since encryption alone is sufficient b) The encryption provides limited real protection, since anyone with access to the co-located, unrestricted key can bypass it entirely c) This configuration satisfies Least Privilege by definition d) This is an example of proper Data Loss Prevention

    **Correct answer:** b) The encryption provides limited real protection, since anyone with access to the co-located, unrestricted key can bypass it entirely.
    **Explanation:** Encryption's protection depends on disciplined key management — access-restricted storage and rotation — and co-locating an unrestricted key with the data it protects effectively defeats the purpose of encrypting it in the first place.
    **Why the others are wrong:** (a) restates the documented exam trap that encryption alone is sufficient; (c) the scenario describes the opposite of Least Privilege, since key access is unrestricted rather than minimized; (d) DLP concerns detecting/blocking unauthorized data movement, unrelated to key storage practice.
    **Related Knowledge Area:** Data Security (this module, Section 4, Section 7).

**Answer Key:** 1-b, 2-b, 3-c, 4-b, 5-b, 6-a,c, 7-b, 8-b, 9-b, 10-c, 11-a,c, 12-b, 13-b

---

## 14. References

### DAMA / Official

- DAMA-DMBOK2, 2nd Edition — Chapter 7: Data Security (primary source for this module; paraphrased and synthesized throughout — verify exact wording, enumerated lists, and classification-tier framing against your own copy)
- DAMA Dictionary of Data Management Terminology (glossary cross-reference for Authentication/Authorization/Classification terminology)
- Certification framing: `research/cdmp_exam_overview.md` — exam structure and Knowledge Area weighting

### Regulation / Standard

*(Real, independently verifiable regulations and standards, cited because they ground this module's concepts in real external obligations — not DAMA-authored content; per `research/source_map.md`, §4.)*

- HIPAA — U.S. regulation governing Protected Health Information (PHI)
- GDPR — EU General Data Protection Regulation governing personal data rights and obligations, including its explicit encouragement of pseudonymization as a risk-reduction technique
- PCI-DSS — Payment Card Industry Data Security Standard governing cardholder (PCI) data protection

### Industry Practice

*(Real-world examples and terminology used for illustration only — not DAMA definitions; sourced per the priority rules in `research/source_map.md`, §5, which treat this tier as directional/illustrative, never authoritative for exam-fact claims.)*

- CIA Triad (Confidentiality, Integrity, Availability) — standard information security framing
- RBAC / ABAC / DAC / MAC access control model names — standard industry access-control taxonomy
- IAM (Identity and Access Management) platforms, secrets management systems — implementation categories, not DAMA concepts

### Internal

- `research/cdmp_exam_overview.md` — exam structure and Knowledge Area weighting
- `research/source_map.md` — source hierarchy and citation rules followed throughout this module
- `roadmap/four_month_plan.md` — Week 10 study plan for this module
- `knowledge_base/data_governance.md` — Data Owner/Custodian roles and the Policy/Standard/Procedure hierarchy
- `knowledge_base/data_storage_and_operations.md` — encryption at rest, non-production data masking, and the technical enforcement layer for this module's policy concepts
- `knowledge_base/metadata_management.md` — classification as a form of Technical/Business Metadata
- `knowledge_base/data_quality.md` — the Integrity dimension's overlap with the CIA Triad's Integrity leg
- `knowledge_base/reference_and_master_data.md` — Patient Data Owner example reused in Section 6
