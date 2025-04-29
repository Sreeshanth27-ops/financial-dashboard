import yfinance as yf
import numpy as np


def get_portfolio_metrics(tickers, weights):
    try:
        data = yf.download(tickers, period = '1y')['Adj Close']
        daily_returns = data.pct_change().dropna()

        mean_returns = daily_returns.mean()
        cov_matrix = daily_returns.cov()

        portfolio_return = np.sum(mean_returns * weights) * 252
        portfolio_std_dev = np.sqrt(np.dot(weights, cov_matrix, weights))

        return {
            "expected_annual_return": round(portfolio_return, 4),
            "annual_volatility": round(portfolio_std_dev, 4),
        }
    except Exception as e:
        return {"error": str(e)}
 