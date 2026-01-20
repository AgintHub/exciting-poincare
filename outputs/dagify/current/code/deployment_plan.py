from pydantic import BaseModel, Field
from typing import List


class FinalReviewAndApprovalOutput(BaseModel):
    """Pydantic model for final_review_and_approval node outputs."""
    checklist_items: List[str] = (
        Field(..., description="List of review items such as methodology soundness, risk limits, compliance coverage, technology readiness, governance.")
    )
    checklist_statuses: List[str] = (
        Field(..., description="Corresponding status for each checklist item; values are 'Approved' or 'Needs Revision'.")
    )
    sign_off_name: str = (
        Field(..., description="Name of the senior manager who signs off the review.")
    )
    sign_off_date: str = (
        Field(..., description="Date of the sign\u2011off in ISO 8601 format (YYYY-MM-DD).")
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


def deployment_plan(final_review_and_approval_input: FinalReviewAndApprovalOutput, outline_technology_stack_input: OutlineTechnologyStackOutput, **kwargs) -> DeploymentPlanOutput:
    """
    Generate a structured phased deployment roadmap from back-test validation to
    full live production launch.

    Returns
    -------
    dict
        Dictionary containing lists describing each deployment phase's name,
        duration in weeks, critical milestones, responsible owners, and a
        markdown summary table consolidating all phases.

    Raises
    ------
    RuntimeError
        If prerequisite reviews or technology stack specifications are
        incomplete or unavailable.
    ValueError
        If timeline weeks or milestone descriptions are inconsistent in
        length or format across phases.

    Examples
    --------
    >>> deployment_plan()
    {

    """
    return DeploymentPlanOutput(
        phase_names=[],
        phase_weeks=[],
        phase_milestones=[],
        phase_owners=[],
        summary_table="",
    )