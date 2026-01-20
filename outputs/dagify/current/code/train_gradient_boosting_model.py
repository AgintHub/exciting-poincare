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


class TrainGradientBoostingModelOutput(BaseModel):
    """Pydantic model for train_gradient_boosting_model node outputs."""
    model_name: str = (
        Field(..., description="Name of the trained model (e.g., XGBoost_GBM).")
    )
    validation_rmse: float = (
        Field(..., description="Root Mean Squared Error on the validation set.")
    )
    feature_names: List[str] = (
        Field(..., description="Ordered list of feature names used in the model.")
    )
    feature_importances: List[float] = (
        Field(..., description="Relative importance scores for each feature, aligned with feature_names.")
    )


def train_gradient_boosting_model(compute_factor_exposures_input: ComputeFactorExposuresOutput, select_significant_factors_input: SelectSignificantFactorsOutput, merge_cleaned_data_input: MergeCleanedDataOutput, **kwargs) -> TrainGradientBoostingModelOutput:
    """
    Train a gradient boosting regression model on selected factor exposures to
    predict next-day excess returns.

    Parameters
    ----------
    merged_data : DataFrame or equivalent
        Cleaned and merged dataset including price, fundamental, and
        alternative data with one row per security-date.
    factor_exposures : DataFrame or equivalent
        Numeric exposures of each security to candidate factors computed
        from merged_data.
    selected_factors : List[str]
        List of factor names selected based on statistical significance to
        be used as features in the model.
    target_returns : Series or array-like
        Next-day excess returns for each security-date, aligned with factor
        exposures and merged data.

    Returns
    -------
    dict
        Dictionary containing trained model name, validation root mean
        squared error (RMSE), ordered list of feature names used, and
        corresponding feature importance scores.

    Raises
    ------
    ValueError
        If no selected factors are provided or if input data dimensions do
        not align.
    TrainingError
        If model training fails due to convergence or data quality issues.

    Examples
    --------
    >>> result = train_gradient_boosting_model(
    ...     merged_data=merged_df,
    ...     factor_exposures=factor_df,
    ...     selected_factors=['Momentum', 'Value', 'Quality'],
    ...     target_returns=next_day_returns_series
    >>> )
    >>> print(result['model_name'], result['validation_rmse'])
    XGBoost_GBM 0.0125

    >>> model_info = train_gradient_boosting_model(
    ...     merged_data=merged_df,
    ...     factor_exposures=factor_df,
    ...     selected_factors=['Sentiment_Score', 'Earnings_Revisions'],
    ...     target_returns=next_day_returns_series
    >>> )
    >>> print(model_info['feature_names'])
    >>> print(model_info['feature_importances'])
    ['Sentiment_Score', 'Earnings_Revisions']
    [0.65, 0.35]

    """
    return TrainGradientBoostingModelOutput(
        model_name="",
        validation_rmse=0.0,
        feature_names=[],
        feature_importances=[],
    )