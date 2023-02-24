from selenium import webdriver
from selenium.webdriver.common.by import By

# driver=webdriver.Chrome()
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
frmea=driver.find_elements(By.TAG_NAME,"iframe")
driver.switch_to.frame(0)
myfile="D://Aircraft wallpapers//1920x1080 Airbus A380 desktop PC and Mac wallpaper.jpg"
fileupload=driver.find_element(By.ID,"RESULT_FileUpload-10")
fileupload.send_keys(myfile)
print(len(frmea))
