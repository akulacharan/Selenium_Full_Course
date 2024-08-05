from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
#driver.maximize_window()

#Note : "//a[contains(text(),'Infosys')]" --> This is the self node based on the self node we will find all the remaining parent,child nodes data

#self

#text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Infosys')]/self::a").text
#print(text_msg)


#parent
#text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Infosys')]/parent::td").text
#print(text_msg) #Infosys

#child

#childs = driver.find_elements(By.XPATH,"//a[contains(text(),'Infosys')]/ancestor::tr/child::td")
#for data in childs:
    #print(data.text)

#Ancestor
#text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Infosys')]/ancestor::tr").text
#print(text_msg)    #Infosys A 1,265.65 1,270.40 + 0.38

#Descendant
#descendants = driver.find_elements(By.XPATH,"//a[contains(text(),'Infosys')]/ancestor::tr/descendant::*")
#for data in descendants:
    #print(data.text)

#Following
#followings = driver.find_elements(By.XPATH,"//a[contains(text(),'Infosys')]/ancestor::tr/following::*")
#print(len(followings)) #730


#Following-sibling
#following_sibling = driver.find_elements(By.XPATH,"//a[contains(text(),'Infosys')]/ancestor::tr/following-sibling::*")
#print("The following siblings count is : ",len(following_sibling)) #74


#Preceding
#Precedings = driver.find_elements(By.XPATH,"//a[contains(text(),'Infosys')]/ancestor::tr/preceding::*")
#print(len(Precedings)) #3090

#Preceding-sibling
preceding_siblings = driver.find_elements(By.XPATH,"//a[contains(text(),'Infosys')]/ancestor::tr/preceding-sibling::*")
print("The preceding siblings count is : ",len(preceding_siblings)) #363

driver.quit()

