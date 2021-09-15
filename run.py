import unittest
import HTMLReport

from Test_Suite import suite_运营用户创建审批,suite_运营用户创建结构性产品及审批,suite_换汇申请单


suite = unittest.TestSuite()

# suite.addTests(suite_运营用户创建审批.get_suite_creatUser新建用户())
# suite.addTests(suite_换汇申请单.get_suite_CreateExchange新建换汇申请单())
suite.addTests(suite_运营用户创建结构性产品及审批.get_suite_creatUser没有结构性产品账号及申请结构性产品审批())




if __name__ == '__main__':
    HTMLReport.TestRunner(
        title="EDDID_CDMS项目接口测试",
        description="如有疑问请联系-ganjiexiang",
        report_file_name="EDDID_CDMS项目接口测试",
        thread_count=1
    ).run(suite)
