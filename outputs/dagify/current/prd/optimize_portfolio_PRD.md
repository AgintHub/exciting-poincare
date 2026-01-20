# optimize_portfolio PRD

## Description
Solve for optimal security weights that maximize predicted return subject to the defined constraints and transaction cost model.


## Conceptual Info

This node performs portfolio optimization by solving a quadratic programming problem that maximizes expected returns based on predicted signals while incorporating transaction costs and satisfying portfolio constraints. It outputs the optimal security weights for a given date and reports gross and net exposures.

## Docstring

### Summary
Compute the optimal portfolio weights that maximize predicted returns net of transaction costs under predefined constraints for a specified date.

### Parameters

- **signal_vector** (List[float]): Predicted excess return signals for each security on the optimization date, aligned with the portfolio universe.
- **constraints** (Dict[str, Any]): A dictionary encapsulating portfolio constraints such as net beta target, dollar exposure target, sector neutrality flag, maximum position size percentage, minimum liquidity threshold, factor names, and factor exposure limits.
- **transaction_costs** (Dict[str, float]): Parameters of the transaction cost model including commission per share, bid-ask spread percentage, and market impact factor.
- **current_positions** (List[float]): Current portfolio weights for each security, used to compute transaction costs related to rebalancing.
- **date** (str): The specific date (ISO format YYYY-MM-DD) for which to compute the optimal portfolio weights.

### Returns

Dict[str, Any]: A dictionary containing: 'optimal_date' the optimization date; 'weight_vector' list of floats for optimal security weights; 'gross_exposure' total absolute exposure float; 'net_exposure' net dollar exposure float.

### Raises

- ValueError: Raised if input vectors lengths do not match or if constraints are not properly specified.
- OptimizationError: Raised if the quadratic programming solver fails to find a feasible or optimal solution.

### Examples

```python
>>> signal_vector = [0.02, 0.01, -0.01]
>>> constraints = {
...     'net_beta_target': 0.0,
...     'dollar_exposure_target': 0.0,
...     'sector_neutrality': True,
...     'max_position_size_pct': 0.05,
...     'min_liquidity_pct': 0.02,
...     'factor_names': ['value', 'momentum'],
...     'factor_exposure_limits': [0.1, 0.15]
>>> }
>>> transaction_costs = {
...     'commission_per_share': 0.005,
...     'bid_ask_spread_percent': 0.001,
...     'impact_factor': 0.2
>>> }
>>> current_positions = [0.0, 0.0, 0.0]
>>> date = '2023-08-01'
>>> output = optimize_portfolio(signal_vector, constraints, transaction_costs, current_positions, date)
{
  'optimal_date': '2023-08-01',
  'weight_vector': [0.04, 0.03, -0.05],
  'gross_exposure': 0.12,
  'net_exposure': 0.02
}
```

```python
>>> # For a single-day optimization with existing positions
>>> signal_vector = [0.015, 0.025]
>>> constraints = {
...     'net_beta_target': 0.0,
...     'dollar_exposure_target': 0.0,
...     'sector_neutrality': False,
...     'max_position_size_pct': 0.1,
...     'min_liquidity_pct': 0.03,
...     'factor_names': ['quality'],
...     'factor_exposure_limits': [0.2]
>>> }
>>> transaction_costs = {
...     'commission_per_share': 0.004,
...     'bid_ask_spread_percent': 0.0015,
...     'impact_factor': 0.15
>>> }
>>> current_positions = [0.02, -0.01]
>>> date = '2023-08-02'
>>> output = optimize_portfolio(signal_vector, constraints, transaction_costs, current_positions, date)
{
  'optimal_date': '2023-08-02',
  'weight_vector': [0.07, -0.06],
  'gross_exposure': 0.13,
  'net_exposure': 0.01
}
```
