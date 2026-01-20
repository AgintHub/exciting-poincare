# train_gradient_boosting_model PRD

## Description
Fit a gradient boosting model using the selected factors to predict next‑day returns.


## Conceptual Info

This node trains a gradient boosting regression model, specifically calibrated to predict next-day excess returns of securities using a selected subset of statistically significant predictive factors. It leverages merged cleaned data and computed factor exposures, fitting the model under specified hyperparameters and evaluating performance with validation metrics and feature importance insights.

## Docstring

### Summary
Train a gradient boosting regression model on selected factor exposures to predict next-day excess returns.

### Parameters

- **merged_data** (DataFrame or equivalent): Cleaned and merged dataset including price, fundamental, and alternative data with one row per security-date.
- **factor_exposures** (DataFrame or equivalent): Numeric exposures of each security to candidate factors computed from merged_data.
- **selected_factors** (List[str]): List of factor names selected based on statistical significance to be used as features in the model.
- **target_returns** (Series or array-like): Next-day excess returns for each security-date, aligned with factor exposures and merged data.

### Returns

dict: Dictionary containing trained model name, validation root mean squared error (RMSE), ordered list of feature names used, and corresponding feature importance scores.

### Raises

- ValueError: If no selected factors are provided or if input data dimensions do not align.
- TrainingError: If model training fails due to convergence or data quality issues.

### Examples

```python
>>> result = train_gradient_boosting_model(
...     merged_data=merged_df,
...     factor_exposures=factor_df,
...     selected_factors=['Momentum', 'Value', 'Quality'],
...     target_returns=next_day_returns_series
>>> )
>>> print(result['model_name'], result['validation_rmse'])
XGBoost_GBM 0.0125
```

```python
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
```
