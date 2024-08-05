from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

'''  Application Commands 
driver.get("https://www.facebook.com/")
time.sleep(1)
title = driver.title
url = driver.current_url
source_code = driver.page_source

print('Page Title is : ',title)
print('The current url is :',url)
print('The Page source code is : ',source_code)
driver.quit()
'''
'''
# Conditional Commands

driver.get('https://demo.nopcommerce.com/register')
# identifying the mal radio button
is_displayed = driver.find_element(By.ID,'gender-male').is_enabled()
is_enabled = driver.find_element(By.ID,'gender-male').is_enabled()

#we didn't selected the element now
is_selected_1 = driver.find_element(By.ID,'gender-male').is_selected()

#Now we select the element
driver.find_element(By.ID,'gender-male').click()
is_selected_2 = driver.find_element(By.ID,'gender-male').is_selected()
time.sleep(1)


print('IS Displayed :',is_displayed)
print('IS Enabled :',is_enabled)
print('IS Selected :',is_selected_1)
print('IS Selected :',is_selected_2)
driver.quit()

'''

'''  (Browser Commands) --> Close and Quit commands 
driver.get('https://accounts.lambdatest.com/register')
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[2]/div/div[2]/div[2]/form/div[4]/div/a[2]").click()
time.sleep(1)
driver.quit()
#driver.close()
'''

''' Navigational Commands 

driver.get('https://accounts.lambdatest.com/register')
time.sleep(1)
driver.get('https://www.facebook.com/')
time.sleep(1)
driver.back()
print('Navigated back to lambdatest ')
time.sleep(1)
driver.forward()
print('Navigated forward to Facebook ')
time.sleep(1)
driver.refresh()
print('Webpage is refreshed')
time.sleep(1)
driver.quit()

'''