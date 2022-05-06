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
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

driver.get(url)

