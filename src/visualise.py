"""
visualise.py
Generates and saves visualisations for JSE stock analysis.
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import os

os.makedirs('outputs', exist_ok=True)
sns.set_theme(style='whitegrid')
COLORS = ['#003f88', '#e63946', '#2a9d8f', '#e9c46a', '#f4a261', '#6a4c93']


def plot_stock_prices(df):
    """Plot historical closing prices for all stocks."""
    fig, ax = plt.subplots(figsize=(14, 6))

    for i, col in enumerate(df.columns):
        ax.plot(df.index, df[col], label=col, color=COLORS[i % len(COLORS)], linewidth=1.5)

    ax.set_title('JSE Stock Closing Prices (2020–2024)', fontsize=14, fontweight='bold')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price (ZAR)')
    ax.legend(loc='upper left')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.tight_layout()
    plt.savefig('outputs/stock_prices.png', dpi=150)
    print("Saved: outputs/stock_prices.png")
    plt.show()


def plot_cumulative_returns(cum_returns):
    """Plot cumulative returns for all stocks."""
    fig, ax = plt.subplots(figsize=(14, 6))

    for i, col in enumerate(cum_returns.columns):
        ax.plot(cum_returns.index, cum_returns[col] * 100,
                label=col, color=COLORS[i % len(COLORS)], linewidth=1.5)

    ax.axhline(0, color='black', linestyle='--', linewidth=0.8)
    ax.set_title('Cumulative Returns — JSE Stocks (2020–2024)', fontsize=14, fontweight='bold')
    ax.set_xlabel('Date')
    ax.set_ylabel('Cumulative Return (%)')
    ax.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig('outputs/cumulative_returns.png', dpi=150)
    print("Saved: outputs/cumulative_returns.png")
    plt.show()


def plot_volatility(volatility):
    """Plot rolling 30-day annualised volatility."""
    fig, ax = plt.subplots(figsize=(14, 6))

    for i, col in enumerate(volatility.columns):
        ax.plot(volatility.index, volatility[col] * 100,
                label=col, color=COLORS[i % len(COLORS)], linewidth=1.5)

    ax.set_title('30-Day Rolling Volatility — JSE Stocks', fontsize=14, fontweight='bold')
    ax.set_xlabel('Date')
    ax.set_ylabel('Annualised Volatility (%)')
    ax.legend(loc='upper right')
    plt.tight_layout()
    plt.savefig('outputs/volatility.png', dpi=150)
    print("Saved: outputs/volatility.png")
    plt.show()


def plot_correlation_heatmap(corr_matrix):
    """Plot a correlation heatmap between stocks."""
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt='.2f',
        cmap='coolwarm',
        center=0,
        linewidths=0.5,
        ax=ax
    )
    ax.set_title('Stock Return Correlation Matrix', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('outputs/correlation_heatmap.png', dpi=150)
    print("Saved: outputs/correlation_heatmap.png")
    plt.show()


def plot_return_distribution(returns):
    """Plot daily return distributions for each stock."""
    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    axes = axes.flatten()

    for i, col in enumerate(returns.columns):
        sns.histplot(returns[col] * 100, bins=50, kde=True,
                     ax=axes[i], color=COLORS[i % len(COLORS)])
        axes[i].set_title(col, fontweight='bold')
        axes[i].set_xlabel('Daily Return (%)')
        axes[i].set_ylabel('Frequency')

    plt.suptitle('Daily Return Distributions — JSE Stocks',
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('outputs/return_distributions.png', dpi=150, bbox_inches='tight')
    print("Saved: outputs/return_distributions.png")
    plt.show()