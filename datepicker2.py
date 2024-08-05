from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")


Year = '1998'
Month = 'Feb'
Day = '3'

dob = driver.find_element(By.XPATH,"//input[@id='dob']").click()

# selecting date from dropdown
Pickermonth = driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']")
selecting_month = Select(Pickermonth)
selecting_month.select_by_visible_text(Month)

# selecting year from dropdown
Pickeryear = driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']")
selecting_year = Select(Pickeryear)
selecting_year.select_by_visible_text(Year)


# Selecting day from date picker

pickerdays = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for ele in pickerdays:
    if ele.text == Day:
        ele.click()


time.sleep(4)
driver.quit()