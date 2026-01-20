import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.create_protagonist_character_profile import create_protagonist_character_profile
from code.define_story_preconditions import define_story_preconditions
from code.design_dragon_character_profile import design_dragon_character_profile
from code.develop_plot_twists_and_turns import develop_plot_twists_and_turns
from code.edit_and_refine_novel import edit_and_refine_novel
from code.plan_moon_landing_sequence import plan_moon_landing_sequence
from code.proofread_and_publish_novel import proofread_and_publish_novel
from code.write_first_draft_of_novel import write_first_draft_of_novel

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

create_protagonist_character_profile_async = make_async(create_protagonist_character_profile)
define_story_preconditions_async = make_async(define_story_preconditions)
design_dragon_character_profile_async = make_async(design_dragon_character_profile)
develop_plot_twists_and_turns_async = make_async(develop_plot_twists_and_turns)
edit_and_refine_novel_async = make_async(edit_and_refine_novel)
plan_moon_landing_sequence_async = make_async(plan_moon_landing_sequence)
proofread_and_publish_novel_async = make_async(proofread_and_publish_novel)
write_first_draft_of_novel_async = make_async(write_first_draft_of_novel)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: define_story_preconditions
    async def run_define_story_preconditions():
        # Call the async version of define_story_preconditions with results from dependencies
        return await define_story_preconditions_async(user_input)

    # Run level 0 nodes in parallel
    results['define_story_preconditions'] = await run_define_story_preconditions()

    # Level 1: design_dragon_character_profile, create_protagonist_character_profile
    async def run_design_dragon_character_profile():
        # Call the async version of design_dragon_character_profile with results from dependencies
        return await design_dragon_character_profile_async(results['define_story_preconditions'])

    async def run_create_protagonist_character_profile():
        # Call the async version of create_protagonist_character_profile with results from dependencies
        return await create_protagonist_character_profile_async(results['define_story_preconditions'])

    # Run level 1 nodes in parallel
    level_1_results = await asyncio.gather(run_design_dragon_character_profile(), run_create_protagonist_character_profile())
    results['design_dragon_character_profile'] = level_1_results[0]
    results['create_protagonist_character_profile'] = level_1_results[1]

    # Level 2: plan_moon_landing_sequence
    async def run_plan_moon_landing_sequence():
        # Call the async version of plan_moon_landing_sequence with results from dependencies
        return await plan_moon_landing_sequence_async(results['create_protagonist_character_profile'], results['design_dragon_character_profile'])

    # Run level 2 nodes in parallel
    results['plan_moon_landing_sequence'] = await run_plan_moon_landing_sequence()

    # Level 3: develop_plot_twists_and_turns
    async def run_develop_plot_twists_and_turns():
        # Call the async version of develop_plot_twists_and_turns with results from dependencies
        return await develop_plot_twists_and_turns_async(results['plan_moon_landing_sequence'])

    # Run level 3 nodes in parallel
    results['develop_plot_twists_and_turns'] = await run_develop_plot_twists_and_turns()

    # Level 4: write_first_draft_of_novel
    async def run_write_first_draft_of_novel():
        # Call the async version of write_first_draft_of_novel with results from dependencies
        return await write_first_draft_of_novel_async(results['create_protagonist_character_profile'], results['design_dragon_character_profile'], results['plan_moon_landing_sequence'], results['develop_plot_twists_and_turns'])

    # Run level 4 nodes in parallel
    results['write_first_draft_of_novel'] = await run_write_first_draft_of_novel()

    # Level 5: edit_and_refine_novel
    async def run_edit_and_refine_novel():
        # Call the async version of edit_and_refine_novel with results from dependencies
        return await edit_and_refine_novel_async(results['write_first_draft_of_novel'])

    # Run level 5 nodes in parallel
    results['edit_and_refine_novel'] = await run_edit_and_refine_novel()

    # Level 6: proofread_and_publish_novel
    async def run_proofread_and_publish_novel():
        # Call the async version of proofread_and_publish_novel with results from dependencies
        return await proofread_and_publish_novel_async(results['edit_and_refine_novel'])

    # Run level 6 nodes in parallel
    results['proofread_and_publish_novel'] = await run_proofread_and_publish_novel()

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
