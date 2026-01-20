# clean_fundamental_data PRD

## Description
Standardize fundamental data, handling missing values and restating periods.


## Conceptual Info

This node transforms raw fundamental accounting data into a clean, analysis‑ready table. It unifies units (e.g., millions vs billions), aligns quarterly/annual reports to fixed calendar dates (e.g., Q1 2023 → 2023-03-31), fills gaps using linear interpolation or flags them, and removes extreme outliers (beyond 5 σ) that could distort factor construction.

## Docstring

### Summary
Clean raw fundamental accounting data by standardizing units, aligning reporting periods, handling missing values, and removing outliers.

### Parameters

- **raw_fundamental_df** (pd.DataFrame): DataFrame returned from acquire_fundamental_data, containing columns such as 'ticker', 'report_date', 'eps', 'book_value', 'cash_flow', 'leverage', 'dividend_yield', etc., possibly in mixed units and with missing values.

### Returns

dict: Dictionary with the following keys:
- cleaned_record_count (int)
- missing_value_records (int)
- missing_value_flagged (bool)
- outlier_removed_count (int)
- unit_consistency_flag (bool)
- reporting_period_aligned (bool)

### Raises

- ValueError: If raw_fundamental_df is empty or missing required columns.
- KeyError: If expected metric columns are not found in the input DataFrame.

### Examples

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
