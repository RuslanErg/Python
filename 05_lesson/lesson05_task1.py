from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.get("http://uitestingplayground.com/classattr")
time.sleep(2)

blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")

blue_button.click()
time.sleep(2)

print("Синяя кнопка успешно нажата!")
time.sleep(2)

driver.quit()
