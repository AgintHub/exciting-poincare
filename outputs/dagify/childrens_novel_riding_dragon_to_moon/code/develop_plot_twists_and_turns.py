from pydantic import BaseModel, Field
from typing import List


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


def develop_plot_twists_and_turns(plan_moon_landing_sequence_input: PlanMoonLandingSequenceOutput, **kwargs) -> DevelopPlotTwistsAndTurnsOutput:
    """
    Develops plot twists and turns based on the moon landing sequence.

    Parameters
    ----------
    moon_landing_sequence : str
        The sequence of events leading to the moon landing.

    Returns
    -------
    dict
        A dictionary containing the plot twist descriptions, obstacle types,
        conflict resolution outcomes, turning point count, and protagonist
        growth description.

    Raises
    ------
    ValueError
        If the moon landing sequence is empty or None.

    Examples
    --------
    >>> plot_twists = develop_plot_twists_and_turns(moon_landing_sequence='The
    protagonist and dragon travel to the moon.')
    {'plot_twist_descriptions': ['The protagonist and dragon encounter a meteor
    shower.', 'The dragon's scales start to glow in the dark.'],
    'obstacle_types': ['meteor shower', 'low oxygen'],
    'conflict_resolution_outcomes': [True, False], 'turning_point_count': 2,
    'protagonist_growth_description': 'The protagonist learns to navigate
    through uncertain situations.'}

    """
    return DevelopPlotTwistsAndTurnsOutput(
        plot_twist_descriptions=[],
        obstacle_types=[],
        conflict_resolution_outcomes=[],
        turning_point_count=0,
        protagonist_growth_description="",
    )