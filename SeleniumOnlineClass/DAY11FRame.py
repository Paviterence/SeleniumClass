import time

from selenium import webdriver
from  selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.redbus.in/")
driver.implicitly_wait(10)
driver.maximize_window()
frame=driver.find_elements(By.TAG_NAME,"iframe")
print(len(frame))
driver.get("http://demo.guru99.com/test/guru99home/")
# frame=driver.find_elements(By.TAG_NAME,"iframe")
# print(len(frame))
driver.find_element(By.XPATH,"//i[@id='i-icon-profile']").click()
driver.find_element(By.CSS_SELECTOR,"#signInLink").click()
f1=driver.find_element(By.XPATH,'(//iframe[@class="modalIframe"])[1]')
driver.switch_to.frame(f1)
time.sleep(5)
driver.find_element(By.ID,"mobileNoInp").send_keys("9876543210")
# '''raise exception_class(message, screen, stacktrace)
# selenium.common.exceptions.NoSuchElementException: Message: no such element:
# Unable to locate element: {"method":"css selector","selector":"#mobileNoInp"}'''
# driver.switch_to.default_content()
# time.sleep(5)
# driver.find_element(By.ID,"redRail").click()
