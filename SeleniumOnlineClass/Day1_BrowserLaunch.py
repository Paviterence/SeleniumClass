# import time
# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.service import Service
# #chrome launch
# driver=webdriver.Chrome("D:\drivers\chromedriver.exe")
# # browser=webdriver.Firefox(executable_path="D:\drivers\geckodriver.exe")
# # brow=webdriver.Edge(executable_path="D:\drivers\msedgedriver")
# # s=Service(executable_path='D:\drivers\chromedriver.exe')
# # driver = webdriver.Chrome(service=s)
# driver.get("https://www.google.com/")
# driver.maximize_window()
# time.sleep(2)
# # browser.get("https://www.google.com/")
# # brow.get("https://www.google.com/")
import time
from selenium import webdriver
driver=webdriver.Chrome("D:\drivers\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(2)#seconds
driver.minimize_window()
time.sleep(2)
driver.fullscreen_window()
time.sleep(2)
print(driver.title)#tittle return
driver.close()#close the current tab not entire browser
# driver.quit()#close the entire browser
