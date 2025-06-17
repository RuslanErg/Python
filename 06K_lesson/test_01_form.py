from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Edge(
        service=EdgeService(
            EdgeChromiumDriverManager().install()
        )
    )

    yield driver
    driver.quit()


def test_fill_form(driver):
    driver.get("https://bonigarcia.dev/"
               "selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 10)

    # Заполнение формы
    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }
    for name, value in fields.items():
        driver.find_element(By.NAME, name).send_keys(value)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверка zip-code (красный)
    zip_code = wait.until(EC.visibility_of_element_located
                          ((By.ID, "zip-code")))
    assert "alert-danger" in zip_code.get_attribute("class"), \
           "Zip code не подсвечен красным"

    # Проверка успешных полей
    success_selectors = ["#first-name", "#last-name",
                         "#address", "#city", "#country",
                         "#e-mail", "#phone", "#company"]  # CSS-селекторы
    for selector in success_selectors:
        element = wait.until(EC.visibility_of_element_located
                             ((By.CSS_SELECTOR, selector)))
        assert "alert-success" in element.get_attribute("class"), \
               f"Элемент {selector} не подсвечен зелёным"
