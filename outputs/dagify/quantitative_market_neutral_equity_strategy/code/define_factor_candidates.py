from pydantic import BaseModel, Field
from typing import List


class DefineStrategyObjectivesOutput(BaseModel):
    """Pydantic model for define_strategy_objectives node outputs."""
    objectives: str = (
        Field(..., description="A list of up to six bullet\u2011point objectives describing target return, risk tolerance, market exposure, investment horizon, and special constraints for the strategy.")
    )


class DefineFactorCandidatesOutput(BaseModel):
    """Pydantic model for define_factor_candidates node outputs."""
    factor_names: List[str] = (
        Field(..., description="A list of candidate factor names to be evaluated.")
    )
    factor_definitions: List[str] = (
        Field(..., description="A short definition or description for each corresponding factor.")
    )


def define_factor_candidates(define_strategy_objectives_input: DefineStrategyObjectivesOutput, **kwargs) -> DefineFactorCandidatesOutput:
    """
    Generate candidate quantitative factor names and their brief definitions for
    evaluation in a market-neutral equity strategy.

    Parameters
    ----------
    objectives : List[str]
        High-level investment objectives of the market-neutral equity
        strategy that guide the factor selection scope and relevance.

    Returns
    -------
    Tuple[List[str], List[str]]
        Two parallel lists containing factor names and their corresponding
        short definitions for use in factor exposure computation and model
        development.

    Raises
    ------
    ValueError
        If the provided objectives list is empty or None, factor candidates
        cannot be aligned properly.

    Examples
    --------
    >>> objectives = [
    ...   'Target annualized return of 10%',
    ...   'Limit market beta to near zero',
    ...   'Investment horizon of 1 year',
    ...   'Incorporate ESG considerations as a constraint'
    >>> ]
    >>> factor_names, factor_definitions = define_factor_candidates(objectives)
    [ 'Book_to_Price', 'Momentum_12M', 'ROE', 'Low_Volatility',
    'Earnings_Revision', 'Sentiment_Score', 'ESG_Score', 'Composite_Factor' ],
    [ 'Ratio of book value to market price indicating value factor.', 'Total
    return over past 12 months representing momentum.', 'Return on equity
    measuring profitability.', 'Standard deviation of daily returns capturing
    volatility.', 'Revision of earnings forecasts reflecting changes in analyst
    expectations.', 'Aggregate news sentiment score derived from alternative
    data.', 'Environmental, Social, and Governance rating score.', 'Weighted
    combination of multiple factor scores.' ]

    >>> factor_names, factor_definitions = define_factor_candidates(['Focus on
    quality and low volatility'])
    [ 'ROE', 'Low_Volatility' ],
    [ 'Return on equity indicating company quality.', 'Standard deviation of
    returns representing low volatility.' ]

    """
    return DefineFactorCandidatesOutput(
        factor_names=[],
        factor_definitions=[],
    )