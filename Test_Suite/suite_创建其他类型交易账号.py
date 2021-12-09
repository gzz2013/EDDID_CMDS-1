import unittest
from Test_Case.test_创建其他类型交易账号 import Test_CreatUser创建其他类型交易账号


def get_suite_CreatUser创建其他类型交易账号():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(Test_CreatUser创建其他类型交易账号))

    return suite