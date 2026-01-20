from pydantic import BaseModel, Field
from typing import List


class IdentifyDataSourcesOutput(BaseModel):
    """Pydantic model for identify_data_sources node outputs."""
    market_price_data_sources: List[str] = (
        Field(..., description="List of provider names for market price data")
    )
    market_price_fields: List[str] = (
        Field(..., description="Comma-separated list of data fields to retrieve from market price providers")
    )
    fundamental_data_sources: List[str] = (
        Field(..., description="List of provider names for fundamental financial data")
    )
    fundamental_fields: List[str] = (
        Field(..., description="Comma-separated list of data fields to retrieve from fundamental providers")
    )
    alternative_data_sources: List[str] = (
        Field(..., description="List of provider names for alternative data")
    )
    alternative_fields: List[str] = (
        Field(..., description="Comma-separated list of data fields to retrieve from alternative data providers")
    )


class DesignExecutionStrategyOutput(BaseModel):
    """Pydantic model for design_execution_strategy node outputs."""
    algorithm_name: str = (
        Field(..., description="Name of the execution algorithm (e.g., VWAP, TWAP, Implementation Shortfall)")
    )
    strategy_type: str = (
        Field(..., description="Broad classification of the strategy (e.g., Market\u2011Milking, Time\u2011Weighted, Volume\u2011Weighted)")
    )
    participation_rate: float = (
        Field(..., description="Maximum percentage of the daily trading volume to participate in for any single security")
    )
    slice_frequency_minutes: int = (
        Field(..., description="Time interval in minutes between successive child order slices")
    )
    child_order_weights: List[float] = (
        Field(..., description="Sequence of target weights to be applied in each child order slice, matching the order_time_stamps list")
    )
    order_time_stamps: List[str] = (
        Field(..., description="ISO 8601 timestamps indicating when each child order slice is scheduled to be sent")
    )
    execution_quality_metric: str = (
        Field(..., description="Key metric used to assess execution quality (e.g., VWAP deviation %, Execution Slippage %)")
    )


class DevelopComplianceChecksOutput(BaseModel):
    """Pydantic model for develop_compliance_checks node outputs."""
    compliance_rule_names: List[str] = (
        Field(..., description="Names of each compliance rule (e.g., Position Limit, Sector Concentration, Short\u2011Selling Restriction, Leverage Cap, Reporting Obligation).")
    )
    threshold_values: List[float] = (
        Field(..., description="Numeric threshold for each compliance rule (e.g., 5% for position limit, 10% for sector concentration, 0 for short selling, 1.5 for leverage cap, 0 for reporting obligation).")
    )
    verification_methods: List[str] = (
        Field(..., description="Verification method used to validate compliance with each rule (e.g., \"Portfolio value check\", \"Sector exposure calculation\", \"Short sale flag\", \"Leverage ratio calculation\", \"Compliance report upload check\").")
    )
    is_compliance_met: List[bool] = (
        Field(..., description="Boolean flags indicating whether each compliance rule is currently satisfied.")
    )


class OutlineTechnologyStackOutput(BaseModel):
    """Pydantic model for outline_technology_stack node outputs."""
    stages: List[str] = (
        Field(..., description="Ordered list of pipeline stages such as Data Ingestion, Model Training, Optimization, Execution, Monitoring.")
    )
    technologies: List[str] = (
        Field(..., description="List of technology components or tools used at each pipeline stage, aligned in order with the stages list.")
    )
    table_summary: str = (
        Field(..., description="Human\u2011readable two\u2011column table representation summarizing each stage and its corresponding technology components.")
    )


def outline_technology_stack(identify_data_sources_input: IdentifyDataSourcesOutput, design_execution_strategy_input: DesignExecutionStrategyOutput, develop_compliance_checks_input: DevelopComplianceChecksOutput, **kwargs) -> OutlineTechnologyStackOutput:
    """
    Outline the technology components and software infrastructure required at
    each key stage of the end-to-end quantitative equity strategy pipeline,
    returning ordered lists of pipeline stages and their corresponding
    technology tools, along with a formatted summary table.

    Returns
    -------
    dict
        A dictionary containing: - 'stages': List[str], an ordered sequence
        of pipeline stages. - 'technologies': List[str], corresponding
        tools/technologies for each stage. - 'table_summary': str, a human-
        readable two-column table presenting stages and technologies.

    Raises
    ------
    RuntimeError
        If required upstream data about data sources, execution strategy, or
        compliance checks is missing or inconsistent.

    Examples
    --------
    >>> output = outline_technology_stack()
    >>> print(output['stages'])
    >>> print(output['technologies'])
    >>> print(output['table_summary'])
    ("['Data Ingestion', 'Model Training', 'Optimization', 'Execution',
    'Monitoring']\n"
                             "['AWS S3, Apache Airflow', 'Python, Jupyter, CUDA
    GPUs', 'CVXOPT, Gurobi', 'FIX Protocol Gateway, OMS', 'Grafana, Prometheus,
    PagerDuty']\n"
    "+-----------------+------------------------------------------+\n"
                             "| Stage           | Technology
    |\n"
    "+-----------------+------------------------------------------+\n"
                             "| Data Ingestion  | AWS S3, Apache Airflow
    |\n"
                             "| Model Training  | Python, Jupyter, CUDA GPUs
    |\n"
                             "| Optimization    | CVXOPT, Gurobi
    |\n"
                             "| Execution       | FIX Protocol Gateway, OMS
    |\n"
                             "| Monitoring      | Grafana, Prometheus, PagerDuty
    |\n"
    "+-----------------+------------------------------------------+")

    """
    return OutlineTechnologyStackOutput(
        stages=[],
        technologies=[],
        table_summary="",
    )