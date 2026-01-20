from pydantic import BaseModel, Field
from typing import List


class SelectBestModelOutput(BaseModel):
    """Pydantic model for select_best_model node outputs."""
    selected_model: str = (
        Field(..., description="Name of the model selected as best performer")
    )
    information_ratio: float = (
        Field(..., description="Information ratio of the selected model")
    )
    sharpe_ratio: float = (
        Field(..., description="Sharpe ratio of the selected model")
    )
    annualized_return: float = (
        Field(..., description="Annualized return of the selected model")
    )
    maximum_drawdown: float = (
        Field(..., description="Maximum drawdown observed for the selected model")
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


class GenerateSignalsOutput(BaseModel):
    """Pydantic model for generate_signals node outputs."""
    date_range_start: str = (
        Field(..., description="The first date for which signals were generated, in ISO format (YYYY-MM-DD).")
    )
    date_range_end: str = (
        Field(..., description="The last date for which signals were generated, in ISO format (YYYY-MM-DD).")
    )
    num_signals: int = (
        Field(..., description="Total number of signal entries generated across all securities and dates.")
    )
    signal_mean: float = (
        Field(..., description="Mean of all predicted excess return signals.")
    )
    signal_std: float = (
        Field(..., description="Standard deviation of all predicted excess return signals.")
    )


def generate_signals(select_best_model_input: SelectBestModelOutput, compute_factor_exposures_input: ComputeFactorExposuresOutput, **kwargs) -> GenerateSignalsOutput:
    """
    Generate daily predicted excess return signals per security by applying the
    selected predictive model to the computed factor exposures over time.

    Parameters
    ----------
    selected_model_name : str
        Name or identifier of the selected best performing predictive model
        (e.g., 'RandomForest').
    factor_exposures : Dict[str, Dict[str, float]] or DataFrame
        Factor exposures mapped by security identifier and date, containing
        factor values as inputs to the model.
    model_object : Any
        Trained predictive model instance capable of scoring or predicting
        excess returns given factor inputs.

    Returns
    -------
    dict
        Dictionary containing signal generation metadata and statistics with
        keys: 'date_range_start' (str), 'date_range_end' (str),
        'num_signals' (int), 'signal_mean' (float), 'signal_std' (float).

    Raises
    ------
    ValueError
        Raised if input factor exposures are empty or model is not properly
        provided.
    RuntimeError
        Raised if signal generation fails due to mismatch in data dimensions
        or model prediction errors.

    Examples
    --------
    >>> signals = generate_signals(
    ...     selected_model_name='RandomForest',
    ...     factor_exposures={
    ...         '2023-01-02': {'AAPL': {'momentum': 0.5, 'value': -0.1}, 'MSFT':
    {'momentum': 0.3, 'value': 0.0}},
    ...         '2023-01-03': {'AAPL': {'momentum': 0.6, 'value': -0.05},
    'MSFT': {'momentum': 0.4, 'value': 0.02}},
    ...     },
    ...     model_object=rf_model_instance
    >>> )
    {'date_range_start': '2023-01-02', 'date_range_end': '2023-01-03',
    'num_signals': 4, 'signal_mean': 0.015, 'signal_std': 0.005}

    >>> # Assuming factor_exposures is a DataFrame with MultiIndex (date,
    security)
    >>> import pandas as pd
    >>> signals = generate_signals(
    ...     selected_model_name='LinearRegression',
    ...     factor_exposures=factor_exposure_df,
    ...     model_object=linreg_model_instance
    >>> )
    {'date_range_start': '2015-01-01', 'date_range_end': '2023-01-01',
    'num_signals': 100000, 'signal_mean': 0.0003, 'signal_std': 0.002}

    """
    return GenerateSignalsOutput(
        date_range_start="",
        date_range_end="",
        num_signals=0,
        signal_mean=0.0,
        signal_std=0.0,
    )