from pydantic import BaseModel, Field
from typing import List


class DefineStoryPreconditionsOutput(BaseModel):
    """Pydantic model for define_story_preconditions node outputs."""
    protagonist_name: str = (
        Field(..., description="The name of the protagonist")
    )
    protagonist_age: int = Field(..., description="The age of the protagonist")
    protagonist_background: str = (
        Field(..., description="The background of the protagonist")
    )
    dragon_meeting_circumstances: str = (
        Field(..., description="How the protagonist meets the dragon")
    )
    protagonist_motivation: str = (
        Field(..., description="What motivates the protagonist to ride the dragon to the moon")
    )
    story_setting: str = Field(..., description="The setting of the story")


class CreateProtagonistCharacterProfileOutput(BaseModel):
    """Pydantic model for create_protagonist_character_profile node outputs."""
    protagonist_name: str = (
        Field(..., description="The name of the protagonist.")
    )
    age: int = Field(..., description="The age of the protagonist.")
    background: str = (
        Field(..., description="A brief background description of the protagonist.")
    )
    strengths: List[str] = (
        Field(..., description="List of the protagonist's key strengths.")
    )
    weaknesses: List[str] = (
        Field(..., description="List of the protagonist's key weaknesses.")
    )
    motivations: List[str] = (
        Field(..., description="List of the protagonist's motivations for the journey.")
    )
    emotions: List[str] = (
        Field(..., description="List of primary emotions the protagonist experiences throughout the story.")
    )


def create_protagonist_character_profile(define_story_preconditions_input: DefineStoryPreconditionsOutput, **kwargs) -> CreateProtagonistCharacterProfileOutput:
    """
    Creates a comprehensive character profile for the protagonist.

    Parameters
    ----------
    protagonist_name : str
        The name of the protagonist.
    protagonist_age : int
        The age of the protagonist.
    protagonist_background : str
        The background of the protagonist.
    protagonist_motivation : str
        What motivates the protagonist to ride the dragon to the moon.

    Returns
    -------
    {protagonist_name: str, age: int, background: str, strengths: List[str], weaknesses: List[str], motivations: List[str], emotions: List[str]}
        A dictionary containing the protagonist's character profile.

    Raises
    ------
    ValueError
        If any of the input parameters are invalid or missing.

    Examples
    --------
    >>> create_protagonist_character_profile(protagonist_name='Alice',
    protagonist_age=25, protagonist_background='Alice is a skilled adventurer.',
    protagonist_motivation='To explore the moon')
    {'protagonist_name': 'Alice', 'age': 25, 'background': 'Alice is a skilled
    adventurer.', 'strengths': ['bravery', 'intelligence'], 'weaknesses':
    ['impulsiveness'], 'motivations': ['curiosity'], 'emotions': ['excitement',
    'determination']}

    """
    return CreateProtagonistCharacterProfileOutput(
        protagonist_name="",
        age=0,
        background="",
        strengths=[],
        weaknesses=[],
        motivations=[],
        emotions=[],
    )