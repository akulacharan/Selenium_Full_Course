from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.infoplease.com/countries")
time.sleep(4)

'''
# 1) Scroll down page by pixel
driver.execute_script("window.scrollBy(0,2000)","")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved : ",value)
'''

'''
# 2) Scroll down the page till the element is visible.
flag = driver.find_element(By.XPATH,"//a[contains(text(),'India')]")
driver.execute_script("arguments[0].scrollIntoView();",flag)
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved : ",value)
'''


# 3) Scroll down the page till the end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved : ",value)

time.sleep(4)

# 4) Scroll up the page to the starting position

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved : ",value)


time.sleep(4)
driver.quit()