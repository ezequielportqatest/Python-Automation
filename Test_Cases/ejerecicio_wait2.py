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


time.sleep(3)
boton_locacion = (By.ID,"downloadButton")
boton: WebElement = wait.until(EC.element_to_be_clickable(boton_locacion))
boton.click()

time.sleep(1)
completo=(By.CSS_SELECTOR,'progress-label')
assert wait.until(EC.text_to_be_present_in_element(completo, "Complete")), "No se encuentra"

time.sleep(1)
cerrar_close = (By.XPATH,"/html/body/div[4]/div[3]/div/button")
cerrar: WebElement = wait.until(EC.element_to_be_clickable(cerrar_close))
cerrar.click()


time.sleep(1)




driver.quit()
