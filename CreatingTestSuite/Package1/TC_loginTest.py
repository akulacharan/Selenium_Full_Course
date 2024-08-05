import unittest

class LoginTest(unittest.TestCase):
    def test_LoginByEmail(self):
        print("This is login by email test")
        self.assertTrue(True)

    def test_LoginByFacebook(self):
        print("This is login by Facebook test")
        self.assertTrue(True)

    def test_LoginByTwitter(self):
        print("This is login by Twitter test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()