# define_transaction_cost_model PRD

## Description
Specify the cost model used to estimate slippage and commissions for back‑testing.


## Conceptual Info

Defines a quantitative transaction cost model including fixed per-share commissions, bid-ask spread as percentage of price, and a market impact factor modeled by the square-root function of trade size relative to average daily volume. These parameters facilitate realistic cost estimation of trades during back-testing and portfolio optimization.

## Docstring

### Summary
Specify the transaction cost model parameters to estimate trading costs including commissions, bid-ask spread, and market impact for back-testing equity strategies.

### Parameters

- **commission_per_share** (float): Fixed commission charged per share traded, e.g., 0.005 equals $0.005 per share.
- **bid_ask_spread_percent** (float): Bid-ask spread expressed as a decimal percentage of the security price, e.g., 0.001 = 0.1% spread.
- **impact_factor** (float): Market impact parameter for the square-root function modeling price impact relative to trade size and average daily volume, typically between 0 and 1.

### Returns

dict: Dictionary containing the parameters: commission_per_share (float), bid_ask_spread_percent (float), impact_factor (float).

### Raises

- ValueError: If any of the input parameter values are negative or not within reasonable bounds.

### Examples

```python
>>> cost_model = define_transaction_cost_model(
...     commission_per_share=0.005,
...     bid_ask_spread_percent=0.001,
...     impact_factor=0.2
>>> )
>>> print(cost_model)
{'commission_per_share': 0.005, 'bid_ask_spread_percent': 0.001, 'impact_factor': 0.2}
```

```python
>>> cost_model = define_transaction_cost_model(
...     commission_per_share=0.007,
...     bid_ask_spread_percent=0.002,
...     impact_factor=0.15
>>> )
>>> print(cost_model)
{'commission_per_share': 0.007, 'bid_ask_spread_percent': 0.002, 'impact_factor': 0.15}
```
