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
url = 'https://demo.seleniumeasy.com/'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

driver.get(url)



locator = (By.ID,"at-cv-lightbox-win")
wait.until(EC.visibility_of_element_located(locator))    #espera que el elemento este visible
assert close_btn.is_display(),"no se encuentra" #no es redundante, ya que anteriormente ya se valido que esta visible
time.sleep(1)

close = (By.ID,"at-cv-lightbox-close")
wait.until(EC.element_to_be_clickable(close))   #espera que el elemento sea clickeable


driver.quit()










