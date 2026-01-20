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


class AcquireAlternativeDataOutput(BaseModel):
    """Pydantic model for acquire_alternative_data node outputs."""
    security_ids: List[str] = (
        Field(..., description="List of security identifiers (e.g., ticker symbols or ISINs) for which data was retrieved.")
    )
    retrieval_dates: List[str] = (
        Field(..., description="List of dates (YYYY-MM-DD) for which alternative data was downloaded.")
    )
    data_sources: List[str] = (
        Field(..., description="List of data provider names used for the alternative data download.")
    )
    data_fields: List[str] = (
        Field(..., description="List of alternative data fields retrieved (e.g., news_sentiment, google_trends, esg_score, analyst_forecast).")
    )
    summary_statement: str = (
        Field(..., description="Brief statement summarizing the acquisition, including coverage period, number of securities, and total data points.")
    )


def acquire_alternative_data(identify_data_sources_input: IdentifyDataSourcesOutput, define_universe_criteria_input: DefineUniverseCriteriaOutput, **kwargs) -> AcquireAlternativeDataOutput:
    """
    Download daily alternative data signals for the screened security universe
    over the past decade.

    Parameters
    ----------
    security_ids : List[str]
        Identifiers of securities selected by the universe criteria.
    data_sources : List[str]
        Provider names specified by identify_data_sources for alternative
        data.
    data_fields : List[str]
        Fields requested from each provider (e.g., news_sentiment,
        google_trends).
    start_date : str
        ISO 8601 date marking the beginning of the 10‑year coverage window.
    end_date : str
        ISO 8601 date marking the end of the 10‑year coverage window.

    Returns
    -------
    dict
        Dictionary containing lists of identifiers, dates, sources, fields,
        and a summary statement.

    Raises
    ------
    ValueError
        If no security IDs are provided or data_sources list is empty.
    RuntimeError
        If a provider returns an error or fails to supply data for the
        requested period.

    Examples
    --------
    >>> result = acquire_alternative_data(
    ...     security_ids=['AAPL', 'MSFT'],
    ...     data_sources=['NewsAPI', 'GoogleTrends', 'ESGData'],
    ...     data_fields=['news_sentiment', 'google_trends', 'esg_score'],
    ...     start_date='2014-01-01',
    ...     end_date='2024-01-01')
    {'security_ids': ['AAPL', 'MSFT'], 'retrieval_dates': ['2014-01-01',
    '2024-01-01'], 'data_sources': ['NewsAPI', 'GoogleTrends', 'ESGData'],
    'data_fields': ['news_sentiment', 'google_trends', 'esg_score'],
    'summary_statement': 'Downloaded 2,000,000 alternative data points for 2
    securities from 2014-01-01 to 2024-01-01.'}

    >>> result = acquire_alternative_data(
    ...     security_ids=['TSLA'],
    ...     data_sources=['AnalystForecast'],
    ...     data_fields=['analyst_forecast'],
    ...     start_date='2015-01-01',
    ...     end_date='2024-01-01')
    {'security_ids': ['TSLA'], 'retrieval_dates': ['2015-01-01', '2024-01-01'],
    'data_sources': ['AnalystForecast'], 'data_fields': ['analyst_forecast'],
    'summary_statement': 'Downloaded 3,650 data points for TSLA from 2015-01-01
    to 2024-01-01.'}

    """
    return AcquireAlternativeDataOutput(
        security_ids=[],
        retrieval_dates=[],
        data_sources=[],
        data_fields=[],
        summary_statement="",
    )