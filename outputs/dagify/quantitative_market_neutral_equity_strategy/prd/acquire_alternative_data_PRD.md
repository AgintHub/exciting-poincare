# acquire_alternative_data PRD

## Description
Download alternative data signals for the universe.


## Conceptual Info

This node is responsible for ingesting daily alternative data streams—such as news sentiment, search trends, ESG ratings, and analyst forecasts—for every security that passed the universe screening. It pulls the data from the providers identified in the preceding node, ensures a 10‑year historical window, and produces a concise summary of the download.

## Docstring

### Summary
Download daily alternative data signals for the screened security universe over the past decade.

### Parameters

- **security_ids** (List[str]): Identifiers of securities selected by the universe criteria.
- **data_sources** (List[str]): Provider names specified by identify_data_sources for alternative data.
- **data_fields** (List[str]): Fields requested from each provider (e.g., news_sentiment, google_trends).
- **start_date** (str): ISO 8601 date marking the beginning of the 10‑year coverage window.
- **end_date** (str): ISO 8601 date marking the end of the 10‑year coverage window.

### Returns

dict: Dictionary containing lists of identifiers, dates, sources, fields, and a summary statement.

### Raises

- ValueError: If no security IDs are provided or data_sources list is empty.
- RuntimeError: If a provider returns an error or fails to supply data for the requested period.

### Examples

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
