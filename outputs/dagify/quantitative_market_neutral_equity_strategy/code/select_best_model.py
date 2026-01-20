from pydantic import BaseModel, Field


class EvaluateModelsOutput(BaseModel):
    """Pydantic model for evaluate_models node outputs."""
    model_name: str = (
        Field(..., description="The name of the model evaluated (e.g., LinearRegression, RandomForest, GradientBoosting).")
    )
    holdout_period_years: int = (
        Field(..., description="Number of years used for the out\u2011of\u2011sample testing period.")
    )
    annualized_return: float = (
        Field(..., description="Annualized return of the model\u2019s strategy during the holdout period.")
    )
    annualized_sharpe: float = (
        Field(..., description="Annualized Sharpe ratio of the model\u2019s strategy during the holdout period.")
    )
    maximum_drawdown: float = (
        Field(..., description="Maximum drawdown (as a negative decimal) of the model\u2019s strategy during the holdout period.")
    )
    information_ratio: float = (
        Field(..., description="Information ratio of the model\u2019s strategy during the holdout period.")
    )


class SelectBestModelOutput(BaseModel):
    """Pydantic model for select_best_model node outputs."""
    selected_model: str = (
        Field(..., description="Name of the model selected as best performer")
    )
    information_ratio: float = (
        Field(..., description="Information ratio of the selected model")
    )
    sharpe_ratio: float = (
        Field(..., description="Sharpe ratio of the selected model")
    )
    annualized_return: float = (
        Field(..., description="Annualized return of the selected model")
    )
    maximum_drawdown: float = (
        Field(..., description="Maximum drawdown observed for the selected model")
    )


def select_best_model(evaluate_models_input: EvaluateModelsOutput, **kwargs) -> SelectBestModelOutput:
    """
    Select the best model based on the highest information ratio or Sharpe ratio
    from the evaluation table.

    Parameters
    ----------
    evaluation_table : dict
        Dictionary containing model performance metrics

    Returns
    -------
    dict
        Dictionary with the selected model name and its key performance
        numbers

    Raises
    ------
    ValueError
        If the evaluation table is empty or no model performance metrics are
        provided

    Examples
    --------
    >>> evaluation_table = {
    ...   'LinearRegression': {'information_ratio': 0.8, 'sharpe_ratio': 1.2,
    'annualized_return': 0.1, 'maximum_drawdown': -0.05},
    ...   'RandomForest': {'information_ratio': 0.9, 'sharpe_ratio': 1.1,
    'annualized_return': 0.2, 'maximum_drawdown': -0.03},
    ...   'GradientBoosting': {'information_ratio': 1.0, 'sharpe_ratio': 1.3,
    'annualized_return': 0.3, 'maximum_drawdown': -0.04}
    >>> }
    >>> select_best_model(evaluation_table)
    {'selected_model': 'GradientBoosting', 'information_ratio': 1.0,
    'sharpe_ratio': 1.3, 'annualized_return': 0.3, 'maximum_drawdown': -0.04}

    """
    return SelectBestModelOutput(
        selected_model="",
        information_ratio=0.0,
        sharpe_ratio=0.0,
        annualized_return=0.0,
        maximum_drawdown=0.0,
    )