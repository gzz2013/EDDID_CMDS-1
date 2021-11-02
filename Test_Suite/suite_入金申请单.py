import unittest
from Test_Case.test_创建入金申请单 import Test_CreatEquitiesDeposit入金




def get_suite_CreatEquitiesDeposit入金():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(Test_CreatEquitiesDeposit入金))

    return suite