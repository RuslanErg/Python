import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator_addition_with_delay(driver):
    calc_page = CalculatorPage(driver)
    calc_page.open()
    calc_page.set_delay("45")
    calc_page.click_button()
    calc_page.expectation()
    result = calc_page.get_result()
    assert result == "15"
