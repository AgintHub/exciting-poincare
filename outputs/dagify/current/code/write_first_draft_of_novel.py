from pydantic import BaseModel, Field
from typing import List


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


class PlanMoonLandingSequenceOutput(BaseModel):
    """Pydantic model for plan_moon_landing_sequence node outputs."""
    moon_landing_sequence: str = (
        Field(..., description="A detailed description of the sequence of events leading to the moon landing")
    )
    preparation_steps: List[str] = (
        Field(..., description="List of preparation steps taken by the protagonist and dragon before launching to the moon")
    )
    flight_details: List[str] = (
        Field(..., description="List of details about the flight to the moon, including navigation, propulsion, and communication")
    )
    lunar_exploration_plan: str = (
        Field(..., description="A detailed plan for the protagonist and dragon's lunar exploration, including sites to visit and experiments to conduct")
    )
    landing_site_coordinates: List[float] = (
        Field(..., description="List of coordinates for the planned moon landing site")
    )
    sequence_completion_status: bool = (
        Field(..., description="Whether the moon landing sequence has been successfully planned")
    )


class DevelopPlotTwistsAndTurnsOutput(BaseModel):
    """Pydantic model for develop_plot_twists_and_turns node outputs."""
    plot_twist_descriptions: List[str] = (
        Field(..., description="List of descriptions for each plot twist")
    )
    obstacle_types: List[str] = (
        Field(..., description="List of types of obstacles the protagonist and dragon will face")
    )
    conflict_resolution_outcomes: List[bool] = (
        Field(..., description="List of boolean outcomes indicating whether each conflict is resolved successfully")
    )
    turning_point_count: int = (
        Field(..., description="Number of turning points in the plot")
    )
    protagonist_growth_description: str = (
        Field(..., description="Description of the protagonist's growth and development throughout the plot twists and turns")
    )


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


def write_first_draft_of_novel(create_protagonist_character_profile_input: CreateProtagonistCharacterProfileOutput, design_dragon_character_profile_input: DesignDragonCharacterProfileOutput, plan_moon_landing_sequence_input: PlanMoonLandingSequenceOutput, develop_plot_twists_and_turns_input: DevelopPlotTwistsAndTurnsOutput, **kwargs) -> WriteFirstDraftOfNovelOutput:
    """
    Generate a first‑draft novel from character profiles, landing sequence, and
    plot twists.

    Parameters
    ----------
    protagonist_profile : dict
        Dictionary containing protagonist_name, age, background, strengths,
        weaknesses, motivations, emotions.
    dragon_profile : dict
        Dictionary containing dragon_name, dragon_age,
        dragon_personality_traits, dragon_skills, dragon_habits,
        dragon_strengths, dragon_weaknesses, dragon_motivations.
    moon_sequence : dict
        Dictionary containing moon_landing_sequence, preparation_steps,
        flight_details, lunar_exploration_plan, landing_site_coordinates,
        sequence_completion_status.
    plot_twists : dict
        Dictionary containing plot_twist_descriptions, obstacle_types,
        conflict_resolution_outcomes, turning_point_count,
        protagonist_growth_description.

    Returns
    -------
    dict
        A dictionary with keys novel_title, protagonist_name, dragon_name,
        chapter_titles, chapter_summaries, key_events, theme, and
        word_count.

    Raises
    ------
    ValueError
        Raised if any required input field is missing or empty.
    TypeError
        Raised if inputs do not match expected structure or types.

    Examples
    --------
    >>> draft = write_first_draft_of_novel(protagonist_profile=protagonist,
    ...                                  dragon_profile=dragon,
    ...                                  moon_sequence=moon_seq,
    ...                                  plot_twists=twists)
    {'novel_title': 'Starlight Riders', 'protagonist_name': 'Luna',
    'dragon_name': 'Eclipse', ...}

    >>> print(draft['theme'])
    'Bravery and friendship can conquer even the sky's limits.'

    """
    return WriteFirstDraftOfNovelOutput(
        novel_title="",
        protagonist_name="",
        dragon_name="",
        chapter_titles=[],
        chapter_summaries=[],
        key_events=[],
        theme="",
        word_count=0,
    )