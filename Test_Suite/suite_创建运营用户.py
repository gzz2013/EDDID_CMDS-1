import unittest
from Test_Case.cdms_创建用户 import Test_新建用户
# from Test_Case.saas_生码 import Test_生码
# from Test_Case.saas_新建营销活动 import Test_新建营销活动



def get_suite():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(Test_新建用户))
    # suite.addTests(loader.loadTestsFromTestCase(Test_生码))

    # suite.addTests(loader.loadTestsFromTestCase(Test_新建商品))
    # suite.addTests(loader.loadTestsFromTestCase(Test_生码))
    # suite.addTests(loader.loadTestsFromTestCase(Test_新建营销活动))
    return suite