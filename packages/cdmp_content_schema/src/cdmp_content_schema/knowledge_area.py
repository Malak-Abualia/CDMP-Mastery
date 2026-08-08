"""KnowledgeArea: the top of the classification hierarchy (DOMAIN_MODEL.md).

`KNOWLEDGE_AREAS` mirrors question_bank/naming_conventions.md's code table
and the physical layout of question_bank/questions/ (one folder per
Knowledge Area). It is the single source of truth this package exposes for
resolving a folder name or code to the other, so the loader and CLI don't
each hardcode their own copy.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from cdmp_content_schema.enums import KnowledgeAreaCode


class KnowledgeArea(BaseModel):
    """One row of the fixed, 14-entry Knowledge Area index."""

    model_config = ConfigDict(frozen=True)

    code: KnowledgeAreaCode
    name: str
    folder: str


KNOWLEDGE_AREAS: dict[KnowledgeAreaCode, KnowledgeArea] = {
    ka.code: ka
    for ka in (
        KnowledgeArea(code=KnowledgeAreaCode.GOV, name="Data Governance", folder="data_governance"),
        KnowledgeArea(code=KnowledgeAreaCode.ARCH, name="Data Architecture", folder="data_architecture"),
        KnowledgeArea(code=KnowledgeAreaCode.MODEL, name="Data Modeling and Design", folder="data_modeling_and_design"),
        KnowledgeArea(code=KnowledgeAreaCode.STOR, name="Data Storage and Operations", folder="data_storage_and_operations"),
        KnowledgeArea(code=KnowledgeAreaCode.SEC, name="Data Security", folder="data_security"),
        KnowledgeArea(code=KnowledgeAreaCode.INTEG, name="Data Integration and Interoperability", folder="data_integration_and_interoperability"),
        KnowledgeArea(code=KnowledgeAreaCode.DOC, name="Document and Content Management", folder="document_and_content_management"),
        KnowledgeArea(code=KnowledgeAreaCode.MASTER, name="Reference and Master Data", folder="reference_and_master_data"),
        KnowledgeArea(code=KnowledgeAreaCode.DWBI, name="Data Warehousing and Business Intelligence", folder="data_warehousing_and_business_intelligence"),
        KnowledgeArea(code=KnowledgeAreaCode.META, name="Metadata Management", folder="metadata_management"),
        KnowledgeArea(code=KnowledgeAreaCode.QUAL, name="Data Quality", folder="data_quality"),
        KnowledgeArea(code=KnowledgeAreaCode.BIGDATA, name="Big Data and Data Science", folder="big_data_and_data_science"),
        KnowledgeArea(code=KnowledgeAreaCode.MAT, name="Data Management Maturity Assessment", folder="data_management_maturity_assessment"),
        KnowledgeArea(code=KnowledgeAreaCode.ETH, name="Data Ethics", folder="data_ethics"),
    )
}

_FOLDER_TO_CODE: dict[str, KnowledgeAreaCode] = {ka.folder: ka.code for ka in KNOWLEDGE_AREAS.values()}


def resolve_ka_code(value: str) -> KnowledgeAreaCode:
    """Resolve a user-supplied Knowledge Area identifier to its code.

    Accepts either the folder-style name (e.g. "data_quality") or the KA
    code itself (e.g. "QUAL"), case-insensitively.

    Raises:
        ValueError: if `value` is not a recognized folder name or code.
    """
    normalized = value.strip().lower()
    if normalized in _FOLDER_TO_CODE:
        return _FOLDER_TO_CODE[normalized]
    upper = value.strip().upper()
    try:
        return KnowledgeAreaCode(upper)
    except ValueError:
        raise ValueError(f"Unrecognized Knowledge Area: {value!r}") from None
