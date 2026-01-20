from pydantic import BaseModel, Field
from typing import List


class WriteFirstDraftOfNovelOutput(BaseModel):
    """Pydantic model for write_first_draft_of_novel node outputs."""
    novel_title: str = Field(..., description="The title of the novel")
    protagonist_name: str = (
        Field(..., description="Name of the protagonist as defined in the character profile")
    )
    dragon_name: str = (
        Field(..., description="Name or designation of the dragon as defined in the character profile")
    )
    chapter_titles: List[str] = (
        Field(..., description="List of chapter titles in order")
    )
    chapter_summaries: List[str] = (
        Field(..., description="Brief summary of each chapter aligned with chapter_titles")
    )
    key_events: List[str] = (
        Field(..., description="List of major events that occur in the novel, each described in a single sentence")
    )
    theme: str = Field(..., description="Primary theme or moral of the story")
    word_count: int = (
        Field(..., description="Estimated total word count of the first draft")
    )


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


def edit_and_refine_novel(write_first_draft_of_novel_input: WriteFirstDraftOfNovelOutput, **kwargs) -> EditAndRefineNovelOutput:
    """
    Revises and refines the novel based on the first draft, ensuring it is
    engaging, well-paced, and free of errors.

    Parameters
    ----------
    first_draft : dict
        The output of the write_first_draft_of_novel node, containing the
        novel's title, protagonist name, dragon name, chapter titles,
        chapter summaries, key events, theme, and word count.

    Returns
    -------
    dict
        A dictionary containing the edited novel content, revision notes,
        error correction count, pacing issues resolved, and character
        consistency checks.

    Raises
    ------
    ValueError
        If the input first draft is invalid or incomplete.

    Examples
    --------
    >>> first_draft = {'novel_title': 'My Novel', 'protagonist_name': 'John',
    'dragon_name': 'Dragon', 'chapter_titles': ['Chapter 1', 'Chapter 2'],
    'chapter_summaries': ['Summary 1', 'Summary 2'], 'key_events': ['Event 1',
    'Event 2'], 'theme': 'My Theme', 'word_count': 1000}
    >>> edited_novel = edit_and_refine_novel(first_draft)
    {'edited_novel_content': 'Refined novel content', 'revision_notes': ['Note
    1', 'Note 2'], 'error_correction_count': 5, 'pacing_issues_resolved': True,
    'character_consistency_checks': [True, False]}

    """
    return EditAndRefineNovelOutput(
        edited_novel_content="",
        revision_notes=[],
        error_correction_count=0,
        pacing_issues_resolved=False,
        character_consistency_checks=[],
    )