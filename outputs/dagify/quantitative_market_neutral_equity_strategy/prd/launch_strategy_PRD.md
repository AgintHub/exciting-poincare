# launch_strategy PRD

## Description
Execute the final steps to go live with the market‑neutral equity strategy.


## Conceptual Info

This node finalizes the launch of the market-neutral equity strategy by verifying completion of all critical pre-launch requirements including infrastructure readiness, data connectivity, compliance approval, risk limit settings, and active monitoring. It then issues a formal launch confirmation stating the strategy is live as of the current date.

## Docstring

### Summary
Finalize and execute the launch sequence for the market-neutral equity strategy, confirming all pre-launch prerequisites are complete and the strategy is live.

### Parameters

- **deployment_plan_status** (dict): Status and details from the deployment plan node indicating readiness of deployment phases.
- **monitoring_setup_status** (dict): Details of monitoring metrics, alert thresholds, and notification channels from setup_monitoring_and_alerts node indicating monitoring readiness.
- **infrastructure_status** (str): Current status of infrastructure confirming readiness ('ready' or 'not ready').
- **data_feeds_status** (str): Connectivity and operational status of data feeds ('connected' or 'not connected').
- **compliance_sign_off** (bool): Flag indicating whether compliance has signed off on the strategy.
- **risk_limits** (str): Description or reference to the risk limits that have been configured and approved.
- **monitoring_status** (str): Status of monitoring systems ('active' or 'inactive').

### Returns

dict: A dictionary containing the launch status boolean, launch date string, checklist of confirmed pre-launch items, and current system/component statuses.

### Raises

- ValueError: If any critical pre-launch item is incomplete or shows a negative status preventing a successful launch.
- RuntimeError: If infrastructure or data feeds are not ready or monitoring is inactive at launch time.

### Examples

```python
>>> launch_strategy(
...   deployment_plan_status={'phase_names': ['Phase 1', 'Phase 2', 'Phase 3'], 'summary_table': '...'},
...   monitoring_setup_status={
...     'metric_names': ['P&L deviation', 'Exposure limits breached'],
...     'threshold_values': [2.0, 0.05],
...     'monitoring_cadence': ['real-time', 'real-time'],
...     'notification_channels': ['Slack', 'email']
...   },
...   infrastructure_status='ready',
...   data_feeds_status='connected',
...   compliance_sign_off=True,
...   risk_limits='Max position size 5%, Net beta 0, Sector neutrality',
...   monitoring_status='active'
>>> )
{
```
