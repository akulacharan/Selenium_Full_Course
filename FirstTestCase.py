"""
FirstTestcase.py file in "SeleniumUpdatedcourse project"

1) Open web Browser.
2) open url https://opensource-demo.orangehrmlive.com
3) Enter username (Admin)
4) Enter password (admin123)
5) Click on login
6) Capture title of the home page.(Actual title)
7) Verify the title of the page: OrangeHRM (Expected)
8) Close browser

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time


#driver = webdriver.Chrome(r"C:\Users\charanteja\PycharmProjects\Selenium\chromedriver.exe")
#To run this directly you need to save the Chromedriver.exe file in Scripts folder of your python installed folder.
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(5)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
Act_title = driver.title
Exp_title = "OrangeHRM"

if Act_title == Exp_title:
    print("Login test passed")
else:
    print("Login test failed")


time.sleep(5)

driver.close()