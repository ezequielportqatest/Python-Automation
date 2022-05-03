import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Init Browsers
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

chrome_driver_path = '../drivers/chromedriver'
gecko_driver_path = '../drivers/geckodriver'
url = "https://demoqa.com/select-menu"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open Web Page
driver.get(url)

# Test Logic
time.sleep(2)
autos = driver.find_element(By.ID, "cars")
assert autos.is_displayed(), "no se encuentran opciones"
autos_dropdown = Select(autos)
autos_dropdown.select_by_visible_text("Volvo")
autos_dropdown.select_by_visible_text("Audi")
selected_option: list = [option.text for item in autos_dropdown.all_selected_options]
assert "Volvo" in selected_option, "no se encuentra Volvo"
assert "Audi" in selected_option, "no se encuentra Volvo"

driver.quit()