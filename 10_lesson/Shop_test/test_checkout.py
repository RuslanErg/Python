import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage
from products_page import ProductsPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()
        )
    )
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка итоговой суммы заказа")
@allure.description(
    """
    Авторизация, добавление товаров в корзину
    и проверка правильности финальной стоимости заказа
    """
)
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.BLOCKER)
def test_total_price(driver):
    with allure.step("Авторизация пользователя"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавление трёх товаров в корзину"):
        products_page = ProductsPage(driver)
        products_page.add_to_cart("add-to-cart-sauce-labs-backpack")
        products_page.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
        products_page.add_to_cart("add-to-cart-sauce-labs-onesie")

    with allure.step("Переход к корзине и оформлению"):
        products_page.go_to_cart()
        cart_page = CartPage(driver)
        cart_page.click_checkout()

    with allure.step("Заполнение формы и получение итоговой суммы"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_info("John", "Doe", "12345")
        total = checkout_page.get_total()

    with allure.step("Проверка суммы заказа"):
        assert total == "$58.29", f"Ожидалось $58.29, получено {total}"
