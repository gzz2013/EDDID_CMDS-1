import unittest
import time
import logging
from Common.eddid_data_select import *
from Common.eddid_data_update import *
# import requests
# from Business.login import cdms_获取token
import json
from Common.random_number import Randoms
from Business.CreatUser import CreatUser


class Test_新建用户(unittest.TestCase):

    def setUp(self):
        self.creatUser = CreatUser()
        logging.info("初始化CreatUser")

    def test_1_applyClient用户资料提交用例校验(self):
        applyClient = self.creatUser.ApplyClinet资料提交()
        # logging.info("资料提交接口'/api/client/applyClient'的响应结果为:'{}'".format(applyClient))
        self.assertEqual(200, applyClient.status_code)
        self.assertEqual("操作成功", applyClient.json().get("msg"))

    def test_2_submitAudit提交审核(self):
        submitAudit = self.creatUser.SubmitAudit提交审核()
        self.assertEqual(200, submitAudit.status_code)
        self.assertEqual("操作成功", submitAudit.json().get("msg"))

    def test_3_operatingWorkFlowFirst提交锁(self):
        operatingWorkFlowFirst = self.creatUser.operatingWorkFlowFirst提交锁()
        self.assertEqual(200, operatingWorkFlowFirst.status_code)
        self.assertEqual("操作成功", operatingWorkFlowFirst.json().get("msg"))
        self.assertEqual("操作成功", operatingWorkFlowFirst.json().get("data")[0].get("operatingMessage"))

    def test_4_saveRiskAssessment风控评估提交(self):
        saveRiskAssessment = self.creatUser.saveRiskAssessment风控评估提交()
        self.assertEqual(200, saveRiskAssessment.status_code)
        self.assertEqual("操作成功", saveRiskAssessment.json().get("msg"))

    def test_5_operatingWorkFlow内部人员审核(self):
        operatingWorkFlow = self.creatUser.operatingWorkFlow内部人员审核()
        self.assertEqual(200, operatingWorkFlow.status_code)
        self.assertEqual("操作成功", operatingWorkFlow.json().get("msg"))
        self.assertEqual("true", operatingWorkFlow.json().get("data")[0].get("result"))

    def test_6_operatingWorkFlowNo不用锁定审核通过(self):
        operatingWorkFlowNo = self.creatUser.operatingWorkFlowNo不用锁定审核通过()
        self.assertEqual(200, operatingWorkFlowNo.status_code)
        self.assertEqual("操作成功", operatingWorkFlowNo.json().get("msg"))
        self.assertEqual("true", operatingWorkFlowNo.json().get("data")[0].get("result"))

    def test_7_operatingWorkFlowAgaint提交锁(self):
        operatingWorkFlowAgaint = self.creatUser.operatingWorkFlowAgain提交锁()
        self.assertEqual(200, operatingWorkFlowAgaint.status_code)
        self.assertEqual("操作成功", operatingWorkFlowAgaint.json().get("msg"))
        self.assertEqual("操作成功", operatingWorkFlowAgaint.json().get("data")[0].get("operatingMessage"))

    def test_8_batchOperatingWorkFlow批量生成账号确定(self):
        batchOperatingWorkFlow = self.creatUser.batchOperatingWorkFlow批量生成账号确定()
        self.assertEqual(200, batchOperatingWorkFlow.status_code)
        self.assertEqual("操作成功", batchOperatingWorkFlow.json().get("msg"))
        self.assertEqual("true", batchOperatingWorkFlow.json().get("data")[0].get("result"))

    def test_9_operatingWorkFlowThird提交锁(self):
        operatingWorkFlowThird = self.creatUser.operatingWorkFlowThird提交锁()
        self.assertEqual(200, operatingWorkFlowThird.status_code)
        self.assertEqual("操作成功", operatingWorkFlowThird.json().get("msg"))
        self.assertEqual("操作成功", operatingWorkFlowThird.json().get("data")[0].get("operatingMessage"))
        self.assertEqual("true", operatingWorkFlowThird.json().get("data")[0].get("result"))

    def test_10_batchOperatingWorkFlowEnd批量确认(self):
        batchOperatingWorkFlowEnd = self.creatUser.batchOperatingWorkFlowEnd批量确认()
        self.assertEqual(200, batchOperatingWorkFlowEnd.status_code)
        self.assertEqual("操作成功", batchOperatingWorkFlowEnd.json().get("msg"))
        # self.assertEqual(applyId, operatingWorkFlowThird.json().get("data")[0].get("applyId"))
        self.assertEqual("true", batchOperatingWorkFlowEnd.json().get("data")[0].get("result"))

    def tearDown(self):
        a = 4
        time.sleep(a)
        logging.info("接口请求完成后，等待系统处理数据，等待{}秒".format(a))
