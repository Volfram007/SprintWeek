import os
import pandas as pd
import yfinance as yf

# Путь к папке для сохранения загруженных данных об акциях
data_dir = "data"

# Создаем папку, если она не существует
os.makedirs(data_dir, exist_ok=True)

def export_data_to_csv(data, filepath):
    """
    Экспорт данных в csv
    """
    print(f">> Экспорт данных в файл, {filepath}")
    data.to_csv(filepath)


def fetch_stock_data(ticker, period="1mo", update=False):
    """
    Получение данных о тикерах за период и сохранение в csv
    :param ticker: торговый тикер
    :param period: период
    :param update: обновление локального файла данных
    """
    file_name = f"{ticker}_{period}.csv"
    filepath = os.path.join(data_dir, file_name)

    if os.path.exists(filepath) and not update:
        print(f">> Используем данные из локального файла.")
        data = pd.read_csv(filepath)
    else:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period)
        export_data_to_csv(data, filepath)
    return data


def add_moving_average(data, window_size=5):
    data["Moving_Average"] = data["Close"].rolling(window=window_size).mean()
    return data
