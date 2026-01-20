from pydantic import BaseModel, Field
from typing import List


class DefineStrategyObjectivesOutput(BaseModel):
    """Pydantic model for define_strategy_objectives node outputs."""
    objectives: str = (
        Field(..., description="A list of up to six bullet\u2011point objectives describing target return, risk tolerance, market exposure, investment horizon, and special constraints for the strategy.")
    )


class EvaluateBacktestPerformanceOutput(BaseModel):
    """Pydantic model for evaluate_backtest_performance node outputs."""
    annualized_return: float = (
        Field(..., description="The annualized return of the backtest")
    )
    annualized_volatility: float = (
        Field(..., description="The annualized volatility of the backtest")
    )
    sharpe_ratio: float = (
        Field(..., description="The Sharpe ratio of the backtest")
    )
    information_ratio: float = (
        Field(..., description="The information ratio of the backtest")
    )
    maximum_drawdown: float = (
        Field(..., description="The maximum drawdown of the backtest")
    )
    turnover: float = Field(..., description="The turnover of the backtest")
    underperformance_periods: str = (
        Field(..., description="List of periods where the backtest underperformed")
    )


class RiskAnalysisOutput(BaseModel):
    """Pydantic model for risk_analysis node outputs."""
    factor_names: List[str] = (
        Field(..., description="Names of the selected factors evaluated.")
    )
    average_exposure: List[float] = (
        Field(..., description="Average portfolio exposure to each factor over the back\u2011test period.")
    )
    max_drawdown: float = (
        Field(..., description="Maximum observed portfolio drawdown during the back\u2011test.")
    )
    top_drawdown_contributors: List[str] = (
        Field(..., description="Factors identified as the largest contributors to the maximum drawdown.")
    )
    drawdown_sensitivity: List[float] = (
        Field(..., description="Estimated change in portfolio return per unit change in each factor during the drawdown period.")
    )
    stress_factor_names: List[str] = (
        Field(..., description="Names of factors used in the \u00b12\u03c3 stress test.")
    )
    stress_sensitivity_positive: List[float] = (
        Field(..., description="Portfolio return sensitivity when each factor is shocked +2\u03c3.")
    )
    stress_sensitivity_negative: List[float] = (
        Field(..., description="Portfolio return sensitivity when each factor is shocked -2\u03c3.")
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


def prepare_strategy_documentation(define_strategy_objectives_input: DefineStrategyObjectivesOutput, evaluate_backtest_performance_input: EvaluateBacktestPerformanceOutput, risk_analysis_input: RiskAnalysisOutput, draft_operational_workflow_input: DraftOperationalWorkflowOutput, design_execution_strategy_input: DesignExecutionStrategyOutput, **kwargs) -> PrepareStrategyDocumentationOutput:
    """
    Compile a comprehensive plain-text strategy memorandum summarizing key
    components of a market-neutral equity quantitative strategy, each section
    limited to 300 words.

    Parameters
    ----------
    objectives : List[str]
        A list of the strategy’s high-level investment objectives, typically
        covering target return, risk tolerance, market exposure, investment
        horizon, and constraints.
    evaluate_backtest_performance : dict
        Performance metrics from the back-test, including annualized return,
        volatility, Sharpe ratio, information ratio, max drawdown, turnover,
        and periods of underperformance.
    risk_analysis : dict
        Risk analysis outputs covering factor exposures, drawdown
        contributors, stress test results, and factor sensitivity measures.
    draft_operational_workflow : dict
        Description of the daily operational steps, including
        responsibilities for each workflow stage.
    design_execution_strategy : dict
        Algorithmic execution strategy details including algorithm name,
        participation rates, slicing frequency, and execution quality
        metrics.

    Returns
    -------
    dict
        A comprehensive dictionary containing string summaries and lists
        documenting the strategy memorandum, including objectives, universe,
        data sources, factor model, signal generation, portfolio
        construction, risk management, execution strategy, compliance,
        technology stack, and performance summary.

    Raises
    ------
    ValueError
        If any required input field is missing or improperly formatted.
    RuntimeError
        If document compilation fails due to inconsistencies among dependent
        inputs.

    Examples
    --------
    >>> prepare_strategy_documentation(
    ...   objectives=['Achieve 8% annualized return', 'Maintain beta near zero',
    'Limit max drawdown to 10%'],
    ...   evaluate_backtest_performance={
    ...     'annualized_return': 0.075,
    ...     'sharpe_ratio': 1.25,
    ...     'maximum_drawdown': -0.095,
    ...     'underperformance_periods': ['2020-Q1']
    ...   },
    ...   risk_analysis={'factor_names':['Value','Momentum'],
    'average_exposure':[0.1,0.05], 'max_drawdown':-0.095,
    'top_drawdown_contributors':['Momentum'],
    'drawdown_sensitivity':[0.02,0.05],
    'stress_factor_names':['Value','Momentum'],
    'stress_sensitivity_positive':[0.01,-0.03],
    'stress_sensitivity_negative':[-0.01,0.03]},
    ...   draft_operational_workflow={'step_numbers':[1,2,3],
    'step_descriptions':['Data ingestion','Cleaning','Optimization'],
    'step_responsible':['Data Team','Quant Team','Portfolio Team'],
    'workflow_summary':'Daily process from data pull through portfolio
    optimization.'},
    ...   design_execution_strategy={'algorithm_name':'VWAP',
    'participation_rate':0.1, 'slice_frequency_minutes':15,
    'execution_quality_metric':'VWAP deviation %'}
    >>> )
    {'objectives': [...], 'universe_description': 'Equities priced above $5 with
    market cap $5B-$100B, listed on NYSE/NASDAQ, positive earnings only.',
    'data_sources': 'Price data from XYZ, fundamentals from ABC, alternative
    data from DEF.', 'factor_model': 'Factors constructed from fundamental
    ratios, momentum scores, and sentiment indicators.', 'signal_generation':
    'Signals derived from linear combination of selected factors weighted by
    regression coefficients.', 'portfolio_construction': 'Quadratic optimization
    maximizing expected return minus transaction costs, with market-neutral
    constraints.', 'risk_management': 'Monitor factor exposures, max drawdown
    limits, and stress test results; mitigate via constraints.',
    'execution_strategy': 'VWAP algorithm with 10% max participation rate,
    slicing every 15 minutes; monitor VWAP deviation.', 'compliance': 'Position
    limits, sector neutrality, short-selling constraints verified daily.',
    'technology_stack': 'Python, CVXOPT for optimization, FIX gateway for
    execution, Grafana monitoring.', 'performance_summary': 'Annualized Return:
    7.5%, Sharpe:1.25, Max Drawdown: 9.5%, noted underperformance in 2020-Q1'}

    """
    return PrepareStrategyDocumentationOutput(
        objectives=[],
        universe_description="",
        data_sources="",
        factor_model="",
        signal_generation="",
        portfolio_construction="",
        risk_management="",
        execution_strategy="",
        compliance="",
        technology_stack="",
        performance_summary="",
    )