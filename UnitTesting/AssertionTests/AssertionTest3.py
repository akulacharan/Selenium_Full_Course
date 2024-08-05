#assertIsNone  assertIsNotNone

import  unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        #driver = None
        driver = "Notnone"
        #self.assertIsNone(driver)  # Returns true if the driver variable value is None
        self.assertIsNotNone(driver)   # Returns true if the driver variable value is not None

if __name__ == "__main__":
    unittest.main()