import unittest

from CreatingTestSuite.Package1.TC_loginTest import LoginTest
from CreatingTestSuite.Package1.TC_SignupTest import SignupTest

from CreatingTestSuite.Package2.TC_PaymentTest import PaymentTest
from CreatingTestSuite.Package2.TC_PaymentReturnTest import PaymentReturnsTest

# Get all the test methods from Logintest,Signuptest,Paymenttest,PaymentReturnsTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)


#Creating Test suite

SanityTestSuite = unittest.TestSuite([tc1,tc2])             # sanity test suite
FunctionalTestSuite = unittest.TestSuite([tc3,tc4])         # Functional test suite
MasterTestSuite = unittest.TestSuite([tc1,tc2,tc3,tc4])     # Master test suite

#unittest.TextTestRunner().run(SanityTestSuite)
#unittest.TextTestRunner().run(FunctionalTestSuite)

unittest.TextTestRunner(verbosity=2).run(MasterTestSuite)