from pydantic import BaseModel, Field
from typing import List


class PrepareStrategyDocumentationOutput(BaseModel):
    """Pydantic model for prepare_strategy_documentation node outputs."""
    objectives: List[str] = (
        Field(..., description="Bullet list of the strategy\u2019s high-level objectives.")
    )
    universe_description: str = (
        Field(..., description="Textual description of the equity universe selection criteria.")
    )
    data_sources: str = (
        Field(..., description="List of data providers and the key data fields retrieved.")
    )
    factor_model: str = (
        Field(..., description="Explanation of the factor construction and selection process.")
    )
    signal_generation: str = (
        Field(..., description="Description of how signals are generated from factor exposures.")
    )
    portfolio_construction: str = (
        Field(..., description="Summary of the optimization approach and constraints applied.")
    )
    risk_management: str = (
        Field(..., description="Outline of risk metrics, monitoring, and mitigation strategies.")
    )
    execution_strategy: str = (
        Field(..., description="Details of the algorithmic execution method and parameters.")
    )
    compliance: str = (
        Field(..., description="Compliance checklist and regulatory requirements.")
    )
    technology_stack: str = (
        Field(..., description="Key technology components used across the pipeline.")
    )
    performance_summary: str = (
        Field(..., description="Table of back-test performance metrics and key observations.")
    )


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


def final_review_and_approval(prepare_strategy_documentation_input: PrepareStrategyDocumentationOutput, **kwargs) -> FinalReviewAndApprovalOutput:
    """
    Perform a final quality and readiness review of the strategy memorandum
    based on a predefined checklist, then record approval sign‑off details.

    Parameters
    ----------
    prepared_documentation : dict
        The comprehensive strategy memorandum output from
        'prepare_strategy_documentation' node. Includes sections such as
        objectives, risk management, compliance, technology, and performance
        summary, used as input context for the review.

    Returns
    -------
    dict
        A dictionary containing the checklist items (list of str),
        corresponding statuses (list of str with values 'Approved' or 'Needs
        Revision'), the sign‑off senior manager's name (str), and the
        approval date in ISO 8601 format (str).

    Raises
    ------
    ValueError
        If the prepared_documentation is missing required sections needed
        for review.
    TypeError
        If input is not a dictionary with expected keys.

    Examples
    --------
    >>> prepared_doc = {
    ...     'objectives': ['Target 10% annual return', 'Market neutral beta'],
    ...     'risk_management': 'Uses VAR limits and stress testing',
    ...     'compliance': 'Meets SEC regulations and internal policies',
    ...     'technology_stack': 'Python, CVXOPT, FIX gateway',
    ...     'performance_summary': 'Sharpe ratio 1.5, max drawdown 10%'
    >>> }
    >>> output = final_review(prepared_doc)
    {

    """
    return FinalReviewAndApprovalOutput(
        checklist_items=[],
        checklist_statuses=[],
        sign_off_name="",
        sign_off_date="",
    )