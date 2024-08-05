from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")


field1 = driver.find_element(By.XPATH,"//input[@id='field1']")
field1.clear()
field1.send_keys('Akula Charanteja...!!!!')


dbclick_element = driver.find_element(By.XPATH, "//button[@ondblclick='myFunction1()']")

action = ActionChains(driver)

action.double_click(dbclick_element).perform()

time.sleep(4)
driver.quit()