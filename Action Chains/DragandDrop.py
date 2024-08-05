from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")
driver.implicitly_wait(10)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

# For Italy
dragable_italy = driver.find_element(By.XPATH, "//*[@id='box6']")
droppable_italy = driver.find_element(By.XPATH, "//*[@id='box106']")

dragable_US = driver.find_element(By.XPATH, "//*[@id='box3']")
droppable_US = driver.find_element(By.XPATH, "//*[@id='box103']")

action = ActionChains(driver)

#italy
action.drag_and_drop(dragable_italy, droppable_italy).perform()

#US
action.drag_and_drop(dragable_US, droppable_US).perform()

action.dr

time.sleep(4)
driver.quit()