from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.ID, "newButtonName")
input_field.clear()
input_field.send_keys("SkyPro")

blue_button = driver.find_element(By.ID, "updatingButton")
blue_button.click()

button_text = blue_button.text

print("Текст кнопки:", button_text)

driver.quit()