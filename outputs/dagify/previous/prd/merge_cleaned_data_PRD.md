# merge_cleaned_data PRD

## Description
Combine cleaned price, fundamental, and alternative data into a single panel dataset.


## Conceptual Info

This node consolidates three cleaned datasets—price data, fundamental data, and alternative data—by joining them on the security identifier and date fields. The output is a comprehensive panel dataset indexed by security and trading day, containing combined features from all three sources, suitable for downstream factor computation and modeling.

## Docstring

### Summary
Merge cleaned price, fundamental, and alternative datasets on security identifier and date to produce a unified panel dataset with combined features.

### Parameters

- **price_data** (DataFrame): Cleaned price data including daily price and corporate action adjusted fields, indexed or containing security identifier and date.
- **fundamental_data** (DataFrame): Cleaned fundamental accounting data standardized to consistent units, aligned to calendar dates, indexed or containing security identifier and date.
- **alternative_data** (DataFrame): Cleaned alternative data series with aligned timestamps and winsorized values, indexed or containing security identifier and date.

### Returns

dict: A dictionary containing: total_rows (int), total_columns (int), column_names (List[str]), is_successful (bool), and merge_summary (str), summarizing the resulting merged dataset.

### Raises

- ValueError: If any input dataset is empty or missing required columns such as 'security_id' or 'date'.
- MergeError: If the join operation fails due to incompatible indices or unmatched key columns.

### Examples

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
