import data_download as dd
import data_plotting as dplt


def input_text(text: str, default_text: str):
    """
    Функция ввода команд и проверки выхода из программы
    :param text: текст для описания ввода команды
    :param default_text: команда по умолчанию
    """
    result = input(text).strip() or default_text
    if ["exit", "q", "quit"].count(result.lower()) > 0:
        exit()
    return result


def main():
    print(f"Выход из программы: exit, q, quit.\n")

    ticker = input_text("Введите тикер акции (дефолт: «AAPL» для Apple Inc): ", "AAPL")
    period = input_text("Введите период для данных (дефолт: 1mo): ", "1mo")

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)

    # Вывод средней цены акции на закрытии
    average_price = dplt.calculate_and_display_average_price(stock_data)
    print(
        f"Средняя цена акций {ticker} за период {period} составляет {round(average_price, 3)}"
    )

    # Вывод превышения колебаний цены
    threshold = float(input_text("Введите порог % колебания цены в данный период (дефолт, 5): ", "5"))

    fluctuations = dplt.notify_if_strong_fluctuations(stock_data, threshold)

    if fluctuations > 0:
        print(f"Выявлено колебание цены до {round(fluctuations, 2)}% в {ticker} за период {period}")


if __name__ == "__main__":
    print(f"Добро пожаловать в инструмент получения и построения графиков биржевых данных.\n"
          f"Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).\n"
          f"Общие периоды времени для данных о запасах включают: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, с начала года, макс.\n"
          )

    while True:
        main()
