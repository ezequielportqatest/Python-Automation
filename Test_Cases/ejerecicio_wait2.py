import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Setup
chrome_driver_path = '../drivers/chromedriver'
gecko_driver_path = '../drivers/geckodriver'
url = 'https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html'
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)
wait = WebDriverWait(driver, 10)

driver.get(url)



boton = (By.ID,"downloadButton")
wait.until(EC.visibility_of_element_located(boton))
time.sleep(1)
wait.until(EC.element_to_be_clickable(boton))
time.sleep(1)
completo=(By.CSS_SELECTOR,"Complete!")
assert wait.until(EC.text_to_be_present_in_element(completo, "Complete")), "No se encuentra"
time.sleep(1)
cerrar = (By.XPATH,"/html/body/div[4]/div[3]/div/button")
wait.until(EC.visibility_of_element_located(cerrar))
time.sleep(1)


time.sleep(1)




driver.quit()
