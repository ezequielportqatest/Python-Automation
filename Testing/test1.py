import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = 'C:\\Users\\tntau\\Python-Automation\\Drivers\\chromedriver.exe'
gecko_driver_path = './Drivers/geckodriver'

url = 'https://www.youtube.com/'
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)
driver.get(url)
time.sleep(3)
driver.quit()