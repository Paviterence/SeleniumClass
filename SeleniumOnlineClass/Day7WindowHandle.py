import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
print((driver.title))
print(driver.current_url)
wait=WebDriverWait(driver,5)
searchbox=wait.until(ec.presence_of_element_located((By.ID,'twotabsearchtextbox')))
searchbox.send_keys("iphone",Keys.ENTER)
clickOnPhone=driver.find_element(By.XPATH,("//span[text()='Apple iPhone 12 (64GB) - Black']"))
clickOnPhone.click()
# element_click=wait.until(ec.element_to_be_clickable((By.XPATH,'(//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"and@target="_blank"])[1]')))
# element_click.click()
paren_windowId=driver.current_window_handle
print("parent window id id --->",paren_windowId)
all_windowids=driver.window_handles
print("all window ids--->",all_windowids)
for eachwindowId in all_windowids:
    if paren_windowId!=eachwindowId:
        driver.switch_to.window(eachwindowId)

childwindow=driver.current_window_handle
print(childwindow)

addToCart = driver.find_element(By.ID("add-to-cart-button"))
addToCart.click()

driver.close()
