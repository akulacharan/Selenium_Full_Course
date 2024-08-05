import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
mywait = WebDriverWait(driver,timeout=10)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# driver will wait explicitly until the "Click on JS Alert" element appears in the webpage.

alert_link = mywait.until(EC.presence_of_element_located((By.XPATH,"//button[@onclick='jsAlert()']")))
alert_link.click()
time.sleep(1)
driver.switch_to_alert().accept()
#driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()

confirm_alert = driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']")
confirm_alert.click()


conf_alert = driver.switch_to_alert()
print(conf_alert.text)
conf_alert.dismiss()

# example for prompt input
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()

prompt_input = driver.switch_to_alert()
prompt_input.send_keys('Charan teja')
prompt_input.accept()
time.sleep(4)

driver.quit()