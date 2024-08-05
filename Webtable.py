
# 1) Count number of Rows & Coloumns
# 2) Read specific row & coloumn data
# 3) Read all the rows & coloumns data
# 4) Read data based on condition (List books name whose name is Mukesh)



from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

# 1) Count number of rows & Coloumns

noOfRows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))  #7
noOfColumns = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/th"))  #4

# 2) Read specific row & coloumn data
data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[3]/td[3]").text
print(data)

'''
# 3) Read all the rows & coloumns data
for r in range(2,noOfRows+1):
    for c in range(1,noOfColumns+1):
        d = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
            print(d,end="    ")
    print()
'''

# 4) Read data based on condition (List books name whose name is Mukesh)
for r in range(2,noOfRows+1):
    authorname = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    if authorname == "Mukesh":
        book = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
        price = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[4]").text
        print(book,"        ",authorname,"     ",price)


time.sleep(4)

driver.quit()