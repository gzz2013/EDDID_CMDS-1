import unittest
from Test_Case.test_closeAcct账号关闭 import Test_closeAcct账号关闭




def get_suite_closeAcct账号关闭():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(Test_closeAcct账号关闭))

    return suite