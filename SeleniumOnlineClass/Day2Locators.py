import time

from selenium import webdriver
from selenium.webdriver.common.by import  By

# username =input("enter username or phonenumber:")
# password =input("enter the password:")

driver = webdriver.Chrome("D:\drivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.facebook.com/")
title=driver.title
if title=="Facebook – log in or sign up":
    print("success")
    print("the title is",title)
else:
    print("failure")
#driver.find_element_by_id("email").send_keys(username)
driver.find_element(By.ID,"email").send_keys("544554479")
driver.find_element(By.ID,"pass").send_keys("Nothing@121345")
#driver.find_element_by_id("pass").send_keys(password)
#driver.find_element_by_name("login")
driver.find_element(By.NAME,"login").click()
time.sleep(10)
# driver.close()

# locators
# //Types of Locator
# //id,
# //name,
# //className,
# //tagName,
# //linkText,
# //partialLinkText,
# //CSS selector and
# //xpath
# //<TagName  attributeName = 'Attribute Value' >