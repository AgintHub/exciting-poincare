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


class AcquireFundamentalDataOutput(BaseModel):
    """Pydantic model for acquire_fundamental_data node outputs."""
    fundamental_data_fields: List[str] = (
        Field(..., description="List of fundamental data fields retrieved (e.g., earnings per share, book value, cash flow, leverage, dividend yield)")
    )
    data_coverage: str = (
        Field(..., description="Statement describing the coverage of the retrieved data (e.g., 10-year horizon, quarterly and annual data)")
    )
    number_of_securities: int = (
        Field(..., description="Number of securities for which fundamental data was retrieved")
    )
    data_retrieval_status: bool = (
        Field(..., description="Whether the fundamental data retrieval was successful")
    )


def acquire_fundamental_data(identify_data_sources_input: IdentifyDataSourcesOutput, define_universe_criteria_input: DefineUniverseCriteriaOutput, **kwargs) -> AcquireFundamentalDataOutput:
    """
    Downloads historical fundamental accounting data for the specified universe
    of securities.

    Parameters
    ----------
    data_providers : List[str]
        List of fundamental data providers
    universe_criteria : dict
        Dictionary containing the universe criteria (e.g., market cap,
        liquidity, price range)

    Returns
    -------
    dict
        Dictionary containing the retrieved fundamental data fields, data
        coverage, number of securities, and data retrieval status

    Raises
    ------
    ValueError
        If the data providers or universe criteria are invalid

    Examples
    --------
    >>> data_providers = ['Yahoo Finance', 'Quandl']
    >>> universe_criteria = {'market_cap': 1000000000, 'liquidity': 1000000}
    >>> result = acquire_fundamental_data(data_providers, universe_criteria)
    {'fundamental_data_fields': ['earnings_per_share', 'book_value',
    'cash_flow'], 'data_coverage': '10-year horizon, quarterly and annual data',
    'number_of_securities': 100, 'data_retrieval_status': True}

    """
    return AcquireFundamentalDataOutput(
        fundamental_data_fields=[],
        data_coverage="",
        number_of_securities=0,
        data_retrieval_status=False,
    )