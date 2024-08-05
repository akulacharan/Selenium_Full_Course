#assetIn  assertNotIn

import unittest

class Test(unittest.TestCase):
    def testName(self):
        list =["Python","Selenium","Java"]
        #self.assertIn("Python",list)         # Returns true if Python present in list
        self.assertNotIn("Ruby",list)        # Returns true if Python  not present in list



if __name__ == "__main__":
    unittest.main()