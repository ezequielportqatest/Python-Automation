import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement




#Ruta del driver(.exe)
chrome_driver_path = '../Drivers/chromedriver.exe'
gecko_driver_path = '../Drivers/geckodriver'

#Direccion de la pagina
url = 'https://laboratorio.qaminds.com/'
service = Service(chrome_driver_path)
#mediante navegador ...
driver = webdriver.Chrome(service=service)


time.sleep(2)
