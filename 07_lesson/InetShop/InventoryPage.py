from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        # Названия товаров по их уникальным селекторам
        self.backpack_add_button = (By.ID, 'add-to-cart-sauce-labs-backpack')
        self.tshirt_add_button = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
        self.onesie_add_button = (By.ID, 'add-to-cart-sauce-labs-onesie')
        self.cart_icon = (By.CLASS_NAME, 'shopping_cart_link')

    def add_backpack(self):
        self.driver.find_element(*self.backpack_add_button).click()

    def add_tshirt(self):
        self.driver.find_element(*self.tshirt_add_button).click()

    def add_onesie(self):
        self.driver.find_element(*self.onesie_add_button).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()
