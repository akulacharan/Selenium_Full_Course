import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
#mywait = WebDriverWait(driver,10)  # explicit wait declaration #basic
mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     Exception]
                       )


driver.get("https://www.google.com/")
driver.maximize_window()

searchbox = driver.find_element(By.NAME,'q')
searchbox.send_keys('selenium')
searchbox.submit()  #It will press enter button

searchlink = mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
searchlink.click()

driver.quit()



#driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()