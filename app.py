"""
Streamlit App for Implied Volatility Surface Visualization

This app allows users to select a stock symbol and visualize its
implied volatility surface using live option data.
"""

import streamlit as st
from src.fetcher import fetch_option_chain, fetch_current_price
from src.surface_builder import build_iv_surface
from src.plotter import plot_iv_surface
import plotly.graph_objects as go


def main():
    st.title("Implied Volatility Surface")

    symbol = st.text_input("Enter stock ticker symbol", value="AAPL").upper()
    if st.button("Generate IV Surface"):

        with st.spinner("Fetching option chain and computing IVs..."):
            try:
                option_data = fetch_option_chain(symbol)
                spot_price = fetch_current_price(symbol)
                strikes, expiries, ivs = build_iv_surface(option_data, spot_price)

                if not strikes:
                    st.warning("No valid option data found to compute surface.")
                    return

                fig = go.Figure(data=[go.Mesh3d(
                    x=strikes,
                    y=expiries,
                    z=ivs,
                    opacity=0.7,
                    colorscale='Viridis',
                    intensity=ivs,
                    showscale=True
                )])

                fig.update_layout(
                    title=f"{symbol} Implied Volatility Surface",
                    scene=dict(
                        xaxis=dict(title=dict(text='Strike Price', font=dict(color='black')), tickfont=dict(color='black')),
                        yaxis=dict(title=dict(text='Time to Expiration (Years)', font=dict(color='black')), tickfont=dict(color='black')),
                        zaxis=dict(title=dict(text='Implied Volatility (%)', font=dict(color='black')), tickfont=dict(color='black')),
                        bgcolor='white'
                    ),
                    margin=dict(l=0, r=0, b=0, t=40),
                    paper_bgcolor='white',
                    font=dict(color='black')
                )

                st.plotly_chart(fig, use_container_width=True)

            except Exception as e:
                st.error(f"Error: {e}")


if __name__ == "__main__":
    main()
