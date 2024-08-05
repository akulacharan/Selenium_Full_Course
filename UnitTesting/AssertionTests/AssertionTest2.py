import unittest
import time
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        cService = webdriver.ChromeService(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")
        self.driver = webdriver.Chrome(service=cService)
        self.driver.get("https://www.google.co.in/")
        titleOfWebpage = self.driver.title
        print(titleOfWebpage)
        # assertTrue
        self.assertTrue('Google',titleOfWebpage)    # returns true if both title are same
        #self.assertFalse('Google',titleOfWebpage)   # Returns true if both title are not same


if __name__ == "__main__":
    unittest.main()