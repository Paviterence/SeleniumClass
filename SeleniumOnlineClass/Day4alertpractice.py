import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
#driver=webdriver.Chrome('G:\driver\chromedriver_win32\chromedriver.exe') #my pc
driver=webdriver.Firefox(executable_path="D:\drivers\geckodriver.exe")
driver.implicitly_wait(30)
driver.get("http://demo.automationtesting.in/Alerts.html")
driver.find_element(By.XPATH,'(//a[@class="analystic"])[1]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//button[contains(text(),"click the button to display an  alert box")]').click()
time.sleep(2)
alt=driver.switch_to.alert
print("alertbox text here:",alt.text)
alt.accept()
#web element 2 ok or cancel practice
driver.find_element(By.XPATH,'//a[text()="Alert with OK & Cancel "]').click()
driver.find_element(By.XPATH,'//*[text()="click the button to display a confirm box "]').click()
time.sleep(2)
alt2=driver.switch_to.alert
print("web element 2\n",alt2.text)
#alt2.accept()
alt2.dismiss()
time.sleep(2)
demo=driver.find_element(By.ID,'demo')
print(demo.text)
#web element 3 Alert prompt practice
driver.find_element(By.XPATH,'(//*[@class="analystic"])[3]').click()
time.sleep(2)
prompt_text=driver.find_element(By.XPATH,'//button[contains(text(),"click the button to demonstrate the prompt box ")]')
#driver.find_element(By.XPATH,'//button[contains(text(),"click the button to demonstrate the prompt box ")]').click()
prompt_text.click()
time.sleep(2)
alt3=driver.switch_to.alert
print("web element 3\ntext--->",alt3.text)
time.sleep(2)
alt3.send_keys("pavi")
time.sleep(2)
alt3.accept()
demo_1=driver.find_element(By.ID,'demo1')
print("text-->",demo_1.text)
#again go 1st web
driver.find_element(By.XPATH,'(//a[@class="analystic"])[1]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//button[contains(text(),"click the button to display an  alert box")]').click()
time.sleep(2)
alt=driver.switch_to.alert
print("alertbox text here:",alt.text)
alt.dismiss()

driver.quit()