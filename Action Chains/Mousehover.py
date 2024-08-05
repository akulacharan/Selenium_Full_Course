from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")

driver.get("https://www.browserstack.com/guide/mouse-hover-in-selenium")

# Hovering on the products option
first_element = driver.find_element(By.XPATH,"//button[@aria-label='Products']")

# Selecting the Web testing option by hovering
second_to_select = driver.find_element(By.XPATH,"//*[@id='products-dd-tab-1']/div")

# Selecting the Accessin=bility testing option by clicking
last_to_select = driver.find_element(By.XPATH,"//*[@id='products-dd-tabpanel-1-inner-1']/div[1]/div[3]/a")

action = ActionChains(driver)

action.move_to_element(first_element).move_to_element(second_to_select).click(last_to_select).perform()



time.sleep(4)

driver.quit()