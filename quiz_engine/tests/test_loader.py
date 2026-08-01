"""Tests for quiz_engine.loader: recursive discovery, parsing, validation, status filtering."""

from __future__ import annotations

import yaml

from quiz_engine.loader.yaml_loader import discover_question_files, load_questions


def test_recursive_discovery_finds_files_across_ka_folders(write_question, questions_root):
    write_question("GOV-001.yaml", ka_folder="data_governance", question_id="GOV-001")
    write_question("QUAL-001.yaml", ka_folder="data_quality", question_id="QUAL-001", knowledge_area="QUAL")

    found = discover_question_files(questions_root)

    assert len(found) == 2


def test_discover_on_missing_directory_returns_empty_list(tmp_path):
    missing = tmp_path / "does_not_exist"
    assert discover_question_files(missing) == []


def test_load_questions_returns_valid_record(write_question, questions_root):
    write_question("GOV-001.yaml")

    result = load_questions(questions_root, allowed_statuses=("Published",))

    assert result.errors == []
    assert len(result.questions) == 1
    question = result.questions[0]
    assert question.question_id == "TEST-001"
    assert question.knowledge_area == "GOV"
    assert question.correct_answer == "B"


def test_malformed_yaml_is_skipped_not_fatal(write_question, questions_root):
    write_question("good.yaml")
    bad_path = questions_root / "data_governance" / "bad.yaml"
    bad_path.write_text("not: [valid: yaml", encoding="utf-8")

    result = load_questions(questions_root, allowed_statuses=("Published",))

    assert len(result.questions) == 1
    assert len(result.errors) == 1
    assert "bad.yaml" in result.errors[0].path


def test_missing_required_field_is_rejected_with_specific_reason(write_question, questions_root):
    path = write_question("missing_field.yaml")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    del data["explanation"]
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")

    result = load_questions(questions_root, allowed_statuses=("Published",))

    assert result.questions == []
    assert len(result.errors) == 1
    assert "explanation" in result.errors[0].reason


def test_invalid_enum_value_is_rejected(write_question, questions_root):
    write_question("bad_difficulty.yaml", difficulty="Impossible")

    result = load_questions(questions_root, allowed_statuses=("Published",))

    assert result.questions == []
    assert "difficulty" in result.errors[0].reason


def test_one_bad_file_does_not_block_other_valid_files(write_question, questions_root):
    write_question("good.yaml", question_id="GOOD-1")
    write_question("bad.yaml", question_id="BAD-1", difficulty="NotReal")

    result = load_questions(questions_root, allowed_statuses=("Published",))

    assert [q.question_id for q in result.questions] == ["GOOD-1"]
    assert len(result.errors) == 1


def test_status_filtering_excludes_draft_by_default(write_question, questions_root):
    write_question("draft.yaml", question_id="TEST-DRAFT", review_status="Draft")
    write_question("published.yaml", question_id="TEST-PUB", review_status="Published")

    result = load_questions(questions_root)  # default allowed_statuses = ("Published",)

    assert {q.question_id for q in result.questions} == {"TEST-PUB"}
    assert result.skipped_by_status == 1


def test_dev_mode_includes_draft_when_explicitly_allowed(write_question, questions_root):
    write_question("draft.yaml", question_id="TEST-DRAFT", review_status="Draft")

    result = load_questions(questions_root, allowed_statuses=("Draft", "Published"))

    assert {q.question_id for q in result.questions} == {"TEST-DRAFT"}
    assert result.skipped_by_status == 0
