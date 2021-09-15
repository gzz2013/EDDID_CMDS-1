import unittest
from Test_Case.test_运营用户创建结构性产品账户及审批 import Test_creatUser没有结构性产品账号及申请结构性产品审批




def get_suite_creatUser没有结构性产品账号及申请结构性产品审批():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(Test_creatUser没有结构性产品账号及申请结构性产品审批))

    return suite