# define_market_neutral_objectives PRD

## Description
Specify the quantitative criteria that enforce market neutrality for the equity portfolio.


## Conceptual Info

This node defines the market neutrality objectives for an equity portfolio, specifying quantitative criteria to ensure the portfolio remains neutral to various market factors.

## Docstring

### Summary
Define market neutral objectives for an equity portfolio.

### Parameters

- **strategy** (str): The investment strategy for which market neutrality is required.

### Returns

List[str]: A list of bullet points describing the market neutrality criteria, and a boolean indicating if the criteria are valid.

### Raises

- ValueError: If the neutrality criteria are not provided.

### Examples

```python
>>> define_market_neutral_objectives(strategy='market_neutral_equity')
['Beta exposure = 0', 'Dollar exposure = 0', 'Sector neutrality'] True
```
