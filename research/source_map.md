# Source Map

Defines how authoritative references get incorporated into this project: what maps where, how to cite it, and which source wins when two disagree. This is the framework — it does not itself contain source content (see `sources/` for that) and it does not change any existing `knowledge_base/` file.

**Status:** Framework only. No bulk source import has happened; `sources/` folders are placeholders populated incrementally as each Knowledge Area is studied per `roadmap/four_month_plan.md`.

---

## 1. DAMA-DMBOK2 Mapping Strategy

DMBOK2 is the primary text and the exam's authoritative content source. Mapping is already 1:1 by design:

| DMBOK2 | Project |
|---|---|
| One chapter per Knowledge Area (Ch.3–16, roughly) | One file per Knowledge Area in `knowledge_base/` (see `knowledge_base/README.md` for the list and shared 14-section template) |
| Chapter sub-sections (business drivers, concepts, activities, tools, governance, metrics) | Mapped into the template's "DAMA Definitions," "Core Concepts," and related sections |
| Glossary terms | Feed the "Flashcards" section of each Knowledge Area file, cross-checked against the DAMA Dictionary (`sources/dama_official/`) |

**Sourcing convention (already in use, formalized here):** every claim in a `knowledge_base/` file is tagged inline —
- **`[DAMA]`** — paraphrased/synthesized from DMBOK2 itself. Paraphrase only; see the copyright rule in `sources/README.md`. Not a verbatim quote unless explicitly marked as one and under ~25 words.
- **`[Industry Practice]`** — real-world convention DMBOK2 does not mandate or specify (tools, specific operating models, modern terminology like "lakehouse zones").
- **`[Regulation/Standard]`** — a named external regulation or standard (e.g., BCBS 239, HIPAA, ISO 8000) cited because DMBOK2 references it or it's directly relevant — real and independently verifiable, not DAMA-authored.

**Citation format for DMBOK2 references:** `DMBOK2 2nd Ed., Ch.<N> <Chapter Name>, §<section>` — page numbers where precision matters (definitions, enumerated lists). Chapter-level citation is sufficient for general concepts.

**Working notes home:** `sources/dmbok2/` holds a page/section index and personal paraphrase-only chapter summaries used as a drafting aid — not the source of truth itself, which remains your own physical/licensed copy of DMBOK2.

**Open item carried from `research/cdmp_exam_overview.md`:** the exact current DAMA-recommended edition/errata isn't yet confirmed. Resolve this before treating any DMBOK2 citation as final — log the confirmed edition in `sources/dmbok2/README.md` once known.

---

## 2. CDMP Exam Guide Mapping

`research/cdmp_exam_overview.md` currently documents exam mechanics (format, timing, scoring, KA weighting) sourced from DAMA's public certification pages, cross-checked against prep-vendor breakdowns. It explicitly flags the per-KA weighting as **directional, not officially confirmed**.

Mapping strategy once an official exam guide/objectives document (if one exists beyond the public certification pages) is located:

1. File it under `sources/exam_guide/`.
2. Update `research/cdmp_exam_overview.md` §3 ("Approximate Exam Weighting") to cite it directly, replacing the prep-vendor-sourced estimate.
3. Any Knowledge Area file's "CDMP Exam Focus" section (`knowledge_base/*.md` §8) that was written against the old estimate gets flagged for review — not silently overwritten, since this task explicitly excludes rewriting existing knowledge files.
4. When the Practitioner phase begins, the same process applies to the 2 chosen Specialist exam guides.

**Priority note:** an official DAMA exam guide, if found, outranks `research/cdmp_exam_overview.md`'s current estimates (see §5 priority rules below).

---

## 3. Official DAMA Resources

Resources to track under `sources/dama_official/`:

