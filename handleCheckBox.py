import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.ironspider.ca/forms/checkradio.htm")

# 1) Select specific checkbox
#driver.find_element(By.XPATH,"//input[@value='green']").click()

# 2) Select all checkboxes
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and @name='color'] ")
print(len(checkboxes))

# Approach-1
'''
for i in range(len(checkboxes)):
    checkboxes[i].click()
'''
# Approach-2

for box in checkboxes:
    box.click()

'''
# 3) Select multiple checkboxes by choice
for box in checkboxes:
    colorname = box.get_attribute('value')
    if colorname == 'green' or colorname == 'blue':
        box.click()
'''

time.sleep(2)
# 4) Un-select all the chckboxes

for box in checkboxes:
    if box.is_selected():
        box.click()

time.sleep(4)
driver.quit()