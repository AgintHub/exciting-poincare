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


def plan_moon_landing_sequence(create_protagonist_character_profile_input: CreateProtagonistCharacterProfileOutput, design_dragon_character_profile_input: DesignDragonCharacterProfileOutput, **kwargs) -> PlanMoonLandingSequenceOutput:
    """
    Plans a moon landing sequence for the protagonist and dragon.

    Parameters
    ----------
    protagonist_profile : dict
        The protagonist's character profile, including name, age,
        background, strengths, weaknesses, motivations, and emotions.
    dragon_profile : dict
        The dragon's character profile, including name, age, personality
        traits, skills, habits, strengths, weaknesses, and motivations.

    Returns
    -------
    dict
        A dictionary containing the moon landing sequence, preparation
        steps, flight details, lunar exploration plan, landing site
        coordinates, and sequence completion status.

    Raises
    ------
    ValueError
        If either the protagonist or dragon profile is incomplete or
        missing.

    Examples
    --------
    >>> protagonist_profile = {'name': 'Alice', 'age': 25, 'background':
    'Astronaut', 'strengths': ['Leadership'], 'weaknesses': ['Impulsiveness'],
    'motivations': ['Explore space'], 'emotions': ['Excitement']}
    >>> dragon_profile = {'name': 'Dragon1', 'age': 100, 'personality_traits':
    ['Loyal'], 'skills': ['Flight'], 'habits': ['Sleeping'], 'strengths':
    ['Speed'], 'weaknesses': ['Vulnerability to fire'], 'motivations': ['Protect
    protagonist']}
    >>> plan_moon_landing_sequence(protagonist_profile, dragon_profile)
    {'moon_landing_sequence': 'The protagonist and dragon will prepare for
    launch, fly to the moon, and conduct lunar exploration.',
    'preparation_steps': ['Check fuel', 'Perform safety checks'],
    'flight_details': ['Navigate through space', 'Communicate with Earth'],
    'lunar_exploration_plan': 'Visit craters and conduct experiments.',
    'landing_site_coordinates': [12.34, 56.78], 'sequence_completion_status':
    True}

    """
    return PlanMoonLandingSequenceOutput(
        moon_landing_sequence="",
        preparation_steps=[],
        flight_details=[],
        lunar_exploration_plan="",
        landing_site_coordinates=[],
        sequence_completion_status=False,
    )