# Серия учебных проектов стажировки

# Sprint 1. Этот проект предназначен для загрузки исторических данных об акциях и их визуализации.
* Задачи:
    * Реализовать функцию calculate_and_display_average_price(data): которая вычисляет и выводит среднюю цену закрытия акций за заданный период.
    * Реализовать функцию notify_if_strong_fluctuations(data, threshold): уведомление если цена колебалась более чем на заданный процент за заданный период.
    * Реализовать функцию export_data_to_csv(data, filepath), которая позволяет сохранять загруженные данные об акциях в CSV файл.
    * Реализовать функцию для расчёта и отображения на графике индикатора RSI.

*data_download.py*:
- Отвечает за загрузку и сохранение данных об акциях.
- Содержит функции для извлечения данных об акциях из интернета и экспорта загруженных данных в файл формата CSV.
- Содержит функцию расчёта индикатора RSI

*data_plotting.py*:
- Содержит функцию для создания и сохранения графиков цен закрытия и скользящих средних.
- Расчет среднего значения цены на закрытии сессии за заданный период.
- Функция для оповещения пользователя о сильных колебаниях цен.

*main.py*:
- Является точкой входа в программу.
- Запрашивает у пользователя тикер акции и временной период, загружает данные, обрабатывает их и выводит результаты.

# <a href="Init.md">🛠️ **Установка и настройка**</a>