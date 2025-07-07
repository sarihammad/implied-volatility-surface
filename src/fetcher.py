"""
Option Chain Data Fetcher Module

This module provides functionality to fetch option chain data
for a given stock symbol using the yfinance library. It retrieves
all available expiration dates and the corresponding call and put
options data for further processing.
"""

import yfinance as yf
from datetime import datetime


def fetch_option_chain(symbol, max_expiries=5):
    """
    Fetches the option chain for a given symbol across multiple expiration dates.

    Args:
        symbol (str): Ticker symbol of the underlying asset (e.g., 'AAPL').
        max_expiries (int): Maximum number of expiration dates to fetch.

    Returns:
        list: A list of dictionaries with call and put options for each expiry.
    """
    ticker = yf.Ticker(symbol)
    expiry_dates = ticker.options[:max_expiries]
    option_data = []

    for expiry in expiry_dates:
        try:
            chain = ticker.option_chain(expiry)
            calls = chain.calls
            puts = chain.puts
            option_data.append({
                "expiry": expiry,
                "calls": calls,
                "puts": puts
            })
        except Exception as e:
            print(f"Failed to fetch options for {expiry}: {e}")

    return option_data


def fetch_current_price(symbol):
    """
    Fetches the current closing price of the underlying asset.

    Args:
        symbol (str): Ticker symbol of the asset.

    Returns:
        float: Latest closing price.
    """
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period="1d")
    if not hist.empty:
        return hist["Close"].iloc[-1]
    else:
        raise ValueError(f"Could not fetch price for symbol: {symbol}")
