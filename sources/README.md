# Sources

This directory is the intake point for authoritative CDMP/DMBOK2 references — where they come from, how they're tracked, and what's allowed to live here. It exists so that `knowledge_base/` content can be traced back to a specific, citable source rather than reconstructed from memory.

**Full mapping strategy, priority rules, and conflict resolution live in [`research/source_map.md`](../research/source_map.md). This README only covers what belongs in each folder below.**

## Hard rule: no copyrighted content

**Never store verbatim DMBOK2 text, scanned/copied pages, PDFs of the book, or any other copyrighted material in this repo.** This directory holds:

- **Citations** — chapter/section/page references (e.g., "DMBOK2 2nd Ed., Ch.3, p.63") pointing to material you own or have legitimate access to elsewhere.
- **Paraphrased summaries** — your own words, synthesizing a concept, always tagged per the convention in `research/source_map.md`.
- **Links** — to official DAMA pages, public regulatory texts, and freely-licensed standards documentation.

Short (<25 word) quoted fragments used for direct definitional precision are acceptable if clearly marked as a quote with a citation. Anything longer gets paraphrased.

## Folder structure

| Folder | Purpose |
|---|---|
| `dmbok2/` | Personal chapter notes and a page/section index for DAMA-DMBOK2, 2nd Edition — your own summaries, not reproductions. |
| `exam_guide/` | Notes on the official CDMP/DMF exam guide (format, scoring, objectives) once located, plus Specialist exam guides when that phase starts. |
| `dama_official/` | Links and notes on official DAMA International resources: dama.org pages, the DAMA Dictionary, chapter webinars. |
| `industry/` | Named regulations, standards, and reputable secondary sources that DMBOK2 itself references or that provide real-world grounding (e.g., BCBS 239, HIPAA, GDPR, ISO 8000). |

Each folder currently contains a placeholder `README.md` describing what will go there — no source content has been added yet. Population happens incrementally, source by source, not as a bulk import.
