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

        self.creatUser=CreatUser()
        logging.info("初始化CreatUser")

    def test_applyClient用户资料提交用例校验(self):

        applyClient=self.creatUser.ApplyClinet资料提交()
        # logging.info("资料提交接口'/api/client/applyClient'的响应结果为:'{}'".format(applyClient))
        self.assertEqual(200, applyClient.status_code)
        self.assertEqual("操作成功", applyClient.json().get("msg"))

    def test_submitAudit提交审核(self):

        submitAudit=self.creatUser.SubmitAudit提交审核()
        self.assertEqual(200, submitAudit.status_code)
        self.assertEqual("操作成功", submitAudit.json().get("msg"))

    def tearDown(self):
        a=4
        time.sleep(a)
        logging.info("接口请求完成后，等待系统处理数据，等待{}秒".format(a))