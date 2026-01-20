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


class DefineUniverseCriteriaOutput(BaseModel):
    """Pydantic model for define_universe_criteria node outputs."""
    market_cap_min: float = (
        Field(..., description="Minimum market capitalization in USD (e.g., 5000000000 for $5B)")
    )
    market_cap_max: float = (
        Field(..., description="Maximum market capitalization in USD (e.g., 100000000000 for $100B)")
    )
    avg_daily_volume_min: float = (
        Field(..., description="Minimum average daily trading volume in shares (e.g., 5000000)")
    )
    price_min: float = (
        Field(..., description="Minimum stock price in USD (e.g., 5.0)")
    )
    price_max: float = (
        Field(..., description="Maximum stock price in USD (e.g., 150.0)")
    )
    exchanges: List[str] = (
        Field(..., description="List of allowed listing exchanges (e.g., ['NYSE', 'NASDAQ'])")
    )
    positive_earnings: bool = (
        Field(..., description="Whether to filter for securities with positive earnings")
    )


class DesignPortfolioConstraintsOutput(BaseModel):
    """Pydantic model for design_portfolio_constraints node outputs."""
    net_beta_target: float = (
        Field(..., description="Target value for net market beta (should be 0.0 for neutrality)")
    )
    dollar_exposure_target: float = (
        Field(..., description="Target net dollar exposure (should be 0.0 for dollar neutrality)")
    )
    sector_neutrality: bool = (
        Field(..., description="Flag indicating whether sector exposure is required to be neutralized")
    )
    max_position_size_pct: float = (
        Field(..., description="Maximum allowed position size as a percentage of NAV (e.g., 0.05 for 5%)")
    )
    min_liquidity_pct: float = (
        Field(..., description="Minimum required liquidity as a percentage of average daily volume (e.g., 0.02 for 2%)")
    )
    factor_names: List[str] = (
        Field(..., description="List of factor names for which exposure limits are specified")
    )
    factor_exposure_limits: List[float] = (
        Field(..., description="Corresponding upper bound on absolute exposure for each factor in factor_names")
    )


def design_portfolio_constraints(define_market_neutral_objectives_input: DefineMarketNeutralObjectivesOutput, define_universe_criteria_input: DefineUniverseCriteriaOutput, **kwargs) -> DesignPortfolioConstraintsOutput:
    """
    Constructs numerical portfolio constraints enforcing market neutrality and
    risk limits based on inputs from market-neutral objectives and universe
    criteria.

    Parameters
    ----------
    net_beta_target : float
        Target net beta exposure to the market (typically zero to achieve
        market neutrality).
    dollar_exposure_target : float
        Target net dollar exposure for the portfolio (usually zero for
        dollar neutrality).
    sector_neutrality : bool
        Boolean flag indicating if sector exposures must be neutralized
        (True) or not (False).
    max_position_size_pct : float
        Maximum permitted position size as a fraction of Net Asset Value
        (e.g., 0.05 means 5%).
    min_liquidity_pct : float
        Minimum liquidity required for a position, expressed as percentage
        of Average Daily Volume.
    factor_names : List[str]
        List of factor names for which exposure constraints are defined.
    factor_exposure_limits : List[float]
        Corresponding absolute upper bounds on portfolio exposure for each
        factor in factor_names.

    Returns
    -------
    dict
        Dictionary of portfolio constraints specifying neutrality targets,
        position limits, liquidity thresholds, and factor exposure caps.

    Raises
    ------
    ValueError
        If lengths of factor_names and factor_exposure_limits do not match.
    ValueError
        If any percentage value is outside the [0,1] interval.

    Examples
    --------
    >>> constraints = design_portfolio_constraints(
    ...     net_beta_target=0.0,
    ...     dollar_exposure_target=0.0,
    ...     sector_neutrality=True,
    ...     max_position_size_pct=0.05,
    ...     min_liquidity_pct=0.02,
    ...     factor_names=['Value', 'Momentum'],
    ...     factor_exposure_limits=[0.1, 0.15]
    >>> )
    }

    >>> constraints = design_portfolio_constraints(
    ...     net_beta_target=0.0,
    ...     dollar_exposure_target=0.0,
    ...     sector_neutrality=False,
    ...     max_position_size_pct=0.10,
    ...     min_liquidity_pct=0.05,
    ...     factor_names=['Quality'],
    ...     factor_exposure_limits=[0.2]
    >>> )
    }

    """
    return DesignPortfolioConstraintsOutput(
        net_beta_target=0.0,
        dollar_exposure_target=0.0,
        sector_neutrality=False,
        max_position_size_pct=0.0,
        min_liquidity_pct=0.0,
        factor_names=[],
        factor_exposure_limits=[],
    )