from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/ajax")
blue_button = driver.find_element(By.ID, "ajaxButton")
blue_button.click()
green_alert = WebDriverWait(driver, 16).until(
EC.presence_of_element_located((By.CLASS_NAME, "bg-success")))

alert_text = green_alert.text
print("Текст из зеленой плашки:", alert_text)
driver.quit()