"""
fetch_data.py
Downloads historical stock data for JSE-listed companies using yfinance.
"""

import yfinance as yf
import pandas as pd
import os

# JSE-listed stocks — .JO suffix tells yfinance to pull from the JSE
JSE_TICKERS = {
    'Naspers': 'NPN.JO',
    'Standard Bank': 'SBK.JO',
    'FirstRand': 'FSR.JO',
    'Sasol': 'SOL.JO',
    'MTN Group': 'MTN.JO',
    'Anglo American': 'AGL.JO'
}

START_DATE = '2020-01-01'
END_DATE = '2024-12-31'
DATA_PATH = 'data/jse_stocks.csv'


def fetch_stock_data():
    """Download closing prices for all JSE tickers."""
    os.makedirs('data', exist_ok=True)

    all_data = {}

    for name, ticker in JSE_TICKERS.items():
        print(f"Fetching {name} ({ticker})...")
        try:
            df = yf.download(ticker, start=START_DATE, end=END_DATE, progress=False)
            if not df.empty:
                all_data[name] = df['Close'].squeeze()
            else:
                print(f"  Warning: No data returned for {ticker}")
        except Exception as e:
            print(f"  Error fetching {ticker}: {e}")

    combined = pd.DataFrame(all_data)
    combined.index = pd.to_datetime(combined.index)
    combined.dropna(how='all', inplace=True)
    combined.to_csv(DATA_PATH)

    print(f"\nData saved to {DATA_PATH}")
    print(f"Shape: {combined.shape}")
    return combined


def load_data():
    """Load saved stock data from CSV."""
    if not os.path.exists(DATA_PATH):
        print("Data not found. Fetching now...")
        return fetch_stock_data()
    return pd.read_csv(DATA_PATH, index_col=0, parse_dates=True)