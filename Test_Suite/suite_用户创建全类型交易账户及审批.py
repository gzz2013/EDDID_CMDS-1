import unittest
from Test_Case.test_用户创建全类型交易账户及审批 import Test_creatUser新建用户创建所有类型账户


def get_suite_creatUser新建所有类型用户():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(Test_creatUser新建用户创建所有类型账户))

    return suite