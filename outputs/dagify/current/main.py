import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.acquire_alternative_data import acquire_alternative_data
from code.acquire_fundamental_data import acquire_fundamental_data
from code.acquire_price_data import acquire_price_data
from code.backtest_portfolio import backtest_portfolio
from code.clean_alternative_data import clean_alternative_data
from code.clean_fundamental_data import clean_fundamental_data
from code.clean_price_data import clean_price_data
from code.compute_factor_exposures import compute_factor_exposures
from code.define_factor_candidates import define_factor_candidates
from code.define_market_neutral_objectives import define_market_neutral_objectives
from code.define_strategy_objectives import define_strategy_objectives
from code.define_transaction_cost_model import define_transaction_cost_model
from code.define_universe_criteria import define_universe_criteria
from code.deployment_plan import deployment_plan
from code.design_execution_strategy import design_execution_strategy
from code.design_portfolio_constraints import design_portfolio_constraints
from code.develop_compliance_checks import develop_compliance_checks
from code.draft_operational_workflow import draft_operational_workflow
from code.evaluate_backtest_performance import evaluate_backtest_performance
from code.evaluate_models import evaluate_models
from code.final_review_and_approval import final_review_and_approval
from code.generate_signals import generate_signals
from code.identify_data_sources import identify_data_sources
from code.launch_strategy import launch_strategy
from code.merge_cleaned_data import merge_cleaned_data
from code.optimize_portfolio import optimize_portfolio
from code.outline_technology_stack import outline_technology_stack
from code.prepare_strategy_documentation import prepare_strategy_documentation
from code.risk_analysis import risk_analysis
from code.select_best_model import select_best_model
from code.select_significant_factors import select_significant_factors
from code.setup_monitoring_and_alerts import setup_monitoring_and_alerts
from code.test_factor_performance import test_factor_performance
from code.train_gradient_boosting_model import train_gradient_boosting_model
from code.train_linear_regression_model import train_linear_regression_model
from code.train_random_forest_model import train_random_forest_model

# Get async mode from environment variable or default to False
ASYNC_MODE = os.environ.get('ASYNC_MODE', '').lower() in ('true', '1', 'yes', 'y')

def make_async(func):
    """Convert a synchronous function to an asynchronous function.

    If the function is already asynchronous, return it unchanged.
    If the function is synchronous, wrap it in an async function.
    """
    # If it's already a coroutine function, return it as is
    if inspect.iscoroutinefunction(func):
        return func

    # Otherwise, wrap it as an async function
    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return async_wrapper

