import requests
from Business.login import cdms_获取token
from Common.random_number import Randoms
import logging
from Common.com_sql.eddid_data_update import *
import time
from Common.com_sql.eddid_data_select import *



class CreateExchange():
    # 步骤1
    def createExchange创建换汇申请单(self):

        global clientId, applyAmount
        clientId=11431
        applyAmount=7766
        #查询符合条件的换汇账号
        a=cd_ac('NORMAL','CASH','EQUITIES',11431)

        token = cdms_获取token()
        s = requests.Session()
        eddidhost = "http://sit-cdms.ynm3k.com/"
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        createExchangeturl = eddidhost + "/api/funds/createExchange"
        print("createExchangeturl为:", createExchangeturl)

        # logging.info("提交审核获取到的手机号为：{}".format(phone))
        # global applyId
        # applyId = cd_clnt_apply_info(phone)
        print("查询数据库cd_ac查询到accountId的值为：{}".format(a))
        print("当前获取到applyAmount的值为：{}".format(applyAmount))
        data = {
            "fromCurrency": "HKD",
            "toCurrency": "USD",
            "exchangeRate": 7.76500,
            "clientId": 11431,
            "applyAmount": applyAmount,
            "accountId": a,
            "accountCategory": "securitiesCash",
            "applySource": 4
        }
        print("data=", data)
        createExchangeResp = s.post(url=createExchangeturl, headers=headers, json=data)
        logging.info("步骤1提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(createExchangeturl,data, createExchangeResp.text))
        print("步骤1提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(createExchangeturl,data, createExchangeResp.text))
        return createExchangeResp

    # 步骤2
    def auditExchange提交审核换汇申请单(self):
        applyid=cd_exch(clientId,applyAmount)

        token = cdms_获取token()
        s = requests.Session()
        eddidhost = "http://sit-cdms.ynm3k.com/"
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        auditExchangeurl = eddidhost + "/api/funds/auditExchange"
        print("auditExchangeurl为:", auditExchangeurl)

        # logging.info("提交审核获取到的手机号为：{}".format(phone))
        # global applyId
        # applyId = cd_clnt_apply_info(phone)
        print("查询数据库cd_exch查询到applyid的值为：{}".format(applyid))
        data = {
            "applyId": applyid,
            "approvalResult": "PASS",
            "fileList": [

            ],
            "statusCode": "SETL"
        }
        print("data=", data)
        auditExchangeResp = s.post(url=auditExchangeurl, headers=headers, json=data)
        logging.info("步骤2提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(auditExchangeurl,data, auditExchangeResp.text))
        print("步骤2提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(auditExchangeurl,data, auditExchangeResp.text))
        return auditExchangeResp

if __name__=="__main__":
    a=1
    CreateExchange = CreateExchange()
    for i in range(a):
        time.sleep(6)
        # 实例化CreatUser
        print("步骤1：", CreateExchange.createExchange创建换汇申请单().text)
        time.sleep(6)
        print("步骤2：", CreateExchange.auditExchange提交审核换汇申请单().text)
        time.sleep(6)