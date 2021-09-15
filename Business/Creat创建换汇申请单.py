import requests
from Business.login import cdms_获取token
import logging
import time
from Common.com_sql.eddid_data_select import *
from Config.cdms_config import *
from Common.random_number import *
from Common.data_文本读写 import *




class CreateExchange():
    # 步骤1
    def createExchange创建换汇申请单(self):

        global clientId, applyAmount,eddidhost
        clientId=CreateExchangeclientId
        applyAmount=Randoms().randomAmount()

        #查询符合条件的换汇账号
        comp_account=cd_ac('NORMAL','CASH','EQUITIES',clientId)

        token = cdms_获取token()
        s = requests.Session()

        #引入url
        eddidhost = url
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
        logging.info("当前获取到applyAmount的值为：{}".format(applyAmount))
        logging.info("查询数据库cd_ac查询到的换汇账号为{}".format(comp_account))

        #将对应的数据写到文本，给用例读取后做断言
        Exchangeoderinfor=[]
        Exchangeoderinfor.append(clientId)
        Exchangeoderinfor.append(comp_account)
        Exchangeoderinfor.append(applyAmount)
        data_write('F:\\python\\EDDID_CDMS\\Data\\exchorderinfor.txt',Exchangeoderinfor)

        print("Exchangeoderinfor:",Exchangeoderinfor)
        # 将userinformationList写入文本
        print("记录数据的文件名为：exchorderinfor.txt，写入数据为:{}".format(Exchangeoderinfor))
        logging.info("记录数据的文件名为：exchorderinfor.txt，写入数据为:{}".format(Exchangeoderinfor))


        print("查询数据库cd_ac查询到的换汇账号为{}".format(comp_account))
        print("当前获取到applyAmount的值为：{}".format(applyAmount))
        data = {
            "fromCurrency": "HKD",
            "toCurrency": "USD",
            "exchangeRate": 7.76500,
            "clientId": clientId,
            "applyAmount": applyAmount,
            "accountId": comp_account,
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

        #设置等待时间
        print("等待系统录入数据后再提交审批，等待时间15s")
        logging.info("等待系统录入数据后再提交审批，等待时间15s")
        time.sleep(15)

        applyid=cd_exch(clientId,applyAmount)[0][0]

        token = cdms_获取token()
        s = requests.Session()
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

        logging.info("查询数据库cd_exch查询到applyid的值为：{}".format(applyid))
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
    def SQLCheckexchorder(self):
        time.sleep(8)
        # 通过直接调用cd_enty表查询
        Checkexchorder = cd_exch(clientId,applyAmount)
        print("通过'{}'账号和交易金额'{}'查询cd_exch表的结果为{}".format(clientId,applyAmount, Checkexchorder))
        logging.info("通过'{}'查询cd_exch表的结果为{}".format(clientId,Checkexchorder))
        return Checkexchorder


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