from pydantic import BaseModel, Field
from typing import List


class DraftOperationalWorkflowOutput(BaseModel):
    """Pydantic model for draft_operational_workflow node outputs."""
    step_numbers: List[int] = (
        Field(..., description="Ordered list of step numbers in the workflow")
    )
    step_descriptions: List[str] = (
        Field(..., description="Textual description of each workflow step")
    )
    step_responsible: List[str] = (
        Field(..., description="Name of the system or team responsible for each step")
    )
    workflow_summary: str = (
        Field(..., description="Concise summary of the overall operational workflow")
    )


class SetupMonitoringAndAlertsOutput(BaseModel):
    """Pydantic model for setup_monitoring_and_alerts node outputs."""
    metric_names: List[str] = (
        Field(..., description="Names of the live monitoring metrics to be tracked")
    )
    threshold_values: List[float] = (
        Field(..., description="Numerical alert thresholds corresponding to each metric, expressed in the metric\u2019s units or standard deviations")
    )
    monitoring_cadence: List[str] = (
        Field(..., description="Cadence for each metric (e.g., \"real\u2011time\", \"hourly\", \"daily\")")
    )
    notification_channels: List[str] = (
        Field(..., description="Channels to be used for alert delivery (e.g., \"email\", \"Slack\", \"PagerDuty\")")
    )


def setup_monitoring_and_alerts(draft_operational_workflow_input: DraftOperationalWorkflowOutput, **kwargs) -> SetupMonitoringAndAlertsOutput:
    """
    Configure the set of real-time monitoring metrics for live trading, their
    alert thresholds, monitoring cadence, and notification channels.

    Parameters
    ----------
    metric_names : List[str]
        List containing the names of each metric to be actively tracked and
        monitored during live trading (e.g., 'P&L deviation', 'Exposure
        Limits Breached').
    threshold_values : List[float]
        Numerical thresholds corresponding to each metric that if crossed
        will trigger an alert. Thresholds may be expressed in metric-
        specific units or multiples of standard deviations (e.g., 2.0 for
        2σ). The list order matches that of metric_names.
    monitoring_cadence : List[str]
        Frequency at which each metric is evaluated, such as 'real-time' for
        continuous monitoring, 'hourly', or 'daily'. This list aligns 1-to-1
        with metric_names.
    notification_channels : List[str]
        Communication channels used to send alerts upon threshold breach,
        for example, 'email', 'Slack', or 'PagerDuty'. Each entry
        corresponds to a metric.

    Returns
    -------
    dict
        A dictionary containing: 'metric_names', 'threshold_values',
        'monitoring_cadence', and 'notification_channels', representing the
        full configuration for live monitoring and alerting.

    Raises
    ------
    ValueError
        If the input lists are of mismatched lengths or if threshold values
        are not numeric.

    Examples
    --------
    >>> metrics = ['P&L Deviation', 'Exposure Breach', 'Latency', 'Execution
    Slippage']
    >>> thresholds = [2.0, 0.0, 200.0, 0.05]
    >>> cadence = ['real-time', 'real-time', 'hourly', 'daily']
    >>> channels = ['Slack', 'PagerDuty', 'Email', 'Email']
    >>> setup_monitoring_and_alerts(metrics, thresholds, cadence, channels)
    {'metric_names': ['P&L Deviation', 'Exposure Breach', 'Latency', 'Execution
    Slippage'],
     'threshold_values': [2.0, 0.0, 200.0, 0.05],
     'monitoring_cadence': ['real-time', 'real-time', 'hourly', 'daily'],
     'notification_channels': ['Slack', 'PagerDuty', 'Email', 'Email']}

    >>> metric_names = ['Portfolio Turnover', 'Max Drawdown']
    >>> threshold_values = [0.1, 0.15]
    >>> monitoring_cadence = ['daily', 'daily']
    >>> notification_channels = ['Email', 'Slack']
    >>> setup_monitoring_and_alerts(metric_names, threshold_values,
    monitoring_cadence, notification_channels)
    {'metric_names': ['Portfolio Turnover', 'Max Drawdown'],
     'threshold_values': [0.1, 0.15],
     'monitoring_cadence': ['daily', 'daily'],
     'notification_channels': ['Email', 'Slack']}

    """
    return SetupMonitoringAndAlertsOutput(
        metric_names=[],
        threshold_values=[],
        monitoring_cadence=[],
        notification_channels=[],
    )