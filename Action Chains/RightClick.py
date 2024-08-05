from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

element_to_be_right_clicked = driver.find_element(By.XPATH,"//span[text()='right click me']")

click_on_quit_option = driver.find_element(By.XPATH,"//li/span[text()='Quit']")

action = ActionChains(driver)

# Right-clicking the element
action.context_click(element_to_be_right_clicked).perform()

# Clicking on quit

action.click(click_on_quit_option).perform()



time.sleep(4)
driver.quit()