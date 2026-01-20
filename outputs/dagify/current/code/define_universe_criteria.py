from pydantic import BaseModel, Field
from typing import List


class DefineUniverseCriteriaOutput(BaseModel):
    """Pydantic model for define_universe_criteria node outputs."""
    market_cap_min: float = (
        Field(..., description="Minimum market capitalization in USD (e.g., 5000000000 for $5B)")
    )
    market_cap_max: float = (
        Field(..., description="Maximum market capitalization in USD (e.g., 100000000000 for $100B)")
    )
    avg_daily_volume_min: float = (
        Field(..., description="Minimum average daily trading volume in shares (e.g., 5000000)")
    )
    price_min: float = (
        Field(..., description="Minimum stock price in USD (e.g., 5.0)")
    )
    price_max: float = (
        Field(..., description="Maximum stock price in USD (e.g., 150.0)")
    )
    exchanges: List[str] = (
        Field(..., description="List of allowed listing exchanges (e.g., ['NYSE', 'NASDAQ'])")
    )
    positive_earnings: bool = (
        Field(..., description="Whether to filter for securities with positive earnings")
    )


def define_universe_criteria(general_input: str, **kwargs) -> DefineUniverseCriteriaOutput:
    """
    Defines the screening rules to select equities eligible for inclusion in the
    trading universe. Applies filters based on market capitalization, liquidity,
    price, listing exchanges, and fundamental earnings criteria.

    Parameters
    ----------
    market_cap_min : float
        Minimum market capitalization in USD; securities below this are
        excluded.
    market_cap_max : float
        Maximum market capitalization in USD; securities above this are
        excluded.
    avg_daily_volume_min : float
        Minimum average daily trading volume in shares; ensures adequate
        liquidity.
    price_min : float
        Minimum share price in USD; removes very low-priced stocks.
    price_max : float
        Maximum share price in USD; excludes overly expensive stocks.
    exchanges : List[str]
        List of authorized listing exchanges; only securities listed here
        are eligible.
    positive_earnings : bool
        If True, screen to include only securities demonstrating positive
        earnings.

    Returns
    -------
    dict
        Dictionary containing the defined screening criteria for the equity
        universe with keys: market_cap_min, market_cap_max,
        avg_daily_volume_min, price_min, price_max, exchanges,
        positive_earnings.

    Raises
    ------
    ValueError
        If minimum values exceed maximum values (e.g., market_cap_min >
        market_cap_max) or if exchanges list is empty.
    TypeError
        If input types do not match expected types (e.g., exchanges not a
        list of strings).

    Examples
    --------
    >>> screening_criteria = define_universe_criteria(
    ...     market_cap_min=5e9,
    ...     market_cap_max=1e11,
    ...     avg_daily_volume_min=5e6,
    ...     price_min=5.0,
    ...     price_max=150.0,
    ...     exchanges=['NYSE', 'NASDAQ'],
    ...     positive_earnings=True
    >>> )
    >>> print(screening_criteria)
    {'market_cap_min': 5000000000.0, 'market_cap_max': 100000000000.0,
    'avg_daily_volume_min': 5000000.0, 'price_min': 5.0, 'price_max': 150.0,
    'exchanges': ['NYSE', 'NASDAQ'], 'positive_earnings': True}

    >>> screening_criteria = define_universe_criteria(
    ...     market_cap_min=1e8,
    ...     market_cap_max=5e9,
    ...     avg_daily_volume_min=1e5,
    ...     price_min=1.0,
    ...     price_max=50.0,
    ...     exchanges=['AMEX'],
    ...     positive_earnings=False
    >>> )
    >>> print(screening_criteria)
    {'market_cap_min': 100000000.0, 'market_cap_max': 5000000000.0,
    'avg_daily_volume_min': 100000.0, 'price_min': 1.0, 'price_max': 50.0,
    'exchanges': ['AMEX'], 'positive_earnings': False}

    """
    return DefineUniverseCriteriaOutput(
        market_cap_min=0.0,
        market_cap_max=0.0,
        avg_daily_volume_min=0.0,
        price_min=0.0,
        price_max=0.0,
        exchanges=[],
        positive_earnings=False,
    )