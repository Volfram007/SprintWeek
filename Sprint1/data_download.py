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
        data = calc_rsi(data, 5)
        export_data_to_csv(data, filepath)
    return data


def calc_rsi(data, period):
    """
    Функция рассчитывает и возвращает RSI, добавляя его к данным акций.
    :param data: DataFrame
    :param period: Минимальный временной интервал для расчёта
    :return: Функция добавляет столбец RSI в DataFrame
    """
    close_delta = data['Close'].diff()

    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)

    avg_up = up.rolling(window=period, min_periods=period).mean()
    avg_down = down.rolling(window=period, min_periods=period).mean()

    rsi = avg_up / avg_down
    rsi = 100 - (100 / (1 + rsi))
    data["RSI"] = rsi
    return data


def add_moving_average(data, window_size=5):
    data["Moving_Average"] = data["Close"].rolling(window=window_size).mean()
    return data
