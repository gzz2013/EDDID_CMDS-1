import unittest
import time
import logging
from Business.Creat创建换汇申请单 import CreateExchange



class Test_CreateExchange新建换汇申请单(unittest.TestCase):

    def setUp(self):
        self.CreateExchange = CreateExchange()
        logging.info("初始化CreateExchange已完成")

    def test_01_createExchange创建换汇申请单(self):
        createExchange = self.CreateExchange.createExchange创建换汇申请单()
        self.assertEqual(200, createExchange.status_code)
        self.assertEqual("操作成功", createExchange.json().get("msg"))
        print("已执行用例1===============================================================")

    def test_02_auditExchange提交审核换汇申请单(self):
        auditExchange = self.CreateExchange.auditExchange提交审核换汇申请单()
        self.assertEqual(200, auditExchange.status_code)
        self.assertEqual("操作成功", auditExchange.json().get("msg"))
        print("已执行用例2===============================================================")

    # def test_03_operatingWorkFlowFirst提交锁(self):
    #     operatingWorkFlowFirst = self.creatUser.operatingWorkFlowFirst提交锁()
    #     self.assertEqual(200, operatingWorkFlowFirst.status_code)
    #     self.assertEqual("操作成功", operatingWorkFlowFirst.json().get("msg"))
    #     self.assertEqual("操作成功", operatingWorkFlowFirst.json().get("data")[0].get("operatingMessage"))
    #     print("已执行用例3=======")
    #
    # def test_04_saveRiskAssessment风控评估提交(self):
    #     saveRiskAssessment = self.creatUser.saveRiskAssessment风控评估提交()
    #     self.assertEqual(200, saveRiskAssessment.status_code)
    #     self.assertEqual("操作成功", saveRiskAssessment.json().get("msg"))
    #     print("已执行用例4=======")

    #
    def tearDown(self):
        a = 6
        time.sleep(a)
        logging.info("接口请求完成后，等待系统处理数据，等待{}秒".format(a))
