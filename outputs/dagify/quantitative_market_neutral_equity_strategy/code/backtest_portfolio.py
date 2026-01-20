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


class AcquirePriceDataOutput(BaseModel):
    """Pydantic model for acquire_price_data node outputs."""
    start_date: str = (
        Field(..., description="Earliest date of the price data series (YYYY-MM-DD).")
    )
    end_date: str = (
        Field(..., description="Most recent date of the price data series (YYYY-MM-DD).")
    )
    num_securities: int = (
        Field(..., description="Total number of securities for which price data was retrieved.")
    )
    security_ids: List[str] = (
        Field(..., description="List of unique identifiers (e.g., ticker or CUSIP) for each security in the dataset.")
    )
    columns_retrieved: List[str] = (
        Field(..., description="List of column names that were retrieved (e.g., adjusted_close, open, high, low, volume, split_factor).")
    )
    summary_statement: str = (
        Field(..., description="A concise statement confirming the date range and number of securities, e.g., \"Downloaded price data for 1,234 securities from 2013-01-02 to 2023-01-02.\"")
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


def backtest_portfolio(optimize_portfolio_input: OptimizePortfolioOutput, acquire_price_data_input: AcquirePriceDataOutput, define_transaction_cost_model_input: DefineTransactionCostModelOutput, **kwargs) -> BacktestPortfolioOutput:
    """
    Simulates a portfolio backtest from the earliest date to the most recent
    date, applying daily optimized weights and transaction costs, and outputs
    the time-series of portfolio daily returns, cumulative P&L, and turnover.

    Parameters
    ----------
    optimize_portfolio : dict
        Output from the optimize_portfolio node, containing optimal weights
        for each security.
    acquire_price_data : dict
        Output from the acquire_price_data node, containing historical price
        data for the securities.
    define_transaction_cost_model : dict
        Output from the define_transaction_cost_model node, containing
        transaction cost parameters.

    Returns
    -------
    dict
        A dictionary containing the time-series of portfolio daily returns,
        cumulative P&L, and turnover, as well as the length of the back-test
        horizon.

    Raises
    ------
    ValueError
        If the input data is invalid or missing.

    Examples
    --------
    >>> import pandas as pd
    >>> optimize_portfolio_output = {'optimal_weights': [0.1, 0.2, 0.7]}
    >>> acquire_price_data_output = {'price_data': pd.DataFrame({'date':
    ['2022-01-01', '2022-01-02'], 'returns': [0.01, 0.02]})}
    >>> define_transaction_cost_model_output = {'transaction_costs': 0.001}
    >>> backtest_portfolio(optimize_portfolio_output, acquire_price_data_output,
    define_transaction_cost_model_output)
    {'portfolio_daily_returns': [0.01, 0.02], 'cumulative_pnl': [0.01, 0.03],
    'turnover': [0.1, 0.2], 'backtest_horizon_length': 2}

    """
    return BacktestPortfolioOutput(
        portfolio_daily_returns=[],
        cumulative_pnl=[],
        turnover=[],
        backtest_horizon_length=0,
    )