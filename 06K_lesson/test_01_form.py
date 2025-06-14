from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
wait = WebDriverWait(driver, 5)

driver.find_element(By.NAME, "first-name").send_keys("Иван")
driver.find_element(By.NAME, "last-name").send_keys("Петров")
driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
driver.find_element(By.NAME, "phone").send_keys("+7985899998787")

driver.find_element(By.NAME, "city").send_keys("Москва")
driver.find_element(By.NAME, "country").send_keys("Россия")
driver.find_element(By.NAME, "job-position").send_keys("QA")
driver.find_element(By.NAME, "company").send_keys("SkyPro")

submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()

def check_field_color(field_name, expected_color):
   field = driver.find_element(By.NAME, field_name)
   style = field.value_of_css_property("border-color")
   return expected_color in style

wait.until(EC.presence_of_element_located((By.ID, "zip-code")))

zip_field = driver.find_element(By.ID, "zip-code")
zip_border_color = zip_field.value_of_css_property("border-color")
assert "rgb(245, 194, 199)" in zip_border_color or "red" in zip_border_color, \
f"Zip code не подсвечен красным, найдено: {zip_border_color}"

fields = [
    "first-name",
    "last-name",
    "address",
    "e-mail",
    "phone",
    "city",
    "country",
    "job-position",
    "company"
]

for field_name in fields:
    wait.until(EC.presence_of_element_located((By.NAME, field_name)))
    field = driver.find_element(By.NAME, field_name)
    border_color = field.value_of_css_property("border-color")
    assert "rgb(25,135,84)" in border_color or "green" in border_color, \
    f"Поле {field_name} не подсвечено зеленым, найдено: {border_color}"

driver.quit()
