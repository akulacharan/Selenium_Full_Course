from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")

driver.maximize_window()

# Absolute XPath
#driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input").send_keys('macbook')
#driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input").click()


# Relative XPath
#driver.find_element(By.XPATH,"//*[@id='twotabsearchtextbox']").send_keys('iPhone')
#driver.find_element(By.XPATH,"//*[@id='nav-search-submit-button']").click()

'''
XPath options OR,AND,contains()

driver.get("https://accounts.lambdatest.com/register")

#OR
driver.find_element(By.XPATH,"//*[@id='name' or @name='name']").send_keys('Charanteja')
#AND
driver.find_element(By.XPATH,"//*[@id='email' and @name='email']").send_keys('Charanteja@gmail.com')

#contains()
driver.find_element(By.XPATH,"//*[contains(@id,'email')]").send_keys('Charanteja@gmail.com')

#starts-with()
driver.find_element(By.XPATH,"//*[starts-with(@name,'name')]").send_keys('Charanteja')

#text()
driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.find_element(By.XPATH,"//a[text()='Mobiles']").click()

'''