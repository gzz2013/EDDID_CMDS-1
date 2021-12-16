import unittest
from Test_Case.test_createClientBankApply import Test_CreateClientBank添加银行卡


def get_suite_CreateClientBank添加银行卡():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(Test_CreateClientBank添加银行卡))

    return suite