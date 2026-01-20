# compute_factor_exposures PRD

## Description
Calculate the factor values for every security-day in the merged dataset.


## Conceptual Info

This node calculates factor exposures for a set of securities on each trading day using a merged dataset. It takes in a set of candidate factors and computes their values for every security-day, providing a description of each factor's calculation and the schema of the resulting factor columns.

## Docstring

### Summary
Compute numerical exposures of each security on each date for all candidate factors.

### Parameters

- **merged_data** (pd.DataFrame): Merged dataset containing price, fundamental, and alternative data for each security-day.
- **factor_candidates** (List[Factor]): List of candidate factors to be computed, each with a name and calculation method.

### Returns

dict: Dictionary containing the list of factor names, calculation descriptions, factor column schema, and total number of factor columns.

### Raises

- ValueError: If the merged data is empty or if no factor candidates are provided.

### Examples

```python
>>> merged_data = pd.DataFrame({'security_id': ['AAPL', 'GOOG'], 'date': ['2022-01-01', '2022-01-01'], 'price': [100.0, 2000.0]})
>>> factor_candidates = [Factor('book_to_price', 'Book-to-Price ratio')]
>>> result = compute_factor_exposures(merged_data, factor_candidates)
{'factor_names': ['book_to_price'], 'factor_calculation_descriptions': ['Book-to-Price ratio'], 'factor_column_schema': 'book_to_price: float, calculation: str', 'total_factor_columns': 1}
```
