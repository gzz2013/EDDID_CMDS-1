import unittest
from Test_Case.test_创建大额入金申请单 import Test_CreatEquitiesDeposit大额入金




def get_suite_CreatEquitiesDeposit大额入金():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(Test_CreatEquitiesDeposit大额入金))

    return suite