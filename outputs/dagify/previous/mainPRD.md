# quantitative_market_neutral_equity_strategy - Complete PRD Documentation

## Overview
PRDs for nodes in the 'quantitative_market_neutral_equity_strategy' module.

## Table of Contents

- [acquire_alternative_data](#acquire_alternative_data)

- [acquire_fundamental_data](#acquire_fundamental_data)

- [acquire_price_data](#acquire_price_data)

- [backtest_portfolio](#backtest_portfolio)

- [clean_alternative_data](#clean_alternative_data)

- [clean_fundamental_data](#clean_fundamental_data)

- [clean_price_data](#clean_price_data)

- [compute_factor_exposures](#compute_factor_exposures)

- [define_factor_candidates](#define_factor_candidates)

- [define_market_neutral_objectives](#define_market_neutral_objectives)

- [define_strategy_objectives](#define_strategy_objectives)

- [define_transaction_cost_model](#define_transaction_cost_model)

- [define_universe_criteria](#define_universe_criteria)

- [deployment_plan](#deployment_plan)

- [design_execution_strategy](#design_execution_strategy)

- [design_portfolio_constraints](#design_portfolio_constraints)

- [develop_compliance_checks](#develop_compliance_checks)

- [draft_operational_workflow](#draft_operational_workflow)

- [evaluate_backtest_performance](#evaluate_backtest_performance)

- [evaluate_models](#evaluate_models)

- [final_review_and_approval](#final_review_and_approval)

- [generate_signals](#generate_signals)

- [identify_data_sources](#identify_data_sources)

- [launch_strategy](#launch_strategy)

- [merge_cleaned_data](#merge_cleaned_data)

- [optimize_portfolio](#optimize_portfolio)

- [outline_technology_stack](#outline_technology_stack)

- [prepare_strategy_documentation](#prepare_strategy_documentation)

- [risk_analysis](#risk_analysis)

- [select_best_model](#select_best_model)

- [select_significant_factors](#select_significant_factors)

- [setup_monitoring_and_alerts](#setup_monitoring_and_alerts)

- [test_factor_performance](#test_factor_performance)

- [train_gradient_boosting_model](#train_gradient_boosting_model)

- [train_linear_regression_model](#train_linear_regression_model)

- [train_random_forest_model](#train_random_forest_model)



---

## acquire_alternative_data

### Description
Download alternative data signals for the universe.

### Conceptual Info

This node is responsible for ingesting daily alternative data streams—such as news sentiment, search trends, ESG ratings, and analyst forecasts—for every security that passed the universe screening. It pulls the data from the providers identified in the preceding node, ensures a 10‑year historical window, and produces a concise summary of the download.

### Docstring

**Summary:** Download daily alternative data signals for the screened security universe over the past decade.

**Parameters:**

- security_ids (List[str]): Identifiers of securities selected by the universe criteria.
- data_sources (List[str]): Provider names specified by identify_data_sources for alternative data.
- data_fields (List[str]): Fields requested from each provider (e.g., news_sentiment, google_trends).
- start_date (str): ISO 8601 date marking the beginning of the 10‑year coverage window.
- end_date (str): ISO 8601 date marking the end of the 10‑year coverage window.
**Returns:** dict - Dictionary containing lists of identifiers, dates, sources, fields, and a summary statement.

**Raises:**

- ValueError: If no security IDs are provided or data_sources list is empty.
- RuntimeError: If a provider returns an error or fails to supply data for the requested period.
**Examples:**

```python
>>> result = acquire_alternative_data(
...     security_ids=['AAPL', 'MSFT'],
...     data_sources=['NewsAPI', 'GoogleTrends', 'ESGData'],
...     data_fields=['news_sentiment', 'google_trends', 'esg_score'],
...     start_date='2014-01-01',
...     end_date='2024-01-01')
{'security_ids': ['AAPL', 'MSFT'], 'retrieval_dates': ['2014-01-01', '2024-01-01'], 'data_sources': ['NewsAPI', 'GoogleTrends', 'ESGData'], 'data_fields': ['news_sentiment', 'google_trends', 'esg_score'], 'summary_statement': 'Downloaded 2,000,000 alternative data points for 2 securities from 2014-01-01 to 2024-01-01.'}
```

```python
>>> result = acquire_alternative_data(
...     security_ids=['TSLA'],
...     data_sources=['AnalystForecast'],
...     data_fields=['analyst_forecast'],
...     start_date='2015-01-01',
...     end_date='2024-01-01')
{'security_ids': ['TSLA'], 'retrieval_dates': ['2015-01-01', '2024-01-01'], 'data_sources': ['AnalystForecast'], 'data_fields': ['analyst_forecast'], 'summary_statement': 'Downloaded 3,650 data points for TSLA from 2015-01-01 to 2024-01-01.'}
```



---

## acquire_fundamental_data

### Description
Download historical fundamental accounting data for the universe.

### Conceptual Info

This node is responsible for downloading historical fundamental accounting data for the specified universe of securities. It takes the identified fundamental data providers and the defined universe criteria as inputs and returns the retrieved fundamental data fields, data coverage, number of securities, and data retrieval status.

### Docstring

**Summary:** Downloads historical fundamental accounting data for the specified universe of securities.

**Parameters:**

- data_providers (List[str]): List of fundamental data providers
- universe_criteria (dict): Dictionary containing the universe criteria (e.g., market cap, liquidity, price range)
**Returns:** dict - Dictionary containing the retrieved fundamental data fields, data coverage, number of securities, and data retrieval status

**Raises:**

- ValueError: If the data providers or universe criteria are invalid
**Examples:**

```python
>>> data_providers = ['Yahoo Finance', 'Quandl']
>>> universe_criteria = {'market_cap': 1000000000, 'liquidity': 1000000}
>>> result = acquire_fundamental_data(data_providers, universe_criteria)
{'fundamental_data_fields': ['earnings_per_share', 'book_value', 'cash_flow'], 'data_coverage': '10-year horizon, quarterly and annual data', 'number_of_securities': 100, 'data_retrieval_status': True}
```



---

## acquire_price_data

### Description
Download historical price data for the screened equity universe.

### Conceptual Info

The acquire_price_data node fetches a complete 10‑year daily price history for every security that passes the universe screening rules. It pulls standard OHLCV fields along with corporate actions and packages the results into a lightweight JSON payload for downstream cleaning, cost modeling, and back‑testing.

### Docstring

**Summary:** Retrieve 10‑year daily market price history for the screened equity universe.

**Parameters:**

- price_sources (List[str]): List of market‑price data provider names returned by identify_data_sources.
- fields (List[str]): List of price fields to request from each provider (e.g., ['adjusted_close', 'open', 'high', 'low', 'volume', 'split_factor']).
- universe (Dict[str, Any]): Dictionary containing universe screening criteria returned by define_universe_criteria.
- start_date (str): Start of the 10‑year period to download (ISO format).
- end_date (str): End of the 10‑year period to download (ISO format).
**Returns:** Dict[str, Any] - A dictionary matching the output_structure, containing metadata and a summary statement.

**Raises:**

- ValueError: If any required input list is empty or the date range is invalid.
- ConnectionError: If a data provider cannot be reached or returns an authentication error.
- RuntimeError: If the number of securities returned is zero, indicating a mismatch between universe criteria and available data.
**Examples:**

```python
>>> price_sources = ['AlphaVantage', 'Polygon']
>>> fields = ['adjusted_close', 'open', 'high', 'low', 'volume', 'split_factor']
>>> universe = {"market_cap_min": 5e9, "market_cap_max": 1e11, "avg_daily_volume_min": 5e6, "price_min": 5.0, "price_max": 150.0, "exchanges": ["NASDAQ", "NYSE"], "positive_earnings": True}
>>> result = acquire_price_data(price_sources, fields, universe, '2013-01-02', '2023-01-02')
{'start_date': '2013-01-02', 'end_date': '2023-01-02', 'num_securities': 1123, 'security_ids': ['AAPL', 'MSFT', 'GOOG'], 'columns_retrieved': ['adjusted_close', 'open', 'high', 'low', 'volume', 'split_factor'], 'summary_statement': 'Downloaded price data for 1,123 securities from 2013-01-02 to 2023-01-02.'}
```

```python
>>> acquire_price_data([], fields, universe, '2013-01-02', '2023-01-02')
ValueError: Input list price_sources cannot be empty.
```



---

## backtest_portfolio

### Description
Simulate the strategy over the historical period using the optimized weights and transaction cost model.

### Conceptual Info

Simulates a portfolio backtest using optimized weights and transaction costs.

### Docstring

**Summary:** Simulates a portfolio backtest from the earliest date to the most recent date, applying daily optimized weights and transaction costs, and outputs the time-series of portfolio daily returns, cumulative P&L, and turnover.

**Parameters:**

- optimize_portfolio (dict): Output from the optimize_portfolio node, containing optimal weights for each security.
- acquire_price_data (dict): Output from the acquire_price_data node, containing historical price data for the securities.
- define_transaction_cost_model (dict): Output from the define_transaction_cost_model node, containing transaction cost parameters.
**Returns:** dict - A dictionary containing the time-series of portfolio daily returns, cumulative P&L, and turnover, as well as the length of the back-test horizon.

**Raises:**

- ValueError: If the input data is invalid or missing.
**Examples:**

```python
>>> import pandas as pd
>>> optimize_portfolio_output = {'optimal_weights': [0.1, 0.2, 0.7]}
>>> acquire_price_data_output = {'price_data': pd.DataFrame({'date': ['2022-01-01', '2022-01-02'], 'returns': [0.01, 0.02]})}
>>> define_transaction_cost_model_output = {'transaction_costs': 0.001}
>>> backtest_portfolio(optimize_portfolio_output, acquire_price_data_output, define_transaction_cost_model_output)
{'portfolio_daily_returns': [0.01, 0.02], 'cumulative_pnl': [0.01, 0.03], 'turnover': [0.1, 0.2], 'backtest_horizon_length': 2}
```



---

## clean_alternative_data

### Description
Standardize alternative data series, handling gaps and outliers.

### Conceptual Info

This node takes raw, possibly sparse and noisy alternative data (e.g., sentiment scores, trend indices) acquired from multiple providers, aligns it to the trading calendar, imputes missing observations, caps extreme values, and emits a concise report of the cleaning operation. It is a critical preprocessing step that ensures downstream models receive consistent, comparable inputs across all securities and dates.

### Docstring

**Summary:** Clean and standardise alternative data for downstream factor modelling.

**Parameters:**

- raw_data (pd.DataFrame): DataFrame containing columns: ['security_id', 'date', 'field', 'value']. Each row represents a daily observation from an alternative data source.
**Returns:** Dict[str, Union[int, str]] - Dictionary with keys 'total_records', 'filled_missing_days', 'excluded_records', and 'summary_statement' that describe the cleaning outcome.

**Raises:**

- ValueError: If raw_data is empty or does not contain the required columns.
- KeyError: If expected columns are missing from the input DataFrame.
**Examples:**

```python
>>> import pandas as pd
>>> from datetime import date
>>> # Sample raw data with gaps and outliers
>>> df_raw = pd.DataFrame({
...     'security_id': ['A', 'A', 'A', 'B', 'B', 'B', 'B'],
...     'date': [date(2023,1,2), date(2023,1,5), date(2023,1,6),
...              date(2023,1,2), date(2023,1,3), date(2023,1,5), date(2023,1,6)],
...     'field': ['sentiment']*7,
...     'value': [0.5, 5.0, -4.0, 0.1, 0.2, 10.0, -10.0]  # contains outliers
>>> })
>>> result = clean_alternative_data(df_raw)
>>> print(result['summary_statement'])
"Cleaned 7 records across 2 securities. 2 missing trading days filled via forward fill. 2 records removed after winsorization at 1%/99% percentiles."
```

```python
>>> # If raw_data has no missing trading days and all values within bounds
>>> df_raw = pd.DataFrame({
...     'security_id': ['C']*3,
...     'date': [date(2023,1,2), date(2023,1,3), date(2023,1,4)],
...     'field': ['esg_score']*3,
...     'value': [0.8, 0.85, 0.9]"
                "})
>>> result = clean_alternative_data(df_raw)
>>> print(result['filled_missing_days'])
0
```



---

## clean_fundamental_data

### Description
Standardize fundamental data, handling missing values and restating periods.

### Conceptual Info

This node transforms raw fundamental accounting data into a clean, analysis‑ready table. It unifies units (e.g., millions vs billions), aligns quarterly/annual reports to fixed calendar dates (e.g., Q1 2023 → 2023-03-31), fills gaps using linear interpolation or flags them, and removes extreme outliers (beyond 5 σ) that could distort factor construction.

### Docstring

**Summary:** Clean raw fundamental accounting data by standardizing units, aligning reporting periods, handling missing values, and removing outliers.

**Parameters:**

- raw_fundamental_df (pd.DataFrame): DataFrame returned from acquire_fundamental_data, containing columns such as 'ticker', 'report_date', 'eps', 'book_value', 'cash_flow', 'leverage', 'dividend_yield', etc., possibly in mixed units and with missing values.
**Returns:** dict - Dictionary with the following keys:
- cleaned_record_count (int)
- missing_value_records (int)
- missing_value_flagged (bool)
- outlier_removed_count (int)
- unit_consistency_flag (bool)
- reporting_period_aligned (bool)

**Raises:**

- ValueError: If raw_fundamental_df is empty or missing required columns.
- KeyError: If expected metric columns are not found in the input DataFrame.
**Examples:**

```python
>>> import pandas as pd
>>> # Example raw data
>>> raw = pd.DataFrame({
...     'ticker': ['A', 'A', 'B'],
...     'report_date': ['2022-12-31', '2023-03-31', '2022-12-31'],
...     'eps': [1.2, None, 0.8],
...     'book_value': [2000, 2100, 1500],  # in thousands
...     'cash_flow': [500, 550, None],
...     'leverage': [1.5, 1.6, 1.4],
...     'dividend_yield': [0.02, 0.025, 0.015]
>>> })
>>> result = clean_fundamental_data(raw)
>>> print(result)
{
  'cleaned_record_count': 3,
  'missing_value_records': 1,
  'missing_value_flagged': False,
  'outlier_removed_count': 0,
  'unit_consistency_flag': True,
  'reporting_period_aligned': True
}
```

```python
>>> # Example with an extreme outlier
>>> raw.loc[0, 'eps'] = 1000
>>> result = clean_fundamental_data(raw)
>>> print(result['outlier_removed_count'])
1
```



---

## clean_price_data

### Description
Standardize and adjust price data, handling missing values and corporate actions.

### Conceptual Info

The clean_price_data node takes raw price data, cleans and standardizes it by adjusting for splits and dividends, aligning dates, handling missing values, and ensuring consistent column names.

### Docstring

**Summary:** Cleans and standardizes price data by adjusting for corporate actions, handling missing values, and ensuring consistent column names.

**Parameters:**

- price_data (DataFrame): Raw price dataset to be cleaned
**Returns:** dict - Dictionary containing cleaned_rows, removed_rows, cleaned_date_range, columns_cleaned, and is_clean

**Raises:**

- ValueError: If the input dataset is empty or contains invalid data
**Examples:**

```python
>>> import pandas as pd
>>> data = pd.DataFrame({'date': ['2022-01-01', '2022-01-02'], 'close': [100, 120]})
>>> cleaned_data = clean_price_data(data)
>>> print(cleaned_data)
{'cleaned_rows': 2, 'removed_rows': 0, 'cleaned_date_range': '2022-01-01 to 2022-01-02', 'columns_cleaned': ['date', 'close'], 'is_clean': True}
```



---

## compute_factor_exposures

### Description
Calculate the factor values for every security-day in the merged dataset.

### Conceptual Info

This node calculates factor exposures for a set of securities on each trading day using a merged dataset. It takes in a set of candidate factors and computes their values for every security-day, providing a description of each factor's calculation and the schema of the resulting factor columns.

### Docstring

**Summary:** Compute numerical exposures of each security on each date for all candidate factors.

**Parameters:**

- merged_data (pd.DataFrame): Merged dataset containing price, fundamental, and alternative data for each security-day.
- factor_candidates (List[Factor]): List of candidate factors to be computed, each with a name and calculation method.
**Returns:** dict - Dictionary containing the list of factor names, calculation descriptions, factor column schema, and total number of factor columns.

**Raises:**

- ValueError: If the merged data is empty or if no factor candidates are provided.
**Examples:**

```python
>>> merged_data = pd.DataFrame({'security_id': ['AAPL', 'GOOG'], 'date': ['2022-01-01', '2022-01-01'], 'price': [100.0, 2000.0]})
>>> factor_candidates = [Factor('book_to_price', 'Book-to-Price ratio')]
>>> result = compute_factor_exposures(merged_data, factor_candidates)
{'factor_names': ['book_to_price'], 'factor_calculation_descriptions': ['Book-to-Price ratio'], 'factor_column_schema': 'book_to_price: float, calculation: str', 'total_factor_columns': 1}
```



---

## define_factor_candidates

### Description
List the quantitative factors to be evaluated for predictive power.

### Conceptual Info

Defines and compiles a comprehensive list of quantitative factor candidates to be evaluated for their predictive power in the market-neutral equity strategy. This includes traditional value, momentum, and quality factors, as well as innovative ones such as ESG, sentiment, earnings revisions, and composite scores. Each factor is named and briefly defined to support subsequent factor exposure computation and model training.

### Docstring

**Summary:** Generate candidate quantitative factor names and their brief definitions for evaluation in a market-neutral equity strategy.

**Parameters:**

- objectives (List[str]): High-level investment objectives of the market-neutral equity strategy that guide the factor selection scope and relevance.
**Returns:** Tuple[List[str], List[str]] - Two parallel lists containing factor names and their corresponding short definitions for use in factor exposure computation and model development.

**Raises:**

- ValueError: If the provided objectives list is empty or None, factor candidates cannot be aligned properly.
**Examples:**

```python
>>> objectives = [
...   'Target annualized return of 10%',
...   'Limit market beta to near zero',
...   'Investment horizon of 1 year',
...   'Incorporate ESG considerations as a constraint'
>>> ]
>>> factor_names, factor_definitions = define_factor_candidates(objectives)
[ 'Book_to_Price', 'Momentum_12M', 'ROE', 'Low_Volatility', 'Earnings_Revision', 'Sentiment_Score', 'ESG_Score', 'Composite_Factor' ],
[ 'Ratio of book value to market price indicating value factor.', 'Total return over past 12 months representing momentum.', 'Return on equity measuring profitability.', 'Standard deviation of daily returns capturing volatility.', 'Revision of earnings forecasts reflecting changes in analyst expectations.', 'Aggregate news sentiment score derived from alternative data.', 'Environmental, Social, and Governance rating score.', 'Weighted combination of multiple factor scores.' ]
```

```python
>>> factor_names, factor_definitions = define_factor_candidates(['Focus on quality and low volatility'])
[ 'ROE', 'Low_Volatility' ],
[ 'Return on equity indicating company quality.', 'Standard deviation of returns representing low volatility.' ]
```



---

## define_market_neutral_objectives

### Description
Specify the quantitative criteria that enforce market neutrality for the equity portfolio.

### Conceptual Info

This node defines the market neutrality objectives for an equity portfolio, specifying quantitative criteria to ensure the portfolio remains neutral to various market factors.

### Docstring

**Summary:** Define market neutral objectives for an equity portfolio.

**Parameters:**

- strategy (str): The investment strategy for which market neutrality is required.
**Returns:** List[str] - A list of bullet points describing the market neutrality criteria, and a boolean indicating if the criteria are valid.

**Raises:**

- ValueError: If the neutrality criteria are not provided.
**Examples:**

```python
>>> define_market_neutral_objectives(strategy='market_neutral_equity')
['Beta exposure = 0', 'Dollar exposure = 0', 'Sector neutrality'] True
```



---

## define_strategy_objectives

### Description
State the high‑level investment objectives of the market‑neutral equity quantitative strategy.

### Conceptual Info

Defines the primary investment objectives for a market-neutral equity quantitative strategy.

### Docstring

**Summary:** Specifies the high-level objectives for a market-neutral equity quantitative trading strategy.

**Returns:** List[str] - A list of bullet points outlining the strategy objectives.

**Examples:**

```python
>>> define_strategy_objectives()
['Target annual return: 10%', 'Risk tolerance: 15% annualized volatility', 'Market exposure: Beta <= 0.1', 'Investment horizon: Medium-term (1-2 years)', 'Special constraint: No net long/short bias']
```



---

## define_transaction_cost_model

### Description
Specify the cost model used to estimate slippage and commissions for back‑testing.

### Conceptual Info

Defines a quantitative transaction cost model including fixed per-share commissions, bid-ask spread as percentage of price, and a market impact factor modeled by the square-root function of trade size relative to average daily volume. These parameters facilitate realistic cost estimation of trades during back-testing and portfolio optimization.

### Docstring

**Summary:** Specify the transaction cost model parameters to estimate trading costs including commissions, bid-ask spread, and market impact for back-testing equity strategies.

**Parameters:**

- commission_per_share (float): Fixed commission charged per share traded, e.g., 0.005 equals $0.005 per share.
- bid_ask_spread_percent (float): Bid-ask spread expressed as a decimal percentage of the security price, e.g., 0.001 = 0.1% spread.
- impact_factor (float): Market impact parameter for the square-root function modeling price impact relative to trade size and average daily volume, typically between 0 and 1.
**Returns:** dict - Dictionary containing the parameters: commission_per_share (float), bid_ask_spread_percent (float), impact_factor (float).

**Raises:**

- ValueError: If any of the input parameter values are negative or not within reasonable bounds.
**Examples:**

```python
>>> cost_model = define_transaction_cost_model(
...     commission_per_share=0.005,
...     bid_ask_spread_percent=0.001,
...     impact_factor=0.2
>>> )
>>> print(cost_model)
{'commission_per_share': 0.005, 'bid_ask_spread_percent': 0.001, 'impact_factor': 0.2}
```

```python
>>> cost_model = define_transaction_cost_model(
...     commission_per_share=0.007,
...     bid_ask_spread_percent=0.002,
...     impact_factor=0.15
>>> )
>>> print(cost_model)
{'commission_per_share': 0.007, 'bid_ask_spread_percent': 0.002, 'impact_factor': 0.15}
```



---

## define_universe_criteria

### Description
Define the screening rules that will select which equities are eligible for trading.

### Conceptual Info

Defines explicit screening criteria describing the equity universe for trading, incorporating quantitative filters like market capitalization, liquidity, price range, listing exchanges, and fundamental performance filters (e.g., positive earnings) to ensure selection of appropriate securities for the strategy.

### Docstring

**Summary:** Defines the screening rules to select equities eligible for inclusion in the trading universe. Applies filters based on market capitalization, liquidity, price, listing exchanges, and fundamental earnings criteria.

**Parameters:**

- market_cap_min (float): Minimum market capitalization in USD; securities below this are excluded.
- market_cap_max (float): Maximum market capitalization in USD; securities above this are excluded.
- avg_daily_volume_min (float): Minimum average daily trading volume in shares; ensures adequate liquidity.
- price_min (float): Minimum share price in USD; removes very low-priced stocks.
- price_max (float): Maximum share price in USD; excludes overly expensive stocks.
- exchanges (List[str]): List of authorized listing exchanges; only securities listed here are eligible.
- positive_earnings (bool): If True, screen to include only securities demonstrating positive earnings.
**Returns:** dict - Dictionary containing the defined screening criteria for the equity universe with keys: market_cap_min, market_cap_max, avg_daily_volume_min, price_min, price_max, exchanges, positive_earnings.

**Raises:**

- ValueError: If minimum values exceed maximum values (e.g., market_cap_min > market_cap_max) or if exchanges list is empty.
- TypeError: If input types do not match expected types (e.g., exchanges not a list of strings).
**Examples:**

```python
>>> screening_criteria = define_universe_criteria(
...     market_cap_min=5e9,
...     market_cap_max=1e11,
...     avg_daily_volume_min=5e6,
...     price_min=5.0,
...     price_max=150.0,
...     exchanges=['NYSE', 'NASDAQ'],
...     positive_earnings=True
>>> )
>>> print(screening_criteria)
{'market_cap_min': 5000000000.0, 'market_cap_max': 100000000000.0, 'avg_daily_volume_min': 5000000.0, 'price_min': 5.0, 'price_max': 150.0, 'exchanges': ['NYSE', 'NASDAQ'], 'positive_earnings': True}
```

```python
>>> screening_criteria = define_universe_criteria(
...     market_cap_min=1e8,
...     market_cap_max=5e9,
...     avg_daily_volume_min=1e5,
...     price_min=1.0,
...     price_max=50.0,
...     exchanges=['AMEX'],
...     positive_earnings=False
>>> )
>>> print(screening_criteria)
{'market_cap_min': 100000000.0, 'market_cap_max': 5000000000.0, 'avg_daily_volume_min': 100000.0, 'price_min': 1.0, 'price_max': 50.0, 'exchanges': ['AMEX'], 'positive_earnings': False}
```



---

## deployment_plan

### Description
Outline the step\u201by\u201step plan to move the strategy from back\u201test to live production.

### Conceptual Info

This node establishes a clear, phased deployment plan to transition the trading strategy from back-testing to live production. It defines phases with timelines, milestones, and ownership to ensure timely and coordinated execution of the launch process.

### Docstring

**Summary:** Generate a structured phased deployment roadmap from back-test validation to full live production launch.

**Returns:** dict - Dictionary containing lists describing each deployment phase's name, duration in weeks, critical milestones, responsible owners, and a markdown summary table consolidating all phases.

**Raises:**

- RuntimeError: If prerequisite reviews or technology stack specifications are incomplete or unavailable.
- ValueError: If timeline weeks or milestone descriptions are inconsistent in length or format across phases.
**Examples:**

```python
>>> deployment_plan()
{
```



---

## design_execution_strategy

### Description
Outline the algorithmic execution approach to implement daily trades with minimal market impact.

### Conceptual Info

This node defines a detailed algorithmic trading execution strategy that translates daily optimized portfolio weights into timed child orders. It aims to minimize market impact and execution costs by controlling participation rates and slicing orders across the trading day while monitoring execution quality.

### Docstring

**Summary:** Generates an execution algorithm strategy converting daily target portfolio weights into time-sliced child orders with participation constraints, supporting minimal market impact and quality monitoring.

**Parameters:**

- algorithm_name (str): The name of the execution algorithm to be used, e.g., 'VWAP', 'TWAP', or 'Implementation Shortfall'.
- strategy_type (str): The broad classification of the execution strategy, such as 'Volume-Weighted', 'Time-Weighted', or 'Market-Milking'.
- participation_rate (float): Maximum fraction (0 to 1) of the estimated daily volume to participate in trading for each security.
- slice_frequency_minutes (int): Interval in minutes between successive child order placements within the trading day.
- child_order_weights (List[float]): List of target fractional order sizes relative to the total daily order, corresponding slice by slice.
- order_time_stamps (List[str]): List of ISO 8601 formatted timestamps indicating the scheduled execution times for each child order slice.
- execution_quality_metric (str): A metric name for assessing execution performance, such as 'VWAP deviation %' or 'Execution Slippage %'.
**Returns:** dict - A dictionary encapsulating the execution algorithm details: algorithm name, strategy type, participation rate limit, slice frequency, weights and timestamps for child slices, and the quality metric for execution assessment.

**Raises:**

- ValueError: If participation_rate is not in (0,1], or if slice_frequency_minutes is non-positive.
- ValueError: If lengths of child_order_weights and order_time_stamps lists differ or are empty.
- TypeError: If input types do not match the expected types.
**Examples:**

```python
>>> design_execution_strategy(
...     algorithm_name='VWAP',
...     strategy_type='Volume-Weighted',
...     participation_rate=0.1,
...     slice_frequency_minutes=15,
...     child_order_weights=[0.05, 0.1, 0.15, 0.2, 0.25, 0.25],
...     order_time_stamps=["2024-06-14T09:30:00Z", "2024-06-14T09:45:00Z", "2024-06-14T10:00:00Z",
...                       "2024-06-14T10:15:00Z", "2024-06-14T10:30:00Z", "2024-06-14T10:45:00Z"],
...     execution_quality_metric='VWAP deviation %'
>>> )
{'algorithm_name': 'VWAP', 'strategy_type': 'Volume-Weighted', 'participation_rate': 0.1, 'slice_frequency_minutes': 15, 'child_order_weights': [0.05, 0.1, 0.15, 0.2, 0.25, 0.25], 'order_time_stamps': ['2024-06-14T09:30:00Z', '2024-06-14T09:45:00Z', '2024-06-14T10:00:00Z', '2024-06-14T10:15:00Z', '2024-06-14T10:30:00Z', '2024-06-14T10:45:00Z'], 'execution_quality_metric': 'VWAP deviation %'}
```

```python
>>> design_execution_strategy(
...     algorithm_name='TWAP',
...     strategy_type='Time-Weighted',
...     participation_rate=0.05,
...     slice_frequency_minutes=30,
...     child_order_weights=[0.2, 0.2, 0.2, 0.2, 0.2],
...     order_time_stamps=["2024-06-14T09:30:00Z", "2024-06-14T10:00:00Z", "2024-06-14T10:30:00Z",
...                       "2024-06-14T11:00:00Z", "2024-06-14T11:30:00Z"],
...     execution_quality_metric='Execution Slippage %'
>>> )
{'algorithm_name': 'TWAP', 'strategy_type': 'Time-Weighted', 'participation_rate': 0.05, 'slice_frequency_minutes': 30, 'child_order_weights': [0.2, 0.2, 0.2, 0.2, 0.2], 'order_time_stamps': ['2024-06-14T09:30:00Z', '2024-06-14T10:00:00Z', '2024-06-14T10:30:00Z', '2024-06-14T11:00:00Z', '2024-06-14T11:30:00Z'], 'execution_quality_metric': 'Execution Slippage %'}
```



---

## design_portfolio_constraints

### Description
Define the quantitative constraints that enforce market neutrality and risk limits.

### Conceptual Info

This node formulates explicit quantitative portfolio constraints to ensure market-neutrality and risk control. It codifies key portfolio requirements such as zero net market beta, zero net dollar exposure, sector neutrality enforcement, limits on individual position sizes relative to NAV, liquidity minimums based on average daily volume, and factor risk exposure bounds for selected risk factors.

### Docstring

**Summary:** Constructs numerical portfolio constraints enforcing market neutrality and risk limits based on inputs from market-neutral objectives and universe criteria.

**Parameters:**

- net_beta_target (float): Target net beta exposure to the market (typically zero to achieve market neutrality).
- dollar_exposure_target (float): Target net dollar exposure for the portfolio (usually zero for dollar neutrality).
- sector_neutrality (bool): Boolean flag indicating if sector exposures must be neutralized (True) or not (False).
- max_position_size_pct (float): Maximum permitted position size as a fraction of Net Asset Value (e.g., 0.05 means 5%).
- min_liquidity_pct (float): Minimum liquidity required for a position, expressed as percentage of Average Daily Volume.
- factor_names (List[str]): List of factor names for which exposure constraints are defined.
- factor_exposure_limits (List[float]): Corresponding absolute upper bounds on portfolio exposure for each factor in factor_names.
**Returns:** dict - Dictionary of portfolio constraints specifying neutrality targets, position limits, liquidity thresholds, and factor exposure caps.

**Raises:**

- ValueError: If lengths of factor_names and factor_exposure_limits do not match.
- ValueError: If any percentage value is outside the [0,1] interval.
**Examples:**

```python
>>> constraints = design_portfolio_constraints(
...     net_beta_target=0.0,
...     dollar_exposure_target=0.0,
...     sector_neutrality=True,
...     max_position_size_pct=0.05,
...     min_liquidity_pct=0.02,
...     factor_names=['Value', 'Momentum'],
...     factor_exposure_limits=[0.1, 0.15]
>>> )
}
```

```python
>>> constraints = design_portfolio_constraints(
...     net_beta_target=0.0,
...     dollar_exposure_target=0.0,
...     sector_neutrality=False,
...     max_position_size_pct=0.10,
...     min_liquidity_pct=0.05,
...     factor_names=['Quality'],
...     factor_exposure_limits=[0.2]
>>> )
}
```



---

## develop_compliance_checks

### Description
Create a checklist of compliance rules the strategy must satisfy before trade submission.

### Conceptual Info

This node establishes a comprehensive compliance checklist for the trading strategy, specifying key regulatory and internal rules such as position limits, sector concentration caps, short-selling restrictions, leverage ceilings, and reporting obligations. It quantifies each rule with thresholds and describes the verification procedures to ensure adherence before submitting trades, using input constraints and neutrality objectives as guiding parameters.

### Docstring

**Summary:** Generate a structured compliance checklist detailing rule names, quantitative thresholds, verification methods, and flags indicating current compliance status for the trading strategy.

**Parameters:**

- net_beta_target (float): Target net market beta for the portfolio, usually zero for neutrality.
- dollar_exposure_target (float): Target net dollar exposure, typically zero to enforce dollar neutrality.
- sector_neutrality (bool): Flag indicating whether sector exposure neutrality is required.
- max_position_size_pct (float): Maximum allowed position size as a fraction of NAV (e.g., 0.05 for 5%).
- min_liquidity_pct (float): Minimum liquidity requirement as fraction of average daily volume (e.g., 0.02 for 2%).
- factor_names (List[str]): List of factor names with exposure limits applied.
- factor_exposure_limits (List[float]): Corresponding upper bounds on absolute exposure for each factor in factor_names.
- neutrality_criteria (List[str]): Market neutrality criteria defining beta, dollar, sector, and factor neutrality constraints.
- is_valid (bool): Flag indicating whether the neutrality criteria are valid and sufficient.
**Returns:** dict - A dictionary containing compliance_rule_names (List[str]), threshold_values (List[float]), verification_methods (List[str]), and is_compliance_met (List[bool]) indicating the compliance status of each rule.

**Raises:**

- ValueError: If input constraints or neutrality objectives are incomplete or inconsistent.
**Examples:**

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



---

## draft_operational_workflow

### Description
Map the sequential operational steps from data pull to trade execution.

### Conceptual Info

This node defines and maps out the complete daily operational workflow for the quantitative market-neutral equity strategy, outlining each step from the initial data acquisition to post-trade monitoring. It assigns responsibility for each step to the corresponding system or team, ensuring clear accountability and operational clarity.

### Docstring

**Summary:** Generate a detailed daily operational workflow as a sequential numbered list, specifying descriptions and responsible parties for each step in the strategy lifecycle.

**Parameters:**

- outline_technology_stack (dict): Output from the technology stack node providing the systems and infrastructure components used in each pipeline stage.
- design_execution_strategy (dict): Details of the execution algorithm and parameters which influence the execution and order generation steps.
- develop_compliance_checks (dict): The compliance rules checklist that must be satisfied before order submission.
**Returns:** dict - A dictionary containing the ordered step numbers, their descriptions, the responsible teams/systems for each step, and a concise summary of the operational workflow.

**Raises:**

- ValueError: Raised if any of the input dependency nodes do not provide the necessary information to map operational steps accurately.
**Examples:**

```python
>>> result = draft_operational_workflow(
...     outline_technology_stack={'stages': ['Data Ingestion', 'Model Training'], 'technologies': ['Cloud Storage, ETL', 'Python, Jupyter'], 'table_summary': 'Stage | Technology\n------|------------\nData Ingestion | Cloud Storage, ETL'},
...     design_execution_strategy={'algorithm_name': 'VWAP', 'strategy_type': 'Volume-Weighted', 'participation_rate': 0.1, 'slice_frequency_minutes': 15, 'child_order_weights': [0.2, 0.3, 0.5], 'order_time_stamps': ['2024-06-01T09:30:00Z', '2024-06-01T09:45:00Z', '2024-06-01T10:00:00Z'], 'execution_quality_metric': 'VWAP deviation %'},
...     develop_compliance_checks={'compliance_rule_names': ['Position Limit', 'Sector Concentration'], 'threshold_values': [0.05, 0.1], 'verification_methods': ['Portfolio value check', 'Sector exposure calculation'], 'is_compliance_met': [True, True]}
>>> )
>>> print(result['step_numbers'])
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

```python
>>> print(result['workflow_summary'])
"The daily operational workflow commences with data acquisition, proceeds through cleaning, factor computation, and signal generation, followed by portfolio optimization, rigorous compliance checking, order generation, execution, post-trade reconciliation, and concludes with performance monitoring. Each step is clearly assigned to dedicated teams or automated systems to ensure end-to-end operational effectiveness."
```



---

## evaluate_backtest_performance

### Description
Calculate performance metrics for the back‑test results.

### Conceptual Info

This node calculates various performance metrics for a backtest, including annualized return, volatility, Sharpe ratio, information ratio, maximum drawdown, and turnover.

### Docstring

**Summary:** Evaluate the performance of a backtest by calculating key metrics.

**Parameters:**

- backtest_results (dict): Results from the backtest, including portfolio daily returns, cumulative P&L, and turnover.
**Returns:** dict - A dictionary containing the calculated performance metrics.

**Raises:**

- ValueError: If the backtest results are invalid or missing required data.
**Examples:**

```python
>>> backtest_results = {'portfolio_daily_returns': [0.01, 0.02, -0.01],
...                         'cumulative_pnl': [100, 120, 110],
...                         'turnover': [0.1, 0.2, 0.1]}
>>> performance_metrics = evaluate_backtest_performance(backtest_results)
{'annualized_return': 0.08, 'annualized_volatility': 0.15, 'sharpe_ratio': 0.53, 'information_ratio': 0.42, 'maximum_drawdown': -0.1, 'turnover': 0.2, 'underperformance_periods': ['2022-01-01']}
```



---

## evaluate_models

### Description
Compare the three trained models using out‑of‑sample back‑testing on a hold‑out period.

### Conceptual Info

This node performs a rolling-window out-of-sample evaluation of three trained predictive models—Linear Regression, Random Forest, and Gradient Boosting—using back-testing on a designated holdout period. It generates risk-adjusted performance metrics including annualized return, Sharpe ratio, maximum drawdown, and information ratio, enabling direct comparison of models' forward-looking predictive efficacy.

### Docstring

**Summary:** Evaluate and compare trained predictive models with rolling-window out-of-sample back-testing over a holdout period, computing key performance metrics for each.

**Parameters:**

- trained_models (dict[str, Any]): Dictionary containing the trained models with keys as model identifiers ('LinearRegression', 'RandomForest', 'GradientBoosting') and values as the corresponding trained model objects or metadata.
- holdout_period_years (int): Integer number of years specifying the holdout (out-of-sample testing) period length used in the rolling evaluation.
- rolling_window_config (dict): Configuration dictionary defining the rolling window evaluation parameters, e.g., training window length (years), testing window length (years), and step size (e.g., 1 year).
- historical_market_data (DataFrame): Historical market data including factor exposures, returns, and relevant security identifiers required for out-of-sample testing.
- benchmark_returns (Series): Benchmark return series for calculating information ratio during back-testing.
**Returns:** List[dict] - List of dictionaries, each containing evaluation metrics ('model_name', 'holdout_period_years', 'annualized_return', 'annualized_sharpe', 'maximum_drawdown', 'information_ratio') for one of the trained models.

**Raises:**

- ValueError: If the holdout_period_years is non-positive or exceeds data availability.
- KeyError: If required model names or training data are missing.
- RuntimeError: If backtesting or metric computations fail due to inconsistent data or errors.
**Examples:**

```python
>>> trained_models = {
...     'LinearRegression': linear_reg_model,
...     'RandomForest': rf_model,
...     'GradientBoosting': gbm_model
>>> }
>>> results = evaluate_models(trained_models, holdout_period_years=1, rolling_window_config={'train_years':2, 'test_years':1}, historical_market_data=market_df, benchmark_returns=bench_returns)
>>> for res in results:
...     print(f"Model: {res['model_name']}, Annualized Return: {res['annualized_return']:.2%}, Sharpe: {res['annualized_sharpe']:.2f}")
Model: LinearRegression, Annualized Return: 8.27%, Sharpe: 1.10
Model: RandomForest, Annualized Return: 10.15%, Sharpe: 1.35
Model: GradientBoosting, Annualized Return: 11.42%, Sharpe: 1.48
```



---

## final_review_and_approval

### Description
Perform a final review of the strategy memorandum and secure sign‑off.

### Conceptual Info

This node conducts a final comprehensive review of the completed strategy memorandum by evaluating predefined critical aspects—methodology soundness, risk limits, compliance coverage, technology readiness, and governance. Each aspect is assigned an approval status. The review culminates with a formal sign‑off by a senior manager, ensuring that all key areas meet quality standards before deployment planning.

### Docstring

**Summary:** Perform a final quality and readiness review of the strategy memorandum based on a predefined checklist, then record approval sign‑off details.

**Parameters:**

- prepared_documentation (dict): The comprehensive strategy memorandum output from 'prepare_strategy_documentation' node. Includes sections such as objectives, risk management, compliance, technology, and performance summary, used as input context for the review.
**Returns:** dict - A dictionary containing the checklist items (list of str), corresponding statuses (list of str with values 'Approved' or 'Needs Revision'), the sign‑off senior manager's name (str), and the approval date in ISO 8601 format (str).

**Raises:**

- ValueError: If the prepared_documentation is missing required sections needed for review.
- TypeError: If input is not a dictionary with expected keys.
**Examples:**

```python
>>> prepared_doc = {
...     'objectives': ['Target 10% annual return', 'Market neutral beta'],
...     'risk_management': 'Uses VAR limits and stress testing',
...     'compliance': 'Meets SEC regulations and internal policies',
...     'technology_stack': 'Python, CVXOPT, FIX gateway',
...     'performance_summary': 'Sharpe ratio 1.5, max drawdown 10%'
>>> }
>>> output = final_review(prepared_doc)
{
```



---

## generate_signals

### Description
Produce daily predicted excess return signals for each security using the selected model.

### Conceptual Info

This node generates daily predicted excess returns signals for each security by applying the best performing predictive model to computed factor exposures over the trading history. The signals represent predicted asset-specific return differentials compared to a benchmark and form the basis for portfolio optimization.

### Docstring

**Summary:** Generate daily predicted excess return signals per security by applying the selected predictive model to the computed factor exposures over time.

**Parameters:**

- selected_model_name (str): Name or identifier of the selected best performing predictive model (e.g., 'RandomForest').
- factor_exposures (Dict[str, Dict[str, float]] or DataFrame): Factor exposures mapped by security identifier and date, containing factor values as inputs to the model.
- model_object (Any): Trained predictive model instance capable of scoring or predicting excess returns given factor inputs.
**Returns:** dict - Dictionary containing signal generation metadata and statistics with keys: 'date_range_start' (str), 'date_range_end' (str), 'num_signals' (int), 'signal_mean' (float), 'signal_std' (float).

**Raises:**

- ValueError: Raised if input factor exposures are empty or model is not properly provided.
- RuntimeError: Raised if signal generation fails due to mismatch in data dimensions or model prediction errors.
**Examples:**

```python
>>> signals = generate_signals(
...     selected_model_name='RandomForest',
...     factor_exposures={
...         '2023-01-02': {'AAPL': {'momentum': 0.5, 'value': -0.1}, 'MSFT': {'momentum': 0.3, 'value': 0.0}},
...         '2023-01-03': {'AAPL': {'momentum': 0.6, 'value': -0.05}, 'MSFT': {'momentum': 0.4, 'value': 0.02}},
...     },
...     model_object=rf_model_instance
>>> )
{'date_range_start': '2023-01-02', 'date_range_end': '2023-01-03', 'num_signals': 4, 'signal_mean': 0.015, 'signal_std': 0.005}
```

```python
>>> # Assuming factor_exposures is a DataFrame with MultiIndex (date, security)
>>> import pandas as pd
>>> signals = generate_signals(
...     selected_model_name='LinearRegression',
...     factor_exposures=factor_exposure_df,
...     model_object=linreg_model_instance
>>> )
{'date_range_start': '2015-01-01', 'date_range_end': '2023-01-01', 'num_signals': 100000, 'signal_mean': 0.0003, 'signal_std': 0.002}
```



---

## identify_data_sources

### Description
Identify the data providers and types needed for price, fundamentals, and alternative signals.

### Conceptual Info

This node identifies and classifies the essential data providers and the specific data fields needed to support a market-neutral equity strategy. It segments required inputs into three categories—market price data, fundamental financial data, and alternative data (such as sentiment and ESG metrics)—providing clarity and structure to data acquisition processes downstream. The output guides subsequent data retrieval and integration steps.

### Docstring

**Summary:** Identify and enumerate data providers along with required data fields for market price, fundamental financial, and alternative data signals used in the quantitative strategy.

**Returns:** dict - Dictionary containing lists of data source provider names and corresponding data fields for three categories: market price data, fundamental data, and alternative data.

**Raises:**

- ValueError: If no valid data sources or fields are identified for one or more categories.
**Examples:**

```python
>>> identify_data_sources()
{" +
                "\n  'market_price_data_sources': ['Bloomberg', 'Refinitiv']," +
                "\n  'market_price_fields': ['adjusted_close, open, high, low, volume, split_factor']," +
                "\n  'fundamental_data_sources': ['FactSet', 'Compustat']," +
                "\n  'fundamental_fields': ['earnings_per_share, book_value, cash_flow, leverage, dividend_yield']," +
                "\n  'alternative_data_sources': ['Sentifi', 'MSCI', 'Google Trends']," +
                "\n  'alternative_fields': ['news_sentiment, esg_score, analyst_forecast, google_trends']" +
                "\n}
```



---

## launch_strategy

### Description
Execute the final steps to go live with the market‑neutral equity strategy.

### Conceptual Info

This node finalizes the launch of the market-neutral equity strategy by verifying completion of all critical pre-launch requirements including infrastructure readiness, data connectivity, compliance approval, risk limit settings, and active monitoring. It then issues a formal launch confirmation stating the strategy is live as of the current date.

### Docstring

**Summary:** Finalize and execute the launch sequence for the market-neutral equity strategy, confirming all pre-launch prerequisites are complete and the strategy is live.

**Parameters:**

- deployment_plan_status (dict): Status and details from the deployment plan node indicating readiness of deployment phases.
- monitoring_setup_status (dict): Details of monitoring metrics, alert thresholds, and notification channels from setup_monitoring_and_alerts node indicating monitoring readiness.
- infrastructure_status (str): Current status of infrastructure confirming readiness ('ready' or 'not ready').
- data_feeds_status (str): Connectivity and operational status of data feeds ('connected' or 'not connected').
- compliance_sign_off (bool): Flag indicating whether compliance has signed off on the strategy.
- risk_limits (str): Description or reference to the risk limits that have been configured and approved.
- monitoring_status (str): Status of monitoring systems ('active' or 'inactive').
**Returns:** dict - A dictionary containing the launch status boolean, launch date string, checklist of confirmed pre-launch items, and current system/component statuses.

**Raises:**

- ValueError: If any critical pre-launch item is incomplete or shows a negative status preventing a successful launch.
- RuntimeError: If infrastructure or data feeds are not ready or monitoring is inactive at launch time.
**Examples:**

```python
>>> launch_strategy(
...   deployment_plan_status={'phase_names': ['Phase 1', 'Phase 2', 'Phase 3'], 'summary_table': '...'},
...   monitoring_setup_status={
...     'metric_names': ['P&L deviation', 'Exposure limits breached'],
...     'threshold_values': [2.0, 0.05],
...     'monitoring_cadence': ['real-time', 'real-time'],
...     'notification_channels': ['Slack', 'email']
...   },
...   infrastructure_status='ready',
...   data_feeds_status='connected',
...   compliance_sign_off=True,
...   risk_limits='Max position size 5%, Net beta 0, Sector neutrality',
...   monitoring_status='active'
>>> )
{
```



---

## merge_cleaned_data

### Description
Combine cleaned price, fundamental, and alternative data into a single panel dataset.

### Conceptual Info

This node consolidates three cleaned datasets—price data, fundamental data, and alternative data—by joining them on the security identifier and date fields. The output is a comprehensive panel dataset indexed by security and trading day, containing combined features from all three sources, suitable for downstream factor computation and modeling.

### Docstring

**Summary:** Merge cleaned price, fundamental, and alternative datasets on security identifier and date to produce a unified panel dataset with combined features.

**Parameters:**

- price_data (DataFrame): Cleaned price data including daily price and corporate action adjusted fields, indexed or containing security identifier and date.
- fundamental_data (DataFrame): Cleaned fundamental accounting data standardized to consistent units, aligned to calendar dates, indexed or containing security identifier and date.
- alternative_data (DataFrame): Cleaned alternative data series with aligned timestamps and winsorized values, indexed or containing security identifier and date.
**Returns:** dict - A dictionary containing: total_rows (int), total_columns (int), column_names (List[str]), is_successful (bool), and merge_summary (str), summarizing the resulting merged dataset.

**Raises:**

- ValueError: If any input dataset is empty or missing required columns such as 'security_id' or 'date'.
- MergeError: If the join operation fails due to incompatible indices or unmatched key columns.
**Examples:**

```python
>>> merged = merge_cleaned_data(price_data, fundamental_data, alternative_data)
>>> print(merged['total_rows'])
>>> print(merged['total_columns'])
>>> print(merged['is_successful'])
>>> print(merged['merge_summary'])
250000
120
True
'Merged 5000 securities over 50 trading days with 120 columns.'
```

```python
>>> # Assuming mismatched keys or empty data triggers error
>>> try:
...     merge_cleaned_data(empty_price_data, fundamental_data, alternative_data)
>>> except ValueError as e:
...     print(str(e))
'Input price_data is empty or missing required keys.'
```



---

## optimize_portfolio

### Description
Solve for optimal security weights that maximize predicted return subject to the defined constraints and transaction cost model.

### Conceptual Info

This node performs portfolio optimization by solving a quadratic programming problem that maximizes expected returns based on predicted signals while incorporating transaction costs and satisfying portfolio constraints. It outputs the optimal security weights for a given date and reports gross and net exposures.

### Docstring

**Summary:** Compute the optimal portfolio weights that maximize predicted returns net of transaction costs under predefined constraints for a specified date.

**Parameters:**

- signal_vector (List[float]): Predicted excess return signals for each security on the optimization date, aligned with the portfolio universe.
- constraints (Dict[str, Any]): A dictionary encapsulating portfolio constraints such as net beta target, dollar exposure target, sector neutrality flag, maximum position size percentage, minimum liquidity threshold, factor names, and factor exposure limits.
- transaction_costs (Dict[str, float]): Parameters of the transaction cost model including commission per share, bid-ask spread percentage, and market impact factor.
- current_positions (List[float]): Current portfolio weights for each security, used to compute transaction costs related to rebalancing.
- date (str): The specific date (ISO format YYYY-MM-DD) for which to compute the optimal portfolio weights.
**Returns:** Dict[str, Any] - A dictionary containing: 'optimal_date' the optimization date; 'weight_vector' list of floats for optimal security weights; 'gross_exposure' total absolute exposure float; 'net_exposure' net dollar exposure float.

**Raises:**

- ValueError: Raised if input vectors lengths do not match or if constraints are not properly specified.
- OptimizationError: Raised if the quadratic programming solver fails to find a feasible or optimal solution.
**Examples:**

```python
>>> signal_vector = [0.02, 0.01, -0.01]
>>> constraints = {
...     'net_beta_target': 0.0,
...     'dollar_exposure_target': 0.0,
...     'sector_neutrality': True,
...     'max_position_size_pct': 0.05,
...     'min_liquidity_pct': 0.02,
...     'factor_names': ['value', 'momentum'],
...     'factor_exposure_limits': [0.1, 0.15]
>>> }
>>> transaction_costs = {
...     'commission_per_share': 0.005,
...     'bid_ask_spread_percent': 0.001,
...     'impact_factor': 0.2
>>> }
>>> current_positions = [0.0, 0.0, 0.0]
>>> date = '2023-08-01'
>>> output = optimize_portfolio(signal_vector, constraints, transaction_costs, current_positions, date)
{
  'optimal_date': '2023-08-01',
  'weight_vector': [0.04, 0.03, -0.05],
  'gross_exposure': 0.12,
  'net_exposure': 0.02
}
```

```python
>>> # For a single-day optimization with existing positions
>>> signal_vector = [0.015, 0.025]
>>> constraints = {
...     'net_beta_target': 0.0,
...     'dollar_exposure_target': 0.0,
...     'sector_neutrality': False,
...     'max_position_size_pct': 0.1,
...     'min_liquidity_pct': 0.03,
...     'factor_names': ['quality'],
...     'factor_exposure_limits': [0.2]
>>> }
>>> transaction_costs = {
...     'commission_per_share': 0.004,
...     'bid_ask_spread_percent': 0.0015,
...     'impact_factor': 0.15
>>> }
>>> current_positions = [0.02, -0.01]
>>> date = '2023-08-02'
>>> output = optimize_portfolio(signal_vector, constraints, transaction_costs, current_positions, date)
{
  'optimal_date': '2023-08-02',
  'weight_vector': [0.07, -0.06],
  'gross_exposure': 0.13,
  'net_exposure': 0.01
}
```



---

## outline_technology_stack

### Description
Specify the software and infrastructure components needed to run the end‑to‑end pipeline.

### Conceptual Info

This node identifies and documents the essential software and infrastructure technologies required to support each stage of a market-neutral equity quantitative strategy pipeline, from data ingestion through monitoring.

### Docstring

**Summary:** Outline the technology components and software infrastructure required at each key stage of the end-to-end quantitative equity strategy pipeline, returning ordered lists of pipeline stages and their corresponding technology tools, along with a formatted summary table.

**Returns:** dict - A dictionary containing:
- 'stages': List[str], an ordered sequence of pipeline stages.
- 'technologies': List[str], corresponding tools/technologies for each stage.
- 'table_summary': str, a human-readable two-column table presenting stages and technologies.

**Raises:**

- RuntimeError: If required upstream data about data sources, execution strategy, or compliance checks is missing or inconsistent.
**Examples:**

```python
>>> output = outline_technology_stack()
>>> print(output['stages'])
>>> print(output['technologies'])
>>> print(output['table_summary'])
("['Data Ingestion', 'Model Training', 'Optimization', 'Execution', 'Monitoring']\n"
                         "['AWS S3, Apache Airflow', 'Python, Jupyter, CUDA GPUs', 'CVXOPT, Gurobi', 'FIX Protocol Gateway, OMS', 'Grafana, Prometheus, PagerDuty']\n"
                         "+-----------------+------------------------------------------+\n"
                         "| Stage           | Technology                               |\n"
                         "+-----------------+------------------------------------------+\n"
                         "| Data Ingestion  | AWS S3, Apache Airflow                   |\n"
                         "| Model Training  | Python, Jupyter, CUDA GPUs               |\n"
                         "| Optimization    | CVXOPT, Gurobi                          |\n"
                         "| Execution       | FIX Protocol Gateway, OMS                |\n"
                         "| Monitoring      | Grafana, Prometheus, PagerDuty          |\n"
                         "+-----------------+------------------------------------------+")
```



---

## prepare_strategy_documentation

### Description
Compile a comprehensive strategy memorandum covering methodology, risk, and operations.

### Conceptual Info

This node compiles a detailed strategy memorandum that documents the quantitative market-neutral equity strategy. It integrates investment objectives, universe definition, data sourcing, factor modeling, signal generation methodology, portfolio construction optimization, risk assessment, execution tactics, compliance policies, technology infrastructure, and summarizes back-test performance metrics. The document serves as a comprehensive manual for stakeholders to understand and assess the strategy holistically.

### Docstring

**Summary:** Compile a comprehensive plain-text strategy memorandum summarizing key components of a market-neutral equity quantitative strategy, each section limited to 300 words.

**Parameters:**

- objectives (List[str]): A list of the strategy’s high-level investment objectives, typically covering target return, risk tolerance, market exposure, investment horizon, and constraints.
- evaluate_backtest_performance (dict): Performance metrics from the back-test, including annualized return, volatility, Sharpe ratio, information ratio, max drawdown, turnover, and periods of underperformance.
- risk_analysis (dict): Risk analysis outputs covering factor exposures, drawdown contributors, stress test results, and factor sensitivity measures.
- draft_operational_workflow (dict): Description of the daily operational steps, including responsibilities for each workflow stage.
- design_execution_strategy (dict): Algorithmic execution strategy details including algorithm name, participation rates, slicing frequency, and execution quality metrics.
**Returns:** dict - A comprehensive dictionary containing string summaries and lists documenting the strategy memorandum, including objectives, universe, data sources, factor model, signal generation, portfolio construction, risk management, execution strategy, compliance, technology stack, and performance summary.

**Raises:**

- ValueError: If any required input field is missing or improperly formatted.
- RuntimeError: If document compilation fails due to inconsistencies among dependent inputs.
**Examples:**

```python
>>> prepare_strategy_documentation(
...   objectives=['Achieve 8% annualized return', 'Maintain beta near zero', 'Limit max drawdown to 10%'],
...   evaluate_backtest_performance={
...     'annualized_return': 0.075,
...     'sharpe_ratio': 1.25,
...     'maximum_drawdown': -0.095,
...     'underperformance_periods': ['2020-Q1']
...   },
...   risk_analysis={'factor_names':['Value','Momentum'], 'average_exposure':[0.1,0.05], 'max_drawdown':-0.095, 'top_drawdown_contributors':['Momentum'], 'drawdown_sensitivity':[0.02,0.05], 'stress_factor_names':['Value','Momentum'], 'stress_sensitivity_positive':[0.01,-0.03], 'stress_sensitivity_negative':[-0.01,0.03]},
...   draft_operational_workflow={'step_numbers':[1,2,3], 'step_descriptions':['Data ingestion','Cleaning','Optimization'], 'step_responsible':['Data Team','Quant Team','Portfolio Team'], 'workflow_summary':'Daily process from data pull through portfolio optimization.'},
...   design_execution_strategy={'algorithm_name':'VWAP', 'participation_rate':0.1, 'slice_frequency_minutes':15, 'execution_quality_metric':'VWAP deviation %'}
>>> )
{'objectives': [...], 'universe_description': 'Equities priced above $5 with market cap $5B-$100B, listed on NYSE/NASDAQ, positive earnings only.', 'data_sources': 'Price data from XYZ, fundamentals from ABC, alternative data from DEF.', 'factor_model': 'Factors constructed from fundamental ratios, momentum scores, and sentiment indicators.', 'signal_generation': 'Signals derived from linear combination of selected factors weighted by regression coefficients.', 'portfolio_construction': 'Quadratic optimization maximizing expected return minus transaction costs, with market-neutral constraints.', 'risk_management': 'Monitor factor exposures, max drawdown limits, and stress test results; mitigate via constraints.', 'execution_strategy': 'VWAP algorithm with 10% max participation rate, slicing every 15 minutes; monitor VWAP deviation.', 'compliance': 'Position limits, sector neutrality, short-selling constraints verified daily.', 'technology_stack': 'Python, CVXOPT for optimization, FIX gateway for execution, Grafana monitoring.', 'performance_summary': 'Annualized Return: 7.5%, Sharpe:1.25, Max Drawdown: 9.5%, noted underperformance in 2020-Q1'}
```



---

## risk_analysis

### Description
Analyze factor exposures, drawdown drivers, and stress scenarios for the strategy.

### Conceptual Info

This node conducts a comprehensive risk analysis of the strategy's portfolio by leveraging back-test results and factor exposures. It quantifies average factor exposures, isolates key factors driving maximum drawdown, estimates how sensitive the portfolio returns were to each factor during drawdown, and performs stress testing by applying ±2 standard deviations shocks to each factor to assess potential risk under extreme movements. The output includes both summary bullet points and detailed factor sensitivity tables for robust risk management insights.

### Docstring

**Summary:** Analyze portfolio factor exposures, identify main drawdown contributors, and perform ±2σ stress tests on factor sensitivities using back-test data and factor exposures.

**Parameters:**

- backtest_returns (List[float]): Time series of portfolio daily returns from the back-test period.
- portfolio_weights (List[List[float]]): Daily portfolio weights for each security, aligned with factor exposures.
- factor_exposures (Dict[str, List[List[float]]]): Dictionary mapping each factor name to its exposure matrix over securities and dates.
- factor_stddevs (Dict[str, float]): Standard deviation values of each factor over the back-test period used for stress shocks.
**Returns:** Dict[str, Any] - Dictionary containing: factor names; average exposures per factor; maximum portfolio drawdown; top contributing factors to drawdown; drawdown period factor sensitivities; and stress test sensitivities for ±2σ shocks.

**Raises:**

- ValueError: If input arrays have inconsistent lengths or missing data.
- RuntimeError: If drawdown or stress test computations fail due to data issues.
**Examples:**

```python
>>> backtest_returns = [-0.005, -0.01, 0.002, 0.001, -0.007]
>>> portfolio_weights = [[0.1, -0.1], [0.12, -0.12], [0.11, -0.11], [0.13, -0.13], [0.1, -0.1]]
>>> factor_exposures = {
...     'Momentum': [[0.5, 0.4], [0.52, 0.42], [0.5, 0.41], [0.49, 0.43], [0.51, 0.4]],
...     'Value': [[-0.3, -0.25], [-0.31, -0.26], [-0.29, -0.24], [-0.3, -0.25], [-0.28, -0.26]]
>>> }
>>> factor_stddevs = {'Momentum': 0.1, 'Value': 0.05}
>>> results = risk_analysis(backtest_returns, portfolio_weights, factor_exposures, factor_stddevs)
>>> print(results['factor_names'])
>>> print(results['max_drawdown'])
['Momentum', 'Value']
-0.015
```

```python
>>> # The output includes average factor exposures, drawdown contributors, and stress test sensitivities in structured lists.
{" +
                ""average_exposure": [0.5, -0.3], " +
                ""top_drawdown_contributors": ["Momentum"], " +
                ""stress_sensitivity_positive": [-0.03, 0.01]" +
                
```



---

## select_best_model

### Description
Identify the model with the highest risk-adjusted performance.

### Conceptual Info

Selects the model with the highest risk-adjusted performance from the evaluation table.

### Docstring

**Summary:** Select the best model based on the highest information ratio or Sharpe ratio from the evaluation table.

**Parameters:**

- evaluation_table (dict): Dictionary containing model performance metrics
**Returns:** dict - Dictionary with the selected model name and its key performance numbers

**Raises:**

- ValueError: If the evaluation table is empty or no model performance metrics are provided
**Examples:**

```python
>>> evaluation_table = {
...   'LinearRegression': {'information_ratio': 0.8, 'sharpe_ratio': 1.2, 'annualized_return': 0.1, 'maximum_drawdown': -0.05},
...   'RandomForest': {'information_ratio': 0.9, 'sharpe_ratio': 1.1, 'annualized_return': 0.2, 'maximum_drawdown': -0.03},
...   'GradientBoosting': {'information_ratio': 1.0, 'sharpe_ratio': 1.3, 'annualized_return': 0.3, 'maximum_drawdown': -0.04}
>>> }
>>> select_best_model(evaluation_table)
{'selected_model': 'GradientBoosting', 'information_ratio': 1.0, 'sharpe_ratio': 1.3, 'annualized_return': 0.3, 'maximum_drawdown': -0.04}
```



---

## select_significant_factors

### Description
Choose the subset of factors that passed significance thresholds.

### Conceptual Info

This node filters factors based on statistical significance and positive predictive strength to identify which factors are meaningfully predictive and should be retained for subsequent modeling.

### Docstring

**Summary:** Select factors with p-value < 0.05 and positive average t-statistic from factor performance results.

**Parameters:**

- factor_names (List[str]): List of factor names evaluated in the performance test.
- avg_t_stats (List[float]): Average t-statistics corresponding to each factor from the regressions.
- p_values (List[float]): P-values for each factor's performance coefficient, indicating statistical significance.
**Returns:** dict - Dictionary with keys 'selected_factors' (list of factor names passing criteria), 'significant_factor_count' (count of these factors), and 'is_valid_selection' (boolean flag if valid selection achieved).

**Raises:**

- ValueError: If input lists (factor_names, avg_t_stats, p_values) are of unequal length.
- ValueError: If input lists are empty, making selection impossible.
**Examples:**

```python
>>> factor_names = ['Value', 'Momentum', 'Quality', 'Volatility']
>>> avg_t_stats = [2.5, -1.2, 3.1, 0.5]
>>> p_values = [0.01, 0.10, 0.03, 0.04]
>>> result = select_significant_factors(factor_names, avg_t_stats, p_values)
>>> print(result)
{'selected_factors': ['Value', 'Quality', 'Volatility'], 'significant_factor_count': 3, 'is_valid_selection': True}
```

```python
>>> factor_names = ['FactorA', 'FactorB']
>>> avg_t_stats = [-0.5, 1.0]
>>> p_values = [0.06, 0.06]
>>> result = select_significant_factors(factor_names, avg_t_stats, p_values)
>>> print(result)
{'selected_factors': [], 'significant_factor_count': 0, 'is_valid_selection': False}
```



---

## setup_monitoring_and_alerts

### Description
Define the real‑time monitoring metrics and alert thresholds for live trading.

### Conceptual Info

This node defines the essential real-time monitoring metrics and their quantitative alert thresholds for the live trading environment of the quantitative market-neutral equity strategy. It specifies the frequency at which these metrics are monitored and the communication channels to notify stakeholders of any breaches or anomalies. The goal is to enable responsive operational oversight that ensures risk and execution performance remain within defined parameters.

### Docstring

**Summary:** Configure the set of real-time monitoring metrics for live trading, their alert thresholds, monitoring cadence, and notification channels.

**Parameters:**

- metric_names (List[str]): List containing the names of each metric to be actively tracked and monitored during live trading (e.g., 'P&L deviation', 'Exposure Limits Breached').
- threshold_values (List[float]): Numerical thresholds corresponding to each metric that if crossed will trigger an alert. Thresholds may be expressed in metric-specific units or multiples of standard deviations (e.g., 2.0 for 2σ). The list order matches that of metric_names.
- monitoring_cadence (List[str]): Frequency at which each metric is evaluated, such as 'real-time' for continuous monitoring, 'hourly', or 'daily'. This list aligns 1-to-1 with metric_names.
- notification_channels (List[str]): Communication channels used to send alerts upon threshold breach, for example, 'email', 'Slack', or 'PagerDuty'. Each entry corresponds to a metric.
**Returns:** dict - A dictionary containing: 'metric_names', 'threshold_values', 'monitoring_cadence', and 'notification_channels', representing the full configuration for live monitoring and alerting.

**Raises:**

- ValueError: If the input lists are of mismatched lengths or if threshold values are not numeric.
**Examples:**

```python
>>> metrics = ['P&L Deviation', 'Exposure Breach', 'Latency', 'Execution Slippage']
>>> thresholds = [2.0, 0.0, 200.0, 0.05]
>>> cadence = ['real-time', 'real-time', 'hourly', 'daily']
>>> channels = ['Slack', 'PagerDuty', 'Email', 'Email']
>>> setup_monitoring_and_alerts(metrics, thresholds, cadence, channels)
{'metric_names': ['P&L Deviation', 'Exposure Breach', 'Latency', 'Execution Slippage'],
 'threshold_values': [2.0, 0.0, 200.0, 0.05],
 'monitoring_cadence': ['real-time', 'real-time', 'hourly', 'daily'],
 'notification_channels': ['Slack', 'PagerDuty', 'Email', 'Email']}
```

```python
>>> metric_names = ['Portfolio Turnover', 'Max Drawdown']
>>> threshold_values = [0.1, 0.15]
>>> monitoring_cadence = ['daily', 'daily']
>>> notification_channels = ['Email', 'Slack']
>>> setup_monitoring_and_alerts(metric_names, threshold_values, monitoring_cadence, notification_channels)
{'metric_names': ['Portfolio Turnover', 'Max Drawdown'],
 'threshold_values': [0.1, 0.15],
 'monitoring_cadence': ['daily', 'daily'],
 'notification_channels': ['Email', 'Slack']}
```



---

## test_factor_performance

### Description
Assess each factor’s historical predictive performance via time‑series regression.

### Conceptual Info

This node quantifies the historical predictive power of each factor by running individual time‑series cross‑sectional regressions between next‑day stock returns and factor exposures. The results yield statistical metrics such as average t‑statistics, annualized Sharpe ratios, and p‑values, providing insight into factor significance and efficacy.

### Docstring

**Summary:** Evaluate historical predictive performance of each individual factor by running cross-sectional regressions of next-day stock returns on factor exposures. Returns summary statistics including average t-statistics, annualized Sharpe ratios, p-values, and significance flags.

**Parameters:**

- factor_names (List[str]): List of factor names computed for each security-day, as generated by compute_factor_exposures.
- factor_exposures (Dict[str, List[float]]): Mapping from factor names to their exposure values for each security-day across the dataset.
- next_day_returns (List[float]): List or array of next-day stock returns for each security-day observation, aligned with factor exposures.
**Returns:** Dict[str, List] - A dictionary containing performance metrics per factor: 'factor_names' (List[str]), 'avg_t_stats' (List[float]), 'annualized_sharpe' (List[float]), 'p_values' (List[float]), and 'is_significant' (List[bool]) indicating statistical significance.

**Raises:**

- ValueError: If factor exposures or returns are missing, misaligned, or empty.
- RuntimeError: If regression fitting fails for any factor due to data issues.
**Examples:**

```python
>>> factor_names = ['momentum', 'value']
>>> factor_exposures = {
...     'momentum': [0.1, 0.2, -0.1, 0.05],
...     'value': [0.5, 0.3, 0.1, -0.2]
>>> }
>>> next_day_returns = [0.02, 0.03, -0.01, 0.0]
>>> results = test_factor_performance(factor_names, factor_exposures, next_day_returns)
{'factor_names': ['momentum', 'value'],
 'avg_t_stats': [2.5, 1.1],
 'annualized_sharpe': [1.3, 0.7],
 'p_values': [0.015, 0.28],
 'is_significant': [True, False]}
```

```python
>>> factor_names = ['quality']
>>> factor_exposures = {'quality': [0.2, 0.4, 0.3]}
>>> next_day_returns = [0.01, 0.02, 0.015]
>>> results = test_factor_performance(factor_names, factor_exposures, next_day_returns)
{'factor_names': ['quality'],
 'avg_t_stats': [3.2],
 'annualized_sharpe': [1.6],
 'p_values': [0.005],
 'is_significant': [True]}
```



---

## train_gradient_boosting_model

### Description
Fit a gradient boosting model using the selected factors to predict next‑day returns.

### Conceptual Info

This node trains a gradient boosting regression model, specifically calibrated to predict next-day excess returns of securities using a selected subset of statistically significant predictive factors. It leverages merged cleaned data and computed factor exposures, fitting the model under specified hyperparameters and evaluating performance with validation metrics and feature importance insights.

### Docstring

**Summary:** Train a gradient boosting regression model on selected factor exposures to predict next-day excess returns.

**Parameters:**

- merged_data (DataFrame or equivalent): Cleaned and merged dataset including price, fundamental, and alternative data with one row per security-date.
- factor_exposures (DataFrame or equivalent): Numeric exposures of each security to candidate factors computed from merged_data.
- selected_factors (List[str]): List of factor names selected based on statistical significance to be used as features in the model.
- target_returns (Series or array-like): Next-day excess returns for each security-date, aligned with factor exposures and merged data.
**Returns:** dict - Dictionary containing trained model name, validation root mean squared error (RMSE), ordered list of feature names used, and corresponding feature importance scores.

**Raises:**

- ValueError: If no selected factors are provided or if input data dimensions do not align.
- TrainingError: If model training fails due to convergence or data quality issues.
**Examples:**

```python
>>> result = train_gradient_boosting_model(
...     merged_data=merged_df,
...     factor_exposures=factor_df,
...     selected_factors=['Momentum', 'Value', 'Quality'],
...     target_returns=next_day_returns_series
>>> )
>>> print(result['model_name'], result['validation_rmse'])
XGBoost_GBM 0.0125
```

```python
>>> model_info = train_gradient_boosting_model(
...     merged_data=merged_df,
...     factor_exposures=factor_df,
...     selected_factors=['Sentiment_Score', 'Earnings_Revisions'],
...     target_returns=next_day_returns_series
>>> )
>>> print(model_info['feature_names'])
>>> print(model_info['feature_importances'])
['Sentiment_Score', 'Earnings_Revisions']
[0.65, 0.35]
```



---

## train_linear_regression_model

### Description
Fit a linear regression model using the selected factors to predict next‑day returns.

### Conceptual Info

This node fits a linear regression model that predicts next-day excess returns of securities based on their exposures to a selected set of significant factors. It applies ordinary least squares regression using a merged dataset that includes price, fundamental, and alternative data alongside computed factor exposures. The model outputs the intercept, coefficients for each factor, the in-sample goodness-of-fit (R-squared), and the sample size used.

### Docstring

**Summary:** Fit a linear regression model to predict next-day excess stock returns from selected factor exposures using the merged dataset.

**Parameters:**

- merged_data (DataFrame): DataFrame containing merged price, fundamental, and alternative data for each security and date.
- factor_exposures (DataFrame): DataFrame with computed exposures of each security to the candidate factors aligned with merged data.
- selected_factors (List[str]): List of factor names that passed significance criteria (p-value < 0.05 and positive average t-statistic).
**Returns:** dict[str, Any] - Dictionary containing: - 'factor_names': List of factor names used in the model - 'coefficients': List of estimated coefficients matching factor order - 'intercept': Regression intercept term (float) - 'r_squared': In-sample R-squared (float) - 'n_observations': Number of observations used (int)

**Raises:**

- ValueError: If the merged dataset is empty or factor exposures for selected factors are missing.
- RuntimeError: If linear regression fitting fails due to numerical instability or insufficient data.
**Examples:**

```python
>>> merged_data = pd.DataFrame({
...     'security': ['A', 'B', 'C'],
...     'date': ['2023-01-01', '2023-01-01', '2023-01-01'],
...     'next_day_excess_return': [0.01, -0.02, 0.03],
...     'factor1': [0.5, 0.3, 0.7],
...     'factor2': [1.2, 0.9, 1.1]
>>> })
>>> factor_exposures = merged_data[['factor1', 'factor2']]
>>> selected_factors = ['factor1', 'factor2']
>>> result = train_linear_regression_model(merged_data, factor_exposures, selected_factors)
{
  'factor_names': ['factor1', 'factor2'],
  'coefficients': [0.04, 0.02],
  'intercept': 0.001,
  'r_squared': 0.85,
  'n_observations': 3
}
```

```python
>>> # Using a larger dataset with multiple observations
>>> result = train_linear_regression_model(merged_data, factor_exposures, ['factor1'])
{
  'factor_names': ['factor1'],
  'coefficients': [0.035],
  'intercept': 0.0005,
  'r_squared': 0.80,
  'n_observations': 3
}
```



---

## train_random_forest_model

### Description
Fit a random forest model using the selected factors to predict next‑day returns.

### Conceptual Info

This node trains a random forest regression model to predict next-day excess returns of securities based on previously computed factor exposures. It utilizes the subset of factors identified as statistically significant and merges cleaned datasets to form the training data. The model uses 500 decision trees with default depth and estimates performance through out-of-bag R-squared. It outputs detailed model parameters and metrics to inform subsequent model evaluation and portfolio optimization.

### Docstring

**Summary:** Train a random forest regressor to predict next-day excess returns using selected factor exposures as features. The model uses 500 trees with default tree depth, employing out-of-bag samples to estimate R-squared performance.

**Parameters:**

- factor_exposures (DataFrame): Table including numerical exposures for each security-day and factor, generated by compute_factor_exposures.
- selected_factors (List[str]): List of factor names that passed significance thresholds (from select_significant_factors) used as features.
- merged_data (DataFrame): Unified dataset merging cleaned price, fundamental, and alternative data to align features with target returns.
- next_day_returns (Series or array-like): Target variable: next-day excess returns corresponding to each security-day in the training period.
**Returns:** dict - A dictionary containing trained model summary and metrics: model_name (str), n_estimators (int), max_depth (int or None), oob_r_squared (float), feature_importances (List[float]), num_training_samples (int), num_selected_factors (int).

**Raises:**

- ValueError: If there are no selected factors or if input datasets have mismatched indices or insufficient data for training.
- RuntimeError: If the random forest training process fails or OOB estimation is not available.
**Examples:**

```python
>>> # Assume factor_exposures is a DataFrame indexed by security-day,
>>> # selected_factors is a list of factor names to use as features,
>>> # merged_data contains joined cleaned data, and next_day_returns is aligned target.
>>> result = train_random_forest_model(factor_exposures, selected_factors, merged_data, next_day_returns)
>>> print(result['model_name'], result['oob_r_squared'], len(result['feature_importances']))
RandomForest_500trees 0.25 10
```

```python
>>> # Using a smaller factor subset
>>> result = train_random_forest_model(factor_exposures, ['momentum', 'value'], merged_data, next_day_returns)
>>> print(f"Model: {result['model_name']}, Trees: {result['n_estimators']}, Features: {result['num_selected_factors']}")
Model: RandomForest_500trees, Trees: 500, Features: 2
```

