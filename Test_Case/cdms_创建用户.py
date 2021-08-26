import unittest

import logging

import requests
from Business.login import cdms_获取token
import json


class Test_新建用户(unittest.TestCase):
    def setUp(self):
        self.s = requests.Session()
        pass

    def tearDown(self):
        self.s.close()

        logging.info("关闭 Session")

    def test_新建用户(self):

        s = self.s
        logging.info("初始化 Session")

        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection":"keep-alive",
            # "Cookie": "GB-SYS-SID-SIT=" + cdms_获取token()
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + cdms_获取token()
        }
        print("headers",headers)
        applyClienturl = "http://sit-cdms.ynm3k.com/api/client/applyClient"

        data = {
                "infos": [
                    {
                        "title": "mr",
                        "informationType": 1,
                        "firstName": "jiexiang5",
                        "lastName": "Gan2",
                        "chName": "R杰祥",
                        "usedCnName": "jiexiang5",
                        "usedChName": "R杰祥",
                        "email": "jiexiang5@qq.com",
                        "phoneAreaCode": "HKG",
                        "phoneNo": "85212305",
                        "houseAddress": "85212304",
                        "houseAddressPinYin": "85212300",
                        "postAddress": "85212300",
                        "natnlty": "HKG",
                        "idCardType": "1",
                        "idCardNo": "R7869210",
                        "otherCardType": "",
                        "otherCardNo": "",
                        "countryIssue": "NZL",
                        "overCountry": "NZL",
                        "birthday": "1993-04-29",
                        "idExpiresDate": "2021-08-06",
                        "birthdayPlace": "NZL",
                        "employmentStatus": "employed",
                        "post": "seniorManagement",
                        "workingYear": "",
                        "companyName": "85212300",
                        "businessNature": "financial",
                        "officeAddress": "8521230085212300",
                        "officePhone": "85212300",
                        "registeredCompany": "",
                        "employmentRemark": "",
                        "totalIncomeYear": "lt999999",
                        "sourceOfIncome": [

                        ],
                        "sourceOfIncomeRemake": "",
                        "totalCapital": "lt8000000",
                        "sourceOfCapital": [
                            "selfOperatedBusinessIncome"
                        ],
                        "sourceOfCapitalRemark": "",
                        "sourceOfMoney": [
                            "selfOperated"
                        ],
                        "sourceOfMoneyRemark": "",
                        "securitiesExperience": "1To5Years",
                        "cbbcExperience": "1To5Years",
                        "warrantExperience": "6To10Years",
                        "futuresExperience": "6To10Years",
                        "optionsExperience": "6To10Years",
                        "foreignExchangExperience": "6To10Years",
                        "metalExperience": "6To10Years",
                        "autoTransationExperience": "6To10Years",
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
                        "relationshipWithInternalEmployees": "N",
                        "employeesName": "",
                        "isRegisteredPerson": "N",
                        "registeredPersonRemark": "",
                        "isUsPerson": "N",
                        "taxNumber": "",
                        "isUsTaxPerson": "N",
                        "taxNumberTwo": "",
                        "isPepPerson": "N",
                        "pepPersonName": "",
                        "investmentObjective": [
                            "hedging"
                        ],
                        "riskTolerance": "high",
                        "throughChannels": [
                            "friend",
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
                        "residencyJurisdiction": "FJI",
                        "taxNumber": "",
                        "resonType": "A",
                        "resonRemark": ""
                    }
                ],
                "attachs": {
                    "passportMaterial": [
                        "public/dinggg_20210806175105.jpg"
                    ],
                    "addressVerificationMaterials": [
                        "public/dinggg_20210806175108.jpg"
                    ],
                    "bankCardMaterials": [
                        "public/dinggg_20210806175112.jpg"
                    ],
                    "proofOfIncome": [
                        "public/dinggg_20210806175120.jpg"
                    ],
                    "otherInformation": [
                        "public/dinggg_20210806175123.jpg"
                    ],
                    "writtenApplicationMaterials": [
                        "public/APP_20200811142432_20210806175129.pdf"
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
                "responsible": "aaron.chan",
                "emailLanguage": "zh-hans",
                "accts": [
                    "securitiesCash",
                    "futuresMargin",
                    "leveragedForeignExchangeAccountMargin"
                ],
                "promotionNumber": "EDAA520",
                "agreeToTheTerms": "true",
                "personalInfoDeclartion": "true"
            }
        r = s.post(url=applyClienturl, headers=headers, json=data)
        print("r:", r.text)

        self.assertEqual(200, r.status_code)


