import unittest
from Test_Case.test_创建换汇申请单 import Test_CreateExchange新建换汇申请单
# from Test_Case.saas_生码 import Test_生码
# from Test_Case.saas_新建营销活动 import Test_新建营销活动



def get_suite_CreateExchange新建换汇申请单():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(Test_CreateExchange新建换汇申请单))
    # suite.addTests(loader.loadTestsFromTestCase(Test_生码))

    # suite.addTests(loader.loadTestsFromTestCase(Test_新建商品))
    # suite.addTests(loader.loadTestsFromTestCase(Test_生码))
    # suite.addTests(loader.loadTestsFromTestCase(Test_新建营销活动))
    return suite