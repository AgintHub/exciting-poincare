from pydantic import BaseModel, Field
from typing import List


class OptimizePortfolioOutput(BaseModel):
    """Pydantic model for optimize_portfolio node outputs."""
    optimal_date: str = (
        Field(..., description="The date for which the optimal weights are computed")
    )
    weight_vector: List[float] = (
        Field(..., description="Optimal portfolio weights for each security in the universe, ordered consistently with the input signal vector")
    )
    gross_exposure: float = (
        Field(..., description="Sum of absolute values of the optimal weights, representing total gross position size")
    )
    net_exposure: float = (
        Field(..., description="Sum of the optimal weights, representing net dollar exposure after market\u2011neutral constraints")
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


class RiskAnalysisOutput(BaseModel):
    """Pydantic model for risk_analysis node outputs."""
    factor_names: List[str] = (
        Field(..., description="Names of the selected factors evaluated.")
    )
    average_exposure: List[float] = (
        Field(..., description="Average portfolio exposure to each factor over the back\u2011test period.")
    )
    max_drawdown: float = (
        Field(..., description="Maximum observed portfolio drawdown during the back\u2011test.")
    )
    top_drawdown_contributors: List[str] = (
        Field(..., description="Factors identified as the largest contributors to the maximum drawdown.")
    )
    drawdown_sensitivity: List[float] = (
        Field(..., description="Estimated change in portfolio return per unit change in each factor during the drawdown period.")
    )
    stress_factor_names: List[str] = (
        Field(..., description="Names of factors used in the \u00b12\u03c3 stress test.")
    )
    stress_sensitivity_positive: List[float] = (
        Field(..., description="Portfolio return sensitivity when each factor is shocked +2\u03c3.")
    )
    stress_sensitivity_negative: List[float] = (
        Field(..., description="Portfolio return sensitivity when each factor is shocked -2\u03c3.")
    )


def risk_analysis(optimize_portfolio_input: OptimizePortfolioOutput, compute_factor_exposures_input: ComputeFactorExposuresOutput, **kwargs) -> RiskAnalysisOutput:
    """
    Analyze portfolio factor exposures, identify main drawdown contributors, and
    perform ±2σ stress tests on factor sensitivities using back-test data and
    factor exposures.

    Parameters
    ----------
    backtest_returns : List[float]
        Time series of portfolio daily returns from the back-test period.
    portfolio_weights : List[List[float]]
        Daily portfolio weights for each security, aligned with factor
        exposures.
    factor_exposures : Dict[str, List[List[float]]]
        Dictionary mapping each factor name to its exposure matrix over
        securities and dates.
    factor_stddevs : Dict[str, float]
        Standard deviation values of each factor over the back-test period
        used for stress shocks.

    Returns
    -------
    Dict[str, Any]
        Dictionary containing: factor names; average exposures per factor;
        maximum portfolio drawdown; top contributing factors to drawdown;
        drawdown period factor sensitivities; and stress test sensitivities
        for ±2σ shocks.

    Raises
    ------
    ValueError
        If input arrays have inconsistent lengths or missing data.
    RuntimeError
        If drawdown or stress test computations fail due to data issues.

    Examples
    --------
    >>> backtest_returns = [-0.005, -0.01, 0.002, 0.001, -0.007]
    >>> portfolio_weights = [[0.1, -0.1], [0.12, -0.12], [0.11, -0.11], [0.13,
    -0.13], [0.1, -0.1]]
    >>> factor_exposures = {
    ...     'Momentum': [[0.5, 0.4], [0.52, 0.42], [0.5, 0.41], [0.49, 0.43],
    [0.51, 0.4]],
    ...     'Value': [[-0.3, -0.25], [-0.31, -0.26], [-0.29, -0.24], [-0.3,
    -0.25], [-0.28, -0.26]]
    >>> }
    >>> factor_stddevs = {'Momentum': 0.1, 'Value': 0.05}
    >>> results = risk_analysis(backtest_returns, portfolio_weights,
    factor_exposures, factor_stddevs)
    >>> print(results['factor_names'])
    >>> print(results['max_drawdown'])
    ['Momentum', 'Value']
    -0.015

    >>> # The output includes average factor exposures, drawdown contributors,
    and stress test sensitivities in structured lists.
    {" +
                    ""average_exposure": [0.5, -0.3], " +
                    ""top_drawdown_contributors": ["Momentum"], " +
                    ""stress_sensitivity_positive": [-0.03, 0.01]" +
                    

    """
    return RiskAnalysisOutput(
        factor_names=[],
        average_exposure=[],
        max_drawdown=0.0,
        top_drawdown_contributors=[],
        drawdown_sensitivity=[],
        stress_factor_names=[],
        stress_sensitivity_positive=[],
        stress_sensitivity_negative=[],
    )