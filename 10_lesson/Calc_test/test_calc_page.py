import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Calc_page import CalcPage  # путь к твоему Page Object

# Фикстура


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()
        )
    )

    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка арифметической операции в калькуляторе")
@allure.description("Проверяет корректность выполнения операций "
                    "калькулятора при установленной задержке")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "delay, num1, num2, op, expected",
    [(45, 7, 8, '+', 15)]
)
def test_calc_operation(driver, delay, num1, num2, op, expected):
    with allure.step("Открытие страницы калькулятора"):
        page = CalcPage(driver)
        page.open()

    with allure.step(f"Установка задержки: {delay} секунд"):
        page.set_delay(delay)

    with allure.step(f"Ввод первого числа: {num1}"):
        page.click_button(num1)

    with allure.step(f"Выбор оператора: {op}"):
        page.click_operator(op)

    with allure.step(f"Ввод второго числа: {num2}"):
        page.click_button(num2)

    with allure.step("Нажатие кнопки равно"):
        page.click_equals()

    with allure.step("Получение результата и проверка"):
        result = page.get_result(timeout=delay+5)
        assert result == str(expected), (
            f"Ожидалось {expected}, получено {result}"
        )
