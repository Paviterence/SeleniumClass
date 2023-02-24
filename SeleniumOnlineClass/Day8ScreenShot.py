
from selenium import webdriver
import time
import datetime
import os
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("D:\drivers\chromedriver.exe")
driver.implicitly_wait(20)
def current_time():
    return datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S_%f")
print(current_time())
driver.get("https://www.google.com/")
driver.maximize_window()
driver.get_screenshot_as_file("google_loadingpage.png")#without date and time
#driver.get_screenshot_as_file("google_"+current_time()+".png")#to get screenshot at working file with
# driver.get_screenshot_as_file(os.getcwd()+"/screenshots/"+"google_"+current_time()+".png")#to get screenshot at different file or directory
# scrnshot=Image.open()
# scrnshot.show()
time.sleep(2)
#step1
driver.find_element(By.XPATH,'//input[@name="q"]').send_keys("iphone 13 green color")
time.sleep(2)
driver.find_element(By.XPATH,'//input[@name="btnK"]').click()
driver.get_screenshot_as_file(os.getcwd()+"/screenshots/"+"Googlesearch_"+current_time()+".png")
time.sleep(3)
#step2
driver.get("https://www.youtube.com/")
driver.find_element(By.XPATH,'//input[@id="search"and@name="search_query"]').send_keys("arabic kuthu song")
time.sleep(2)
driver.find_element(By.XPATH,'//button[@id="search-icon-legacy"and@aria-label="Search"]').click()
driver.get_screenshot_as_file(os.getcwd()+"/screenshots/"+"yt_"+current_time()+".png")
time.sleep(5)
driver.quit()
