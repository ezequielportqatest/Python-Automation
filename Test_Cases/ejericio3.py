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

driver.get(url)

time.sleep(2)
drop: WebElement = driver.find_element(By.CLASS_NAME,"caret")
assert drop.is_displayed(), "No se encuentra el boton "
drop.click()
time.sleep(3)

acceso: WebElement = driver.find_element(By.LINK_TEXT, "Login")
assert acceso.is_displayed(),"No se encuentra el elemento"
acceso.click()
time.sleep(2)

email: WebElement = driver.find_element(By.NAME,"email")
assert email.is_displayed(), "no se encuentra el cmapo "
email.click()
email.send_keys("test@nada.com")


login: WebElement = driver.find_element(By.XPATH, "//*[@id='content']/div/div[2]/div/form/input")
assert login.is_displayed(), "No se encuentra el boton"
login.click()
time.sleep(2)

mensaje: WebElement = driver.find_element(By.XPATH,"//*[@id=‘top’]//a[normalize-space(.)=‘My Account’])
assert mensaje.is_displayed(), "No se observa el mensaje"





time.sleep(3)
driver.quit()