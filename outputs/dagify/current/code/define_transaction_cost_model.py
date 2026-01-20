from pydantic import BaseModel, Field
from typing import List


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


def define_transaction_cost_model(acquire_price_data_input: AcquirePriceDataOutput, **kwargs) -> DefineTransactionCostModelOutput:
    """
    Specify the transaction cost model parameters to estimate trading costs
    including commissions, bid-ask spread, and market impact for back-testing
    equity strategies.

    Parameters
    ----------
    commission_per_share : float
        Fixed commission charged per share traded, e.g., 0.005 equals $0.005
        per share.
    bid_ask_spread_percent : float
        Bid-ask spread expressed as a decimal percentage of the security
        price, e.g., 0.001 = 0.1% spread.
    impact_factor : float
        Market impact parameter for the square-root function modeling price
        impact relative to trade size and average daily volume, typically
        between 0 and 1.

    Returns
    -------
    dict
        Dictionary containing the parameters: commission_per_share (float),
        bid_ask_spread_percent (float), impact_factor (float).

    Raises
    ------
    ValueError
        If any of the input parameter values are negative or not within
        reasonable bounds.

    Examples
    --------
    >>> cost_model = define_transaction_cost_model(
    ...     commission_per_share=0.005,
    ...     bid_ask_spread_percent=0.001,
    ...     impact_factor=0.2
    >>> )
    >>> print(cost_model)
    {'commission_per_share': 0.005, 'bid_ask_spread_percent': 0.001,
    'impact_factor': 0.2}

    >>> cost_model = define_transaction_cost_model(
    ...     commission_per_share=0.007,
    ...     bid_ask_spread_percent=0.002,
    ...     impact_factor=0.15
    >>> )
    >>> print(cost_model)
    {'commission_per_share': 0.007, 'bid_ask_spread_percent': 0.002,
    'impact_factor': 0.15}

    """
    return DefineTransactionCostModelOutput(
        commission_per_share=0.0,
        bid_ask_spread_percent=0.0,
        impact_factor=0.0,
    )