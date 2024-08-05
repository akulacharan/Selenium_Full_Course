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
        # assertEqul
        #self.assertEqual('Google',titleOfWebpage,"Title is not matched")    # returns true if both title are same, else returns the msg
        self.assertNotEqual('Google',titleOfWebpage,'Webpages title are same')   # Returns true if both title are not same, else returns msg



if __name__ == "__main__":
    unittest.main()