import yfinance as yf
import talib as ta
import pandas as pd
import numpy as np
import plotly.express as px
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns


class FinancialAnalyzer:
    def __init__(self, stock_info):
        self.stock_info = stock_info  # List of tuples (ticker, file_path)
        self.ticker_data = {}  # Dictionary to hold Ticker instances

    def load_stock_data(self, ticker):
        """Load stock data from CSV files."""
        for stock_name, file_path in self.stock_info:
            if stock_name == ticker:
                return pd.read_csv(file_path, index_col='Date', parse_dates=True)

    def calculate_moving_average(self, data, window_size):
        return ta.SMA(data['Close'], timeperiod=window_size)

    def calculate_technical_indicators(self, data):
        # Calculate various technical indicators
        data['SMA'] = self.calculate_moving_average(data, 20)
        data['RSI'] = ta.RSI(data['Close'], timeperiod=14)
        data['EMA'] = ta.EMA(data['Close'], timeperiod=20)
        macd, macd_signal, _ = ta.MACD(data['Close'])
        data['MACD'] = macd
        data['MACD_Signal'] = macd_signal
        return data

    def plot_stock_data(self, data):
        """Plot stock price with moving average."""
        # Drop rows with NaN values in 'Close' or 'SMA'
        data = data.dropna(subset=['Close', 'SMA'])
        
        # Create a line plot for 'Close' and 'SMA' using Plotly Express
        fig = px.line(data, x=data.index, y=['Close', 'SMA'], title='Stock Price with Moving Average')
        # Display the plot
        fig.show()

    def plot_rsi(self, data):
        """Plot the Relative Strength Index (RSI)."""
        # Drop rows with NaN values in 'RSI'
        data = data.dropna(subset=['RSI'])
        
        # Create a line plot for 'RSI'
        fig = px.line(data, x=data.index, y='RSI', title='Relative Strength Index (RSI)')
        # Display the plot
        fig.show()

    def plot_ema(self, data):
        """Plot stock price with Exponential Moving Average (EMA)."""
        # Drop rows with NaN values in 'Close' or 'EMA'
        data = data.dropna(subset=['Close', 'EMA'])

        # Create a line plot for 'Close' and 'EMA'
        fig = px.line(data, x=data.index, y=['Close', 'EMA'], title='Stock Price with Exponential Moving Average')
        # Display the plot
        fig.show()

    def plot_macd(self, data):
        """Plot Moving Average Convergence Divergence (MACD)."""
        # Drop rows with NaN values in 'MACD' or 'MACD_Signal'
        data = data.dropna(subset=['MACD', 'MACD_Signal'])

        # Create a line plot for 'MACD' and 'MACD_Signal'
        fig = px.line(data, x=data.index, y=['MACD', 'MACD_Signal'], title='Moving Average Convergence Divergence (MACD)')
        # Display the plot
        fig.show()

    def get_financial_metrics(self, stock_name):
        """Retrieve financial metrics using yfinance for a specific stock."""
        ticker = yf.Ticker(stock_name)  # Create a Ticker object with yfinance
        metrics = {
            'P/E Ratio': ticker.info.get('forwardPE', 'N/A'),
            'Market Cap': ticker.info.get('marketCap', 'N/A'),
            'Dividend Yield': ticker.info.get('dividendYield', 'N/A'),
            'Beta': ticker.info.get('beta', 'N/A'),
            'EPS': ticker.info.get('trailingEps', 'N/A'),
            'Revenue': ticker.info.get('totalRevenue', 'N/A'),
        }
        return metrics

