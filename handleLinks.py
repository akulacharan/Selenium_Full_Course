import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")

# Click on link

#driver.find_element(By.LINK_TEXT,"Digital downloads").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

# Find total number of links in a pege
#all_links_in_page = driver.find_elements(By.TAG_NAME,'a')
all_links_in_page = driver.find_elements(By.XPATH,'//a')
print("no of links : ",len(all_links_in_page))

for link in all_links_in_page:
    print(link.text)

time.sleep(2)

driver.quit()