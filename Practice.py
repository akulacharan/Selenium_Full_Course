import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
'''
name = driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Akula Charanteja")
email = driver.find_element(By.XPATH,"//input[@id='email']").send_keys("akulacharanteja@gmail.com")
Phone = driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("7032172247")
address = driver.find_element(By.XPATH,"//textarea[@id='textarea']").send_keys("8=666-1,marampalli street, kalyandurg,515761")
gender = driver.find_element(By.XPATH,"//input[@id='male']").click()
all_days = driver.find_elements(By.CSS_SELECTOR,"input.form-check-input[type='checkbox']")
for day in all_days:
    day.click()
#Select country
element_to_be_selected = Select(driver.find_element(By.XPATH,"//select[@id='country']"))

all_options = element_to_be_selected.options

for option in all_options:
    if option.text == "India":
        option.click()
        break

colors = driver.find_elements(By.XPATH,"//select[@id='colors']")

for color in colors:
    if color.text == "Blue":
        color.click()
        break

date = driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("09/09/2023")
wikipedia = driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input").send_keys("Charan")
driver.find_element(By.XPATH,"//*[@id='Wikipedia1_wikipedia-search-form']/div/span[2]/span[2]/input").submit()


#Double click
action = ActionChains(driver)
action.double_click(driver.find_element(By.XPATH,"//button[@ondblclick='myFunction1()']")).perform()


'''

#new_window = driver.find_element(By.XPATH,"//button[@onclick='myFunction()']").click()

alert = driver.find_element(By.XPATH,"//button[@onclick='myFunctionAlert()']").click()


a = driver.switch_to_alert()
time.sleep(1)
a.accept()

time.sleep(4)
driver.quit()
