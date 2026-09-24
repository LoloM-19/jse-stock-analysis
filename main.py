"""
main.py
Entry point for JSE Stock Market Analysis.
"""

from src.fetch_data import load_data
from src.analysis import (
    calculate_daily_returns,
    calculate_cumulative_returns,
    calculate_volatility,
    calculate_correlation,
    summary_statistics
)
from src.visualise import (
    plot_stock_prices,
    plot_cumulative_returns,
    plot_volatility,
    plot_correlation_heatmap,
    plot_return_distribution
)


def main():
    print("=" * 55)
    print("   JSE Stock Market Analysis")
    print("=" * 55)

    # Step 1: Load data
    print("\n[Step 1] Loading stock data...")
    df = load_data()
    print(df.tail())

    # Step 2: Analysis
    print("\n[Step 2] Running analysis...")
    returns = calculate_daily_returns(df)
    cum_returns = calculate_cumulative_returns(returns)
    volatility = calculate_volatility(returns)
    corr_matrix = calculate_correlation(returns)

    print("\nSummary Statistics:")
    print(summary_statistics(returns).to_string())

    # Step 3: Visualisations
    print("\n[Step 3] Generating charts...")
    plot_stock_prices(df)
    plot_cumulative_returns(cum_returns)
    plot_volatility(volatility)
    plot_correlation_heatmap(corr_matrix)
    plot_return_distribution(returns)

    print("\n" + "=" * 55)
    print("   Analysis complete! Check outputs/ folder.")
    print("=" * 55)


if __name__ == "__main__":
    main()