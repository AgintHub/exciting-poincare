# clean_price_data PRD

## Description
Standardize and adjust price data, handling missing values and corporate actions.


## Conceptual Info

The clean_price_data node takes raw price data, cleans and standardizes it by adjusting for splits and dividends, aligning dates, handling missing values, and ensuring consistent column names.

## Docstring

### Summary
Cleans and standardizes price data by adjusting for corporate actions, handling missing values, and ensuring consistent column names.

### Parameters

- **price_data** (DataFrame): Raw price dataset to be cleaned

### Returns

dict: Dictionary containing cleaned_rows, removed_rows, cleaned_date_range, columns_cleaned, and is_clean

### Raises

- ValueError: If the input dataset is empty or contains invalid data

### Examples

```python
>>> import pandas as pd
>>> data = pd.DataFrame({'date': ['2022-01-01', '2022-01-02'], 'close': [100, 120]})
>>> cleaned_data = clean_price_data(data)
>>> print(cleaned_data)
{'cleaned_rows': 2, 'removed_rows': 0, 'cleaned_date_range': '2022-01-01 to 2022-01-02', 'columns_cleaned': ['date', 'close'], 'is_clean': True}
```
