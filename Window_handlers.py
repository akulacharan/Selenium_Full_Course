import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")



driver.get("https://demo.automationtesting.in/Windows.html")

driver.find_element(By.XPATH,"//a/button[@class='btn btn-info']").click()

handles = driver.window_handles

for h in handles:
    driver.switch_to.window(h)
    time.sleep(2)
    print(driver.title)
    if driver.title == 'Frames & windows':
        driver.close()

time.sleep(8)

driver.quit()