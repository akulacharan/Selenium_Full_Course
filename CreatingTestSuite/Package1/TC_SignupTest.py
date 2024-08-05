import unittest


class SignupTest(unittest.TestCase):
    def test_SignByEmail(self):
        print("This is sign by email test")
        self.assertTrue(True)

    def test_SignByFacebook(self):
        print("This is sign by Facebook test")
        self.assertTrue(True)

    def test_SignByTwitter(self):
        print("This is sign by Twitter test")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()