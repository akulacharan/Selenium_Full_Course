import unittest
import time

def setUpModule():  # Will be executed only once in the begining of the module
    print('Setup module is starting')

def tearDownModule():   # Will be executed once after completing executing everything in the module
    print('tearDown module is ended...')

class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):  # This (setUp) method will execute before every method in the class
        print('This is login test')

    @classmethod
    def tearDown(self):  # This (tearDown) method will execute after every method in the class
        print("This is logout test")

    @classmethod
    def setUpClass(cls):  # This (setUpClass) method will execute only once in the begining of the class
        print('Opening Application.......!')

    @classmethod
    def tearDownClass(cls):  # This (tearDownClass) method will execute only once in the ending of the class
        print('Closing Application.')

    def test_Search(self):
        print('This is test search')

    def test_AdvancedSearch(self):
        print('This is advanced search')

    def test_Prepaid(self):
        print('This is Prepaid search')

    def test_Postpaid(self):
        print('This is Postpaid search')

if __name__ == "__main__":
    unittest.main()