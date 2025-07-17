from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = ("https://bonigarcia.dev/selenium-webdriver-java/"
                    "slow-calculator.html")
        # Локаторы элементов
        self.delay_input = (By.ID, "delay")
        self.result_field = (By.ID, "result")
        self.buttons = {
            '7': (By.XPATH, "//button[text()='7']"),
            '8': (By.XPATH, "//button[text()='8']"),
            '+': (By.XPATH, "//button[text()='+']"),
            '=': (By.XPATH, "//button[text()='=']")
        }

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds: str):
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.clear()
        delay_element.send_keys(seconds)

    def click_button(self):
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()

    def expectation(self):
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"))

    def get_result(self):
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return result.text
