"""Integration test: load the real question_bank/questions data (read-only).

Confirms the Question Loader works against the actual project content, not
just synthetic fixtures, and stays in sync with the current ground truth:
307 question records across all 14 Knowledge Areas, 140 Published / 167
Draft. Six Knowledge Areas (GOV, MODEL, QUAL, META, ARCH, MASTER) were
expanded from 20 to 26-28 questions each in a source-verification-driven
gap-filling batch; all newly added questions are Draft, so the Published
totals/per-KA breakdown are unchanged from the prior snapshot.
"""

from __future__ import annotations

from collections import Counter

from cdmp_content_schema import QuestionType
from cdmp_engine.loader import default_questions_dir, load_questions

EXPECTED_TOTAL_BY_KA = {
    "GOV": 28,
    "ARCH": 26,
    "MODEL": 27,
    "STOR": 20,
    "SEC": 20,
    "INTEG": 20,
    "DOC": 20,
    "MASTER": 27,
    "DWBI": 20,
    "META": 26,
    "QUAL": 27,
    "BIGDATA": 20,
    "MAT": 6,
    "ETH": 20,
}

EXPECTED_PUBLISHED_BY_KA = {
    "BIGDATA": 20,
    "DOC": 20,
    "DWBI": 20,
    "ETH": 20,
    "INTEG": 20,
    "SEC": 20,
    "STOR": 20,
}


def test_default_questions_dir_resolves_to_the_real_question_bank():
    path = default_questions_dir()

    assert path.is_dir()
    assert path.parts[-2:] == ("question_bank", "questions")


def test_real_question_bank_loads_all_307_records_with_zero_rejections():
    index, report = load_questions(include_unreviewed=True)

    assert report.total_files == 307
    assert report.rejected == ()
    assert len(index) == 307


def test_real_question_bank_strict_mode_yields_140_published():
    index, report = load_questions()  # default: Published-only

    assert len(index) == 140
    assert report.excluded_non_published_count == 167
    assert report.rejected == ()


def test_real_question_bank_total_counts_match_per_knowledge_area():
    index, _ = load_questions(include_unreviewed=True)

    counts = Counter(q.knowledge_area.value for q in index.all())

    assert dict(counts) == EXPECTED_TOTAL_BY_KA


def test_real_question_bank_published_counts_match_per_knowledge_area():
    index, _ = load_questions()

    counts = Counter(q.knowledge_area.value for q in index.all())

    assert dict(counts) == EXPECTED_PUBLISHED_BY_KA


def test_gov_016_ingests_as_multi_select_shape_despite_scenario_based_label():
    """The known real-world edge case answer_evaluation.md's Core Rule exists for:
    GOV-016 is labeled 'Scenario-Based' but is Multiple-Select-shaped."""
    index, _ = load_questions(include_unreviewed=True)

    matches = [q for q in index.all() if q.question_id == "GOV-016"]

    assert len(matches) == 1
    gov_016 = matches[0]
    assert gov_016.question_type == QuestionType.SCENARIO_BASED
    assert gov_016.is_multi_select is True
    assert set(gov_016.correct_answer) == {"A", "B", "D"}
