# evaluate_models PRD

## Description
Compare the three trained models using out‑of‑sample back‑testing on a hold‑out period.


## Conceptual Info

This node performs a rolling-window out-of-sample evaluation of three trained predictive models—Linear Regression, Random Forest, and Gradient Boosting—using back-testing on a designated holdout period. It generates risk-adjusted performance metrics including annualized return, Sharpe ratio, maximum drawdown, and information ratio, enabling direct comparison of models' forward-looking predictive efficacy.

## Docstring

### Summary
Evaluate and compare trained predictive models with rolling-window out-of-sample back-testing over a holdout period, computing key performance metrics for each.

### Parameters

- **trained_models** (dict[str, Any]): Dictionary containing the trained models with keys as model identifiers ('LinearRegression', 'RandomForest', 'GradientBoosting') and values as the corresponding trained model objects or metadata.
- **holdout_period_years** (int): Integer number of years specifying the holdout (out-of-sample testing) period length used in the rolling evaluation.
- **rolling_window_config** (dict): Configuration dictionary defining the rolling window evaluation parameters, e.g., training window length (years), testing window length (years), and step size (e.g., 1 year).
- **historical_market_data** (DataFrame): Historical market data including factor exposures, returns, and relevant security identifiers required for out-of-sample testing.
- **benchmark_returns** (Series): Benchmark return series for calculating information ratio during back-testing.

### Returns

List[dict]: List of dictionaries, each containing evaluation metrics ('model_name', 'holdout_period_years', 'annualized_return', 'annualized_sharpe', 'maximum_drawdown', 'information_ratio') for one of the trained models.

### Raises

- ValueError: If the holdout_period_years is non-positive or exceeds data availability.
- KeyError: If required model names or training data are missing.
- RuntimeError: If backtesting or metric computations fail due to inconsistent data or errors.

### Examples

```python
>>> trained_models = {
...     'LinearRegression': linear_reg_model,
...     'RandomForest': rf_model,
...     'GradientBoosting': gbm_model
>>> }
>>> results = evaluate_models(trained_models, holdout_period_years=1, rolling_window_config={'train_years':2, 'test_years':1}, historical_market_data=market_df, benchmark_returns=bench_returns)
>>> for res in results:
...     print(f"Model: {res['model_name']}, Annualized Return: {res['annualized_return']:.2%}, Sharpe: {res['annualized_sharpe']:.2f}")
Model: LinearRegression, Annualized Return: 8.27%, Sharpe: 1.10
Model: RandomForest, Annualized Return: 10.15%, Sharpe: 1.35
Model: GradientBoosting, Annualized Return: 11.42%, Sharpe: 1.48
```
