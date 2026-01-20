# define_factor_candidates PRD

## Description
List the quantitative factors to be evaluated for predictive power.


## Conceptual Info

Defines and compiles a comprehensive list of quantitative factor candidates to be evaluated for their predictive power in the market-neutral equity strategy. This includes traditional value, momentum, and quality factors, as well as innovative ones such as ESG, sentiment, earnings revisions, and composite scores. Each factor is named and briefly defined to support subsequent factor exposure computation and model training.

## Docstring

### Summary
Generate candidate quantitative factor names and their brief definitions for evaluation in a market-neutral equity strategy.

### Parameters

- **objectives** (List[str]): High-level investment objectives of the market-neutral equity strategy that guide the factor selection scope and relevance.

### Returns

Tuple[List[str], List[str]]: Two parallel lists containing factor names and their corresponding short definitions for use in factor exposure computation and model development.

### Raises

- ValueError: If the provided objectives list is empty or None, factor candidates cannot be aligned properly.

### Examples

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
