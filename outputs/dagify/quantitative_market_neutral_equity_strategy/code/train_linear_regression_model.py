from pydantic import BaseModel, Field
from typing import List


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


class SelectSignificantFactorsOutput(BaseModel):
    """Pydantic model for select_significant_factors node outputs."""
    selected_factors: List[str] = (
        Field(..., description="Names of factors that met the significance criteria (p-value < 0.05 and positive average t-statistic). Each name represents one factor.")
    )
    significant_factor_count: int = (
        Field(..., description="Total number of factors that passed the significance thresholds.")
    )
    is_valid_selection: bool = (
        Field(..., description="Indicates whether the selection process completed without errors and produced at least one significant factor.")
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


class TrainLinearRegressionModelOutput(BaseModel):
    """Pydantic model for train_linear_regression_model node outputs."""
    factor_names: List[str] = (
        Field(..., description="Ordered list of factor names used as regressors in the model.")
    )
    coefficients: List[float] = (
        Field(..., description="Estimated regression coefficient for each factor, in the same order as factor_names.")
    )
    intercept: float = (
        Field(..., description="Estimated intercept term of the linear regression.")
    )
    r_squared: float = (
        Field(..., description="In\u2011sample R\u2011squared value of the fitted model.")
    )
    n_observations: int = (
        Field(..., description="Number of observations (security\u2011days) used to fit the model.")
    )


def train_linear_regression_model(compute_factor_exposures_input: ComputeFactorExposuresOutput, select_significant_factors_input: SelectSignificantFactorsOutput, merge_cleaned_data_input: MergeCleanedDataOutput, **kwargs) -> TrainLinearRegressionModelOutput:
    """
    Fit a linear regression model to predict next-day excess stock returns from
    selected factor exposures using the merged dataset.

    Parameters
    ----------
    merged_data : DataFrame
        DataFrame containing merged price, fundamental, and alternative data
        for each security and date.
    factor_exposures : DataFrame
        DataFrame with computed exposures of each security to the candidate
        factors aligned with merged data.
    selected_factors : List[str]
        List of factor names that passed significance criteria (p-value <
        0.05 and positive average t-statistic).

    Returns
    -------
    dict[str, Any]
        Dictionary containing: - 'factor_names': List of factor names used
        in the model - 'coefficients': List of estimated coefficients
        matching factor order - 'intercept': Regression intercept term
        (float) - 'r_squared': In-sample R-squared (float) -
        'n_observations': Number of observations used (int)

    Raises
    ------
    ValueError
        If the merged dataset is empty or factor exposures for selected
        factors are missing.
    RuntimeError
        If linear regression fitting fails due to numerical instability or
        insufficient data.

    Examples
    --------
    >>> merged_data = pd.DataFrame({
    ...     'security': ['A', 'B', 'C'],
    ...     'date': ['2023-01-01', '2023-01-01', '2023-01-01'],
    ...     'next_day_excess_return': [0.01, -0.02, 0.03],
    ...     'factor1': [0.5, 0.3, 0.7],
    ...     'factor2': [1.2, 0.9, 1.1]
    >>> })
    >>> factor_exposures = merged_data[['factor1', 'factor2']]
    >>> selected_factors = ['factor1', 'factor2']
    >>> result = train_linear_regression_model(merged_data, factor_exposures,
    selected_factors)
    {
      'factor_names': ['factor1', 'factor2'],
      'coefficients': [0.04, 0.02],
      'intercept': 0.001,
      'r_squared': 0.85,
      'n_observations': 3
    }

    >>> # Using a larger dataset with multiple observations
    >>> result = train_linear_regression_model(merged_data, factor_exposures,
    ['factor1'])
    {
      'factor_names': ['factor1'],
      'coefficients': [0.035],
      'intercept': 0.0005,
      'r_squared': 0.80,
      'n_observations': 3
    }

    """
    return TrainLinearRegressionModelOutput(
        factor_names=[],
        coefficients=[],
        intercept=0.0,
        r_squared=0.0,
        n_observations=0,
    )