import unittest
import time
import logging
from Business.CreatUser import CreatUser


class Test_新建用户(unittest.TestCase):

    def setUp(self):
        self.creatUser = CreatUser()
        logging.info("初始化CreatUser")

    def test_01_applyClient用户资料提交用例校验(self):
        applyClient = self.creatUser.ApplyClinet资料提交()
        self.assertEqual(200, applyClient.status_code)
        self.assertEqual("操作成功", applyClient.json().get("msg"))
        print("已执行用例1=======")

    def test_02_submitAudit提交审核(self):
        submitAudit = self.creatUser.SubmitAudit提交审核()
        self.assertEqual(200, submitAudit.status_code)
        self.assertEqual("操作成功", submitAudit.json().get("msg"))
        print("已执行用例2=======")

    def test_03_operatingWorkFlowFirst提交锁(self):
        operatingWorkFlowFirst = self.creatUser.operatingWorkFlowFirst提交锁()
        self.assertEqual(200, operatingWorkFlowFirst.status_code)
        self.assertEqual("操作成功", operatingWorkFlowFirst.json().get("msg"))
        self.assertEqual("操作成功", operatingWorkFlowFirst.json().get("data")[0].get("operatingMessage"))
        print("已执行用例3=======")

    def test_04_saveRiskAssessment风控评估提交(self):
        saveRiskAssessment = self.creatUser.saveRiskAssessment风控评估提交()
        self.assertEqual(200, saveRiskAssessment.status_code)
        self.assertEqual("操作成功", saveRiskAssessment.json().get("msg"))
        print("已执行用例4=======")

    def test_05_operatingWorkFlow内部人员审核(self):
        operatingWorkFlow = self.creatUser.operatingWorkFlow内部人员审核()
        self.assertEqual(200, operatingWorkFlow.status_code)
        self.assertEqual("操作成功", operatingWorkFlow.json().get("msg"))
        self.assertEqual(True, operatingWorkFlow.json().get("data")[0].get("result"))
        print("已执行用例5=======")

    def test_06_operatingWorkFlowNo不用锁定审核通过(self):
        operatingWorkFlowNo = self.creatUser.operatingWorkFlowNo不用锁定审核通过()
        self.assertEqual(200, operatingWorkFlowNo.status_code)
        self.assertEqual("操作成功", operatingWorkFlowNo.json().get("msg"))
        self.assertEqual(True, operatingWorkFlowNo.json().get("data")[0].get("result"))
        print("已执行用例6=======")

    def test_07_operatingWorkFlowAgaint提交锁(self):
        operatingWorkFlowAgaint = self.creatUser.operatingWorkFlowAgain提交锁()
        self.assertEqual(200, operatingWorkFlowAgaint.status_code)
        self.assertEqual("操作成功", operatingWorkFlowAgaint.json().get("msg"))
        self.assertEqual("操作成功", operatingWorkFlowAgaint.json().get("data")[0].get("operatingMessage"))
        print("已执行用例7=======")

    def test_08_batchOperatingWorkFlow批量生成账号确定(self):
        batchOperatingWorkFlow = self.creatUser.batchOperatingWorkFlow批量生成账号确定()
        self.assertEqual(200, batchOperatingWorkFlow.status_code)
        self.assertEqual("操作成功", batchOperatingWorkFlow.json().get("msg"))
        self.assertEqual(True, batchOperatingWorkFlow.json().get("data")[0].get("result"))
        print("已执行用例8=======")

    # @unittest.skip("我在调试")
    def test_09_operatingWorkFlowThird提交锁(self):
        operatingWorkFlowThird = self.creatUser.operatingWorkFlowThird提交锁()
        self.assertEqual(200, operatingWorkFlowThird.status_code)
        self.assertEqual("操作成功", operatingWorkFlowThird.json().get("msg"))
        self.assertEqual("操作成功", operatingWorkFlowThird.json().get("data")[0].get("operatingMessage"))
        self.assertEqual(True, operatingWorkFlowThird.json().get("data")[0].get("result"))
        print("已执行用例9=======")

    def test_10_batchOperatingWorkFlowEnd批量确认(self):
        batchOperatingWorkFlowEnd = self.creatUser.batchOperatingWorkFlowEnd批量确认()
        self.assertEqual(200, batchOperatingWorkFlowEnd.status_code)
        self.assertEqual("操作成功", batchOperatingWorkFlowEnd.json().get("msg"))
        self.assertEqual(True, batchOperatingWorkFlowEnd.json().get("data")[0].get("result"))

    #
    def tearDown(self):
        a = 4
        time.sleep(a)
        logging.info("接口请求完成后，等待系统处理数据，等待{}秒".format(a))
