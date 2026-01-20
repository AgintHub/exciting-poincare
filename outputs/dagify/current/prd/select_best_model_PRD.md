# select_best_model PRD

## Description
Identify the model with the highest risk-adjusted performance.


## Conceptual Info

Selects the model with the highest risk-adjusted performance from the evaluation table.

## Docstring

### Summary
Select the best model based on the highest information ratio or Sharpe ratio from the evaluation table.

### Parameters

- **evaluation_table** (dict): Dictionary containing model performance metrics

### Returns

dict: Dictionary with the selected model name and its key performance numbers

### Raises

- ValueError: If the evaluation table is empty or no model performance metrics are provided

### Examples

```python
>>> evaluation_table = {
...   'LinearRegression': {'information_ratio': 0.8, 'sharpe_ratio': 1.2, 'annualized_return': 0.1, 'maximum_drawdown': -0.05},
...   'RandomForest': {'information_ratio': 0.9, 'sharpe_ratio': 1.1, 'annualized_return': 0.2, 'maximum_drawdown': -0.03},
...   'GradientBoosting': {'information_ratio': 1.0, 'sharpe_ratio': 1.3, 'annualized_return': 0.3, 'maximum_drawdown': -0.04}
>>> }
>>> select_best_model(evaluation_table)
{'selected_model': 'GradientBoosting', 'information_ratio': 1.0, 'sharpe_ratio': 1.3, 'annualized_return': 0.3, 'maximum_drawdown': -0.04}
```
