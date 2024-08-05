from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")
driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.execute_script("window.scrollBy(0,500)","")

driver.find_element(By.XPATH,"//*[@id='billing_country_field']/span").click()

all_countries = driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")

for c in all_countries:
    if c.text == 'Thailand':
        c.click()
        break


time.sleep(4)
driver.quit()