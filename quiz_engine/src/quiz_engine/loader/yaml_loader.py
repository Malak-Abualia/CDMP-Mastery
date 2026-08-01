"""Discovers, parses, validates, and loads question_bank YAML records.

Strictly read-only: this module never writes to question_bank/questions
under any circumstance. Implements the pipeline in quiz_engine/data_loading.md
(discover -> parse -> validate -> lifecycle filter -> index), including
that document's central rule: by default, only `review_status: "Published"`
questions are eligible to load. As of Phase 1 (research/question_bank_phase1_validation.md),
every question in the bank is currently "Draft" -- under the default
allowed_statuses, that means zero questions load today, by design. Pass a
wider `allowed_statuses` (e.g. including "Draft") to load unreviewed
content anyway; every caller that does so is responsible for making that
loud and explicit to the end user (see quiz_engine/data_loading.md,
"Lifecycle Filter", and quiz_engine/cli_design.md's `--dev-unreviewed` flag).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Sequence

import yaml

from ..models.question import Question, WhyIncorrect
from ..utils.exceptions import QuestionParseError
from .validation import validate_question_dict

DEFAULT_ALLOWED_STATUSES: Sequence[str] = ("Published",)


@dataclass
class LoadError:
    """One file that failed to parse or validate, and why."""

    path: str
    reason: str


@dataclass
class LoadResult:
    """The outcome of loading a directory tree of question files."""

    questions: List[Question] = field(default_factory=list)
    errors: List[LoadError] = field(default_factory=list)
    skipped_by_status: int = 0


def discover_question_files(base_path: Path) -> List[Path]:
    """Recursively find every .yaml file under base_path, sorted for determinism."""
    if not base_path.is_dir():
        return []
    return sorted(base_path.rglob("*.yaml"))


def _parse_yaml_file(path: Path) -> dict:
    try:
        with path.open("r", encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
    except yaml.YAMLError as exc:
        raise QuestionParseError(str(path), f"invalid YAML: {exc}") from exc
    if not isinstance(data, dict):
        raise QuestionParseError(str(path), "top-level YAML content is not a mapping")
    return data


def build_question(data: dict, source_path: str) -> Question:
    """Construct a Question from an already-validated raw dict.

    Callers must run `validate_question_dict` first; this function assumes
    every required key is present and does not re-check.
    """
    why_incorrect = [
        WhyIncorrect(option=entry["option"], reason=entry["reason"])
        for entry in data["why_incorrect"]
    ]
    return Question(
        question_id=data["question_id"],
        version=data["version"],
        knowledge_area=data["knowledge_area"],
        topic=data["topic"],
        subtopic=data["subtopic"],
        difficulty=data["difficulty"],
        blooms_level=data["blooms_level"],
        learning_objective=data["learning_objective"],
        dama_concept=data.get("dama_concept"),
        industry_practice_concept=data.get("industry_practice_concept"),
        keywords=list(data["keywords"]),
        estimated_solving_time=data["estimated_solving_time"],
        question_type=data["question_type"],
        stem=data["stem"],
        answer_choices=list(data["answer_choices"]),
        correct_answer=data["correct_answer"],
        explanation=data["explanation"],
        why_incorrect=why_incorrect,
        related_knowledge_areas=list(data["related_knowledge_areas"]),
        related_flashcards=list(data.get("related_flashcards") or []),
        related_exercises=list(data.get("related_exercises") or []),
        references=list(data["references"]),
        source_confidence=data["source_confidence"],
        review_status=data["review_status"],
        approval_status=data["approval_status"],
        author=data["author"],
        reviewer=list(data.get("reviewer") or []),
        creation_date=str(data["creation_date"]),
        last_modified=str(data["last_modified"]),
        source_path=source_path,
    )


def load_questions(
    base_path: Path,
    allowed_statuses: Sequence[str] = DEFAULT_ALLOWED_STATUSES,
) -> LoadResult:
    """Load every eligible question under base_path.

    A single malformed or schema-invalid file is skipped and recorded in
    the result's `errors` list; it never aborts the whole load (per
    quiz_engine/data_loading.md's pipeline diagram). Only questions whose
    `review_status` is in `allowed_statuses` are returned.
    """
    result = LoadResult()

    for path in discover_question_files(Path(base_path)):
        try:
            data = _parse_yaml_file(path)
        except QuestionParseError as exc:
            result.errors.append(LoadError(path=str(path), reason=str(exc)))
            continue

        validation_errors = validate_question_dict(data)
        if validation_errors:
            result.errors.append(
                LoadError(path=str(path), reason="; ".join(validation_errors))
            )
            continue

        if data["review_status"] not in allowed_statuses:
            result.skipped_by_status += 1
            continue

        result.questions.append(build_question(data, source_path=str(path)))

    return result
