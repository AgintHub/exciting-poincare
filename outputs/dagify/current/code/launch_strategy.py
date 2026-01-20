from pydantic import BaseModel, Field
from typing import List


class DeploymentPlanOutput(BaseModel):
    """Pydantic model for deployment_plan node outputs."""
    phase_names: List[str] = (
        Field(..., description="Names of the deployment phases (e.g., Phase\\u2021, Phase\\u2022, Phase\\u2023).")
    )
    phase_weeks: List[int] = (
        Field(..., description="Number of weeks allocated for each deployment phase.")
    )
    phase_milestones: List[str] = (
        Field(..., description="Key milestones for each phase, provided as a comma-separated or line-break separated string.")
    )
    phase_owners: List[str] = (
        Field(..., description="Primary responsible owner or team for each deployment phase.")
    )
    summary_table: str = (
        Field(..., description="A markdown-style table summarizing phases, weeks, milestones, and owners.")
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


class LaunchStrategyOutput(BaseModel):
    """Pydantic model for launch_strategy node outputs."""
    launch_status: bool = (
        Field(..., description="Whether the strategy has been successfully launched")
    )
    launch_date: str = Field(..., description="Date of launch")
    pre_launch_items: List[str] = (
        Field(..., description="List of pre-launch items that have been confirmed as complete")
    )
    infrastructure_status: str = (
        Field(..., description="Status of infrastructure (e.g., 'ready', 'not ready')")
    )
    data_feeds_status: str = (
        Field(..., description="Status of data feeds (e.g., 'connected', 'not connected')")
    )
    compliance_sign_off: bool = (
        Field(..., description="Whether compliance sign-off has been obtained")
    )
    risk_limits: str = Field(..., description="Risk limits that have been set")
    monitoring_status: str = (
        Field(..., description="Status of monitoring (e.g., 'active', 'inactive')")
    )


def launch_strategy(deployment_plan_input: DeploymentPlanOutput, setup_monitoring_and_alerts_input: SetupMonitoringAndAlertsOutput, **kwargs) -> LaunchStrategyOutput:
    """
    Finalize and execute the launch sequence for the market-neutral equity
    strategy, confirming all pre-launch prerequisites are complete and the
    strategy is live.

    Parameters
    ----------
    deployment_plan_status : dict
        Status and details from the deployment plan node indicating
        readiness of deployment phases.
    monitoring_setup_status : dict
        Details of monitoring metrics, alert thresholds, and notification
        channels from setup_monitoring_and_alerts node indicating monitoring
        readiness.
    infrastructure_status : str
        Current status of infrastructure confirming readiness ('ready' or
        'not ready').
    data_feeds_status : str
        Connectivity and operational status of data feeds ('connected' or
        'not connected').
    compliance_sign_off : bool
        Flag indicating whether compliance has signed off on the strategy.
    risk_limits : str
        Description or reference to the risk limits that have been
        configured and approved.
    monitoring_status : str
        Status of monitoring systems ('active' or 'inactive').

    Returns
    -------
    dict
        A dictionary containing the launch status boolean, launch date
        string, checklist of confirmed pre-launch items, and current
        system/component statuses.

    Raises
    ------
    ValueError
        If any critical pre-launch item is incomplete or shows a negative
        status preventing a successful launch.
    RuntimeError
        If infrastructure or data feeds are not ready or monitoring is
        inactive at launch time.

    Examples
    --------
    >>> launch_strategy(
    ...   deployment_plan_status={'phase_names': ['Phase 1', 'Phase 2', 'Phase
    3'], 'summary_table': '...'},
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

    """
    return LaunchStrategyOutput(
        launch_status=False,
        launch_date="",
        pre_launch_items=[],
        infrastructure_status="",
        data_feeds_status="",
        compliance_sign_off=False,
        risk_limits="",
        monitoring_status="",
    )