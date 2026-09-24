# JSE Stock Market Analysis

A Python-based analysis of Johannesburg Stock Exchange (JSE) listed companies,
covering historical prices, returns, volatility, and correlations from 2020 to 2024.

## Companies Analysed
| Company | Ticker |
|---|---|
| Naspers | NPN.JO |
| Standard Bank | SBK.JO |
| FirstRand | FSR.JO |
| Sasol | SOL.JO |
| MTN Group | MTN.JO |
| Anglo American | AGL.JO |

## Features
- Automatic data download via yfinance API
- Daily and cumulative return calculations
- Rolling 30-day annualised volatility
- Sharpe Ratio and summary statistics
- Correlation matrix between stocks
- 5 publication-quality charts saved to outputs/

## Output Charts
- Historical closing prices
- Cumulative returns (2020–2024)
- Rolling volatility
- Correlation heatmap
- Daily return distributions

## How to Run
1. Clone the repository:
```bash
   git clone https://github.com/LoloM-19/jse-stock-analysis.git
   cd jse-stock-analysis
```
2. Install dependencies:
```bash
   pip install -r requirements.txt
```
3. Run the analysis:
```bash
   python main.py
```

## Tech Stack
Python | yfinance | pandas | matplotlib | seaborn | numpy