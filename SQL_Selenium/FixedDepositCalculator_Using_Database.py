from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import mysql.connector




cService = webdriver.ChromeService(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")

driver = webdriver.Chrome(service = cService)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.find_element(By.XPATH,"//*[@id='wzrk-cancel']").click()
print('clicked on cancel')

# To get data from the database first we have to create the table with the expected data in our database
    """
            use mydb;        # use mydb database which is already available.

            create table caldata (principle int,rateOfIntrest int, per1 int, per2 varchar(255),frequency varchar(255),maturityvalue int);     # Creating a table
            
            Insert commands to enter data into the table :
            
            insert into caldata values (20000,10,2,'year(s)','Simple Interest',24000);
            insert into caldata values (40000,15,5,'year(s)','Simple Interest',70000);
            insert into caldata values (50000,10,3,'month(s)','Simple Interest',51250);
            insert into caldata values (75000,12,2,'month(s)','Simple Interest',76500);
            insert into caldata values (745000,12,2,'day(s)','Simple Interest',75045);

        
    """



try:
    con = mysql.connector.connect(
        host="localhost",
        port=143,
        user="charan",
        password="charan",
        database="mydb")   #Connecting with database

    curs = con.cursor()  # Create cursor
    curs.execute("select * from caldata")  # Ececute query through cursor


    for row in curs:

        pric = row[0]
        rateOfInterest = row[1]
        per1 = row[2]
        per2 = row[3]
        feq = row[4]
        Exp_MV = row[5]

        principal = driver.find_element(By.XPATH, "//input[@name='principal']").send_keys(pric)
        interest = driver.find_element(By.XPATH, "//input[@name='interest']").send_keys(rateOfInterest)
        tenure = driver.find_element(By.XPATH, "//input[@name='tenure']").send_keys(per1)

        tenure_period = driver.find_element(By.XPATH, "//select[@name='tenurePeriod']")
        select = Select(tenure_period)
        select.select_by_visible_text(str(per2))

        frequency = driver.find_element(By.XPATH, "//select[@name='frequency']")
        select = Select(frequency)
        select.select_by_visible_text(feq)

        calculate = driver.find_element(By.XPATH, "//a[@onclick='return getfdMatVal(this);']").click()

        matured_amount = driver.find_element(By.XPATH, "//span[@id='resp_matval']").text

        if matured_amount == matured_amount:
            print('Matured Amount is Correct')
        else:
            print('Matured Amount is Not-Correct')



        driver.find_element(By.XPATH, "//a[@onclick='javascript:reset_fdcalcfrm();']").click()  # Clearing the data by "Clear" button
        time.sleep(1)

    #con.commit()   # Commit the transaction means save the transaction
    con.close()    # Close the connection

except:
    print(print('Connection is Unsuccessful'))

time.sleep(4)
driver.close()

