# train_linear_regression_model PRD

## Description
Fit a linear regression model using the selected factors to predict next‑day returns.


## Conceptual Info

This node fits a linear regression model that predicts next-day excess returns of securities based on their exposures to a selected set of significant factors. It applies ordinary least squares regression using a merged dataset that includes price, fundamental, and alternative data alongside computed factor exposures. The model outputs the intercept, coefficients for each factor, the in-sample goodness-of-fit (R-squared), and the sample size used.

## Docstring

### Summary
Fit a linear regression model to predict next-day excess stock returns from selected factor exposures using the merged dataset.

### Parameters

- **merged_data** (DataFrame): DataFrame containing merged price, fundamental, and alternative data for each security and date.
- **factor_exposures** (DataFrame): DataFrame with computed exposures of each security to the candidate factors aligned with merged data.
- **selected_factors** (List[str]): List of factor names that passed significance criteria (p-value < 0.05 and positive average t-statistic).

### Returns

dict[str, Any]: Dictionary containing: - 'factor_names': List of factor names used in the model - 'coefficients': List of estimated coefficients matching factor order - 'intercept': Regression intercept term (float) - 'r_squared': In-sample R-squared (float) - 'n_observations': Number of observations used (int)

### Raises

- ValueError: If the merged dataset is empty or factor exposures for selected factors are missing.
- RuntimeError: If linear regression fitting fails due to numerical instability or insufficient data.

### Examples

```python
>>> merged_data = pd.DataFrame({
...     'security': ['A', 'B', 'C'],
...     'date': ['2023-01-01', '2023-01-01', '2023-01-01'],
...     'next_day_excess_return': [0.01, -0.02, 0.03],
...     'factor1': [0.5, 0.3, 0.7],
...     'factor2': [1.2, 0.9, 1.1]
>>> })
>>> factor_exposures = merged_data[['factor1', 'factor2']]
>>> selected_factors = ['factor1', 'factor2']
>>> result = train_linear_regression_model(merged_data, factor_exposures, selected_factors)
{
  'factor_names': ['factor1', 'factor2'],
  'coefficients': [0.04, 0.02],
  'intercept': 0.001,
  'r_squared': 0.85,
  'n_observations': 3
}
```

```python
>>> # Using a larger dataset with multiple observations
>>> result = train_linear_regression_model(merged_data, factor_exposures, ['factor1'])
{
  'factor_names': ['factor1'],
  'coefficients': [0.035],
  'intercept': 0.0005,
  'r_squared': 0.80,
  'n_observations': 3
}
```
