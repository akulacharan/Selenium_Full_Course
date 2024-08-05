import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("http://www.deadlinkcity.com/")
count = 0
all_lkinks_in_page = driver.find_elements(By.TAG_NAME,'a')

for link in all_lkinks_in_page:
    url = link.get_attribute('href')
    try:
        response = requests.head(url)
        #print(response)
    except:
        None

    if response.status_code>=400:
        print(url," is broken link")
        count +=1
    else:
        print(url," is valid link")

print("Total broken links count : ",count)

driver.quit()