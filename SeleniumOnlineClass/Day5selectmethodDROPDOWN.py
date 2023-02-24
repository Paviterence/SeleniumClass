import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#driver = webdriver.Chrome(executable_path="G:\driver\chromedriver_win32\chromedriver.exe") #my computer
driver=webdriver.Chrome("D:\drivers\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/")
regbtn=driver.find_element(By.XPATH,'//a[@role="button"and@data-testid="open-registration-form-button"]')
regbtn.click()
fname=driver.find_element(By.XPATH,'//input[@name="firstname"and@aria-label="First name"]')
fname.send_keys('pavithran')
lname=driver.find_element(By.XPATH,'//input[@name="lastname"and@aria-label="Surname"]')
lname.send_keys('sethu')
driver.find_element(By.XPATH,'//input[@aria-label="Mobile number or email address"]').send_keys('9784561524')
driver.find_element(By.XPATH,'//input[@id="password_step_input"and@type="password"]').send_keys('Passcode')
time.sleep(2)
print("--------days-------")
days_elements=driver.find_element(By.ID,"day")#assign the id
days=Select(days_elements)#selecting the all elements 31 days
#giving the values manually to the dropdownlist
days.select_by_visible_text("17")#text method
time.sleep(2)
days.select_by_index(2)#index method
time.sleep(2)
days.select_by_value("6")#value method
time.sleep(2)
days_elements.send_keys("25")#send my value to days dropdown box NORMAL METHOD
print("get attribute method the value sent to the dropbox:",days_elements.get_attribute('value')) #get my value from dropbox
time.sleep(2)
#finding total or lenghth number of dropdownlist
totaloptions=len(days.options)#to find total options available in days
print("Total options in day dropdownlist:",totaloptions)#31 options are there
alloptions=days.options#to get all options
print("total options")#just for heading
for option in alloptions:#for loop
    # print(option.text)
    print("option text is-{}-option value is={}".format(option.text,option.get_attribute("value")))
#month
month_element=driver.find_element(By.ID,'month')
months=Select(month_element)
months.select_by_value("2")#feb
time.sleep(2)
months.select_by_index(4)
time.sleep(2)
months.select_by_visible_text("Aug")
month_length=len(months.options)
print("total months options are available in facebook\n:",month_length)
ops=months.options
for option in ops:
   print("option text is-{}-option value is={}".format(option.text, option.get_attribute("value")))
print("-------year--------")
year_elements=driver.find_element(By.ID,"year")
years=Select(year_elements)
years.select_by_visible_text("1997")
time.sleep(3)
years.select_by_value("1996")
time.sleep(3)
years.select_by_index(1)#2021
totalyears=len(years.options)
print("total no of options in year:",totalyears)#118
opsy=years.options
for x in opsy:
   print("year is={} year value is={}".format(x.text,x.get_attribute("value")))
driver.quit()