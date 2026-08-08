"""Integration test: load the real question_bank/questions data (read-only).

Confirms the Loader works against the actual project content, not just
synthetic fixtures. Expectations are derived at test time directly from an
independent scan of question_bank/questions/ (the single authoritative
source for "what's actually in the bank right now"), rather than from a
hardcoded snapshot count -- research/question_bank_phase1_validation.md's
120-question, 6-Knowledge-Area, zero-Published figures were accurate as of
that report's date (2026-08-01) but describe a since-superseded Phase 1
milestone, not the current state of the repository (see
question_bank/roadmap.md and question_bank/taxonomy.md's 14-Knowledge-Area
Index). Deriving from a live scan means these tests keep documenting the
current repository state as the bank continues to grow, instead of going
stale again the next time a question is authored or published.

The independent scan below intentionally bypasses `load_questions` (reading
each YAML file directly) so these tests cross-check the loader's discovery,
parsing, and status-filtering behavior against the real files rather than
just restating the loader's own output back at itself.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import List

import yaml

from quiz_engine.loader.yaml_loader import load_questions
from quiz_engine.utils.paths import default_question_bank_path


def _scan_raw_question_records(path: Path) -> List[dict]:
    """Parse every .yaml file's raw fields directly, independent of the loader."""
    return [
        yaml.safe_load(p.read_text(encoding="utf-8"))
        for p in sorted(path.rglob("*.yaml"))
    ]


def test_real_question_bank_loads_with_no_errors():
    path = default_question_bank_path()
    raw_records = _scan_raw_question_records(path)

    result = load_questions(path, allowed_statuses=("Draft", "Published"))

    assert result.errors == []
    assert len(result.questions) == len(raw_records)


def test_real_question_bank_ka_counts_match_source_files():
    path = default_question_bank_path()
    raw_records = _scan_raw_question_records(path)
    expected_counts = dict(Counter(record["knowledge_area"] for record in raw_records))

    result = load_questions(path, allowed_statuses=("Draft", "Published"))
    counts = Counter(q.knowledge_area for q in result.questions)

    assert dict(counts) == expected_counts


def test_real_question_bank_default_strict_mode_matches_published_count():
    """Documents the current, honest state: only Published questions load by
    default; everything still in Draft (per question_bank/question_lifecycle.md)
    is correctly excluded unless a caller explicitly opts into unreviewed content."""
    path = default_question_bank_path()
    raw_records = _scan_raw_question_records(path)
    expected_published = sum(
        1 for record in raw_records if record["review_status"] == "Published"
    )
    expected_skipped = len(raw_records) - expected_published

    result = load_questions(path)  # default: allowed_statuses=("Published",)

    assert len(result.questions) == expected_published
    assert result.skipped_by_status == expected_skipped
