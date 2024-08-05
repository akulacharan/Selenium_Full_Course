import unittest
import time

from selenium import webdriver


def setUpModule():  # Will be executed only once in the begining of the module
    print('Setup module is starting')

def tearDownModule():   # Will be executed once after completing executing everything in the module
    print('tearDown module is ended...')


class SearchEngineTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # This (setUpClass) method will execute only once in the begining of the class
        print('Opening Application.......!')

    @classmethod
    def tearDownClass(cls):  # This (tearDownClass) method will execute only once in the ending of the class
        print('Closing Application.')

    @classmethod
    def setUp(self):     # This method will execute before every test in our class
        cService = webdriver.ChromeService(executable_path=r"C:\Users\charanteja\Desktop\chromedriver.exe")
        self.driver = webdriver.Chrome(service=cService)
    @classmethod
    def tearDown(self):     # This method will execute after every test in our class
        self.driver.close()

    def test_Google(self):
        self.driver.get("https://www.google.co.in/")
        print("The title of the page is :" + self.driver.title)
        time.sleep(2)

    def test_Bing(self):
        self.driver.get("https://www.bing.com/")
        print("The title of the page is :" + self.driver.title)
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()