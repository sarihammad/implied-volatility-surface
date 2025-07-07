"""
Implied Volatility Calculation Module

This module provides functionality to calculate implied volatility
using the Black-Scholes option pricing model. It includes numerical
root-finding to invert the model and solve for implied volatility
from observed option market prices.
"""

import numpy as np
from scipy.stats import norm
from scipy.optimize import brentq


def black_scholes_price(S, K, T, r, sigma, option_type="call"):
    """
    Calculates the Black-Scholes option price.

    Args:
        S (float): Current price of the underlying asset.
        K (float): Strike price of the option.
        T (float): Time to expiration in years.
        r (float): Risk-free interest rate.
        sigma (float): Volatility of the underlying asset.
        option_type (str): 'call' or 'put'.

    Returns:
        float: Theoretical price of the option.
    """
    if T <= 0 or sigma <= 0 or S <= 0 or K <= 0:
        return 0.0

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")


def implied_volatility(market_price, S, K, T, r, option_type="call", tol=1e-5, max_iter=100):
    """
    Computes the implied volatility by inverting the Black-Scholes model.

    Args:
        market_price (float): Observed market price of the option.
        S (float): Current price of the underlying asset.
        K (float): Strike price of the option.
        T (float): Time to expiration in years.
        r (float): Risk-free interest rate.
        option_type (str): 'call' or 'put'.
        tol (float): Tolerance for root finding.
        max_iter (int): Maximum number of iterations.

    Returns:
        float: Implied volatility (sigma) as a decimal, or np.nan if not solvable.
    """
    if market_price <= 0 or S <= 0 or K <= 0 or T <= 0:
        return np.nan

    def objective_function(sigma):
        return black_scholes_price(S, K, T, r, sigma, option_type) - market_price

    try:
        return brentq(objective_function, 1e-6, 5.0, xtol=tol, maxiter=max_iter)
    except (ValueError, RuntimeError):
        return np.nan
