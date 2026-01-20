from pydantic import BaseModel, Field
from typing import List


class GenerateSignalsOutput(BaseModel):
    """Pydantic model for generate_signals node outputs."""
    date_range_start: str = (
        Field(..., description="The first date for which signals were generated, in ISO format (YYYY-MM-DD).")
    )
    date_range_end: str = (
        Field(..., description="The last date for which signals were generated, in ISO format (YYYY-MM-DD).")
    )
    num_signals: int = (
        Field(..., description="Total number of signal entries generated across all securities and dates.")
    )
    signal_mean: float = (
        Field(..., description="Mean of all predicted excess return signals.")
    )
    signal_std: float = (
        Field(..., description="Standard deviation of all predicted excess return signals.")
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


class DefineTransactionCostModelOutput(BaseModel):
    """Pydantic model for define_transaction_cost_model node outputs."""
    commission_per_share: float = (
        Field(..., description="Fixed commission charged per share traded")
    )
    bid_ask_spread_percent: float = (
        Field(..., description="Bid\u2011ask spread expressed as a percentage of the security price")
    )
    impact_factor: float = (
        Field(..., description="Parameter for the square\u2011root market impact function (trade size relative to daily volume)")
    )


class OptimizePortfolioOutput(BaseModel):
    """Pydantic model for optimize_portfolio node outputs."""
    optimal_date: str = (
        Field(..., description="The date for which the optimal weights are computed")
    )
    weight_vector: List[float] = (
        Field(..., description="Optimal portfolio weights for each security in the universe, ordered consistently with the input signal vector")
    )
    gross_exposure: float = (
        Field(..., description="Sum of absolute values of the optimal weights, representing total gross position size")
    )
    net_exposure: float = (
        Field(..., description="Sum of the optimal weights, representing net dollar exposure after market\u2011neutral constraints")
    )


def optimize_portfolio(generate_signals_input: GenerateSignalsOutput, design_portfolio_constraints_input: DesignPortfolioConstraintsOutput, define_transaction_cost_model_input: DefineTransactionCostModelOutput, **kwargs) -> OptimizePortfolioOutput:
    """
    Compute the optimal portfolio weights that maximize predicted returns net of
    transaction costs under predefined constraints for a specified date.

    Parameters
    ----------
    signal_vector : List[float]
        Predicted excess return signals for each security on the
        optimization date, aligned with the portfolio universe.
    constraints : Dict[str, Any]
        A dictionary encapsulating portfolio constraints such as net beta
        target, dollar exposure target, sector neutrality flag, maximum
        position size percentage, minimum liquidity threshold, factor names,
        and factor exposure limits.
    transaction_costs : Dict[str, float]
        Parameters of the transaction cost model including commission per
        share, bid-ask spread percentage, and market impact factor.
    current_positions : List[float]
        Current portfolio weights for each security, used to compute
        transaction costs related to rebalancing.
    date : str
        The specific date (ISO format YYYY-MM-DD) for which to compute the
        optimal portfolio weights.

    Returns
    -------
    Dict[str, Any]
        A dictionary containing: 'optimal_date' the optimization date;
        'weight_vector' list of floats for optimal security weights;
        'gross_exposure' total absolute exposure float; 'net_exposure' net
        dollar exposure float.

    Raises
    ------
    ValueError
        Raised if input vectors lengths do not match or if constraints are
        not properly specified.
    OptimizationError
        Raised if the quadratic programming solver fails to find a feasible
        or optimal solution.

    Examples
    --------
    >>> signal_vector = [0.02, 0.01, -0.01]
    >>> constraints = {
    ...     'net_beta_target': 0.0,
    ...     'dollar_exposure_target': 0.0,
    ...     'sector_neutrality': True,
    ...     'max_position_size_pct': 0.05,
    ...     'min_liquidity_pct': 0.02,
    ...     'factor_names': ['value', 'momentum'],
    ...     'factor_exposure_limits': [0.1, 0.15]
    >>> }
    >>> transaction_costs = {
    ...     'commission_per_share': 0.005,
    ...     'bid_ask_spread_percent': 0.001,
    ...     'impact_factor': 0.2
    >>> }
    >>> current_positions = [0.0, 0.0, 0.0]
    >>> date = '2023-08-01'
    >>> output = optimize_portfolio(signal_vector, constraints,
    transaction_costs, current_positions, date)
    {
      'optimal_date': '2023-08-01',
      'weight_vector': [0.04, 0.03, -0.05],
      'gross_exposure': 0.12,
      'net_exposure': 0.02
    }

    >>> # For a single-day optimization with existing positions
    >>> signal_vector = [0.015, 0.025]
    >>> constraints = {
    ...     'net_beta_target': 0.0,
    ...     'dollar_exposure_target': 0.0,
    ...     'sector_neutrality': False,
    ...     'max_position_size_pct': 0.1,
    ...     'min_liquidity_pct': 0.03,
    ...     'factor_names': ['quality'],
    ...     'factor_exposure_limits': [0.2]
    >>> }
    >>> transaction_costs = {
    ...     'commission_per_share': 0.004,
    ...     'bid_ask_spread_percent': 0.0015,
    ...     'impact_factor': 0.15
    >>> }
    >>> current_positions = [0.02, -0.01]
    >>> date = '2023-08-02'
    >>> output = optimize_portfolio(signal_vector, constraints,
    transaction_costs, current_positions, date)
    {
      'optimal_date': '2023-08-02',
      'weight_vector': [0.07, -0.06],
      'gross_exposure': 0.13,
      'net_exposure': 0.01
    }

    """
    return OptimizePortfolioOutput(
        optimal_date="",
        weight_vector=[],
        gross_exposure=0.0,
        net_exposure=0.0,
    )