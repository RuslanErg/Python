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
    # Переключиться на таблицу
    # Добавить все книги на первой странице в корзину и посчитать
    buy_buttons = browser.find_elements(
        By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")

    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1
    # Перейти в корзину
    browser.get("https://www.labirint.ru/cart/")

    # Проверить счетчик товаров. Должен быть равен числу нажатий
    # Получить текущее значение
    txt = browser.find_element(
        By.CSS_SELECTOR, "a[data-event-label='myCart']").find_element(By.CSS_SELECTOR, 'b').text

    # Сравнить c counter
    assert counter == int(txt)
    browser.quit()