from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")
driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://text-compare.com/")

input1 = driver.find_element(By.XPATH,"//textarea[@name='text1']")
input2 = driver.find_element(By.XPATH,"//textarea[@name='text2']")

#To scroll
driver.execute_script("arguments[0].scrollIntoView();",input1)

input1.send_keys('Charanteja')

actions = ActionChains(driver)
time.sleep(1)
# input1 --> (ctrl + A) select the text
actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

# input1 --> (Ctrl +C) copying the text
actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()


# Pressing tab key to move to next input2 area
actions.send_keys(Keys.TAB).perform()


# Copying (Ctrl + V) in input2 area
actions.key_down(Keys.CONTROL)
actions.send_keys('v')
actions.key_up(Keys.CONTROL)
actions.perform()


time.sleep(4)
driver.quit()