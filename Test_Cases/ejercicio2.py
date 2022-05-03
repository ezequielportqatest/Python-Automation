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

driver.implicitly_wait(0)
driver.get(url)


boton: WebElement = driver.find_element(By.LINK_TEXT,"Tablets")
assert boton.is_displayed(), "No se encuentra el boton "
boton.click()


samsung: WebElement = driver.find_element(By.LINK_TEXT, "Samsung Galaxy Tab 10.1")
assert samsung.is_displayed(),"No se encuentra el elemento"
samsung.click()


precio: WebElement = driver.find_element(By.XPATH, "//h2[text()='$241.99']")
assert precio.is_displayed(), "el precio no coincide"

compra: WebElement = driver.find_element(By.ID, "button-cart")
assert compra.is_displayed(), "No se encuentra el boton"
compra.click()

carrito: WebElement = driver.find_element(By.ID,"cart-total")
assert carrito.is_displayed(), "No se encuentra el elemento"





driver.quit()