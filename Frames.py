
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")



driver.get("https://demo.automationtesting.in/Frames.html")

'''Single frame example 
#Switching to frame
driver.switch_to.frame("SingleFrame")

driver.find_element(By.XPATH,"//div/input[@type='text']").send_keys("Hey you are entered into the frame")

driver.switch_to.default_content()
'''

#Dealing with nested frames

driver.find_element(By.XPATH,"//a[text()='Iframe with in an Iframe']").click()

outerframe = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")

driver.switch_to.frame(outerframe)

innerframe = driver.find_element(By.XPATH,"//iframe[@src='SingleFrame.html']")

driver.switch_to.frame(innerframe)

# filling the input element

driver.find_element(By.XPATH,"//div/input[@type='text']").send_keys("Finally you got it")

driver.switch_to.parent_frame()  #directly switched to the parent frame (i.e outerframe)

time.sleep(4)

driver.quit()
