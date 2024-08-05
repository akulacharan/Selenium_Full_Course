from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")

driver.get("https://jqueryui.com/datepicker/")

driver.switch_to.frame(0)  # switches to first frame
#driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys('02/03/1998')  # Normal way to enter date


Year = "2024"
Month = "July"
Day = "31"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

# Here we are getting the current month and year and running the loop until we find our desired month and Year

while True:

    current_month = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    current_year = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if current_year == Year and current_month == Month:
        #driver.find_element(By.XPATH,"//a[@data-date="+str(Day)+"]").click()
        break
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()  #click on next Arrow
        #driver.find_element(By.XPATH,"//a[@class='ui-datepicker-prev ui-corner-all']").click()  # To click on previous Arrow

# to select date

all_days_from_picker = driver.find_elements(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")

for ele in all_days_from_picker:
    if ele.text == Day:
        ele.click()
        break

time.sleep(4)

driver.quit()