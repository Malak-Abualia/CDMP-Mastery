"""Integration test: load the real question_bank/questions data (read-only).

Confirms the Loader works against the actual project content, not just
synthetic fixtures, and stays in sync with the verified counts in
research/question_bank_phase1_validation.md (120 questions, 20 per
Knowledge Area, all currently "Draft" as of Phase 1).
"""

from __future__ import annotations

from collections import Counter

from quiz_engine.loader.yaml_loader import load_questions
from quiz_engine.utils.paths import default_question_bank_path

EXPECTED_KA_COUNTS = {
    "GOV": 20,
    "MODEL": 20,
    "ARCH": 20,
    "QUAL": 20,
    "META": 20,
    "MASTER": 20,
}


def test_real_question_bank_loads_with_no_errors():
    path = default_question_bank_path()

    result = load_questions(path, allowed_statuses=("Draft", "Published"))

    assert result.errors == []
    assert len(result.questions) == 120


def test_real_question_bank_ka_counts_match_phase1_validation():
    path = default_question_bank_path()

    result = load_questions(path, allowed_statuses=("Draft", "Published"))

    counts = Counter(q.knowledge_area for q in result.questions)
    assert dict(counts) == EXPECTED_KA_COUNTS


def test_real_question_bank_default_strict_mode_yields_zero_published_today():
    """Documents the current, honest Phase 1 state: nothing has cleared review yet."""
    path = default_question_bank_path()

    result = load_questions(path)  # default: allowed_statuses=("Published",)

    assert result.questions == []
    assert result.skipped_by_status == 120
