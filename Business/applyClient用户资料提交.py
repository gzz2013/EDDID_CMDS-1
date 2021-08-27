import requests
import unittest
from Business.login import cdms_获取token
from Common.random_number import Randoms
import logging
from Common.eddid_data_update import *
import time
from Common.eddid_data_select import *

class CreatUser():

    def ApplyClinet资料提交(self):
        global phone,token,eddidhost,s
        phone = Randoms().telephone()
        eddidhost = "http://sit-cdms.ynm3k.com"
        idCardNo = Randoms().ident_generator()
        token = cdms_获取token()
        s = requests.Session()
        logging.info("获取到的token为:{}".format(token))

        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        print("headers", headers)
        applyClienturl = eddidhost + "/api/client/applyClient"
        print("applyClienturl:",applyClienturl)
        # logging.info("接口请求url为：{}".format(applyClienturl))

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
        logging.info("提交申请单时注册用户手机号码为：{}".format(phone))
        applyClientResp= s.post(url=applyClienturl, headers=headers, json=data)
        logging.info("接口'{}'的响应结果为：'{}'".format(applyClienturl,applyClientResp.text))

        return applyClientResp
    def SubmitAudit提交审核(self):
        cd_clnt_wc_match(phone)
        logging.info("已完成修改WorldCheck的状态为FALSE")
        time.sleep(4)
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            # "Cookie": "GB-SYS-SID-SIT=" + cdms_获取token()
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("获取到的token为:{}".format(token))
        print("headers", headers)
        submitAuditurl = eddidhost + "/api/client/submitAudit"

        print("submitAuditurl为:", submitAuditurl)

        # logging.info("接口请求url为：{}".format(submitAuditurl))

        logging.info("提交审核获取到的手机号为：{}".format(phone))
        applyId = cd_clnt_apply_info(phone)

        print("查询数据库cd_clnt_apply_info查询到applyId的值为：{}".format(applyId))
        # print("applyId",applyId)
        data = {
            "applyId": applyId,
            "clientSource": "CDMS",
            "workFlowCode": "openClient"
        }
        print("data=", data)
        SubmitAuditResp = s.post(url=submitAuditurl, headers=headers, json=data)
        logging.info("提交审核接口'{}'的响应结果为:'{}'".format(submitAuditurl,SubmitAuditResp.text))
        return SubmitAuditResp

if __name__=="__main__":
    CreatUser=CreatUser()

    # t=ApplyClinet.ApplyClinet资料提交()
    print(CreatUser.ApplyClinet资料提交())
    print(CreatUser.SubmitAudit提交审核())
