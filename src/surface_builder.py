"""
Implied Volatility Surface Builder Module

This module organizes raw option data into a structured format
for plotting the implied volatility surface. It extracts relevant
fields, computes time to expiration, and prepares a grid of strike,
maturity, and implied volatility values.
"""

from datetime import datetime
import numpy as np
from src.volatility import implied_volatility


def build_iv_surface(option_data, spot_price, risk_free_rate=0.01, option_type="call"):
    """
    Constructs the implied volatility surface grid.

    Args:
        option_data (list): List of dicts with 'expiry', 'calls' or 'puts' DataFrames.
        spot_price (float): Current price of the underlying asset.
        risk_free_rate (float): Risk-free interest rate.
        option_type (str): 'call' or 'put', determines which option DataFrame ("calls" or "puts") is used.

    Returns:
        tuple: (strikes, expiries, iv_values) as flat lists for 3D plotting.
    """
    strikes = []
    expiries = []
    iv_values = []

    for entry in option_data:
        expiry_str = entry["expiry"]
        options_df = entry["calls"] if option_type.lower() == "call" else entry["puts"]

        if options_df is None or options_df.empty:
            continue

        expiry_date = datetime.strptime(expiry_str, "%Y-%m-%d")
        T = (expiry_date - datetime.today()).days / 365.0
        if T <= 0:
            continue

        for _, row in options_df.iterrows():
            K = row["strike"]
            bid = row["bid"]
            ask = row["ask"]

            if not all(map(np.isreal, [K, bid, ask])):
                continue

            if bid > 0 and ask > 0:
                mid_price = (bid + ask) / 2.0
                iv = implied_volatility(mid_price, spot_price, K, T, risk_free_rate, option_type)
                if not np.isnan(iv):
                    strikes.append(K)
                    expiries.append(T)
                    iv_values.append(iv * 100)  # percent

    return strikes, expiries, iv_values