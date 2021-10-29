import unittest
from Test_Case.test_创建出金申请单 import Test_CreatEquitiesWithdrawal
# from Test_Case.saas_生码 import Test_生码
# from Test_Case.saas_新建营销活动 import Test_新建营销活动



def get_suite_CreatEquitiesWithdrawal():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(Test_CreatEquitiesWithdrawal))

    return suite