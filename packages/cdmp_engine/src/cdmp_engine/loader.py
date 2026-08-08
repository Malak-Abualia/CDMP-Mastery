"""The Question Loader: discover, parse, validate, and index question_bank/questions/**/*.yaml.

Implements quiz_engine/data_loading.md's Loading Pipeline end to end:
discovery -> YAML parse -> schema validation (delegated to validation.py)
-> the Published/Draft lifecycle filter -> an in-memory index. A single
malformed or invalid file never halts the load; it is rejected and
reported, per data_loading.md's explicit "never halts the load" rule.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict

from cdmp_content_schema import Difficulty, KnowledgeAreaCode, Question, ReviewStatus
from cdmp_engine.validation import FieldError, ValidationResult, validate_question_record


def default_questions_dir() -> Path:
    """The real question_bank/questions/ directory, resolved relative to this package.

    packages/cdmp_engine/src/cdmp_engine/loader.py -> repo root is four
    levels up -- resolved this way (not a hardcoded absolute path or an
    env var) so the loader works from any working directory once the
    package is installed, without requiring configuration for this sprint's
    single, fixed content location.
    """
    repo_root = Path(__file__).resolve().parents[4]
    return repo_root / "question_bank" / "questions"


class LoadReport(BaseModel):
    """Summary of one load run -- data_loading.md's Error Reporting, at batch scope."""

    model_config = ConfigDict(frozen=True)

    total_files: int
    indexed_count: int
    excluded_non_published_count: int
    rejected: tuple[ValidationResult, ...] = ()
    """Files that failed YAML parsing or schema validation."""
    warned_count: int = 0

    @property
    def rejected_count(self) -> int:
        return len(self.rejected)


class QuestionIndex:
    """In-memory index of loaded questions, queryable by Knowledge Area and difficulty.

    data_loading.md's Indexing step: "organized into an in-memory index
    supporting fast lookup by every dimension question_selection.md's modes
    need." This sprint's three modes (Practice/Knowledge Area/Difficulty)
    need KA and difficulty lookup; topic/Bloom's/keyword indices are not
    built because no mode or scoring path in this sprint queries by them
    directly (scoring's topic breakdown groups the already-loaded question
    list in memory, per-session, rather than needing a standing index).
    """

    def __init__(self, questions: list[Question]) -> None:
        self._questions: tuple[Question, ...] = tuple(questions)
        self._by_ka: dict[KnowledgeAreaCode, list[Question]] = defaultdict(list)
        self._by_difficulty: dict[Difficulty, list[Question]] = defaultdict(list)
        for question in self._questions:
            self._by_ka[question.knowledge_area].append(question)
            self._by_difficulty[question.difficulty].append(question)

    def __len__(self) -> int:
        return len(self._questions)

    def all(self) -> tuple[Question, ...]:
        return self._questions

    def by_knowledge_area(self, code: KnowledgeAreaCode) -> tuple[Question, ...]:
        return tuple(self._by_ka.get(code, ()))

    def by_difficulty(self, difficulty: Difficulty) -> tuple[Question, ...]:
        return tuple(self._by_difficulty.get(difficulty, ()))


def _parse_failure(file_path: str, error: yaml.YAMLError) -> ValidationResult:
    return ValidationResult(
        file_path=file_path,
        passed=False,
        errors=(
            FieldError(
                field="(file)",
                expected="parseable YAML",
                actual=file_path,
                reason=f"YAML parse error: {error}",
            ),
        ),
    )


def load_questions(base_dir: Path | None = None, *, include_unreviewed: bool = False) -> tuple[QuestionIndex, LoadReport]:
    """Load every question record under `base_dir`, apply the lifecycle filter, and index it.

    Strict mode (default, `include_unreviewed=False`) indexes only
    `review_status: Published` records -- data_loading.md's "most
    consequential rule," which must remain the default in every caller
    without an explicit override.
    """
    directory = base_dir if base_dir is not None else default_questions_dir()
    files = sorted(directory.rglob("*.yaml"))

    indexed: list[Question] = []
    rejected: list[ValidationResult] = []
    excluded_non_published = 0
    warned_count = 0

    for path in files:
        text = path.read_text(encoding="utf-8")
        try:
            raw = yaml.safe_load(text)
        except yaml.YAMLError as exc:
            rejected.append(_parse_failure(str(path), exc))
            continue

        result = validate_question_record(raw, str(path))
        if not result.passed:
            rejected.append(result)
            continue
        if result.warnings:
            warned_count += 1

        question = result.question
        assert question is not None  # passed implies question is set
        eligible = include_unreviewed or question.review_status == ReviewStatus.PUBLISHED
        if not eligible:
            excluded_non_published += 1
            continue
        indexed.append(question)

    report = LoadReport(
        total_files=len(files),
        indexed_count=len(indexed),
        excluded_non_published_count=excluded_non_published,
        rejected=tuple(rejected),
        warned_count=warned_count,
    )
    return QuestionIndex(indexed), report
