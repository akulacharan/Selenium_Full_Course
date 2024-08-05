from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import os


driver = webdriver.Chrome(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")
driver.maximize_window()

driver.implicitly_wait(10)

#This is old method to open a new tab
driver.get("https://demo.nopcommerce.com/")
# To open the registration link in new tab
driver.find_element(By.LINK_TEXT,"Register").send_keys(Keys.CONTROL+Keys.ENTER)

handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    if handle.title() == 'nopCommerce demo store. Register':
        break


'''
# New tab -- in selenium4: Opens a new tab and switches to the new tab
driver.get('https://www.opencart.com/')
driver.switch_to.new_window('tab')
driver.get('https://www.orangehrm.com/')
'''
'''
# New window -- in selenium4: Opens a new window and switches to the new tab
driver.get('https://www.opencart.com/')
driver.switch_to.new_window('window')
driver.get('https://www.orangehrm.com/')
'''


time.sleep(8)
driver.quit()