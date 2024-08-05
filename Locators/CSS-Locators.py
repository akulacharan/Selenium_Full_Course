from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()



# Customized locators
driver.get("https://www.facebook.com/")
driver.maximize_window()

# tag & Id locator
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
# tagname is optional you can also use Id directly but # symbol must be used before.
#driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc")

# tag and class name
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys('abc@gmail.com')
#driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys('abc@gmail.com')

# Tag and Attribute
#driver.find_element(By.CSS_SELECTOR,"input[data-testid='royal_email']").send_keys('abc@gmail.com')
#driver.find_element(By.CSS_SELECTOR,"[data-testid='royal_email']").send_keys('abc@gmail.com')

# Tag , class & Attribute
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid='royal_pass']").send_keys("abc@gmail.com")



driver.close()

