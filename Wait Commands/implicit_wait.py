import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.implicitly_wait(10) #seconds #implicit wait
driver.get("https://www.google.com/")
driver.maximize_window()

searchbox = driver.find_element(By.NAME,'q')
searchbox.send_keys('selenium')
searchbox.submit()  #It will press enter button


driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()