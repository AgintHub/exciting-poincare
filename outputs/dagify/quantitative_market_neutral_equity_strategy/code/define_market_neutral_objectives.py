from pydantic import BaseModel, Field
from typing import List


class DefineMarketNeutralObjectivesOutput(BaseModel):
    """Pydantic model for define_market_neutral_objectives node outputs."""
    neutrality_criteria: List[str] = (
        Field(..., description="List of individual market\u2011neutral criteria expressed as bullet points, e.g., \"Beta exposure = 0\", \"Dollar exposure = 0\", \"Sector neutrality\", \"Factor X neutrality\".")
    )
    is_valid: bool = (
        Field(..., description="Indicates whether the defined criteria meet the strategy's overall neutrality requirements.")
    )


def define_market_neutral_objectives(general_input: str, **kwargs) -> DefineMarketNeutralObjectivesOutput:
    """
    Define market neutral objectives for an equity portfolio.

    Parameters
    ----------
    strategy : str
        The investment strategy for which market neutrality is required.

    Returns
    -------
    List[str]
        A list of bullet points describing the market neutrality criteria,
        and a boolean indicating if the criteria are valid.

    Raises
    ------
    ValueError
        If the neutrality criteria are not provided.

    Examples
    --------
    >>> define_market_neutral_objectives(strategy='market_neutral_equity')
    ['Beta exposure = 0', 'Dollar exposure = 0', 'Sector neutrality'] True

    """
    return DefineMarketNeutralObjectivesOutput(
        neutrality_criteria=[],
        is_valid=False,
    )