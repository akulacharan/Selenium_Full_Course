import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time



class Test(unittest.TestCase):
    def test_Name(self):
        cService = webdriver.ChromeService(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")
        driver = webdriver.Chrome(service=cService)
        driver.get("https://www.google.co.in/")
        titleOfWebpage = driver.title + "df"
        print(titleOfWebpage)
        self.assertEqual("Google",titleOfWebpage,"Web pages title are not same")

if __name__ == "__main__":
    unittest.main()



