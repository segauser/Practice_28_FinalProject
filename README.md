## Тестирование UI, для интернет-магазина https://www.labirint.ru/

#### Тестируем основной функционал: поиск, понравившиеся товары, корзину.
#### Тестируем отображение контента на странице сайта, ссылки на актуальные страницы
#### Тестирование осуществляется в рамках учебного проекта.
#### Главная цель тестирования - демонстрация умения применять инструменты автоматизированного тестирования.

Для тестирования необходим:
----------------

1) #### Импорт зависимостей из requirements.txt:

    ```bash
    pip install -r requirements
    ```

2) #### Загрузить Selenium WebDriver from https://chromedriver.chromium.org/downloads (выбрать версию совместимую с вашим браузером)

3) #### Команда для запуска тестов:

    ```bash
    python -m pytest -v --driver chrome --driver-path chromedriver.exe tests/test_labirint.py
    ```
Для просмотра отчёта allure:
-------------
1. #### Установить фреймворк allure для своей операционной системы https://docs.qameta.io/allure-report/
2. #### Команда для запуска:

   ```bash
    python -m pytest --alluredir=tests/test_results/ tests/test_labirint.py
    ```
3. #### Команда для запуска сервера и просмотра отчёта в браузере, предварительно добавив allure в переменные окружения:

   ```bash
    allure serve tests/test_results/
    ```
