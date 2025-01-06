import os
import pandas as pd
import yfinance as yf


def fetch_stock_data(ticker, period="1mo", filename="data.csv"):
    if os.path.exists(f"{ticker}_{period}_" + filename):
        print(f"Используем данные из локального файла.")
        data = pd.read_csv(f"{ticker}_{period}_" + filename)
    else:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period)
        data.to_csv(f"{ticker}_{period}_" + filename)
    return data


def add_moving_average(data, window_size=5):
    data["Moving_Average"] = data["Close"].rolling(window=window_size).mean()
    return data
