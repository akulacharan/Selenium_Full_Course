import time
from selenium import webdriver

# to disable the popups
from selenium.webdriver.chrome.service import Service

opts = webdriver.ChromeOptions()
opts.add_argument('--disable-notifications')

driver = webdriver.Chrome(r"C:\Users\charanteja\Desktop\chromedriver.exe",chrome_options=opts)

driver.get("https://whatmylocation.com/")


time.sleep(80)

driver.quit()