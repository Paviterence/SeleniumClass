import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://www.youtube.com')
driver.maximize_window()
time.sleep(2)
print("1st website",driver.title)
driver.get("https://www.google.com/")
time.sleep(2)
print("2nd website ",driver.title)
driver.back()
print("back to the 1st website ",driver.title)
time.sleep(2)
driver.forward()
print("againg frwd to the 2nd website ",driver.title)
driver.refresh()
time.sleep(4)
print("navigation commands success")
driver.close()