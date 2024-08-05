# Relational comparision
# assertGrater

import unittest

class Test(unittest.TestCase):
    def testName(self):
        self.assertGreater(100,10)           # Here 100 is greater than 10
        self.assertGreaterEqual(100,10)      # Here 100 is greater than and also equal to 10

        self.assertLess(10,200)              # Here 10 is less than 200
        self.assertLessEqual(10,200)         # Here 10 is less than and equal to 200



if __name__ == "__main__":
    unittest.main()