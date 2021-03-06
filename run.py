import unittest
import HTMLReport
from Business.login import cdms_获取token
from Common.data_文本读写 import *

from Test_Suite import suite_用户创建及审批, suite_用户创建结构性产品及审批, suite_换汇申请单, suite_出金申请单, suite_入金申请单, suite_大额入金申请单, \
    suite_用户创建全类型交易账户及审批, suite_用户创建及审批后停用, suite_停用账号操作开启, suite_账号关闭,suite_创建其他类型交易账号,suite_申请添加银行卡


#收集用例之前先把token写到对应文件
# token = cdms_获取token()
# 将token写入文本
# data_write('F:\\python\\EDDID_CDMS\\Data\\token.txt', token)

suite = unittest.TestSuite()
suite.addTests(suite_用户创建及审批.get_suite_creatUser新建用户())
suite.addTests(suite_换汇申请单.get_suite_CreateExchange新建换汇申请单())
suite.addTests(suite_用户创建结构性产品及审批.get_suite_creatUser没有结构性产品账号及申请结构性产品审批())
suite.addTests(suite_出金申请单.get_suite_CreatEquitiesWithdrawal出金())
suite.addTests(suite_入金申请单.get_suite_CreatEquitiesDeposit入金())
suite.addTests(suite_大额入金申请单.get_suite_CreatEquitiesDeposit大额入金())
suite.addTests(suite_用户创建全类型交易账户及审批.get_suite_creatUser新建所有类型用户())
suite.addTests(suite_用户创建及审批后停用.get_suite_creatUser新建用户后停用())
suite.addTests(suite_停用账号操作开启.get_suite_enableAcct停用后开启())
suite.addTests(suite_账号关闭.get_suite_closeAcct账号关闭())
suite.addTests(suite_创建其他类型交易账号.get_suite_CreatUser创建其他类型交易账号())
suite.addTests(suite_申请添加银行卡.get_suite_CreateClientBank添加银行卡())

if __name__ == '__main__':
    HTMLReport.TestRunner(
        title="EDDID_CDMS项目接口测试",
        description="如有疑问请联系-ganjiexiang",
        report_file_name="EDDID_CDMS项目接口测试",
        # report_file_name字段不能改，关系到Jenkins的配置报告的生成
        thread_count=1
    ).run(suite)
