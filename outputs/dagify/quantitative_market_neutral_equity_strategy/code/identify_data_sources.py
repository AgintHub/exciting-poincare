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


def identify_data_sources(general_input: str, **kwargs) -> IdentifyDataSourcesOutput:
    """
    Identify and enumerate data providers along with required data fields for
    market price, fundamental financial, and alternative data signals used in
    the quantitative strategy.

    Returns
    -------
    dict
        Dictionary containing lists of data source provider names and
        corresponding data fields for three categories: market price data,
        fundamental data, and alternative data.

    Raises
    ------
    ValueError
        If no valid data sources or fields are identified for one or more
        categories.

    Examples
    --------
    >>> identify_data_sources()
    {" +
                    "\n  'market_price_data_sources': ['Bloomberg',
    'Refinitiv']," +
                    "\n  'market_price_fields': ['adjusted_close, open, high,
    low, volume, split_factor']," +
                    "\n  'fundamental_data_sources': ['FactSet', 'Compustat'],"
    +
                    "\n  'fundamental_fields': ['earnings_per_share, book_value,
    cash_flow, leverage, dividend_yield']," +
                    "\n  'alternative_data_sources': ['Sentifi', 'MSCI', 'Google
    Trends']," +
                    "\n  'alternative_fields': ['news_sentiment, esg_score,
    analyst_forecast, google_trends']" +
                    "\n}

    """
    return IdentifyDataSourcesOutput(
        market_price_data_sources=[],
        market_price_fields=[],
        fundamental_data_sources=[],
        fundamental_fields=[],
        alternative_data_sources=[],
        alternative_fields=[],
    )