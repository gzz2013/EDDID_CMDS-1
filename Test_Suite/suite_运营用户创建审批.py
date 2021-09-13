import unittest
from Test_Case.test_运营用户创建审批 import Test_creatUser新建用户
# from Test_Case.saas_生码 import Test_生码
# from Test_Case.saas_新建营销活动 import Test_新建营销活动



def get_suite_creatUser新建用户():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(Test_creatUser新建用户))
    # suite.addTests(loader.loadTestsFromTestCase(Test_生码))

    # suite.addTests(loader.loadTestsFromTestCase(Test_新建商品))
    # suite.addTests(loader.loadTestsFromTestCase(Test_生码))
    # suite.addTests(loader.loadTestsFromTestCase(Test_新建营销活动))
    return suite