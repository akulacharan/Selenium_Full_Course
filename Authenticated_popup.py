import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
'''
Actual_url = driver.get("https://the-internet.herokuapp.com/basic_auth")

Now we are bypassing by injecting username ans password into the url of the website below 
Syntax:  https:// username : password @abcdt.com

here username is admin and password is also admin.
'''


Injected_url = driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

time.sleep(4)

driver.quit()