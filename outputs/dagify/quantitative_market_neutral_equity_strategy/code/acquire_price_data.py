from pydantic import BaseModel, Field
from typing import List


class IdentifyDataSourcesOutput(BaseModel):
    """Pydantic model for identify_data_sources node outputs."""
    market_price_data_sources: List[str] = (
        Field(..., description="List of provider names for market price data")
    )
    market_price_fields: List[str] = (
        Field(..., description="Comma-separated list of data fields to retrieve from market price providers")
    )
    fundamental_data_sources: List[str] = (
        Field(..., description="List of provider names for fundamental financial data")
    )
    fundamental_fields: List[str] = (
        Field(..., description="Comma-separated list of data fields to retrieve from fundamental providers")
    )
    alternative_data_sources: List[str] = (
        Field(..., description="List of provider names for alternative data")
    )
    alternative_fields: List[str] = (
        Field(..., description="Comma-separated list of data fields to retrieve from alternative data providers")
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


def acquire_price_data(identify_data_sources_input: IdentifyDataSourcesOutput, define_universe_criteria_input: DefineUniverseCriteriaOutput, **kwargs) -> AcquirePriceDataOutput:
    """
    Retrieve 10‑year daily market price history for the screened equity
    universe.

    Parameters
    ----------
    price_sources : List[str]
        List of market‑price data provider names returned by
        identify_data_sources.
    fields : List[str]
        List of price fields to request from each provider (e.g.,
        ['adjusted_close', 'open', 'high', 'low', 'volume',
        'split_factor']).
    universe : Dict[str, Any]
        Dictionary containing universe screening criteria returned by
        define_universe_criteria.
    start_date : str
        Start of the 10‑year period to download (ISO format).
    end_date : str
        End of the 10‑year period to download (ISO format).

    Returns
    -------
    Dict[str, Any]
        A dictionary matching the output_structure, containing metadata and
        a summary statement.

    Raises
    ------
    ValueError
        If any required input list is empty or the date range is invalid.
    ConnectionError
        If a data provider cannot be reached or returns an authentication
        error.
    RuntimeError
        If the number of securities returned is zero, indicating a mismatch
        between universe criteria and available data.

    Examples
    --------
    >>> price_sources = ['AlphaVantage', 'Polygon']
    >>> fields = ['adjusted_close', 'open', 'high', 'low', 'volume',
    'split_factor']
    >>> universe = {"market_cap_min": 5e9, "market_cap_max": 1e11,
    "avg_daily_volume_min": 5e6, "price_min": 5.0, "price_max": 150.0,
    "exchanges": ["NASDAQ", "NYSE"], "positive_earnings": True}
    >>> result = acquire_price_data(price_sources, fields, universe,
    '2013-01-02', '2023-01-02')
    {'start_date': '2013-01-02', 'end_date': '2023-01-02', 'num_securities':
    1123, 'security_ids': ['AAPL', 'MSFT', 'GOOG'], 'columns_retrieved':
    ['adjusted_close', 'open', 'high', 'low', 'volume', 'split_factor'],
    'summary_statement': 'Downloaded price data for 1,123 securities from
    2013-01-02 to 2023-01-02.'}

    >>> acquire_price_data([], fields, universe, '2013-01-02', '2023-01-02')
    ValueError: Input list price_sources cannot be empty.

    """
    return AcquirePriceDataOutput(
        start_date="",
        end_date="",
        num_securities=0,
        security_ids=[],
        columns_retrieved=[],
        summary_statement="",
    )