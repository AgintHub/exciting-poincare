# generate_signals PRD

## Description
Produce daily predicted excess return signals for each security using the selected model.


## Conceptual Info

This node generates daily predicted excess returns signals for each security by applying the best performing predictive model to computed factor exposures over the trading history. The signals represent predicted asset-specific return differentials compared to a benchmark and form the basis for portfolio optimization.

## Docstring

### Summary
Generate daily predicted excess return signals per security by applying the selected predictive model to the computed factor exposures over time.

### Parameters

- **selected_model_name** (str): Name or identifier of the selected best performing predictive model (e.g., 'RandomForest').
- **factor_exposures** (Dict[str, Dict[str, float]] or DataFrame): Factor exposures mapped by security identifier and date, containing factor values as inputs to the model.
- **model_object** (Any): Trained predictive model instance capable of scoring or predicting excess returns given factor inputs.

### Returns

dict: Dictionary containing signal generation metadata and statistics with keys: 'date_range_start' (str), 'date_range_end' (str), 'num_signals' (int), 'signal_mean' (float), 'signal_std' (float).

### Raises

- ValueError: Raised if input factor exposures are empty or model is not properly provided.
- RuntimeError: Raised if signal generation fails due to mismatch in data dimensions or model prediction errors.

### Examples

```python
>>> signals = generate_signals(
...     selected_model_name='RandomForest',
...     factor_exposures={
...         '2023-01-02': {'AAPL': {'momentum': 0.5, 'value': -0.1}, 'MSFT': {'momentum': 0.3, 'value': 0.0}},
...         '2023-01-03': {'AAPL': {'momentum': 0.6, 'value': -0.05}, 'MSFT': {'momentum': 0.4, 'value': 0.02}},
...     },
...     model_object=rf_model_instance
>>> )
{'date_range_start': '2023-01-02', 'date_range_end': '2023-01-03', 'num_signals': 4, 'signal_mean': 0.015, 'signal_std': 0.005}
```

```python
>>> # Assuming factor_exposures is a DataFrame with MultiIndex (date, security)
>>> import pandas as pd
>>> signals = generate_signals(
...     selected_model_name='LinearRegression',
...     factor_exposures=factor_exposure_df,
...     model_object=linreg_model_instance
>>> )
{'date_range_start': '2015-01-01', 'date_range_end': '2023-01-01', 'num_signals': 100000, 'signal_mean': 0.0003, 'signal_std': 0.002}
```
