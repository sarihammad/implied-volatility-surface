"""
Entry Point for Implied Volatility Surface Project

This script fetches option data, computes implied volatilities, and
plots the IV surface for a specified stock symbol.
"""

from src.fetcher import fetch_option_chain, fetch_current_price
from src.surface_builder import build_iv_surface
from src.plotter import plot_iv_surface


def main():
    symbol = "AAPL"
    print(f"Fetching data for {symbol}...")

    try:
        option_data = fetch_option_chain(symbol)
        spot_price = fetch_current_price(symbol)

        print("Building implied volatility surface...")
        strikes, expiries, ivs = build_iv_surface(option_data, spot_price)

        if not strikes:
            print("No valid option data found to compute surface.")
            return

        plot_iv_surface(strikes, expiries, ivs, title=f"{symbol} Implied Volatility Surface")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()