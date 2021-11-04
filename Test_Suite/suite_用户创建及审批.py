import unittest
from Test_Case.test_用户创建审批 import Test_creatUser新建用户


def get_suite_creatUser新建用户():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(Test_creatUser新建用户))

    return suite