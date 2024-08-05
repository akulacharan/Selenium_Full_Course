import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(100)
driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")

select_element = Select(driver.find_element(By.XPATH,"//select[@id='first']"))

#select_element.select_by_visible_text("Google")
#select_element.select_by_value("Google")
#select_element.select_by_index(1)


all_options = select_element.options
print("Total number of options : ",len(all_options))

#select option from dropdown without using builtin function

for opt in all_options:
    if opt.text == "Google":
        opt.click()
        break


# Another method to get all options if we don't have select tag in website

all_opts = driver.find_elements(By.XPATH,"//select[@id='first']/option")
print(len(all_opts))

time.sleep(4)
driver.quit()


