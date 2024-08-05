from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")
driver.get('https://demo.nopcommerce.com/')

#### find_element() returns single element only
'''
# Scenario 1 --> Locator matching with single web-element

single_element = driver.find_element(By.XPATH,"//*[@id='small-searchterms']")
single_element.send_keys('Macbook pro')
time.sleep(4)
driver.quit()
'''

'''
# Scenario 2 --> Locator matching with multiple web-elements

element = driver.find_element(By.XPATH,"//div[@class='footer']//a")
print(element.text)  #Sitemap
driver.quit()
'''

'''
# Scenario 3 --> Element not available then throw NoSuchElementException
login_element = driver.find_element(By.LINK_TEXT,"Log")
login_element.click()
driver.quit()
'''

#### find_elements() returns multiple web-elements

'''
# Scenario 1 --> Locator matching with single web-element

elements = driver.find_elements(By.XPATH,"//*[@id='small-searchterms']")
print(len(elements))  #1
elements[0].send_keys("Macbook pro")
time.sleep(1)
driver.quit()
'''

'''
# Scenario 2 --> Locator matching with multiple web-elements

elements = driver.find_elements(By.XPATH,"//div[@class='footer']//a")
print(len(elements))  #23
print(elements[0].text) #Sitemap
# To capture all 23 links
for ele in elements:
    print(ele.text)
driver.quit()
'''
# Scenario 3 --> Element not available - returns Zero  not error ...!!!!

login_element = driver.find_elements(By.LINK_TEXT,"Log")
print('Elements Returned : ',len(login_element))
driver.quit()
