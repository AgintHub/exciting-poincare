# identify_data_sources PRD

## Description
Identify the data providers and types needed for price, fundamentals, and alternative signals.


## Conceptual Info

This node identifies and classifies the essential data providers and the specific data fields needed to support a market-neutral equity strategy. It segments required inputs into three categories—market price data, fundamental financial data, and alternative data (such as sentiment and ESG metrics)—providing clarity and structure to data acquisition processes downstream. The output guides subsequent data retrieval and integration steps.

## Docstring

### Summary
Identify and enumerate data providers along with required data fields for market price, fundamental financial, and alternative data signals used in the quantitative strategy.

### Returns

dict: Dictionary containing lists of data source provider names and corresponding data fields for three categories: market price data, fundamental data, and alternative data.

### Raises

- ValueError: If no valid data sources or fields are identified for one or more categories.

### Examples

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
