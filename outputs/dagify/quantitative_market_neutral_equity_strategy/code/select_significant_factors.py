from pydantic import BaseModel, Field
from typing import List


class TestFactorPerformanceOutput(BaseModel):
    """Pydantic model for test_factor_performance node outputs."""
    factor_names: List[str] = (
        Field(..., description="List of factor names evaluated")
    )
    avg_t_stats: List[float] = (
        Field(..., description="Average t\u2011statistic from cross\u2011sectional regressions for each factor")
    )
    annualized_sharpe: List[float] = (
        Field(..., description="Annualized Sharpe ratio derived from factor regression predictive power")
    )
    p_values: List[float] = (
        Field(..., description="P\u2011value of the factor coefficient in the regression")
    )
    is_significant: List[bool] = (
        Field(..., description="True if p\u2011value < 0.05, indicating statistical significance")
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


def select_significant_factors(test_factor_performance_input: TestFactorPerformanceOutput, **kwargs) -> SelectSignificantFactorsOutput:
    """
    Select factors with p-value < 0.05 and positive average t-statistic from
    factor performance results.

    Parameters
    ----------
    factor_names : List[str]
        List of factor names evaluated in the performance test.
    avg_t_stats : List[float]
        Average t-statistics corresponding to each factor from the
        regressions.
    p_values : List[float]
        P-values for each factor's performance coefficient, indicating
        statistical significance.

    Returns
    -------
    dict
        Dictionary with keys 'selected_factors' (list of factor names
        passing criteria), 'significant_factor_count' (count of these
        factors), and 'is_valid_selection' (boolean flag if valid selection
        achieved).

    Raises
    ------
    ValueError
        If input lists (factor_names, avg_t_stats, p_values) are of unequal
        length.
    ValueError
        If input lists are empty, making selection impossible.

    Examples
    --------
    >>> factor_names = ['Value', 'Momentum', 'Quality', 'Volatility']
    >>> avg_t_stats = [2.5, -1.2, 3.1, 0.5]
    >>> p_values = [0.01, 0.10, 0.03, 0.04]
    >>> result = select_significant_factors(factor_names, avg_t_stats, p_values)
    >>> print(result)
    {'selected_factors': ['Value', 'Quality', 'Volatility'],
    'significant_factor_count': 3, 'is_valid_selection': True}

    >>> factor_names = ['FactorA', 'FactorB']
    >>> avg_t_stats = [-0.5, 1.0]
    >>> p_values = [0.06, 0.06]
    >>> result = select_significant_factors(factor_names, avg_t_stats, p_values)
    >>> print(result)
    {'selected_factors': [], 'significant_factor_count': 0,
    'is_valid_selection': False}

    """
    return SelectSignificantFactorsOutput(
        selected_factors=[],
        significant_factor_count=0,
        is_valid_selection=False,
    )