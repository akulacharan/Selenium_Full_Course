import unittest
import time

from selenium import webdriver

class SearchEngineTest(unittest.TestCase):
    def test_Google(self):
        cService = webdriver.ChromeService(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")
        self.driver = webdriver.Chrome(service=cService)
        self.driver.get("https://www.google.co.in/")
        print("The title of the page is :" + self.driver.title)
        self.driver.close()
        time.sleep(2)

    def test_Bing(self):
        cService = webdriver.ChromeService(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")
        self.driver = webdriver.Chrome(service=cService)
        self.driver.get("https://www.bing.com/")
        print("The title of the page is :" + self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()