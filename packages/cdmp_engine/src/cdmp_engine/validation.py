"""The Validation Layer: metadata, required-field, and answer-shape validation.

Wraps `cdmp_content_schema.Question`'s Pydantic validation (which already
enforces every required field, enum value, and the answer-shape rules from
answer_evaluation.md's Core Rule) and translates its errors into the
file/field/reason shape quiz_engine/data_loading.md's Error Reporting
section requires -- "the file path, the specific reason, and, for schema
violations, the specific field and expected vs. actual value" -- mirroring
DOMAIN_MODEL.md's `ValidationResult` value object.

This module owns *how a validation outcome is reported*; `loader.py` owns
*discovering and parsing files*, and calls into this module per file.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, ValidationError

from cdmp_content_schema import Question


class FieldError(BaseModel):
    """One field-level validation failure."""

    model_config = ConfigDict(frozen=True)

    field: str
    expected: str
    actual: str
    reason: str


class ValidationResult(BaseModel):
    """The outcome of validating one raw record against the content schema."""

    model_config = ConfigDict(frozen=True)

    file_path: str
    passed: bool
    errors: tuple[FieldError, ...] = ()
    warnings: tuple[str, ...] = ()
    question: Question | None = None
    """The successfully parsed record, present only when `passed` is True."""


def _field_path(loc: tuple) -> str:
    return ".".join(str(part) for part in loc) or "(root)"


def _to_field_errors(exc: ValidationError) -> tuple[FieldError, ...]:
    errors = []
    for err in exc.errors():
        errors.append(
            FieldError(
                field=_field_path(err["loc"]),
                expected=err["type"],
                actual=repr(err.get("input")),
                reason=err["msg"],
            )
        )
    return tuple(errors)


def _warnings_for(question: Question) -> tuple[str, ...]:
    warnings: list[str] = []
    if question.dama_concept is None and question.industry_practice_concept is None:
        warnings.append(
            "neither dama_concept nor industry_practice_concept is populated "
            "(metadata_schema.md: a question typically populates one or both)"
        )
    if question.estimated_solving_time > 0 and len(question.stem) / question.estimated_solving_time > 5:
        warnings.append(
            f"estimated_solving_time ({question.estimated_solving_time}s) looks low "
            f"for a {len(question.stem)}-character stem"
        )
    return tuple(warnings)


def validate_question_record(raw: dict, file_path: str) -> ValidationResult:
    """Validate one raw (already-YAML-parsed) record against the content schema.

    Never raises: a schema violation is reported as a failed `ValidationResult`,
    not an exception, so a single bad record never halts a batch load
    (data_loading.md: "a single malformed or invalid file never halts the load").
    """
    try:
        question = Question(**raw, source_path=file_path)
    except ValidationError as exc:
        return ValidationResult(file_path=file_path, passed=False, errors=_to_field_errors(exc))
    return ValidationResult(
        file_path=file_path,
        passed=True,
        question=question,
        warnings=_warnings_for(question),
    )
