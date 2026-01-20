# risk_analysis PRD

## Description
Analyze factor exposures, drawdown drivers, and stress scenarios for the strategy.


## Conceptual Info

This node conducts a comprehensive risk analysis of the strategy's portfolio by leveraging back-test results and factor exposures. It quantifies average factor exposures, isolates key factors driving maximum drawdown, estimates how sensitive the portfolio returns were to each factor during drawdown, and performs stress testing by applying ±2 standard deviations shocks to each factor to assess potential risk under extreme movements. The output includes both summary bullet points and detailed factor sensitivity tables for robust risk management insights.

## Docstring

### Summary
Analyze portfolio factor exposures, identify main drawdown contributors, and perform ±2σ stress tests on factor sensitivities using back-test data and factor exposures.

### Parameters

- **backtest_returns** (List[float]): Time series of portfolio daily returns from the back-test period.
- **portfolio_weights** (List[List[float]]): Daily portfolio weights for each security, aligned with factor exposures.
- **factor_exposures** (Dict[str, List[List[float]]]): Dictionary mapping each factor name to its exposure matrix over securities and dates.
- **factor_stddevs** (Dict[str, float]): Standard deviation values of each factor over the back-test period used for stress shocks.

### Returns

Dict[str, Any]: Dictionary containing: factor names; average exposures per factor; maximum portfolio drawdown; top contributing factors to drawdown; drawdown period factor sensitivities; and stress test sensitivities for ±2σ shocks.

### Raises

- ValueError: If input arrays have inconsistent lengths or missing data.
- RuntimeError: If drawdown or stress test computations fail due to data issues.

### Examples

```python
>>> backtest_returns = [-0.005, -0.01, 0.002, 0.001, -0.007]
>>> portfolio_weights = [[0.1, -0.1], [0.12, -0.12], [0.11, -0.11], [0.13, -0.13], [0.1, -0.1]]
>>> factor_exposures = {
...     'Momentum': [[0.5, 0.4], [0.52, 0.42], [0.5, 0.41], [0.49, 0.43], [0.51, 0.4]],
...     'Value': [[-0.3, -0.25], [-0.31, -0.26], [-0.29, -0.24], [-0.3, -0.25], [-0.28, -0.26]]
>>> }
>>> factor_stddevs = {'Momentum': 0.1, 'Value': 0.05}
>>> results = risk_analysis(backtest_returns, portfolio_weights, factor_exposures, factor_stddevs)
>>> print(results['factor_names'])
>>> print(results['max_drawdown'])
['Momentum', 'Value']
-0.015
```

```python
>>> # The output includes average factor exposures, drawdown contributors, and stress test sensitivities in structured lists.
{" +
                ""average_exposure": [0.5, -0.3], " +
                ""top_drawdown_contributors": ["Momentum"], " +
                ""stress_sensitivity_positive": [-0.03, 0.01]" +
                
```
