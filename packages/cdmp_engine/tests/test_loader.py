"""Tests for cdmp_engine.loader: discovery, parsing, the lifecycle filter, and the index."""

from __future__ import annotations

from cdmp_content_schema import Difficulty, KnowledgeAreaCode
from cdmp_engine.loader import load_questions


def test_recursive_discovery_finds_files_across_ka_folders(write_question, questions_root):
    write_question("GOV-001.yaml", ka_folder="data_governance", question_id="GOV-001")
    write_question(
        "QUAL-001.yaml",
        ka_folder="data_quality",
        question_id="QUAL-001",
        knowledge_area="QUAL",
        related_knowledge_areas=["QUAL"],
    )

    index, report = load_questions(questions_root, include_unreviewed=True)

    assert report.total_files == 2
    assert len(index) == 2


def test_load_questions_returns_valid_record(write_question, questions_root):
    write_question("GOV-001.yaml")

    index, report = load_questions(questions_root)

    assert report.rejected == ()
    assert len(index) == 1
    question = index.all()[0]
    assert question.question_id == "TEST-001"
    assert question.knowledge_area == KnowledgeAreaCode.GOV
    assert question.correct_answer == "B"


def test_malformed_yaml_is_skipped_not_fatal(write_question, questions_root):
    write_question("good.yaml")
    bad_path = questions_root / "data_governance" / "bad.yaml"
    bad_path.parent.mkdir(parents=True, exist_ok=True)
    bad_path.write_text("not: [valid: yaml", encoding="utf-8")

    index, report = load_questions(questions_root)

    assert len(index) == 1
    assert report.rejected_count == 1
    assert "bad.yaml" in report.rejected[0].file_path


def test_missing_required_field_is_rejected_with_specific_reason(write_question, questions_root):
    write_question("missing_field.yaml", question_id="BAD-001")
    path = questions_root / "data_governance" / "missing_field.yaml"
    import yaml

    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    del data["explanation"]
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")

    index, report = load_questions(questions_root)

    assert len(index) == 0
    assert report.rejected_count == 1
    assert any(err.field == "explanation" for err in report.rejected[0].errors)


def test_invalid_enum_value_is_rejected(write_question, questions_root):
    write_question("bad_difficulty.yaml", difficulty="Impossible")

    index, report = load_questions(questions_root)

    assert len(index) == 0
    assert report.rejected_count == 1
    assert any(err.field == "difficulty" for err in report.rejected[0].errors)


def test_one_bad_file_does_not_block_other_valid_files(write_question, questions_root):
    write_question("good.yaml", question_id="GOOD-001")
    write_question("bad.yaml", question_id="BAD-001", difficulty="NotReal")

    index, report = load_questions(questions_root)

    assert [q.question_id for q in index.all()] == ["GOOD-001"]
    assert report.rejected_count == 1


def test_status_filtering_excludes_draft_by_default(write_question, questions_root):
    write_question(
        "draft.yaml",
        question_id="DFT-001",
        review_status="Draft",
        approval_status="Pending",
        reviewer=[],
    )
    write_question("published.yaml", question_id="PUB-001", review_status="Published")

    index, report = load_questions(questions_root)  # default: include_unreviewed=False

    assert {q.question_id for q in index.all()} == {"PUB-001"}
    assert report.excluded_non_published_count == 1
    assert report.indexed_count == 1


def test_dev_mode_includes_draft_when_explicitly_allowed(write_question, questions_root):
    write_question(
        "draft.yaml",
        question_id="DFT-001",
        review_status="Draft",
        approval_status="Pending",
        reviewer=[],
    )

    index, report = load_questions(questions_root, include_unreviewed=True)

    assert {q.question_id for q in index.all()} == {"DFT-001"}
    assert report.excluded_non_published_count == 0


def test_load_report_counts_are_internally_consistent(write_question, questions_root):
    write_question(
        "draft.yaml",
        question_id="DFT-001",
        review_status="Draft",
        approval_status="Pending",
        reviewer=[],
    )
    write_question("published.yaml", question_id="PUB-001", review_status="Published")
    write_question("bad.yaml", question_id="BAD-001", difficulty="NotReal")

    _, report = load_questions(questions_root)

    assert report.total_files == 3
    assert report.indexed_count + report.excluded_non_published_count + report.rejected_count == report.total_files


def test_index_by_knowledge_area(write_question, questions_root):
    write_question("GOV-001.yaml", question_id="GOV-001", knowledge_area="GOV", related_knowledge_areas=["GOV"])
    write_question(
        "QUAL-001.yaml",
        ka_folder="data_quality",
        question_id="QUAL-001",
        knowledge_area="QUAL",
        related_knowledge_areas=["QUAL"],
    )

    index, _ = load_questions(questions_root)

    gov_questions = index.by_knowledge_area(KnowledgeAreaCode.GOV)
    assert [q.question_id for q in gov_questions] == ["GOV-001"]
    assert index.by_knowledge_area(KnowledgeAreaCode.ARCH) == ()


def test_index_by_difficulty(write_question, questions_root):
    write_question("beginner.yaml", question_id="BEG-001", difficulty="Beginner")
    write_question("expert.yaml", question_id="EXP-001", difficulty="Expert")

    index, _ = load_questions(questions_root)

    assert [q.question_id for q in index.by_difficulty(Difficulty.EXPERT)] == ["EXP-001"]
    assert index.by_difficulty(Difficulty.ADVANCED) == ()


def test_load_questions_on_missing_directory_returns_empty_index(tmp_path):
    missing = tmp_path / "does_not_exist"

    index, report = load_questions(missing)

    assert len(index) == 0
    assert report.total_files == 0
