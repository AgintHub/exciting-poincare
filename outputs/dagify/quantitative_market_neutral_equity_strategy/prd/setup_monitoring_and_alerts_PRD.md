# setup_monitoring_and_alerts PRD

## Description
Define the real‑time monitoring metrics and alert thresholds for live trading.


## Conceptual Info

This node defines the essential real-time monitoring metrics and their quantitative alert thresholds for the live trading environment of the quantitative market-neutral equity strategy. It specifies the frequency at which these metrics are monitored and the communication channels to notify stakeholders of any breaches or anomalies. The goal is to enable responsive operational oversight that ensures risk and execution performance remain within defined parameters.

## Docstring

### Summary
Configure the set of real-time monitoring metrics for live trading, their alert thresholds, monitoring cadence, and notification channels.

### Parameters

- **metric_names** (List[str]): List containing the names of each metric to be actively tracked and monitored during live trading (e.g., 'P&L deviation', 'Exposure Limits Breached').
- **threshold_values** (List[float]): Numerical thresholds corresponding to each metric that if crossed will trigger an alert. Thresholds may be expressed in metric-specific units or multiples of standard deviations (e.g., 2.0 for 2σ). The list order matches that of metric_names.
- **monitoring_cadence** (List[str]): Frequency at which each metric is evaluated, such as 'real-time' for continuous monitoring, 'hourly', or 'daily'. This list aligns 1-to-1 with metric_names.
- **notification_channels** (List[str]): Communication channels used to send alerts upon threshold breach, for example, 'email', 'Slack', or 'PagerDuty'. Each entry corresponds to a metric.

### Returns

dict: A dictionary containing: 'metric_names', 'threshold_values', 'monitoring_cadence', and 'notification_channels', representing the full configuration for live monitoring and alerting.

### Raises

- ValueError: If the input lists are of mismatched lengths or if threshold values are not numeric.

### Examples

```python
>>> metrics = ['P&L Deviation', 'Exposure Breach', 'Latency', 'Execution Slippage']
>>> thresholds = [2.0, 0.0, 200.0, 0.05]
>>> cadence = ['real-time', 'real-time', 'hourly', 'daily']
>>> channels = ['Slack', 'PagerDuty', 'Email', 'Email']
>>> setup_monitoring_and_alerts(metrics, thresholds, cadence, channels)
{'metric_names': ['P&L Deviation', 'Exposure Breach', 'Latency', 'Execution Slippage'],
 'threshold_values': [2.0, 0.0, 200.0, 0.05],
 'monitoring_cadence': ['real-time', 'real-time', 'hourly', 'daily'],
 'notification_channels': ['Slack', 'PagerDuty', 'Email', 'Email']}
```

```python
>>> metric_names = ['Portfolio Turnover', 'Max Drawdown']
>>> threshold_values = [0.1, 0.15]
>>> monitoring_cadence = ['daily', 'daily']
>>> notification_channels = ['Email', 'Slack']
>>> setup_monitoring_and_alerts(metric_names, threshold_values, monitoring_cadence, notification_channels)
{'metric_names': ['Portfolio Turnover', 'Max Drawdown'],
 'threshold_values': [0.1, 0.15],
 'monitoring_cadence': ['daily', 'daily'],
 'notification_channels': ['Email', 'Slack']}
```
