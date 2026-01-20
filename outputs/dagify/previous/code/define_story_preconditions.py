from pydantic import BaseModel, Field


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


def define_story_preconditions(general_input: str, **kwargs) -> DefineStoryPreconditionsOutput:
    """
    Defines the preconditions for the story by specifying the protagonist's
    details, their meeting with the dragon, the motivation for their adventure,
    and the setting in which the story unfolds.

    Parameters
    ----------
    protagonist_info : dict
        A dictionary containing the protagonist's name, age, and background.
    dragon_encounter : str
        A string describing how the protagonist meets the dragon.
    protagonist_motivation : str
        A string outlining what motivates the protagonist to ride the dragon
        to the moon.
    story_setting : str
        A string describing the setting of the story.

    Returns
    -------
    dict
        A dictionary containing the protagonist's name, age, background, the
        circumstances of their meeting with the dragon, their motivation for
        the journey, and the story's setting.

    Raises
    ------
    TypeError
        If the input types do not match the expected types.

    Examples
    --------
    >>> define_story_preconditions({
    ...     'protagonist_name': 'Eva',
    ...     'protagonist_age': 25,
    ...     'protagonist_background': 'Scientist'},
    >>> 'The protagonist meets the dragon in a dream.',
    >>> 'To explore the moon and discover new species.',
    >>> 'In a futuristic, space-exploring world.')
    {'protagonist_name': 'Eva', 'protagonist_age': 25, 'protagonist_background':
    'Scientist', 'dragon_meeting_circumstances': 'The protagonist meets the
    dragon in a dream.', 'protagonist_motivation': 'To explore the moon and
    discover new species.', 'story_setting': 'In a futuristic, space-exploring
    world.'}

    """
    return DefineStoryPreconditionsOutput(
        protagonist_name="",
        protagonist_age=0,
        protagonist_background="",
        dragon_meeting_circumstances="",
        protagonist_motivation="",
        story_setting="",
    )