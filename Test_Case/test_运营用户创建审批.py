import unittest
import time
import logging
from Common.eddid_data_select import *
from Common.eddid_data_update import *
import requests
from Business.login import cdms_获取token
import json
from Common.random_number import *


class Test_新建用户(unittest.TestCase):
    def setUp(self):
        self.s = requests.Session()
        self.phone=Randoms().telephone()
        self.idCardNo=Randoms().ident_generator()
        self.eddidhost="http://sit-cdms.ynm3k.com"

        print("随机生成的phone",self.phone)
        print("身份证号", self.idCardNo)

    def tearDown(self):
        self.s.close()

        logging.info("关闭 Session")

    def test_applyClient用户资料提交(self):
        eddidhost=self.eddidhost
        idCardNo=self.idCardNo
        phone=self.phone
        s = self.s
        logging.info("初始化 Session")

        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + cdms_获取token()
        }
        print("headers", headers)
        applyClienturl = eddidhost + "/api/client/applyClient"
        print("applyClienturl:",applyClienturl)
        logging.info("接口请求url为：".format(applyClienturl))

        data = {
            "infos": [
                {
                    "title": "mr",
                    "informationType": 1,
                    "firstName": "ZDH"+ phone,
                    "lastName": "ZDH"+phone,
                    "chName": "自动化甘"+phone,
                    "usedCnName": "自动化"+phone,
                    "usedChName": "自动化"+phone,
                    "email": "gan"+ phone +"@qq.com",
                    "phoneAreaCode": "CHN",
                    "phoneNo": phone,
                    "houseAddress": "104phone"+phone,
                    "houseAddressPinYin": "104phone"+phone,
                    "postAddress": "接口自动化",
                    "natnlty": "CHN",
                    "idCardType": "2",
                    "idCardNo": idCardNo,
                    "otherCardType": "",
                    "otherCardNo": "",
                    "countryIssue": "CHN",
                    "overCountry": "CHN",
                    "birthday": "1994-08-09",
                    "idExpiresDate": "2023-08-31",
                    "birthdayPlace": "CHN",
                    "employmentStatus": "self",
                    "post": "businessOwner",
                    "workingYear": "11",
                    "companyName": "接口自动化"+phone,
                    "businessNature": "wholesale&retail",
                    "officeAddress": "47845512245"+phone,
                    "officePhone": "0771-${phone}",
                    "registeredCompany": "Y",
                    "employmentRemark": "",
                    "totalIncomeYear": "gt1000000",
                    "sourceOfIncome": [
                        "selfOperatedBusinessIncome",
                        "salary"
                    ],
                    "sourceOfIncomeRemake": "",
                    "totalCapital": "gt8000000",
                    "sourceOfCapital": [
                        "salary",
                        "savings",
                        "pension"
                    ],
                    "sourceOfCapitalRemark": "",
                    "sourceOfMoney": [
                        "selfOperated"
                    ],
                    "sourceOfMoneyRemark": "",
                    "securitiesExperience": "gt10Years",
                    "cbbcExperience": "gt10Years",
                    "warrantExperience": "gt10Years",
                    "futuresExperience": "gt10Years",
                    "optionsExperience": "gt10Years",
                    "foreignExchangExperience": "gt10Years",
                    "metalExperience": "gt10Years",
                    "autoTransationExperience": "gt10Years",
                    "otherInvest": "",
                    "otherExperience": "",
                    "withDerivativesKnowledge": "Y",
                    "withDerivativesWoking": "Y",
                    "withDerivativesDeal": "Y",
                    "applicationOpenDerivatives": "Y",
                    "understandTheRisks": "Y",
                    "haveDeclaredBankruptcy": "N",
                    "declaredBankruptcyDate": "",
                    "isInternalStaff": "N",
                    "staffNameRelationship": "",
                    "relationshipWithInternalEmployees": "Y",
                    "employeesName": "11212",
                    "isRegisteredPerson": "N",
                    "registeredPersonRemark": "",
                    "isUsPerson": "N",
                    "taxNumber": "",
                    "isUsTaxPerson": "N",
                    "taxNumberTwo": "",
                    "isPepPerson": "N",
                    "pepPersonName": "",
                    "investmentObjective": [
                        "asset",
                        "income"
                    ],
                    "riskTolerance": "high",
                    "throughChannels": [
                        "lecture"
                    ],
                    "throughChannelRemark": "",
                    "isFinalBeneficiary": "Y",
                    "finalBeneficiaryName": "",
                    "isFinalPrincipal": "Y",
                    "finalPrincipalName": "",
                    "businessNatureRemark": ""
                }
            ],
            "marginAcctS": [

            ],
            "taxs": [
                {
                    "residencyJurisdiction": "CHN",
                    "taxNumber": "",
                    "resonType": "A",
                    "resonRemark": ""
                }
            ],
            "attachs": {
                "passportMaterial": [
                    "/hzlc_20210819191744.jpg"
                ],
                "addressVerificationMaterials": [
                    "/hzlc_20210819191748.jpg"
                ],
                "bankCardMaterials": [
                    "/hzlc_20210819191751.jpg"
                ],
                "proofOfIncome": [
                    "/hzlc_20210819191759.jpg"
                ],
                "writtenApplicationMaterials": [
                    "/APP_20200811142432_20210819191759.pdf"
                ],
                "otherInformation": [
                    "/dinggg_20210819191801.jpg"
                ],
                "bankruptcyProve": [

                ],
                "acquaintHighLevelInstructionsProve": [

                ],
                "tradingAuthorization": [

                ]
            },
            "settleAcctS": [

            ],
            "clientType": "PERSONAL",
            "openWay": "visitingAccount",
            "bankName": "",
            "bankCardNo": "",
            "elecNo": "",
            "responsible": "kwokwah.wong",
            "emailLanguage": "zh-hans",
            "accts": [
                "securitiesCash",
                "futuresMargin",
                "leveragedForeignExchangeAccountMargin",
                "securitiesAyersCash"
            ],
            "promotionNumber": "EDAC520",
            "agreeToTheTerms": "true",
            "personalInfoDeclartion": "true"
        }
        print("提交申请单时用户手机号码为：{}".format(phone))
        r = s.post(url=applyClienturl, headers=headers, json=data)
        print("r:", r.text)
        time.sleep(5)
        self.assertEqual(200, r.status_code)
        self.assertEqual("操作成功", r.json().get("msg"))

    def test_submitAudit提交审核(self):

        s = self.s
        phone=self.phone
        eddidhost=self.eddidhost

        cd_clnt_wc_match(phone)
        logging.info("已完成修改WorldCheck的状态为FALSE")
        time.sleep(4)
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            # "Cookie": "GB-SYS-SID-SIT=" + cdms_获取token()
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + cdms_获取token()
        }
        print("headers", headers)
        submitAuditurl = eddidhost+"/api/client/submitAudit"

        print("submitAuditurl为:", submitAuditurl)

        logging.info("接口请求url为：".format(submitAuditurl))

        logging.info("提交审核获取到的手机号为：{}".format(phone))
        applyId = cd_clnt_apply_info(phone)

        logging.info("请求数据库cd_clnt_apply_info查询到applyId的值为：{}".format(applyId))
        # print("applyId",applyId)
        data = {
            "applyId": applyId,
            "clientSource": "CDMS",
            "workFlowCode": "openClient"
        }
        print("data=", data)
        r = s.post(url=submitAuditurl, headers=headers, json=data)
        print("r:", r.text)
        print("提交审核时用户手机号码为：{}".format(phone))

        self.assertEqual(200, r.status_code)
        self.assertEqual("操作成功", r.json().get("msg"))
