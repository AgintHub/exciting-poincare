# backtest_portfolio PRD

## Description
Simulate the strategy over the historical period using the optimized weights and transaction cost model.


## Conceptual Info

Simulates a portfolio backtest using optimized weights and transaction costs.

## Docstring

### Summary
Simulates a portfolio backtest from the earliest date to the most recent date, applying daily optimized weights and transaction costs, and outputs the time-series of portfolio daily returns, cumulative P&L, and turnover.

### Parameters

- **optimize_portfolio** (dict): Output from the optimize_portfolio node, containing optimal weights for each security.
- **acquire_price_data** (dict): Output from the acquire_price_data node, containing historical price data for the securities.
- **define_transaction_cost_model** (dict): Output from the define_transaction_cost_model node, containing transaction cost parameters.

### Returns

dict: A dictionary containing the time-series of portfolio daily returns, cumulative P&L, and turnover, as well as the length of the back-test horizon.

### Raises

- ValueError: If the input data is invalid or missing.

### Examples

```python
>>> import pandas as pd
>>> optimize_portfolio_output = {'optimal_weights': [0.1, 0.2, 0.7]}
>>> acquire_price_data_output = {'price_data': pd.DataFrame({'date': ['2022-01-01', '2022-01-02'], 'returns': [0.01, 0.02]})}
>>> define_transaction_cost_model_output = {'transaction_costs': 0.001}
>>> backtest_portfolio(optimize_portfolio_output, acquire_price_data_output, define_transaction_cost_model_output)
{'portfolio_daily_returns': [0.01, 0.02], 'cumulative_pnl': [0.01, 0.03], 'turnover': [0.1, 0.2], 'backtest_horizon_length': 2}
```
