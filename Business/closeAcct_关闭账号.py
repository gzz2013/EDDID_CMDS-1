import requests
from Business.login import cdms_获取token
from Common.random_number import Randoms
import logging
from Common.com_sql.eddid_data_update import *
import time
from Common.com_sql.eddid_data_select import *
from Config.cdms_config import *
from Common.data_文本读写 import *


class CloseAcct账号关闭():

    # 账号开启前确认账号的状态是否是已经关闭
    def SQLCheck_ac_stat_front(self):
        global clnt
        clnt = datahandle(data_read('F:\\python\\EDDID_CDMS\\Data\\unableAcct.txt'))

        # print("步骤13执行完成，通过clnt='{}'查询cd_ac表的结果为{}".format(ac_id[0]))
        # 通过交易账户直接调用cd_ac表查询
        Check_ac_stat_front = cd_ac_id(clnt[0])
        print("步骤1查询账号当前状态执行完成，通过clnt='{}'查询cd_ac表的结果为{}".format(clnt[0], Check_ac_stat_front))
        logging.info("步骤1查询账号当前状态执行完成，通过clnt='{}'查询cd_ac表的结果为{}".format(clnt[0], Check_ac_stat_front))
        return Check_ac_stat_front

    # 账号停用发起
    def closeAcct账号关闭(self):
        global token, eddidhost, s, cookfront
        # 生成新邮箱
        eddidhost = url
        token=cdms_获取token()
        # token = data_read('F:\\python\\EDDID_CDMS\\Data\\token.txt')
        s = requests.Session()
        # cookies的前缀
        cookfront = cookfr
        headers = {
            "Accept": "application/x-www-form-urlencoded, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": cookfront + token
        }
        print("当前token为:{}".format(token))
        print("headers", headers)
        closeAccturl = eddidhost + "/api/acct/closeAcct"
        logging.info("提交开启的交易账号为：{}".format(clnt))
        print("提交开启的交易账号为：{}".format(clnt))
        data = {
            "accountId": clnt,
            "suspendReason": "自动化测试账号开启"
        }
        print("data=", data)
        closeAcctResp = s.post(url=closeAccturl, headers=headers, data=data)
        logging.info("步骤2提交接口'{}';请求参数为:{};的响应结果为:'{}'".format(closeAccturl, data, closeAcctResp.text))
        print("步骤2提交接口'{}';请求参数为:{};响应结果为:'{}'".format(closeAccturl, data, closeAcctResp.text))
        return closeAcctResp

    # 账号开启后校验状态
    def SQLCheck_ac_stat_after(self):
        # 通过交易账户直接调用cd_ac表查询
        Check_ac_stat_after = cd_ac_id(clnt[0])
        print("步骤3执行完成，通过clnt='{}'查询cd_ac表的结果为{}".format(clnt, Check_ac_stat_after))
        logging.info("步骤3执行完成，通过clnt='{}'查询cd_ac表的结果为{}".format(clnt, Check_ac_stat_after))
        return Check_ac_stat_after


if __name__ == "__main__":
    a = 1
    closeAcct = CloseAcct账号关闭()
    for i in range(a):
        # 实例化CreatUser
        print("=====================================步骤1：", closeAcct.SQLCheck_ac_stat_front())
        time.sleep(10)
        print("=====================================步骤2：", closeAcct.closeAcct账号关闭().text)
        time.sleep(10)
        print("=====================================步骤3：", closeAcct.SQLCheck_ac_stat_after())
        time.sleep(4)
