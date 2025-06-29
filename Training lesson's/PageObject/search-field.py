from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


cookie = {"name": "cookie_policy", "value": "1"}


def test_card_counter():
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))

    # Перейти на сайт «Лабиринта»
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)
    # Найти все книги по слову python
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys('python')
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

    sleep(5)
    # Переключиться на таблицу
    # Добавить все книги в корзину и посчитать
    # Перейти в корзину
    # Проверить счетчик товаров.
    browser.quit()