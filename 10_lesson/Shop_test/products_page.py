from selenium.webdriver.common.by import By


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_id):
        self.driver.find_element(By.ID, product_id).click()

    def go_to_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link"
        ).click()
