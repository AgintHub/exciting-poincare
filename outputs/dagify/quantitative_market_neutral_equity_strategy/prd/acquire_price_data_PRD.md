# acquire_price_data PRD

## Description
Download historical price data for the screened equity universe.


## Conceptual Info

The acquire_price_data node fetches a complete 10‑year daily price history for every security that passes the universe screening rules. It pulls standard OHLCV fields along with corporate actions and packages the results into a lightweight JSON payload for downstream cleaning, cost modeling, and back‑testing.

## Docstring

### Summary
Retrieve 10‑year daily market price history for the screened equity universe.

### Parameters

- **price_sources** (List[str]): List of market‑price data provider names returned by identify_data_sources.
- **fields** (List[str]): List of price fields to request from each provider (e.g., ['adjusted_close', 'open', 'high', 'low', 'volume', 'split_factor']).
- **universe** (Dict[str, Any]): Dictionary containing universe screening criteria returned by define_universe_criteria.
- **start_date** (str): Start of the 10‑year period to download (ISO format).
- **end_date** (str): End of the 10‑year period to download (ISO format).

### Returns

Dict[str, Any]: A dictionary matching the output_structure, containing metadata and a summary statement.

### Raises

- ValueError: If any required input list is empty or the date range is invalid.
- ConnectionError: If a data provider cannot be reached or returns an authentication error.
- RuntimeError: If the number of securities returned is zero, indicating a mismatch between universe criteria and available data.

### Examples

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
