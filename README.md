# Implied Volatility Surface Visualization

Calculates and visualizes the Implied Volatility (IV) Surface for a given stock using real options market data.

The IV surface is a 3D representation of how implied volatility changes with respect to Strike Price, Time to Expiration, Option Type (Call/Put). It's a valuable tool for options pricing, volatility modeling, and identifying market anomalies.

## Live Demo

https://implied-volatility-surface-visual.streamlit.app/

## Example Visualization

![Figure_1](https://github.com/user-attachments/assets/a4977eca-b348-4dd5-b593-0a62c99b92a9)

The plot shows implied volatility across different strikes and expiries for a selected stock, giving insight into volatility skew, smiles, and term structure.

## Features

- Fetches live option chain data with `yfinance`
- Calculates implied volatility using the Black-Scholes model
- Builds a clean surface data structure of IVs by strike & maturity
- Renders a 3D interactive plot using Plotly (via Streamlit)
- Modular, testable, and production-ready codebase

## How to Run 

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch the Streamlit app:

```bash
streamlit run app.py
```
