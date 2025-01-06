import matplotlib.pyplot as plt
import pandas as pd
import os

# Путь к папке для сохранения изображений
images_dir = "images"

# Создаем папку, если она не существует
os.makedirs(images_dir, exist_ok=True)


def notify_if_strong_fluctuations(data, threshold=1):
    """
    Функция для оповещения пользователя о сильных колебаниях цен.
    :param data: DataFrame
    :param threshold: Порог колебаний в % процентах
    :return: Возвращаем True, если колебания превышают заданный порог, иначе False.
    """

    min_price = data['Close'].min()
    max_price = data['Close'].max()

    # Расчёт колебания в процентах
    res = (max_price - min_price) / min_price * 100
    if res > threshold:
        return res
    else:
        return 0


def calculate_and_display_average_price(data):
    """
    Расчет среднего значения цены на закрытии сессии за заданный период.
    :param data: DataFrame
    :return: Возвращаем среднюю цену закрытия акций за заданный период.
    """
    return data["Close"].mean()


def create_and_save_plot(data, ticker, period, filename=None):
    plt.figure(figsize=(10, 6))

    if "Date" not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data["Close"].values, label="Close Price")
            plt.plot(dates, data["Moving_Average"].values, label="Moving Average")
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data["Date"]):
            data["Date"] = pd.to_datetime(data["Date"])
        plt.plot(data["Date"], data["Close"], label="Close Price")
        plt.plot(data["Date"], data["Moving_Average"], label="Moving Average")

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    filepath = os.path.join(images_dir, filename)

    plt.savefig(filepath)
    print(f"График сохранен как {filename}")
