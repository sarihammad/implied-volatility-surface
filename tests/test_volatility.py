import pytest
import numpy as np
from src.volatility import black_scholes_price, implied_volatility

def test_black_scholes_call_price():
    S = 100  # spot price
    K = 100  # strike price
    T = 1    # time to expiration (1 year)
    r = 0.05 # risk-free rate
    sigma = 0.2  # volatility

    price = black_scholes_price(S, K, T, r, sigma, option_type="call")
    assert isinstance(price, float)
    assert price > 0

def test_black_scholes_put_price():
    S = 100
    K = 100
    T = 1
    r = 0.05
    sigma = 0.2

    price = black_scholes_price(S, K, T, r, sigma, option_type="put")
    assert isinstance(price, float)
    assert price > 0

def test_implied_volatility_matches_input():
    S = 100
    K = 100
    T = 1
    r = 0.05
    true_sigma = 0.25
    option_type = "call"

    market_price = black_scholes_price(S, K, T, r, true_sigma, option_type)
    computed_iv = implied_volatility(market_price, S, K, T, r, option_type)

    assert isinstance(computed_iv, float)
    assert abs(computed_iv - true_sigma) < 1e-3

def test_implied_volatility_invalid_input():
    iv = implied_volatility(-1, 100, 100, 1, 0.05, "call")
    assert np.isnan(iv)