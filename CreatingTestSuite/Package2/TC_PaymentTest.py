import unittest

class PaymentTest(unittest.TestCase):

    def test_Paymentindollar(self):
        print("This is payment in dollar test")
        self.assertTrue(True)

    def test_Paymentinrupee(self):
        print("This is payment in rupee test")
        self.assertTrue(True)




if __name__ == '__main__':
    unittest.main()