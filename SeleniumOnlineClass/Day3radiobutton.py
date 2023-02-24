import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
# browser=webdriver.Chrome(executable_path='D:\drivers\chromedriver.exe')
browser=webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.facebook.com/")

print("url is:\n",browser.current_url)
time.sleep(2)
reg_btn=browser.find_element(By.XPATH,'//a[@data-testid="open-registration-form-button"]')
reg_btn.click()
print("signup url is:\n",browser.current_url)
time.sleep(4)
fname=browser.find_element(By.XPATH,'//input[@name="firstname"]')
fname.send_keys("myname")
time.sleep(1)
lname=browser.find_element(By.XPATH,'(//input[@type="text"])[3]')
lname.send_keys("lastname")
time.sleep(1)
mail_or_number=browser.find_element(By.XPATH,'(//input[@type="text"])[4]')
mail_or_number.send_keys("mynamelast@gmail.com")
mail_confrm=browser.find_element(By.XPATH,'//input[@name="reg_email_confirmation__"]')
mail_confrm.send_keys("mynamelast@gmail.com")
time.sleep(1)
password=browser.find_element(By.XPATH,'(//input[@type="password"])[2]')
password.send_keys("pae23456dfd")
date=browser.find_element(By.XPATH,'//select[@aria-label="Day"]')
date.send_keys("17")
month=browser.find_element(By.XPATH,'//select[@aria-label="Month"]')
month.send_keys("may")
year=browser.find_element(By.XPATH,'//select[@aria-label="Year"]')
year.send_keys("1997")
male_radiobtn=browser.find_element(By.XPATH,'(//input[@type="radio"])[2]')
male_radiobtn.click()
signup_btn=browser.find_element(By.XPATH,'//button[text()="Sign Up"]')
browser.find_element(By.XPATH,'//button[text()="Sign Up"]').click()
time.sleep(5)
browser.close()

# Task
# http://demo.automationtesting.in/Register.html