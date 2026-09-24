"""
analysis.py
Performs statistical analysis on JSE stock price data.
"""

import pandas as pd
import numpy as np


def calculate_daily_returns(df):
    """Calculate daily percentage returns for each stock."""
    return df.pct_change().dropna()


def calculate_cumulative_returns(returns):
    """Calculate cumulative returns from daily returns."""
    return (1 + returns).cumprod() - 1


def calculate_volatility(returns, window=30):
    """Calculate rolling 30-day annualised volatility."""
    return returns.rolling(window=window).std() * np.sqrt(252)


def calculate_correlation(returns):
    """Calculate correlation matrix between stocks."""
    return returns.corr()


def summary_statistics(returns):
    """Generate a summary table of key statistics."""
    stats = pd.DataFrame({
        'Mean Daily Return (%)': (returns.mean() * 100).round(3),
        'Volatility (Ann. %)': (returns.std() * np.sqrt(252) * 100).round(2),
        'Best Day (%)': (returns.max() * 100).round(2),
        'Worst Day (%)': (returns.min() * 100).round(2),
        'Sharpe Ratio': (
            (returns.mean() / returns.std()) * np.sqrt(252)
        ).round(3)
    })
    return stats