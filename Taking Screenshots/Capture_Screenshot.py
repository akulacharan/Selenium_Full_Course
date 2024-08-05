from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


driver = webdriver.Chrome(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")
driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")

# driver.save_screenshot('C:\\Users\\charanteja\\PycharmProjects\\SeleniumUpdatedCourse\\Taking Screenshots\\Homepage.png')

# driver.save_screenshot(os.getcwd()+"\\Homepage.png")

# driver.get_screenshot_as_file(os.getcwd()+"\\Homepage.png")

# driver.get_screenshot_as_png()   driver.get_screenshot_as_base64()  Saves screenshot in binary format again we have to encode it to grt the image

time.sleep(4)
driver.quit()