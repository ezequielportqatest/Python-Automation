import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Ruta del driver(.exe)
chrome_driver_path = 'C:\\Users\\tntau\\Python-Automation\\Drivers\\chromedriver.exe'
gecko_driver_path = './Drivers/geckodriver'

#Direccion de la pagina
url = 'https://www.youtube.com/'
service = Service(chrome_driver_path)

#mediante navegador ...
driver = webdriver.Chrome(service=service)
driver.get(url)
time.sleep(3)
driver.quit()