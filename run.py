import unittest
import HTMLReport
from Test_Suite import suite_创建运营用户
# from Business.saas_login import saas_获取token
# from Common.生成时间随机数 import write_numtime


suite = unittest.TestSuite()

suite.addTests(suite_创建运营用户.get_suite())
# saas_获取token()
# 跑用例前先生成token存到token.txt
# write_numtime()
#随机数写入文本

if __name__ == '__main__':
    HTMLReport.TestRunner(
        title="EDDID_CDMS项目接口测试",
        description="ganjiexiang1123",
        report_file_name="index",
        thread_count=1
    ).run(suite)
