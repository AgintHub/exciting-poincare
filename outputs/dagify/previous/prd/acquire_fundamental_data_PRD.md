# acquire_fundamental_data PRD

## Description
Download historical fundamental accounting data for the universe.


## Conceptual Info

This node is responsible for downloading historical fundamental accounting data for the specified universe of securities. It takes the identified fundamental data providers and the defined universe criteria as inputs and returns the retrieved fundamental data fields, data coverage, number of securities, and data retrieval status.

## Docstring

### Summary
Downloads historical fundamental accounting data for the specified universe of securities.

### Parameters

- **data_providers** (List[str]): List of fundamental data providers
- **universe_criteria** (dict): Dictionary containing the universe criteria (e.g., market cap, liquidity, price range)

### Returns

dict: Dictionary containing the retrieved fundamental data fields, data coverage, number of securities, and data retrieval status

### Raises

- ValueError: If the data providers or universe criteria are invalid

### Examples

```python
>>> data_providers = ['Yahoo Finance', 'Quandl']
>>> universe_criteria = {'market_cap': 1000000000, 'liquidity': 1000000}
>>> result = acquire_fundamental_data(data_providers, universe_criteria)
{'fundamental_data_fields': ['earnings_per_share', 'book_value', 'cash_flow'], 'data_coverage': '10-year horizon, quarterly and annual data', 'number_of_securities': 100, 'data_retrieval_status': True}
```
