import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert


driver = webdriver.Chrome(executable_path=r"C:\Users\charanteja\PycharmProjects\chromedriver.exe")

driver.get("https://www.nobroker.in/")
driver.delete_all_cookies()
#driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.ID,"listPageSearchLocality").send_keys('Doddanekundi')

time.sleep(2)
all_items = driver.find_element(By.XPATH,"//div[@class='nb-google-autocomplete nb-google-autocomplete-lg']//div[1]//span[1]").click()

#select_first_item = driver.find_element(By.XPATH,"/html[1]/body[1]/div[4]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div[1]/span[1]").click()

#full_house = driver.find_element(By.XPATH,"//label[@for='RENT']").click()

time.sleep(2)
driver.quit()