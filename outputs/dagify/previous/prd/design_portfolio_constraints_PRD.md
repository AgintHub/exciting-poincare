# design_portfolio_constraints PRD

## Description
Define the quantitative constraints that enforce market neutrality and risk limits.


## Conceptual Info

This node formulates explicit quantitative portfolio constraints to ensure market-neutrality and risk control. It codifies key portfolio requirements such as zero net market beta, zero net dollar exposure, sector neutrality enforcement, limits on individual position sizes relative to NAV, liquidity minimums based on average daily volume, and factor risk exposure bounds for selected risk factors.

## Docstring

### Summary
Constructs numerical portfolio constraints enforcing market neutrality and risk limits based on inputs from market-neutral objectives and universe criteria.

### Parameters

- **net_beta_target** (float): Target net beta exposure to the market (typically zero to achieve market neutrality).
- **dollar_exposure_target** (float): Target net dollar exposure for the portfolio (usually zero for dollar neutrality).
- **sector_neutrality** (bool): Boolean flag indicating if sector exposures must be neutralized (True) or not (False).
- **max_position_size_pct** (float): Maximum permitted position size as a fraction of Net Asset Value (e.g., 0.05 means 5%).
- **min_liquidity_pct** (float): Minimum liquidity required for a position, expressed as percentage of Average Daily Volume.
- **factor_names** (List[str]): List of factor names for which exposure constraints are defined.
- **factor_exposure_limits** (List[float]): Corresponding absolute upper bounds on portfolio exposure for each factor in factor_names.

### Returns

dict: Dictionary of portfolio constraints specifying neutrality targets, position limits, liquidity thresholds, and factor exposure caps.

### Raises

- ValueError: If lengths of factor_names and factor_exposure_limits do not match.
- ValueError: If any percentage value is outside the [0,1] interval.

### Examples

```python
>>> constraints = design_portfolio_constraints(
...     net_beta_target=0.0,
...     dollar_exposure_target=0.0,
...     sector_neutrality=True,
...     max_position_size_pct=0.05,
...     min_liquidity_pct=0.02,
...     factor_names=['Value', 'Momentum'],
...     factor_exposure_limits=[0.1, 0.15]
>>> )
}
```

```python
>>> constraints = design_portfolio_constraints(
...     net_beta_target=0.0,
...     dollar_exposure_target=0.0,
...     sector_neutrality=False,
...     max_position_size_pct=0.10,
...     min_liquidity_pct=0.05,
...     factor_names=['Quality'],
...     factor_exposure_limits=[0.2]
>>> )
}
```
