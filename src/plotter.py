"""
Implied Volatility Surface Plotter Module

This module handles 3D visualization of the implied volatility surface
using matplotlib. It takes strike prices, time to expiration, and
implied volatilities and renders a smooth surface plot.
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def plot_iv_surface(strikes, expiries, iv_values, title="Implied Volatility Surface"):
    """
    Plots the implied volatility surface using 3D trisurf.

    Args:
        strikes (list of float): Strike prices.
        expiries (list of float): Time to expiration in years.
        iv_values (list of float): Implied volatility values (in percent).
        title (str): Title of the plot.
    """
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_trisurf(strikes, expiries, iv_values, cmap='viridis', edgecolor='none', alpha=0.9)

    ax.set_title(title)
    ax.set_xlabel("Strike Price")
    ax.set_ylabel("Time to Expiration (Years)")
    ax.set_zlabel("Implied Volatility (%)")

    ax.view_init(elev=30, azim=135)
    plt.tight_layout()
    plt.show()