from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")

driver.get("https://jqueryui.com/datepicker/")

day = '3'
month = 'April'
year = '2024'

driver.switch_to.frame(0)

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()



while True:

    displayed_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text

    displayed_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if month == displayed_month and year == displayed_year:
        break
    else:
        previous_button = driver.find_element(By.XPATH, "//a[@data-handler='prev']").click()

days = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tr/td")

for d in days:
    if d.text == day:
        d.click()

time.sleep(4)

driver.quit()