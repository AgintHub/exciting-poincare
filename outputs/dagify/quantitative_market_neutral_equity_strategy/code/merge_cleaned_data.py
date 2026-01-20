from pydantic import BaseModel, Field
from typing import List


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


class CleanFundamentalDataOutput(BaseModel):
    """Pydantic model for clean_fundamental_data node outputs."""
    cleaned_record_count: int = (
        Field(..., description="Total number of fundamental records after cleaning")
    )
    missing_value_records: int = (
        Field(..., description="Number of records that had missing values before imputation")
    )
    missing_value_flagged: bool = (
        Field(..., description="Whether any records were flagged for missing values after cleaning")
    )
    outlier_removed_count: int = (
        Field(..., description="Number of records removed due to outlier detection")
    )
    unit_consistency_flag: bool = (
        Field(..., description="True if all metrics were converted to consistent units")
    )
    reporting_period_aligned: bool = (
        Field(..., description="True if all reporting periods were aligned to calendar dates")
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


class MergeCleanedDataOutput(BaseModel):
    """Pydantic model for merge_cleaned_data node outputs."""
    total_rows: int = (
        Field(..., description="Total number of security\u2011day observations in the merged dataset.")
    )
    total_columns: int = (
        Field(..., description="Total number of columns (features) in the merged dataset, including identifier, date, price, fundamental, and alternative fields.")
    )
    column_names: List[str] = (
        Field(..., description="List of all column names present in the merged dataset.")
    )
    is_successful: bool = (
        Field(..., description="Flag indicating whether the merge operation completed without errors.")
    )
    merge_summary: str = (
        Field(..., description="Short textual summary of the merge operation, e.g., \"Merged 5,000 securities over 2,500 trading days with 120 columns.\"")
    )


def merge_cleaned_data(clean_price_data_input: CleanPriceDataOutput, clean_fundamental_data_input: CleanFundamentalDataOutput, clean_alternative_data_input: CleanAlternativeDataOutput, **kwargs) -> MergeCleanedDataOutput:
    """
    Merge cleaned price, fundamental, and alternative datasets on security
    identifier and date to produce a unified panel dataset with combined
    features.

    Parameters
    ----------
    price_data : DataFrame
        Cleaned price data including daily price and corporate action
        adjusted fields, indexed or containing security identifier and date.
    fundamental_data : DataFrame
        Cleaned fundamental accounting data standardized to consistent
        units, aligned to calendar dates, indexed or containing security
        identifier and date.
    alternative_data : DataFrame
        Cleaned alternative data series with aligned timestamps and
        winsorized values, indexed or containing security identifier and
        date.

    Returns
    -------
    dict
        A dictionary containing: total_rows (int), total_columns (int),
        column_names (List[str]), is_successful (bool), and merge_summary
        (str), summarizing the resulting merged dataset.

    Raises
    ------
    ValueError
        If any input dataset is empty or missing required columns such as
        'security_id' or 'date'.
    MergeError
        If the join operation fails due to incompatible indices or unmatched
        key columns.

    Examples
    --------
    >>> merged = merge_cleaned_data(price_data, fundamental_data,
    alternative_data)
    >>> print(merged['total_rows'])
    >>> print(merged['total_columns'])
    >>> print(merged['is_successful'])
    >>> print(merged['merge_summary'])
    250000
    120
    True
    'Merged 5000 securities over 50 trading days with 120 columns.'

    >>> # Assuming mismatched keys or empty data triggers error
    >>> try:
    ...     merge_cleaned_data(empty_price_data, fundamental_data,
    alternative_data)
    >>> except ValueError as e:
    ...     print(str(e))
    'Input price_data is empty or missing required keys.'

    """
    return MergeCleanedDataOutput(
        total_rows=0,
        total_columns=0,
        column_names=[],
        is_successful=False,
        merge_summary="",
    )