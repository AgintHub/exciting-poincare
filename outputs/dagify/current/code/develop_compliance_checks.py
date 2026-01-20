from pydantic import BaseModel, Field
from typing import List


class DesignPortfolioConstraintsOutput(BaseModel):
    """Pydantic model for design_portfolio_constraints node outputs."""
    net_beta_target: float = (
        Field(..., description="Target value for net market beta (should be 0.0 for neutrality)")
    )
    dollar_exposure_target: float = (
        Field(..., description="Target net dollar exposure (should be 0.0 for dollar neutrality)")
    )
    sector_neutrality: bool = (
        Field(..., description="Flag indicating whether sector exposure is required to be neutralized")
    )
    max_position_size_pct: float = (
        Field(..., description="Maximum allowed position size as a percentage of NAV (e.g., 0.05 for 5%)")
    )
    min_liquidity_pct: float = (
        Field(..., description="Minimum required liquidity as a percentage of average daily volume (e.g., 0.02 for 2%)")
    )
    factor_names: List[str] = (
        Field(..., description="List of factor names for which exposure limits are specified")
    )
    factor_exposure_limits: List[float] = (
        Field(..., description="Corresponding upper bound on absolute exposure for each factor in factor_names")
    )


class DefineMarketNeutralObjectivesOutput(BaseModel):
    """Pydantic model for define_market_neutral_objectives node outputs."""
    neutrality_criteria: List[str] = (
        Field(..., description="List of individual market\u2011neutral criteria expressed as bullet points, e.g., \"Beta exposure = 0\", \"Dollar exposure = 0\", \"Sector neutrality\", \"Factor X neutrality\".")
    )
    is_valid: bool = (
        Field(..., description="Indicates whether the defined criteria meet the strategy's overall neutrality requirements.")
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


def develop_compliance_checks(design_portfolio_constraints_input: DesignPortfolioConstraintsOutput, define_market_neutral_objectives_input: DefineMarketNeutralObjectivesOutput, **kwargs) -> DevelopComplianceChecksOutput:
    """
    Generate a structured compliance checklist detailing rule names,
    quantitative thresholds, verification methods, and flags indicating current
    compliance status for the trading strategy.

    Parameters
    ----------
    net_beta_target : float
        Target net market beta for the portfolio, usually zero for
        neutrality.
    dollar_exposure_target : float
        Target net dollar exposure, typically zero to enforce dollar
        neutrality.
    sector_neutrality : bool
        Flag indicating whether sector exposure neutrality is required.
    max_position_size_pct : float
        Maximum allowed position size as a fraction of NAV (e.g., 0.05 for
        5%).
    min_liquidity_pct : float
        Minimum liquidity requirement as fraction of average daily volume
        (e.g., 0.02 for 2%).
    factor_names : List[str]
        List of factor names with exposure limits applied.
    factor_exposure_limits : List[float]
        Corresponding upper bounds on absolute exposure for each factor in
        factor_names.
    neutrality_criteria : List[str]
        Market neutrality criteria defining beta, dollar, sector, and factor
        neutrality constraints.
    is_valid : bool
        Flag indicating whether the neutrality criteria are valid and
        sufficient.

    Returns
    -------
    dict
        A dictionary containing compliance_rule_names (List[str]),
        threshold_values (List[float]), verification_methods (List[str]),
        and is_compliance_met (List[bool]) indicating the compliance status
        of each rule.

    Raises
    ------
    ValueError
        If input constraints or neutrality objectives are incomplete or
        inconsistent.

    Examples
    --------
    >>> develop_compliance_checks(
    ...   net_beta_target=0.0,
    ...   dollar_exposure_target=0.0,
    ...   sector_neutrality=True,
    ...   max_position_size_pct=0.05,
    ...   min_liquidity_pct=0.02,
    ...   factor_names=['Value', 'Momentum'],
    ...   factor_exposure_limits=[0.1, 0.1],
    ...   neutrality_criteria=['Beta exposure=0', 'Dollar exposure=0', 'Sector
    neutrality'],
    ...   is_valid=True
    >>> )
    {"
                    "'compliance_rule_names': ["
                    "'Position Limit', 'Sector Concentration', 'Short-Selling
    Restriction', 'Leverage Cap', 'Reporting Obligation'], "
                    "'threshold_values': [0.05, 0.1, 0.0, 1.5, 0.0], "
                    "'verification_methods': ["
                    "'Portfolio value check', "
                    "'Sector exposure calculation', "
                    "'Short sale flag', "
                    "'Leverage ratio calculation', "
                    "'Compliance report upload check'"
                    

    """
    return DevelopComplianceChecksOutput(
        compliance_rule_names=[],
        threshold_values=[],
        verification_methods=[],
        is_compliance_met=[],
    )