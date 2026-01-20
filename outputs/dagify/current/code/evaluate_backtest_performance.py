from pydantic import BaseModel, Field
from typing import List


class BacktestPortfolioOutput(BaseModel):
    """Pydantic model for backtest_portfolio node outputs."""
    portfolio_daily_returns: List[float] = (
        Field(..., description="Time-series of portfolio daily returns")
    )
    cumulative_pnl: List[float] = (
        Field(..., description="Time-series of cumulative P&L")
    )
    turnover: List[float] = (
        Field(..., description="Time-series of portfolio turnover")
    )
    backtest_horizon_length: int = (
        Field(..., description="Length of the back-test horizon in days")
    )


class EvaluateBacktestPerformanceOutput(BaseModel):
    """Pydantic model for evaluate_backtest_performance node outputs."""
    annualized_return: float = (
        Field(..., description="The annualized return of the backtest")
    )
    annualized_volatility: float = (
        Field(..., description="The annualized volatility of the backtest")
    )
    sharpe_ratio: float = (
        Field(..., description="The Sharpe ratio of the backtest")
    )
    information_ratio: float = (
        Field(..., description="The information ratio of the backtest")
    )
    maximum_drawdown: float = (
        Field(..., description="The maximum drawdown of the backtest")
    )
    turnover: float = Field(..., description="The turnover of the backtest")
    underperformance_periods: str = (
        Field(..., description="List of periods where the backtest underperformed")
    )


def evaluate_backtest_performance(backtest_portfolio_input: BacktestPortfolioOutput, **kwargs) -> EvaluateBacktestPerformanceOutput:
    """
    Evaluate the performance of a backtest by calculating key metrics.

    Parameters
    ----------
    backtest_results : dict
        Results from the backtest, including portfolio daily returns,
        cumulative P&L, and turnover.

    Returns
    -------
    dict
        A dictionary containing the calculated performance metrics.

    Raises
    ------
    ValueError
        If the backtest results are invalid or missing required data.

    Examples
    --------
    >>> backtest_results = {'portfolio_daily_returns': [0.01, 0.02, -0.01],
    ...                         'cumulative_pnl': [100, 120, 110],
    ...                         'turnover': [0.1, 0.2, 0.1]}
    >>> performance_metrics = evaluate_backtest_performance(backtest_results)
    {'annualized_return': 0.08, 'annualized_volatility': 0.15, 'sharpe_ratio':
    0.53, 'information_ratio': 0.42, 'maximum_drawdown': -0.1, 'turnover': 0.2,
    'underperformance_periods': ['2022-01-01']}

    """
    return EvaluateBacktestPerformanceOutput(
        annualized_return=0.0,
        annualized_volatility=0.0,
        sharpe_ratio=0.0,
        information_ratio=0.0,
        maximum_drawdown=0.0,
        turnover=0.0,
        underperformance_periods="",
    )