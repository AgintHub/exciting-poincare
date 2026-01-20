from pydantic import BaseModel, Field


class DefineStrategyObjectivesOutput(BaseModel):
    """Pydantic model for define_strategy_objectives node outputs."""
    objectives: str = (
        Field(..., description="A list of up to six bullet\u2011point objectives describing target return, risk tolerance, market exposure, investment horizon, and special constraints for the strategy.")
    )


def define_strategy_objectives(general_input: str, **kwargs) -> DefineStrategyObjectivesOutput:
    """
    Specifies the high-level objectives for a market-neutral equity quantitative
    trading strategy.

    Returns
    -------
    List[str]
        A list of bullet points outlining the strategy objectives.

    Examples
    --------
    >>> define_strategy_objectives()
    ['Target annual return: 10%', 'Risk tolerance: 15% annualized volatility',
    'Market exposure: Beta <= 0.1', 'Investment horizon: Medium-term (1-2
    years)', 'Special constraint: No net long/short bias']

    """
    return DefineStrategyObjectivesOutput(
        objectives="",
    )