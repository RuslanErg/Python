from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shopping_flow(driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    (wait.until(EC.presence_of_element_located((By.ID, "user-name"))).
     send_keys("standard_user"))
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for product_name in products:
        product_xpath = (f"//div[text()='{product_name}']"
                         f"/ancestor::div[@class='inventory_item']//button")
        add_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, product_xpath)
            )
        )

        add_button.click()

    sleep(10)
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    element = wait.until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    element.send_keys("Ruslan")

    driver.find_element(By.ID, "last-name").send_keys("Belgorod")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    sleep(10)

    driver.find_element(By.ID, "continue").click()

    # Ждем появления элемента с общей суммой
    total_element = wait.until(
        EC.presence_of_element_located(
            # Локатор по классу
            (By.CLASS_NAME, "summary_total_label")
        )
    )

    total_text = total_element.text  # например, "Total: $58.29"
    total_amount = total_text.split("$")[-1]

    sleep(10)

    assert total_amount == "58.29", (f"Expected total "
                                     f"to be $58.29, but got "
                                     f"${total_amount}")

    driver.quit()
