# select_significant_factors PRD

## Description
Choose the subset of factors that passed significance thresholds.


## Conceptual Info

This node filters factors based on statistical significance and positive predictive strength to identify which factors are meaningfully predictive and should be retained for subsequent modeling.

## Docstring

### Summary
Select factors with p-value < 0.05 and positive average t-statistic from factor performance results.

### Parameters

- **factor_names** (List[str]): List of factor names evaluated in the performance test.
- **avg_t_stats** (List[float]): Average t-statistics corresponding to each factor from the regressions.
- **p_values** (List[float]): P-values for each factor's performance coefficient, indicating statistical significance.

### Returns

dict: Dictionary with keys 'selected_factors' (list of factor names passing criteria), 'significant_factor_count' (count of these factors), and 'is_valid_selection' (boolean flag if valid selection achieved).

### Raises

- ValueError: If input lists (factor_names, avg_t_stats, p_values) are of unequal length.
- ValueError: If input lists are empty, making selection impossible.

### Examples

```python
>>> factor_names = ['Value', 'Momentum', 'Quality', 'Volatility']
>>> avg_t_stats = [2.5, -1.2, 3.1, 0.5]
>>> p_values = [0.01, 0.10, 0.03, 0.04]
>>> result = select_significant_factors(factor_names, avg_t_stats, p_values)
>>> print(result)
{'selected_factors': ['Value', 'Quality', 'Volatility'], 'significant_factor_count': 3, 'is_valid_selection': True}
```

```python
>>> factor_names = ['FactorA', 'FactorB']
>>> avg_t_stats = [-0.5, 1.0]
>>> p_values = [0.06, 0.06]
>>> result = select_significant_factors(factor_names, avg_t_stats, p_values)
>>> print(result)
{'selected_factors': [], 'significant_factor_count': 0, 'is_valid_selection': False}
```
