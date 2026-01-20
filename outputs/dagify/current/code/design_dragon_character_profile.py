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


class DesignDragonCharacterProfileOutput(BaseModel):
    """Pydantic model for design_dragon_character_profile node outputs."""
    dragon_name: str = Field(..., description="The name of the dragon")
    dragon_age: int = Field(..., description="The age of the dragon")
    dragon_personality_traits: List[str] = (
        Field(..., description="A list of personality traits that describe the dragon")
    )
    dragon_skills: List[str] = (
        Field(..., description="A list of skills that the dragon possesses")
    )
    dragon_habits: List[str] = (
        Field(..., description="A list of habits that the dragon has")
    )
    dragon_strengths: List[str] = (
        Field(..., description="A list of strengths that the dragon has")
    )
    dragon_weaknesses: List[str] = (
        Field(..., description="A list of weaknesses that the dragon has")
    )
    dragon_motivations: List[str] = (
        Field(..., description="A list of motivations that drive the dragon's actions")
    )


def design_dragon_character_profile(define_story_preconditions_input: DefineStoryPreconditionsOutput, **kwargs) -> DesignDragonCharacterProfileOutput:
    """
    Develops a comprehensive character profile for the dragon.

    Parameters
    ----------
    story_preconditions : dict
        A dictionary containing the story preconditions, including
        protagonist, dragon, motivation, and setting.

    Returns
    -------
    dict
        A dictionary containing the detailed character profile of the
        dragon.

    Raises
    ------
    ValueError
        If the story preconditions are incomplete or invalid.

    Examples
    --------
    >>> dragon_profile =
    design_dragon_character_profile(define_story_preconditions())
    >>> print(dragon_profile['dragon_name'])  # Output: 'Scorched'
    >>> print(dragon_profile['dragon_age'])   # Output: 500
    >>> print(dragon_profile['dragon_personality_traits'])  # Output: ['fiery',
    'curious', 'loyal']
    {'dragon_name': 'Scorched', 'dragon_age': 500, 'dragon_personality_traits':
    ['fiery', 'curious', 'loyal'], ...}

    """
    return DesignDragonCharacterProfileOutput(
        dragon_name="",
        dragon_age=0,
        dragon_personality_traits=[],
        dragon_skills=[],
        dragon_habits=[],
        dragon_strengths=[],
        dragon_weaknesses=[],
        dragon_motivations=[],
    )