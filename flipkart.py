import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert


driver = webdriver.Chrome(executable_path=r"C:\Users\charanteja\PycharmProjects\chromedriver.exe")


driver.get("https://www.google.com/")
#driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//*[@id='APjFqb']").send_keys("Akula Charanteja")

time.sleep(4)
driver.quit()