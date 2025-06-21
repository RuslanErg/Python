import pytest
from selenium import webdriver
from LoginPage import LoginPage
from InventoryPage import InventoryPage
from CartPage import CartPage
from CheckoutPage import CheckoutPage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get('https://www.saucedemo.com')

    yield driver
    driver.quit()


def test_purchase_flow(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Добавляем товары в корзину
    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack()
    inventory_page.add_tshirt()
    inventory_page.add_onesie()
    inventory_page.go_to_cart()

    # Переходим в корзину
    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # Заполняем форму заказа
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form('John', 'Doe', '12345')

    # Получаем итоговую сумму
    total_text = checkout_page.get_total()

    # Проверка, что итоговая сумма равна $58.29
    assert total_text == 'Total: $58.29'


def teardown(self):
    # Закрываем браузер
    self.driver.quit()
