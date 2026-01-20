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


class CleanPriceDataOutput(BaseModel):
    """Pydantic model for clean_price_data node outputs."""
    cleaned_rows: int = (
        Field(..., description="Total number of rows after cleaning")
    )
    removed_rows: int = (
        Field(..., description="Number of rows removed due to invalid or duplicate data")
    )
    cleaned_date_range: str = (
        Field(..., description="Date range of the cleaned dataset in ISO format (e.g., 2013-01-02 to 2023-01-01)")
    )
    columns_cleaned: List[str] = (
        Field(..., description="List of column names that were standardized or renamed")
    )
    is_clean: bool = (
        Field(..., description="Indicates whether the dataset passed all integrity checks")
    )


def clean_price_data(acquire_price_data_input: AcquirePriceDataOutput, **kwargs) -> CleanPriceDataOutput:
    """
    Cleans and standardizes price data by adjusting for corporate actions,
    handling missing values, and ensuring consistent column names.

    Parameters
    ----------
    price_data : DataFrame
        Raw price dataset to be cleaned

    Returns
    -------
    dict
        Dictionary containing cleaned_rows, removed_rows,
        cleaned_date_range, columns_cleaned, and is_clean

    Raises
    ------
    ValueError
        If the input dataset is empty or contains invalid data

    Examples
    --------
    >>> import pandas as pd
    >>> data = pd.DataFrame({'date': ['2022-01-01', '2022-01-02'], 'close':
    [100, 120]})
    >>> cleaned_data = clean_price_data(data)
    >>> print(cleaned_data)
    {'cleaned_rows': 2, 'removed_rows': 0, 'cleaned_date_range': '2022-01-01 to
    2022-01-02', 'columns_cleaned': ['date', 'close'], 'is_clean': True}

    """
    return CleanPriceDataOutput(
        cleaned_rows=0,
        removed_rows=0,
        cleaned_date_range="",
        columns_cleaned=[],
        is_clean=False,
    )