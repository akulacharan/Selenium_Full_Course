from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import openpyxl
import XLUtils




driver = webdriver.Chrome(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.find_element(By.XPATH,"//*[@id='wzrk-cancel']").click()
print('clicked on cancel')

file = r"C:\Users\charanteja\PycharmProjects\SeleniumUpdatedCourse\Excel\PrincipleTestingFile.xlsx"  # Test data file

rows = XLUtils.getRowCount(file,'Sheet1')


for r in range(2,rows+1):

    pric = XLUtils.readData(file, 'Sheet1', r, 1)
    rateOfInterest = XLUtils.readData(file, 'Sheet1', r, 2)
    per1 = XLUtils.readData(file, 'Sheet1', r, 3)
    per2 = XLUtils.readData(file, 'Sheet1', r, 4)
    feq = XLUtils.readData(file, 'Sheet1', r, 5)
    Exp_MV = XLUtils.readData(file, 'Sheet1', r, 6)

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

    matured_amount = float(matured_amount)

    # Validation

    if matured_amount == Exp_MV:
        print('Test Passed')
        XLUtils.writeData(file, 'Sheet1', r, 8, 'Pass')
        XLUtils.fillGreenColor(file, 'Sheet1', r, 8)
    else:
        print('Test Failed')
        XLUtils.writeData(file, 'Sheet1', r, 8, 'Fail')
        XLUtils.fillRedColor(file, 'Sheet1', r, 8)

    driver.find_element(By.XPATH, "//a[@onclick='javascript:reset_fdcalcfrm();']").click()  # Clearing the data by "Clear" button
    time.sleep(1)

time.sleep(4)
driver.close()

