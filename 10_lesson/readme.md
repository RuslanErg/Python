Проект содержит автоматизированные тесты для веб-приложений "Calculator" и "SauceDemo", написанные на Python с использованием Selenium WebDriver и фреймворка Pytest. 
Отчеты о выполнении тестов генерируются с помощью Allure Report.

## Структура проекта

* `calc_page.py`: Объектная модель страницы для калькулятора.
* `test_calc_page.py`: Тесты для калькулятора, использующие Pytest и Allure.
* `login_page.py`: Объектная модель страницы логина SauceDemo.
* `shop_.py`: Объектная модель страницы инвентаря SauceDemo.
* `cart_page.py`: Объектная модель страницы корзины SauceDemo.
* `checkout_page.py`: Объектная модель страницы оформления заказа SauceDemo.
* `test_checkout_pytest.py`: Тесты для SauceDemo, использующие Pytest и Allure.
* `product_page.py`: Объектная модель страницы для корзины

## Установка и запуск

### Предварительные требования

* Python 3.x
* Allure Commandline.
### Установка зависимостей

Установите все необходимые библиотеки Python, выполнив следующую команду:

```bash
pip install selenium pytest allure-pytest webdriver-manager