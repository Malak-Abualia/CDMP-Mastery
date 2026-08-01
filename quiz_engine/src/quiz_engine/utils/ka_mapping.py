"""Knowledge Area folder-name <-> code mapping.

Mirrors the table in question_bank/naming_conventions.md and the physical
layout of question_bank/questions/ (one folder per Knowledge Area, named
after the corresponding knowledge_base/*.md module). The CLI accepts the
folder-style name (e.g. "data_quality"); question records store the short
code (e.g. "QUAL") in their `knowledge_area` field.
"""

from __future__ import annotations

FOLDER_TO_CODE = {
    "data_governance": "GOV",
    "data_architecture": "ARCH",
    "data_modeling_and_design": "MODEL",
    "data_storage_and_operations": "STOR",
    "data_security": "SEC",
    "data_integration_and_interoperability": "INTEG",
    "document_and_content_management": "DOC",
    "reference_and_master_data": "MASTER",
    "data_warehousing_and_business_intelligence": "DWBI",
    "metadata_management": "META",
    "data_quality": "QUAL",
    "big_data_and_data_science": "BIGDATA",
    "data_management_maturity_assessment": "MAT",
    "data_ethics": "ETH",
}

CODE_TO_FOLDER = {code: folder for folder, code in FOLDER_TO_CODE.items()}


def resolve_ka_code(value: str) -> str:
    """Resolve a user-supplied Knowledge Area identifier to its code.

    Accepts either the folder-style name (e.g. "data_quality") or the KA
    code itself (e.g. "QUAL"), case-insensitively.

    Raises:
        KeyError: if `value` is not a recognized folder name or code.
    """
    normalized = value.strip().lower()
    if normalized in FOLDER_TO_CODE:
        return FOLDER_TO_CODE[normalized]
    upper = value.strip().upper()
    if upper in CODE_TO_FOLDER:
        return upper
    raise KeyError(value)