- **dama.org** — Certification & Exam Information pages, CDMP Certification Levels page (already cited in `research/cdmp_exam_overview.md`), Knowledge Area overview pages.
- **DAMA Dictionary of Data Management Terminology** — definitional cross-reference for role/term precision (Owner/Steward/Custodian and similar recurring exam-trap terminology).
- **DAMA International chapter resources** — local chapter webinars, published FAQs, official errata for DMBOK2 editions.

Rule: link and cite, do not mirror content. A `sources/dama_official/` entry is a URL + a short note on what it's useful for, not a copy of the page.

---

## 4. Industry References

Two distinct categories, both tracked under `sources/industry/`:

**A. Named regulations/standards** — real, independently citable, not DAMA property. Already used informally in `knowledge_base/data_governance.md` §6 and §14:
- BCBS 239 (Basel Committee — risk data aggregation and reporting)
- HIPAA (U.S. — Protected Health Information)
- GDPR (EU — personal data)
- Expected to expand to: ISO 8000 (data quality), ISO/IEC 11179 (metadata registries), and similar standards as later Knowledge Areas (Data Quality, Metadata Management, Data Security) are studied.

**B. Practitioner/secondary sources** — prep-provider material, technical blogs, modern architecture conventions (data mesh, lakehouse zones). These are the **lowest-priority** source tier (see §5) — useful for real-world grounding (`[Industry Practice]` tag) and for practice-question *style*, never as the basis for an exam-fact claim. Cross-check anything from this tier against DMBOK2 before treating it as fact.

---

## 5. Source Priority Rules

When sources conflict, resolve using this hierarchy, highest authority first:

1. **DAMA-DMBOK2 (2nd Edition)** — the exam's actual content source. Wins on any question of DMBOK2 terminology, framework, or definition.
2. **Official DAMA/CDMP exam guide + dama.org pages** — authoritative for exam *mechanics* (format, timing, scoring, structure) and, if an objectives document is found, for KA weighting.
3. **DAMA Dictionary of Data Management Terminology** — authoritative for precise definitional wording when DMBOK2's chapter prose is ambiguous.
4. **Named regulations/standards directly cited by DMBOK2 or a Knowledge Area** (BCBS 239, HIPAA, GDPR, ISO 8000, etc.) — authoritative for their own domain, used to ground DAMA concepts in real enforcement, never to override DAMA's framing of a concept.
5. **Reputable CDMP prep-provider material** — usable for practice-question format/style and for filling the exam-weighting gap directionally (as already done in `research/cdmp_exam_overview.md`), but must be cross-checked against DMBOK2 before being stated as fact. Never cited as if it were DAMA-official.
6. **General industry blogs/practitioner content** — lowest priority. Usable only for `[Industry Practice]`-tagged real-world grounding (tool categories, modern architecture patterns). Never used to support an exam-fact or DAMA-definitional claim.

**Conflict resolution rule:** if two sources at different tiers disagree, the higher tier wins and the lower-tier claim is dropped or explicitly re-tagged as `[Industry Practice]` rather than presented as DAMA fact. If two sources at the **same** tier disagree (e.g., two prep vendors give different KA weight percentages), don't average or guess — log it as an open question (see the existing "Open Questions" pattern in `research/cdmp_exam_overview.md`) rather than silently picking one.

**Uncertainty rule:** if recall of an exact DMBOK2 detail (an enumerated list, a specific percentage, exact wording) is uncertain, tag it explicitly as uncertain in the knowledge file rather than presenting it as verbatim fact — this convention is already established in `knowledge_base/data_governance.md`'s editorial note and applies project-wide.

---

## Related

- `sources/README.md` — folder structure and the no-copyrighted-content rule this map depends on.
- `research/cdmp_exam_overview.md` — exam mechanics; §2 and its "Open Questions" section are the first things to update once an official exam guide is sourced.
- `knowledge_base/README.md` — the per-KA file template that DMBOK2 chapter content maps into.
- `CLAUDE.md` — Source Hierarchy Rules section (top-level pointer to this file for anyone/anything working in this project).
