# design_execution_strategy PRD

## Description
Outline the algorithmic execution approach to implement daily trades with minimal market impact.


## Conceptual Info

This node defines a detailed algorithmic trading execution strategy that translates daily optimized portfolio weights into timed child orders. It aims to minimize market impact and execution costs by controlling participation rates and slicing orders across the trading day while monitoring execution quality.

## Docstring

### Summary
Generates an execution algorithm strategy converting daily target portfolio weights into time-sliced child orders with participation constraints, supporting minimal market impact and quality monitoring.

### Parameters

- **algorithm_name** (str): The name of the execution algorithm to be used, e.g., 'VWAP', 'TWAP', or 'Implementation Shortfall'.
- **strategy_type** (str): The broad classification of the execution strategy, such as 'Volume-Weighted', 'Time-Weighted', or 'Market-Milking'.
- **participation_rate** (float): Maximum fraction (0 to 1) of the estimated daily volume to participate in trading for each security.
- **slice_frequency_minutes** (int): Interval in minutes between successive child order placements within the trading day.
- **child_order_weights** (List[float]): List of target fractional order sizes relative to the total daily order, corresponding slice by slice.
- **order_time_stamps** (List[str]): List of ISO 8601 formatted timestamps indicating the scheduled execution times for each child order slice.
- **execution_quality_metric** (str): A metric name for assessing execution performance, such as 'VWAP deviation %' or 'Execution Slippage %'.

### Returns

dict: A dictionary encapsulating the execution algorithm details: algorithm name, strategy type, participation rate limit, slice frequency, weights and timestamps for child slices, and the quality metric for execution assessment.

### Raises

- ValueError: If participation_rate is not in (0,1], or if slice_frequency_minutes is non-positive.
- ValueError: If lengths of child_order_weights and order_time_stamps lists differ or are empty.
- TypeError: If input types do not match the expected types.

### Examples

```python
>>> design_execution_strategy(
...     algorithm_name='VWAP',
...     strategy_type='Volume-Weighted',
...     participation_rate=0.1,
...     slice_frequency_minutes=15,
...     child_order_weights=[0.05, 0.1, 0.15, 0.2, 0.25, 0.25],
...     order_time_stamps=["2024-06-14T09:30:00Z", "2024-06-14T09:45:00Z", "2024-06-14T10:00:00Z",
...                       "2024-06-14T10:15:00Z", "2024-06-14T10:30:00Z", "2024-06-14T10:45:00Z"],
...     execution_quality_metric='VWAP deviation %'
>>> )
{'algorithm_name': 'VWAP', 'strategy_type': 'Volume-Weighted', 'participation_rate': 0.1, 'slice_frequency_minutes': 15, 'child_order_weights': [0.05, 0.1, 0.15, 0.2, 0.25, 0.25], 'order_time_stamps': ['2024-06-14T09:30:00Z', '2024-06-14T09:45:00Z', '2024-06-14T10:00:00Z', '2024-06-14T10:15:00Z', '2024-06-14T10:30:00Z', '2024-06-14T10:45:00Z'], 'execution_quality_metric': 'VWAP deviation %'}
```

```python
>>> design_execution_strategy(
...     algorithm_name='TWAP',
...     strategy_type='Time-Weighted',
...     participation_rate=0.05,
...     slice_frequency_minutes=30,
...     child_order_weights=[0.2, 0.2, 0.2, 0.2, 0.2],
...     order_time_stamps=["2024-06-14T09:30:00Z", "2024-06-14T10:00:00Z", "2024-06-14T10:30:00Z",
...                       "2024-06-14T11:00:00Z", "2024-06-14T11:30:00Z"],
...     execution_quality_metric='Execution Slippage %'
>>> )
{'algorithm_name': 'TWAP', 'strategy_type': 'Time-Weighted', 'participation_rate': 0.05, 'slice_frequency_minutes': 30, 'child_order_weights': [0.2, 0.2, 0.2, 0.2, 0.2], 'order_time_stamps': ['2024-06-14T09:30:00Z', '2024-06-14T10:00:00Z', '2024-06-14T10:30:00Z', '2024-06-14T11:00:00Z', '2024-06-14T11:30:00Z'], 'execution_quality_metric': 'Execution Slippage %'}
```
