from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = ("https://bonigarcia.dev/selenium-webdriver-java"
                    "/slow-calculator.html")
        self.delay_input = (By.ID, "delay")
        self.screen = (By.CSS_SELECTOR, "div.screen")
        self.button = lambda val: (By.XPATH, f"//span[contains(@class, 'btn')"
                                             f" and text()='{val}']")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, value):
        delay = self.driver.find_element(*self.delay_input)
        delay.clear()
        delay.send_keys(str(value))

    def click_button(self, value):
        for digit in str(value):
            self.driver.find_element(*self.button(digit)).click()

    def click_operator(self, op):
        self.driver.find_element(*self.button(op)).click()

    def click_equals(self):
        self.driver.find_element(*self.button("=")).click()

    def get_result(self, timeout=50):
        screen_elem = self.driver.find_element(*self.screen)
        initial_text = screen_elem.text
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(*self.screen).text != initial_text
        )
        return self.driver.find_element(*self.screen).text
