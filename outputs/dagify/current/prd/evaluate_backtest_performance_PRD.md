# evaluate_backtest_performance PRD

## Description
Calculate performance metrics for the back‑test results.


## Conceptual Info

This node calculates various performance metrics for a backtest, including annualized return, volatility, Sharpe ratio, information ratio, maximum drawdown, and turnover.

## Docstring

### Summary
Evaluate the performance of a backtest by calculating key metrics.

### Parameters

- **backtest_results** (dict): Results from the backtest, including portfolio daily returns, cumulative P&L, and turnover.

### Returns

dict: A dictionary containing the calculated performance metrics.

### Raises

- ValueError: If the backtest results are invalid or missing required data.

### Examples

```python
>>> backtest_results = {'portfolio_daily_returns': [0.01, 0.02, -0.01],
...                         'cumulative_pnl': [100, 120, 110],
...                         'turnover': [0.1, 0.2, 0.1]}
>>> performance_metrics = evaluate_backtest_performance(backtest_results)
{'annualized_return': 0.08, 'annualized_volatility': 0.15, 'sharpe_ratio': 0.53, 'information_ratio': 0.42, 'maximum_drawdown': -0.1, 'turnover': 0.2, 'underperformance_periods': ['2022-01-01']}
```
