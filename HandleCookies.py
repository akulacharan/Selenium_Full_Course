from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os


driver = webdriver.Chrome(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)


driver.get("https://demo.nopcommerce.com/")

# Capture cookies from browser
all_cookies = driver.get_cookies()
print('Len of cookies',len(all_cookies))

'''
# Print details of all cookies
for cookie in all_cookies:
    # print(cookie)
    print(cookie.get('name'),":",cookie.get('value'))
'''


# To create our own cookie
driver.add_cookie({'name':'Cherry','value':'123456'})
all_cookies = driver.get_cookies()
print('Size of cookies after adding my cookie',len(all_cookies))
print(all_cookies)



# Delete specific cookie from the browser
driver.delete_cookie('Cherry')
all_cookies = driver.get_cookies()
print('Size of cookies after adding my cookie',len(all_cookies))
print(all_cookies)

# Delete all cookies
driver.delete_all_cookies()
all_cookies = driver.get_cookies()
print('Size of cookies after adding my cookie',len(all_cookies))
print(all_cookies)

time.sleep(4)
driver.quit()