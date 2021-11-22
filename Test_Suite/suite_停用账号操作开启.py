import unittest
from Test_Case.test_enableAcct账号开启 import Test_enableAcct停用后开启




def get_suite_enableAcct停用后开启():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(Test_enableAcct停用后开启))

    return suite