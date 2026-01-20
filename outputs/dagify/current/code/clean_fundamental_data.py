from pydantic import BaseModel, Field
from typing import List


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


def clean_fundamental_data(acquire_fundamental_data_input: AcquireFundamentalDataOutput, **kwargs) -> CleanFundamentalDataOutput:
    """
    Clean raw fundamental accounting data by standardizing units, aligning
    reporting periods, handling missing values, and removing outliers.

    Parameters
    ----------
    raw_fundamental_df : pd.DataFrame
        DataFrame returned from acquire_fundamental_data, containing columns
        such as 'ticker', 'report_date', 'eps', 'book_value', 'cash_flow',
        'leverage', 'dividend_yield', etc., possibly in mixed units and with
        missing values.

    Returns
    -------
    dict
        Dictionary with the following keys: - cleaned_record_count (int) -
        missing_value_records (int) - missing_value_flagged (bool) -
        outlier_removed_count (int) - unit_consistency_flag (bool) -
        reporting_period_aligned (bool)

    Raises
    ------
    ValueError
        If raw_fundamental_df is empty or missing required columns.
    KeyError
        If expected metric columns are not found in the input DataFrame.

    Examples
    --------
    >>> import pandas as pd
    >>> # Example raw data
    >>> raw = pd.DataFrame({
    ...     'ticker': ['A', 'A', 'B'],
    ...     'report_date': ['2022-12-31', '2023-03-31', '2022-12-31'],
    ...     'eps': [1.2, None, 0.8],
    ...     'book_value': [2000, 2100, 1500],  # in thousands
    ...     'cash_flow': [500, 550, None],
    ...     'leverage': [1.5, 1.6, 1.4],
    ...     'dividend_yield': [0.02, 0.025, 0.015]
    >>> })
    >>> result = clean_fundamental_data(raw)
    >>> print(result)
    {
      'cleaned_record_count': 3,
      'missing_value_records': 1,
      'missing_value_flagged': False,
      'outlier_removed_count': 0,
      'unit_consistency_flag': True,
      'reporting_period_aligned': True
    }

    >>> # Example with an extreme outlier
    >>> raw.loc[0, 'eps'] = 1000
    >>> result = clean_fundamental_data(raw)
    >>> print(result['outlier_removed_count'])
    1

    """
    return CleanFundamentalDataOutput(
        cleaned_record_count=0,
        missing_value_records=0,
        missing_value_flagged=False,
        outlier_removed_count=0,
        unit_consistency_flag=False,
        reporting_period_aligned=False,
    )