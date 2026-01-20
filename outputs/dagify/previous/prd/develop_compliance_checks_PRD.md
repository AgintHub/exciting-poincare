# develop_compliance_checks PRD

## Description
Create a checklist of compliance rules the strategy must satisfy before trade submission.


## Conceptual Info

This node establishes a comprehensive compliance checklist for the trading strategy, specifying key regulatory and internal rules such as position limits, sector concentration caps, short-selling restrictions, leverage ceilings, and reporting obligations. It quantifies each rule with thresholds and describes the verification procedures to ensure adherence before submitting trades, using input constraints and neutrality objectives as guiding parameters.

## Docstring

### Summary
Generate a structured compliance checklist detailing rule names, quantitative thresholds, verification methods, and flags indicating current compliance status for the trading strategy.

### Parameters

- **net_beta_target** (float): Target net market beta for the portfolio, usually zero for neutrality.
- **dollar_exposure_target** (float): Target net dollar exposure, typically zero to enforce dollar neutrality.
- **sector_neutrality** (bool): Flag indicating whether sector exposure neutrality is required.
- **max_position_size_pct** (float): Maximum allowed position size as a fraction of NAV (e.g., 0.05 for 5%).
- **min_liquidity_pct** (float): Minimum liquidity requirement as fraction of average daily volume (e.g., 0.02 for 2%).
- **factor_names** (List[str]): List of factor names with exposure limits applied.
- **factor_exposure_limits** (List[float]): Corresponding upper bounds on absolute exposure for each factor in factor_names.
- **neutrality_criteria** (List[str]): Market neutrality criteria defining beta, dollar, sector, and factor neutrality constraints.
- **is_valid** (bool): Flag indicating whether the neutrality criteria are valid and sufficient.

### Returns

dict: A dictionary containing compliance_rule_names (List[str]), threshold_values (List[float]), verification_methods (List[str]), and is_compliance_met (List[bool]) indicating the compliance status of each rule.

### Raises

- ValueError: If input constraints or neutrality objectives are incomplete or inconsistent.

### Examples

```python
>>> develop_compliance_checks(
...   net_beta_target=0.0,
...   dollar_exposure_target=0.0,
...   sector_neutrality=True,
...   max_position_size_pct=0.05,
...   min_liquidity_pct=0.02,
...   factor_names=['Value', 'Momentum'],
...   factor_exposure_limits=[0.1, 0.1],
...   neutrality_criteria=['Beta exposure=0', 'Dollar exposure=0', 'Sector neutrality'],
...   is_valid=True
>>> )
{"
                "'compliance_rule_names': ["
                "'Position Limit', 'Sector Concentration', 'Short-Selling Restriction', 'Leverage Cap', 'Reporting Obligation'], "
                "'threshold_values': [0.05, 0.1, 0.0, 1.5, 0.0], "
                "'verification_methods': ["
                "'Portfolio value check', "
                "'Sector exposure calculation', "
                "'Short sale flag', "
                "'Leverage ratio calculation', "
                "'Compliance report upload check'"
                
```
