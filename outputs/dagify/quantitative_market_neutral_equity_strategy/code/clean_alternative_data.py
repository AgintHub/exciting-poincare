from pydantic import BaseModel, Field
from typing import List


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


class CleanAlternativeDataOutput(BaseModel):
    """Pydantic model for clean_alternative_data node outputs."""
    total_records: int = (
        Field(..., description="Total number of alternative data records downloaded before cleaning.")
    )
    filled_missing_days: int = (
        Field(..., description="Total number of missing days that were filled during the cleaning process.")
    )
    excluded_records: int = (
        Field(..., description="Number of records excluded due to being outside the 1%/99% percentile after winsorization.")
    )
    summary_statement: str = (
        Field(..., description="A brief textual summary of the cleaning outcome, including date range and number of securities processed.")
    )


def clean_alternative_data(acquire_alternative_data_input: AcquireAlternativeDataOutput, **kwargs) -> CleanAlternativeDataOutput:
    """
    Clean and standardise alternative data for downstream factor modelling.

    Parameters
    ----------
    raw_data : pd.DataFrame
        DataFrame containing columns: ['security_id', 'date', 'field',
        'value']. Each row represents a daily observation from an
        alternative data source.

    Returns
    -------
    Dict[str, Union[int, str]]
        Dictionary with keys 'total_records', 'filled_missing_days',
        'excluded_records', and 'summary_statement' that describe the
        cleaning outcome.

    Raises
    ------
    ValueError
        If raw_data is empty or does not contain the required columns.
    KeyError
        If expected columns are missing from the input DataFrame.

    Examples
    --------
    >>> import pandas as pd
    >>> from datetime import date
    >>> # Sample raw data with gaps and outliers
    >>> df_raw = pd.DataFrame({
    ...     'security_id': ['A', 'A', 'A', 'B', 'B', 'B', 'B'],
    ...     'date': [date(2023,1,2), date(2023,1,5), date(2023,1,6),
    ...              date(2023,1,2), date(2023,1,3), date(2023,1,5),
    date(2023,1,6)],
    ...     'field': ['sentiment']*7,
    ...     'value': [0.5, 5.0, -4.0, 0.1, 0.2, 10.0, -10.0]  # contains
    outliers
    >>> })
    >>> result = clean_alternative_data(df_raw)
    >>> print(result['summary_statement'])
    "Cleaned 7 records across 2 securities. 2 missing trading days filled via
    forward fill. 2 records removed after winsorization at 1%/99% percentiles."

    >>> # If raw_data has no missing trading days and all values within bounds
    >>> df_raw = pd.DataFrame({
    ...     'security_id': ['C']*3,
    ...     'date': [date(2023,1,2), date(2023,1,3), date(2023,1,4)],
    ...     'field': ['esg_score']*3,
    ...     'value': [0.8, 0.85, 0.9]"
                "})
    >>> result = clean_alternative_data(df_raw)
    >>> print(result['filled_missing_days'])
    0

    """
    return CleanAlternativeDataOutput(
        total_records=0,
        filled_missing_days=0,
        excluded_records=0,
        summary_statement="",
    )