from pydantic import BaseModel, Field
from typing import List


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


def draft_operational_workflow(outline_technology_stack_input: OutlineTechnologyStackOutput, design_execution_strategy_input: DesignExecutionStrategyOutput, develop_compliance_checks_input: DevelopComplianceChecksOutput, **kwargs) -> DraftOperationalWorkflowOutput:
    """
    Generate a detailed daily operational workflow as a sequential numbered
    list, specifying descriptions and responsible parties for each step in the
    strategy lifecycle.

    Parameters
    ----------
    outline_technology_stack : dict
        Output from the technology stack node providing the systems and
        infrastructure components used in each pipeline stage.
    design_execution_strategy : dict
        Details of the execution algorithm and parameters which influence
        the execution and order generation steps.
    develop_compliance_checks : dict
        The compliance rules checklist that must be satisfied before order
        submission.

    Returns
    -------
    dict
        A dictionary containing the ordered step numbers, their
        descriptions, the responsible teams/systems for each step, and a
        concise summary of the operational workflow.

    Raises
    ------
    ValueError
        Raised if any of the input dependency nodes do not provide the
        necessary information to map operational steps accurately.

    Examples
    --------
    >>> result = draft_operational_workflow(
    ...     outline_technology_stack={'stages': ['Data Ingestion', 'Model
    Training'], 'technologies': ['Cloud Storage, ETL', 'Python, Jupyter'],
    'table_summary': 'Stage | Technology\n------|------------\nData Ingestion |
    Cloud Storage, ETL'},
    ...     design_execution_strategy={'algorithm_name': 'VWAP',
    'strategy_type': 'Volume-Weighted', 'participation_rate': 0.1,
    'slice_frequency_minutes': 15, 'child_order_weights': [0.2, 0.3, 0.5],
    'order_time_stamps': ['2024-06-01T09:30:00Z', '2024-06-01T09:45:00Z',
    '2024-06-01T10:00:00Z'], 'execution_quality_metric': 'VWAP deviation %'},
    ...     develop_compliance_checks={'compliance_rule_names': ['Position
    Limit', 'Sector Concentration'], 'threshold_values': [0.05, 0.1],
    'verification_methods': ['Portfolio value check', 'Sector exposure
    calculation'], 'is_compliance_met': [True, True]}
    >>> )
    >>> print(result['step_numbers'])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> print(result['workflow_summary'])
    "The daily operational workflow commences with data acquisition, proceeds
    through cleaning, factor computation, and signal generation, followed by
    portfolio optimization, rigorous compliance checking, order generation,
    execution, post-trade reconciliation, and concludes with performance
    monitoring. Each step is clearly assigned to dedicated teams or automated
    systems to ensure end-to-end operational effectiveness."

    """
    return DraftOperationalWorkflowOutput(
        step_numbers=[],
        step_descriptions=[],
        step_responsible=[],
        workflow_summary="",
    )