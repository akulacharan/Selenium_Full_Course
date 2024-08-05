from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")
driver.maximize_window()

driver.get("https://mdbootstrap.com/docs/standard/forms/multi-range-slider/")
time.sleep(2)

clicking_on_AcceptCookies = driver.find_element(By.XPATH,"//*[@id='accept_cookies_btn']").click()

min_slider = driver.find_element(By.XPATH,"(//div[contains(@role,'slider')])[3]")
max_slider = driver.find_element(By.XPATH,"(//div[contains(@role,'slider')])[4]")

print('Location of sliders before moving....')

print(min_slider.location)   # {'x': 306, 'y': 1150}
print(max_slider.location)   # {'x': 1237, 'y': 1150}

action = ActionChains(driver)

''' 
Now we have to move the sliders by increasing/Decreasing the X-axis location,
as we are moving the slider only in X-axis, 
here we can ignore Y-axis and give the value 0 in the offset method.
'''

action.drag_and_drop_by_offset(min_slider,100,0).perform()
# Here we have given 100 means it will move the left slider from 306 to 406 location

action.drag_and_drop_by_offset(max_slider,-150,0).perform()
# Here we have given -150 means it will move the right slider from 1237 to 1136 location


print('Location of sliders after moving....')

print(min_slider.location)      # {'x': 505, 'y': 1150}
print(max_slider.location)      # {'x': 1136, 'y': 1150}

time.sleep(4)
driver.quit()
