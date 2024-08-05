from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/login")


emailbox = driver.find_element(By.XPATH,"//*[@id='Email']")
emailbox.send_keys('akulacharanteja@gmail.com')
'''
print("result of text :",emailbox.text)  #printed nothing
print("result of get_attribute :",emailbox.get_attribute('value'))  # akulacharanteja@gmail.com
driver.quit()
'''

button = driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print("result of text :",button.text)  #Log In
print("result of get_attribute :",button.get_attribute('value'))  # Nothing
print("result of get_attribute :",button.get_attribute('type'))  # submit
driver.quit()