from pydantic import BaseModel, Field
from typing import List


class EditAndRefineNovelOutput(BaseModel):
    """Pydantic model for edit_and_refine_novel node outputs."""
    edited_novel_content: str = (
        Field(..., description="The refined content of the novel")
    )
    revision_notes: List[str] = (
        Field(..., description="List of notes and comments made during the revision process")
    )
    error_correction_count: int = (
        Field(..., description="The number of errors corrected during the editing process")
    )
    pacing_issues_resolved: bool = (
        Field(..., description="Whether pacing issues in the novel have been resolved")
    )
    character_consistency_checks: List[bool] = (
        Field(..., description="List of checks for character consistency throughout the novel")
    )


class ProofreadAndPublishNovelOutput(BaseModel):
    """Pydantic model for proofread_and_publish_novel node outputs."""
    publication_status: bool = (
        Field(..., description="Whether the novel has been successfully published")
    )
    error_count: int = (
        Field(..., description="Number of errors found during proofreading")
    )
    typos_corrected: List[str] = (
        Field(..., description="List of typos corrected during proofreading")
    )
    publication_format: str = (
        Field(..., description="Format of the published novel (e.g. eBook, paperback, hardcover)")
    )
    publication_date: str = Field(..., description="Date of publication")


def proofread_and_publish_novel(edit_and_refine_novel_input: EditAndRefineNovelOutput, **kwargs) -> ProofreadAndPublishNovelOutput:
    """
    Proofread and publish the novel.

    Parameters
    ----------
    edited_novel_content : str
        The refined content of the novel from the edit_and_refine_novel node

    Returns
    -------
    dict
        A dictionary containing the publication status, error count, typos
        corrected, publication format, and publication date

    Raises
    ------
    ValueError
        If the input novel content is empty or invalid

    Examples
    --------
    >>> proofread_and_publish_novel(edited_novel_content='The final draft of the
    novel.')
    {'publication_status': True, 'error_count': 0, 'typos_corrected': [],
    'publication_format': 'eBook', 'publication_date': '2024-01-01'}

    >>> proofread_and_publish_novel(edited_novel_content='The novel with
    typos.')
    {'publication_status': True, 'error_count': 1, 'typos_corrected': ['typo1'],
    'publication_format': 'paperback', 'publication_date': '2024-01-15'}

    """
    return ProofreadAndPublishNovelOutput(
        publication_status=False,
        error_count=0,
        typos_corrected=[],
        publication_format="",
        publication_date="",
    )