acquire_alternative_data_async = make_async(acquire_alternative_data)
acquire_fundamental_data_async = make_async(acquire_fundamental_data)
acquire_price_data_async = make_async(acquire_price_data)
backtest_portfolio_async = make_async(backtest_portfolio)
clean_alternative_data_async = make_async(clean_alternative_data)
clean_fundamental_data_async = make_async(clean_fundamental_data)
clean_price_data_async = make_async(clean_price_data)
compute_factor_exposures_async = make_async(compute_factor_exposures)
define_factor_candidates_async = make_async(define_factor_candidates)
define_market_neutral_objectives_async = make_async(define_market_neutral_objectives)
define_strategy_objectives_async = make_async(define_strategy_objectives)
define_transaction_cost_model_async = make_async(define_transaction_cost_model)
define_universe_criteria_async = make_async(define_universe_criteria)
deployment_plan_async = make_async(deployment_plan)
design_execution_strategy_async = make_async(design_execution_strategy)
design_portfolio_constraints_async = make_async(design_portfolio_constraints)
develop_compliance_checks_async = make_async(develop_compliance_checks)
draft_operational_workflow_async = make_async(draft_operational_workflow)
evaluate_backtest_performance_async = make_async(evaluate_backtest_performance)
evaluate_models_async = make_async(evaluate_models)
final_review_and_approval_async = make_async(final_review_and_approval)
generate_signals_async = make_async(generate_signals)
identify_data_sources_async = make_async(identify_data_sources)
launch_strategy_async = make_async(launch_strategy)
merge_cleaned_data_async = make_async(merge_cleaned_data)
optimize_portfolio_async = make_async(optimize_portfolio)
outline_technology_stack_async = make_async(outline_technology_stack)
prepare_strategy_documentation_async = make_async(prepare_strategy_documentation)
risk_analysis_async = make_async(risk_analysis)
select_best_model_async = make_async(select_best_model)
select_significant_factors_async = make_async(select_significant_factors)
setup_monitoring_and_alerts_async = make_async(setup_monitoring_and_alerts)
test_factor_performance_async = make_async(test_factor_performance)
train_gradient_boosting_model_async = make_async(train_gradient_boosting_model)
train_linear_regression_model_async = make_async(train_linear_regression_model)
train_random_forest_model_async = make_async(train_random_forest_model)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: identify_data_sources, define_universe_criteria, define_strategy_objectives, define_market_neutral_objectives
    async def run_identify_data_sources():
        # Call the async version of identify_data_sources with results from dependencies
        return await identify_data_sources_async(user_input)

    async def run_define_universe_criteria():
        # Call the async version of define_universe_criteria with results from dependencies
        return await define_universe_criteria_async(user_input)

    async def run_define_strategy_objectives():
        # Call the async version of define_strategy_objectives with results from dependencies
        return await define_strategy_objectives_async(user_input)

    async def run_define_market_neutral_objectives():
        # Call the async version of define_market_neutral_objectives with results from dependencies
        return await define_market_neutral_objectives_async(user_input)

    # Run level 0 nodes in parallel
    level_0_results = await asyncio.gather(run_identify_data_sources(), run_define_universe_criteria(), run_define_strategy_objectives(), run_define_market_neutral_objectives())
    results['identify_data_sources'] = level_0_results[0]
    results['define_universe_criteria'] = level_0_results[1]
    results['define_strategy_objectives'] = level_0_results[2]
    results['define_market_neutral_objectives'] = level_0_results[3]

    # Level 1: define_factor_candidates, design_portfolio_constraints, acquire_price_data, acquire_fundamental_data, acquire_alternative_data
    async def run_define_factor_candidates():
        # Call the async version of define_factor_candidates with results from dependencies
        return await define_factor_candidates_async(results['define_strategy_objectives'])

    async def run_design_portfolio_constraints():
        # Call the async version of design_portfolio_constraints with results from dependencies
        return await design_portfolio_constraints_async(results['define_market_neutral_objectives'], results['define_universe_criteria'])

    async def run_acquire_price_data():
        # Call the async version of acquire_price_data with results from dependencies
        return await acquire_price_data_async(results['identify_data_sources'], results['define_universe_criteria'])

    async def run_acquire_fundamental_data():
        # Call the async version of acquire_fundamental_data with results from dependencies
        return await acquire_fundamental_data_async(results['identify_data_sources'], results['define_universe_criteria'])

    async def run_acquire_alternative_data():
        # Call the async version of acquire_alternative_data with results from dependencies
        return await acquire_alternative_data_async(results['identify_data_sources'], results['define_universe_criteria'])

    # Run level 1 nodes in parallel
    level_1_results = await asyncio.gather(run_define_factor_candidates(), run_design_portfolio_constraints(), run_acquire_price_data(), run_acquire_fundamental_data(), run_acquire_alternative_data())
    results['define_factor_candidates'] = level_1_results[0]
    results['design_portfolio_constraints'] = level_1_results[1]
    results['acquire_price_data'] = level_1_results[2]
    results['acquire_fundamental_data'] = level_1_results[3]
    results['acquire_alternative_data'] = level_1_results[4]

    # Level 2: clean_alternative_data, develop_compliance_checks, clean_price_data, clean_fundamental_data, define_transaction_cost_model
    async def run_clean_alternative_data():
        # Call the async version of clean_alternative_data with results from dependencies
        return await clean_alternative_data_async(results['acquire_alternative_data'])

    async def run_develop_compliance_checks():
        # Call the async version of develop_compliance_checks with results from dependencies
        return await develop_compliance_checks_async(results['design_portfolio_constraints'], results['define_market_neutral_objectives'])

    async def run_clean_price_data():
        # Call the async version of clean_price_data with results from dependencies
        return await clean_price_data_async(results['acquire_price_data'])

    async def run_clean_fundamental_data():
        # Call the async version of clean_fundamental_data with results from dependencies
        return await clean_fundamental_data_async(results['acquire_fundamental_data'])

    async def run_define_transaction_cost_model():
        # Call the async version of define_transaction_cost_model with results from dependencies
        return await define_transaction_cost_model_async(results['acquire_price_data'])

    # Run level 2 nodes in parallel
    level_2_results = await asyncio.gather(run_clean_alternative_data(), run_develop_compliance_checks(), run_clean_price_data(), run_clean_fundamental_data(), run_define_transaction_cost_model())
    results['clean_alternative_data'] = level_2_results[0]
    results['develop_compliance_checks'] = level_2_results[1]
    results['clean_price_data'] = level_2_results[2]
    results['clean_fundamental_data'] = level_2_results[3]
    results['define_transaction_cost_model'] = level_2_results[4]

    # Level 3: merge_cleaned_data
    async def run_merge_cleaned_data():
        # Call the async version of merge_cleaned_data with results from dependencies
        return await merge_cleaned_data_async(results['clean_price_data'], results['clean_fundamental_data'], results['clean_alternative_data'])

    # Run level 3 nodes in parallel
    results['merge_cleaned_data'] = await run_merge_cleaned_data()

    # Level 4: compute_factor_exposures
    async def run_compute_factor_exposures():
        # Call the async version of compute_factor_exposures with results from dependencies
        return await compute_factor_exposures_async(results['merge_cleaned_data'], results['define_factor_candidates'])

    # Run level 4 nodes in parallel
    results['compute_factor_exposures'] = await run_compute_factor_exposures()

    # Level 5: test_factor_performance
    async def run_test_factor_performance():
        # Call the async version of test_factor_performance with results from dependencies
        return await test_factor_performance_async(results['compute_factor_exposures'])

    # Run level 5 nodes in parallel
    results['test_factor_performance'] = await run_test_factor_performance()

    # Level 6: select_significant_factors
    async def run_select_significant_factors():
        # Call the async version of select_significant_factors with results from dependencies
        return await select_significant_factors_async(results['test_factor_performance'])

    # Run level 6 nodes in parallel
    results['select_significant_factors'] = await run_select_significant_factors()

    # Level 7: train_linear_regression_model, train_random_forest_model, train_gradient_boosting_model
    async def run_train_linear_regression_model():
        # Call the async version of train_linear_regression_model with results from dependencies
        return await train_linear_regression_model_async(results['compute_factor_exposures'], results['select_significant_factors'], results['merge_cleaned_data'])

    async def run_train_random_forest_model():
        # Call the async version of train_random_forest_model with results from dependencies
        return await train_random_forest_model_async(results['compute_factor_exposures'], results['select_significant_factors'], results['merge_cleaned_data'])

    async def run_train_gradient_boosting_model():
        # Call the async version of train_gradient_boosting_model with results from dependencies
        return await train_gradient_boosting_model_async(results['compute_factor_exposures'], results['select_significant_factors'], results['merge_cleaned_data'])

    # Run level 7 nodes in parallel
    level_7_results = await asyncio.gather(run_train_linear_regression_model(), run_train_random_forest_model(), run_train_gradient_boosting_model())
    results['train_linear_regression_model'] = level_7_results[0]
    results['train_random_forest_model'] = level_7_results[1]
    results['train_gradient_boosting_model'] = level_7_results[2]

    # Level 8: evaluate_models
    async def run_evaluate_models():
        # Call the async version of evaluate_models with results from dependencies
        return await evaluate_models_async(results['train_linear_regression_model'], results['train_random_forest_model'], results['train_gradient_boosting_model'])

    # Run level 8 nodes in parallel
    results['evaluate_models'] = await run_evaluate_models()

    # Level 9: select_best_model
    async def run_select_best_model():
        # Call the async version of select_best_model with results from dependencies
        return await select_best_model_async(results['evaluate_models'])

    # Run level 9 nodes in parallel
    results['select_best_model'] = await run_select_best_model()

    # Level 10: generate_signals
    async def run_generate_signals():
        # Call the async version of generate_signals with results from dependencies
        return await generate_signals_async(results['select_best_model'], results['compute_factor_exposures'])

    # Run level 10 nodes in parallel
    results['generate_signals'] = await run_generate_signals()

    # Level 11: optimize_portfolio
    async def run_optimize_portfolio():
        # Call the async version of optimize_portfolio with results from dependencies
        return await optimize_portfolio_async(results['generate_signals'], results['design_portfolio_constraints'], results['define_transaction_cost_model'])

    # Run level 11 nodes in parallel
    results['optimize_portfolio'] = await run_optimize_portfolio()

    # Level 12: risk_analysis, backtest_portfolio, design_execution_strategy
    async def run_risk_analysis():
        # Call the async version of risk_analysis with results from dependencies
        return await risk_analysis_async(results['optimize_portfolio'], results['compute_factor_exposures'])

    async def run_backtest_portfolio():
        # Call the async version of backtest_portfolio with results from dependencies
        return await backtest_portfolio_async(results['optimize_portfolio'], results['acquire_price_data'], results['define_transaction_cost_model'])

    async def run_design_execution_strategy():
        # Call the async version of design_execution_strategy with results from dependencies
        return await design_execution_strategy_async(results['optimize_portfolio'], results['define_market_neutral_objectives'])

    # Run level 12 nodes in parallel
    level_12_results = await asyncio.gather(run_risk_analysis(), run_backtest_portfolio(), run_design_execution_strategy())
    results['risk_analysis'] = level_12_results[0]
    results['backtest_portfolio'] = level_12_results[1]
    results['design_execution_strategy'] = level_12_results[2]

    # Level 13: outline_technology_stack, evaluate_backtest_performance
    async def run_outline_technology_stack():
        # Call the async version of outline_technology_stack with results from dependencies
        return await outline_technology_stack_async(results['identify_data_sources'], results['design_execution_strategy'], results['develop_compliance_checks'])

    async def run_evaluate_backtest_performance():
        # Call the async version of evaluate_backtest_performance with results from dependencies
        return await evaluate_backtest_performance_async(results['backtest_portfolio'])

    # Run level 13 nodes in parallel
    level_13_results = await asyncio.gather(run_outline_technology_stack(), run_evaluate_backtest_performance())
    results['outline_technology_stack'] = level_13_results[0]
    results['evaluate_backtest_performance'] = level_13_results[1]

    # Level 14: draft_operational_workflow
    async def run_draft_operational_workflow():
        # Call the async version of draft_operational_workflow with results from dependencies
        return await draft_operational_workflow_async(results['outline_technology_stack'], results['design_execution_strategy'], results['develop_compliance_checks'])

    # Run level 14 nodes in parallel
    results['draft_operational_workflow'] = await run_draft_operational_workflow()

    # Level 15: prepare_strategy_documentation, setup_monitoring_and_alerts
    async def run_prepare_strategy_documentation():
        # Call the async version of prepare_strategy_documentation with results from dependencies
        return await prepare_strategy_documentation_async(results['define_strategy_objectives'], results['evaluate_backtest_performance'], results['risk_analysis'], results['draft_operational_workflow'], results['design_execution_strategy'])

    async def run_setup_monitoring_and_alerts():
        # Call the async version of setup_monitoring_and_alerts with results from dependencies
        return await setup_monitoring_and_alerts_async(results['draft_operational_workflow'])

    # Run level 15 nodes in parallel
    level_15_results = await asyncio.gather(run_prepare_strategy_documentation(), run_setup_monitoring_and_alerts())
    results['prepare_strategy_documentation'] = level_15_results[0]
    results['setup_monitoring_and_alerts'] = level_15_results[1]

    # Level 16: final_review_and_approval
    async def run_final_review_and_approval():
        # Call the async version of final_review_and_approval with results from dependencies
        return await final_review_and_approval_async(results['prepare_strategy_documentation'])

    # Run level 16 nodes in parallel
    results['final_review_and_approval'] = await run_final_review_and_approval()

    # Level 17: deployment_plan
    async def run_deployment_plan():
        # Call the async version of deployment_plan with results from dependencies
        return await deployment_plan_async(results['final_review_and_approval'], results['outline_technology_stack'])

    # Run level 17 nodes in parallel
    results['deployment_plan'] = await run_deployment_plan()

    # Level 18: launch_strategy
    async def run_launch_strategy():
        # Call the async version of launch_strategy with results from dependencies
        return await launch_strategy_async(results['deployment_plan'], results['setup_monitoring_and_alerts'])

    # Run level 18 nodes in parallel
    results['launch_strategy'] = await run_launch_strategy()

    # Return all results
    return results

def run_workflow_sync(user_input: str) -> Dict[str, Any]:
    """Synchronous wrapper around the async workflow execution."""
    return asyncio.run(run_workflow(user_input))

def main():
    """Main entry point.

    Handles arguments in the following priority:
    1. Command-line argument (sys.argv[1])
    2. If no argument, uses empty string as input but displays a warning.
    """
    # Get user input from command line or use empty string
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        # No input provided - display help message but continue with empty string
        print('Warning: No input provided. Using empty string as input.')
        print('For better results, provide an input argument:')
        print(f'  python {os.path.basename(__file__)} "your input text here"')
        print('Or use a file as input:')
        print(f'  python {os.path.basename(__file__)} "$(cat input.txt)"')
        user_input = ""

    print(f'Running workflow with input: {user_input}')

    # Run the workflow
    results = run_workflow_sync(user_input)

    # Print results
    try:
        # Convert results to JSON
        json_results = json.dumps(results, indent=2, default=str)
        print(json_results)
    except (TypeError, ValueError) as e:
        print(f'Results could not be converted to JSON: {e}')
        print(f'Raw results: {results}')

    return results

if __name__ == '__main__':
    main()
