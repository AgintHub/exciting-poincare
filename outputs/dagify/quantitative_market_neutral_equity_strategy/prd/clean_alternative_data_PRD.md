# clean_alternative_data PRD

## Description
Standardize alternative data series, handling gaps and outliers.


## Conceptual Info

This node takes raw, possibly sparse and noisy alternative data (e.g., sentiment scores, trend indices) acquired from multiple providers, aligns it to the trading calendar, imputes missing observations, caps extreme values, and emits a concise report of the cleaning operation. It is a critical preprocessing step that ensures downstream models receive consistent, comparable inputs across all securities and dates.

## Docstring

### Summary
Clean and standardise alternative data for downstream factor modelling.

### Parameters

- **raw_data** (pd.DataFrame): DataFrame containing columns: ['security_id', 'date', 'field', 'value']. Each row represents a daily observation from an alternative data source.

### Returns

Dict[str, Union[int, str]]: Dictionary with keys 'total_records', 'filled_missing_days', 'excluded_records', and 'summary_statement' that describe the cleaning outcome.

### Raises

- ValueError: If raw_data is empty or does not contain the required columns.
- KeyError: If expected columns are missing from the input DataFrame.

### Examples

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
