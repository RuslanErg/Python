from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleMainPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, 'q')
        self.results_selector = (By.CSS_SELECTOR, 'div.g')

    def search_for(self, query):
        search_box_element = self.driver.find_element(*self.search_box)
        search_box_element.clear()
        search_box_element.send_keys(query)
        search_box_element.send_keys(Keys.RETURN)

    def get_search_results(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.results_selector)
        )
        return self.driver.find_elements(*self.results_selector)