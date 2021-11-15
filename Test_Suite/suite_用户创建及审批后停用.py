import unittest
from Test_Case.test_用户创建审批后停用 import Test_creatUser新建用户后停用


def get_suite_creatUser新建用户后停用():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(Test_creatUser新建用户后停用))

    return suite