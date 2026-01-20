from pydantic import BaseModel, Field
from typing import List


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


class DefineMarketNeutralObjectivesOutput(BaseModel):
    """Pydantic model for define_market_neutral_objectives node outputs."""
    neutrality_criteria: List[str] = (
        Field(..., description="List of individual market\u2011neutral criteria expressed as bullet points, e.g., \"Beta exposure = 0\", \"Dollar exposure = 0\", \"Sector neutrality\", \"Factor X neutrality\".")
    )
    is_valid: bool = (
        Field(..., description="Indicates whether the defined criteria meet the strategy's overall neutrality requirements.")
    )


class DesignExecutionStrategyOutput(BaseModel):
    """Pydantic model for design_execution_strategy node outputs."""
    algorithm_name: str = (
        Field(..., description="Name of the execution algorithm (e.g., VWAP, TWAP, Implementation Shortfall)")
    )
    strategy_type: str = (
        Field(..., description="Broad classification of the strategy (e.g., Market\u2011Milking, Time\u2011Weighted, Volume\u2011Weighted)")
    )
    participation_rate: float = (
        Field(..., description="Maximum percentage of the daily trading volume to participate in for any single security")
    )
    slice_frequency_minutes: int = (
        Field(..., description="Time interval in minutes between successive child order slices")
    )
    child_order_weights: List[float] = (
        Field(..., description="Sequence of target weights to be applied in each child order slice, matching the order_time_stamps list")
    )
    order_time_stamps: List[str] = (
        Field(..., description="ISO 8601 timestamps indicating when each child order slice is scheduled to be sent")
    )
    execution_quality_metric: str = (
        Field(..., description="Key metric used to assess execution quality (e.g., VWAP deviation %, Execution Slippage %)")
    )


def design_execution_strategy(optimize_portfolio_input: OptimizePortfolioOutput, define_market_neutral_objectives_input: DefineMarketNeutralObjectivesOutput, **kwargs) -> DesignExecutionStrategyOutput:
    """
    Generates an execution algorithm strategy converting daily target portfolio
    weights into time-sliced child orders with participation constraints,
    supporting minimal market impact and quality monitoring.

    Parameters
    ----------
    algorithm_name : str
        The name of the execution algorithm to be used, e.g., 'VWAP',
        'TWAP', or 'Implementation Shortfall'.
    strategy_type : str
        The broad classification of the execution strategy, such as 'Volume-
        Weighted', 'Time-Weighted', or 'Market-Milking'.
    participation_rate : float
        Maximum fraction (0 to 1) of the estimated daily volume to
        participate in trading for each security.
    slice_frequency_minutes : int
        Interval in minutes between successive child order placements within
        the trading day.
    child_order_weights : List[float]
        List of target fractional order sizes relative to the total daily
        order, corresponding slice by slice.
    order_time_stamps : List[str]
        List of ISO 8601 formatted timestamps indicating the scheduled
        execution times for each child order slice.
    execution_quality_metric : str
        A metric name for assessing execution performance, such as 'VWAP
        deviation %' or 'Execution Slippage %'.

    Returns
    -------
    dict
        A dictionary encapsulating the execution algorithm details:
        algorithm name, strategy type, participation rate limit, slice
        frequency, weights and timestamps for child slices, and the quality
        metric for execution assessment.

    Raises
    ------
    ValueError
        If participation_rate is not in (0,1], or if slice_frequency_minutes
        is non-positive.
    ValueError
        If lengths of child_order_weights and order_time_stamps lists differ
        or are empty.
    TypeError
        If input types do not match the expected types.

    Examples
    --------
    >>> design_execution_strategy(
    ...     algorithm_name='VWAP',
    ...     strategy_type='Volume-Weighted',
    ...     participation_rate=0.1,
    ...     slice_frequency_minutes=15,
    ...     child_order_weights=[0.05, 0.1, 0.15, 0.2, 0.25, 0.25],
    ...     order_time_stamps=["2024-06-14T09:30:00Z", "2024-06-14T09:45:00Z",
    "2024-06-14T10:00:00Z",
    ...                       "2024-06-14T10:15:00Z", "2024-06-14T10:30:00Z",
    "2024-06-14T10:45:00Z"],
    ...     execution_quality_metric='VWAP deviation %'
    >>> )
    {'algorithm_name': 'VWAP', 'strategy_type': 'Volume-Weighted',
    'participation_rate': 0.1, 'slice_frequency_minutes': 15,
    'child_order_weights': [0.05, 0.1, 0.15, 0.2, 0.25, 0.25],
    'order_time_stamps': ['2024-06-14T09:30:00Z', '2024-06-14T09:45:00Z',
    '2024-06-14T10:00:00Z', '2024-06-14T10:15:00Z', '2024-06-14T10:30:00Z',
    '2024-06-14T10:45:00Z'], 'execution_quality_metric': 'VWAP deviation %'}

    >>> design_execution_strategy(
    ...     algorithm_name='TWAP',
    ...     strategy_type='Time-Weighted',
    ...     participation_rate=0.05,
    ...     slice_frequency_minutes=30,
    ...     child_order_weights=[0.2, 0.2, 0.2, 0.2, 0.2],
    ...     order_time_stamps=["2024-06-14T09:30:00Z", "2024-06-14T10:00:00Z",
    "2024-06-14T10:30:00Z",
    ...                       "2024-06-14T11:00:00Z", "2024-06-14T11:30:00Z"],
    ...     execution_quality_metric='Execution Slippage %'
    >>> )
    {'algorithm_name': 'TWAP', 'strategy_type': 'Time-Weighted',
    'participation_rate': 0.05, 'slice_frequency_minutes': 30,
    'child_order_weights': [0.2, 0.2, 0.2, 0.2, 0.2], 'order_time_stamps':
    ['2024-06-14T09:30:00Z', '2024-06-14T10:00:00Z', '2024-06-14T10:30:00Z',
    '2024-06-14T11:00:00Z', '2024-06-14T11:30:00Z'], 'execution_quality_metric':
    'Execution Slippage %'}

    """
    return DesignExecutionStrategyOutput(
        algorithm_name="",
        strategy_type="",
        participation_rate=0.0,
        slice_frequency_minutes=0,
        child_order_weights=[],
        order_time_stamps=[],
        execution_quality_metric="",
    )