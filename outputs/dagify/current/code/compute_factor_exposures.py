from pydantic import BaseModel, Field
from typing import List


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


class DefineFactorCandidatesOutput(BaseModel):
    """Pydantic model for define_factor_candidates node outputs."""
    factor_names: List[str] = (
        Field(..., description="A list of candidate factor names to be evaluated.")
    )
    factor_definitions: List[str] = (
        Field(..., description="A short definition or description for each corresponding factor.")
    )


class ComputeFactorExposuresOutput(BaseModel):
    """Pydantic model for compute_factor_exposures node outputs."""
    factor_names: List[str] = (
        Field(..., description="List of all factor names computed for each security-day")
    )
    factor_calculation_descriptions: List[str] = (
        Field(..., description="For each factor, a brief description of the calculation method (e.g., ratio, ranking)")
    )
    factor_column_schema: str = (
        Field(..., description="Text representation of the table schema for the factor columns (e.g., \"factor_name: float, calculation: str\")")
    )
    total_factor_columns: int = (
        Field(..., description="Total number of factor columns generated across all securities and dates")
    )


def compute_factor_exposures(merge_cleaned_data_input: MergeCleanedDataOutput, define_factor_candidates_input: DefineFactorCandidatesOutput, **kwargs) -> ComputeFactorExposuresOutput:
    """
    Compute numerical exposures of each security on each date for all candidate
    factors.

    Parameters
    ----------
    merged_data : pd.DataFrame
        Merged dataset containing price, fundamental, and alternative data
        for each security-day.
    factor_candidates : List[Factor]
        List of candidate factors to be computed, each with a name and
        calculation method.

    Returns
    -------
    dict
        Dictionary containing the list of factor names, calculation
        descriptions, factor column schema, and total number of factor
        columns.

    Raises
    ------
    ValueError
        If the merged data is empty or if no factor candidates are provided.

    Examples
    --------
    >>> merged_data = pd.DataFrame({'security_id': ['AAPL', 'GOOG'], 'date':
    ['2022-01-01', '2022-01-01'], 'price': [100.0, 2000.0]})
    >>> factor_candidates = [Factor('book_to_price', 'Book-to-Price ratio')]
    >>> result = compute_factor_exposures(merged_data, factor_candidates)
    {'factor_names': ['book_to_price'], 'factor_calculation_descriptions':
    ['Book-to-Price ratio'], 'factor_column_schema': 'book_to_price: float,
    calculation: str', 'total_factor_columns': 1}

    """
    return ComputeFactorExposuresOutput(
        factor_names=[],
        factor_calculation_descriptions=[],
        factor_column_schema="",
        total_factor_columns=0,
    )