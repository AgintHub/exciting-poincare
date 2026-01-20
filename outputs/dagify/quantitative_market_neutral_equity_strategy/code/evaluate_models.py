from pydantic import BaseModel, Field
from typing import List


class TrainLinearRegressionModelOutput(BaseModel):
    """Pydantic model for train_linear_regression_model node outputs."""
    factor_names: List[str] = (
        Field(..., description="Ordered list of factor names used as regressors in the model.")
    )
    coefficients: List[float] = (
        Field(..., description="Estimated regression coefficient for each factor, in the same order as factor_names.")
    )
    intercept: float = (
        Field(..., description="Estimated intercept term of the linear regression.")
    )
    r_squared: float = (
        Field(..., description="In\u2011sample R\u2011squared value of the fitted model.")
    )
    n_observations: int = (
        Field(..., description="Number of observations (security\u2011days) used to fit the model.")
    )


class TrainRandomForestModelOutput(BaseModel):
    """Pydantic model for train_random_forest_model node outputs."""
    model_name: str = (
        Field(..., description="Identifier for the trained model instance")
    )
    n_estimators: int = (
        Field(..., description="Number of trees in the random forest")
    )
    max_depth: int = (
        Field(..., description="Maximum depth of each tree (default if not specified)")
    )
    oob_r_squared: float = (
        Field(..., description="Out\u2011of\u2011bag R\u2011squared score for model performance")
    )
    feature_importances: List[float] = (
        Field(..., description="Relative importance scores for each selected factor in the model")
    )
    num_training_samples: int = (
        Field(..., description="Count of samples used in the training set")
    )
    num_selected_factors: int = (
        Field(..., description="Number of factor features included in the model")
    )


class TrainGradientBoostingModelOutput(BaseModel):
    """Pydantic model for train_gradient_boosting_model node outputs."""
    model_name: str = (
        Field(..., description="Name of the trained model (e.g., XGBoost_GBM).")
    )
    validation_rmse: float = (
        Field(..., description="Root Mean Squared Error on the validation set.")
    )
    feature_names: List[str] = (
        Field(..., description="Ordered list of feature names used in the model.")
    )
    feature_importances: List[float] = (
        Field(..., description="Relative importance scores for each feature, aligned with feature_names.")
    )


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


def evaluate_models(train_linear_regression_model_input: TrainLinearRegressionModelOutput, train_random_forest_model_input: TrainRandomForestModelOutput, train_gradient_boosting_model_input: TrainGradientBoostingModelOutput, **kwargs) -> EvaluateModelsOutput:
    """
    Evaluate and compare trained predictive models with rolling-window out-of-
    sample back-testing over a holdout period, computing key performance metrics
    for each.

    Parameters
    ----------
    trained_models : dict[str, Any]
        Dictionary containing the trained models with keys as model
        identifiers ('LinearRegression', 'RandomForest', 'GradientBoosting')
        and values as the corresponding trained model objects or metadata.
    holdout_period_years : int
        Integer number of years specifying the holdout (out-of-sample
        testing) period length used in the rolling evaluation.
    rolling_window_config : dict
        Configuration dictionary defining the rolling window evaluation
        parameters, e.g., training window length (years), testing window
        length (years), and step size (e.g., 1 year).
    historical_market_data : DataFrame
        Historical market data including factor exposures, returns, and
        relevant security identifiers required for out-of-sample testing.
    benchmark_returns : Series
        Benchmark return series for calculating information ratio during
        back-testing.

    Returns
    -------
    List[dict]
        List of dictionaries, each containing evaluation metrics
        ('model_name', 'holdout_period_years', 'annualized_return',
        'annualized_sharpe', 'maximum_drawdown', 'information_ratio') for
        one of the trained models.

    Raises
    ------
    ValueError
        If the holdout_period_years is non-positive or exceeds data
        availability.
    KeyError
        If required model names or training data are missing.
    RuntimeError
        If backtesting or metric computations fail due to inconsistent data
        or errors.

    Examples
    --------
    >>> trained_models = {
    ...     'LinearRegression': linear_reg_model,
    ...     'RandomForest': rf_model,
    ...     'GradientBoosting': gbm_model
    >>> }
    >>> results = evaluate_models(trained_models, holdout_period_years=1,
    rolling_window_config={'train_years':2, 'test_years':1},
    historical_market_data=market_df, benchmark_returns=bench_returns)
    >>> for res in results:
    ...     print(f"Model: {res['model_name']}, Annualized Return:
    {res['annualized_return']:.2%}, Sharpe: {res['annualized_sharpe']:.2f}")
    Model: LinearRegression, Annualized Return: 8.27%, Sharpe: 1.10
    Model: RandomForest, Annualized Return: 10.15%, Sharpe: 1.35
    Model: GradientBoosting, Annualized Return: 11.42%, Sharpe: 1.48

    """
    return EvaluateModelsOutput(
        model_name="",
        holdout_period_years=0,
        annualized_return=0.0,
        annualized_sharpe=0.0,
        maximum_drawdown=0.0,
        information_ratio=0.0,
    )