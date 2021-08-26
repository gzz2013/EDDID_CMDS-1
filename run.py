import unittest
import HTMLReport
from Test_Suite import suite_运营用户创建审批
# from Business.saas_login import saas_获取token
# from Common.生成时间随机数 import write_numtime


suite = unittest.TestSuite()

suite.addTests(suite_运营用户创建审批.get_suite())
# saas_获取token()
# 跑用例前先生成token存到token.txt
# write_numtime()
#随机数写入文本

if __name__ == '__main__':
    HTMLReport.TestRunner(
        title="EDDID_CDMS项目接口测试",
        description="如有疑问请联系-ganjiexiang",
        report_file_name="EDDID_CDMS项目接口测试",
        thread_count=1
    ).run(suite)
