import requests
from Business.login import cdms_获取token
from Common.random_number import Randoms
import logging
from Common.eddid_data_update import *
import time
from Common.eddid_data_select import *


class CreatUser():

    # 步骤1
    def ApplyClinet资料提交(self):
        global phone, token, eddidhost, s
        phone = Randoms().telephone()
        eddidhost = "http://sit-cdms.ynm3k.com"
        idCardNo = Randoms().ident_generator()
        token = cdms_获取token()
        s = requests.Session()

        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))

        print("headers", headers)
        applyClienturl = eddidhost + "/api/client/applyClient"
        print("applyClienturl:", applyClienturl)
        # logging.info("接口请求url为：{}".format(applyClienturl))

        data = {
            "infos": [
                {
                    "title": "mr",
                    "informationType": 1,
                    "firstName": "ZDH" + phone,
                    "lastName": "ZDH" + phone,
                    "chName": "自动化甘" + phone,
                    "usedCnName": "自动化" + phone,
                    "usedChName": "自动化" + phone,
                    "email": "gan" + phone + "@qq.com",
                    "phoneAreaCode": "CHN",
                    "phoneNo": phone,
                    "houseAddress": "104phone" + phone,
                    "houseAddressPinYin": "104phone" + phone,
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
                    "companyName": "接口自动化" + phone,
                    "businessNature": "wholesale&retail",
                    "officeAddress": "47845512245" + phone,
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
        applyClientResp = s.post(url=applyClienturl, headers=headers, json=data)
        logging.info("接口'{}'的响应结果为：'{}'".format(applyClienturl, applyClientResp.text))
        return applyClientResp

    # 步骤2
    def SubmitAudit提交审核(self):
        cd_clnt_wc_match(phone)
        logging.info("已完成修改WorldCheck的状态为FALSE")
        # 必须要等待修改完成后才能提交审核
        time.sleep(5)
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("headers", headers)
        submitAuditurl = eddidhost + "/api/client/submitAudit"
        print("submitAuditurl为:", submitAuditurl)

        logging.info("提交审核获取到的手机号为：{}".format(phone))
        global applyId
        applyId = cd_clnt_apply_info(phone)
        print("查询数据库cd_clnt_apply_info查询到applyId的值为：{}".format(applyId))
        data = {
            "applyId": applyId,
            "clientSource": "CDMS",
            "workFlowCode": "openClient"
        }
        print("data=", data)
        SubmitAuditResp = s.post(url=submitAuditurl, headers=headers, json=data)
        logging.info("提交审核接口'{}'的响应结果为:'{}'".format(submitAuditurl, SubmitAuditResp.text))
        return SubmitAuditResp

    # 步骤3
    def operatingWorkFlowFirst提交锁(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("headers", headers)
        operatingWorkFlowFirsturl = eddidhost + "/api/common/operatingWorkFlow"

        print("submitAuditurl为:", operatingWorkFlowFirsturl)

        # logging.info("接口请求url为：{}".format(submitAuditurl))

        # logging.info("提交审核获取到的手机号为：{}".format(phone))
        global applyId
        applyId = cd_clnt_apply_info(phone)
        print("查询数据库cd_clnt_apply_info查询到applyId的值为：{}".format(applyId))
        data = {
            "applyId": applyId,
            "workFlowCode": "openClient",
            "controlCode": "LOCK"
        }
        print("data=", data)
        operatingWorkFlowFirstResp = s.post(url=operatingWorkFlowFirsturl, headers=headers, json=data)
        logging.info("提交审核接口'{}'的响应结果为:'{}'".format(operatingWorkFlowFirsturl, operatingWorkFlowFirstResp.text))
        return operatingWorkFlowFirstResp

    # 步骤4
    def saveRiskAssessment风控评估提交(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("headers", headers)
        saveRiskAssessmenturl = eddidhost + "/api/client/saveRiskAssessment"

        print("submitAuditurl为:", saveRiskAssessmenturl)
        logging.info("当前applyId为：{}".format(applyId))
        data = {
            "applyId": applyId,
            "riskAssessmentInfoDTO": {
                "isAmlOrCft": "true",
                "isPeb": None,
                "isPolice": None,
                "isIcac": None,
                "isHighRiskBusiness": None,
                "isJfiu": None,
                "isCorruption": None,
                "isOtherInformation": None,
                "nonFaceToFace": None,
                "isUnemployed": None,
                "isNonFatf": None,
                "isNonFinancial": None,
                "isTemporaryAddr": None,
                "residence": "新西兰",
                "otherInformation": "",
                "riskAssessmentLevel": "TERMINATE"
            }
        }
        print("data=", data)
        saveRiskAssessmentResp = s.post(url=saveRiskAssessmenturl, headers=headers, json=data)
        logging.info("提交审核接口'{}'的响应结果为:'{}'".format(saveRiskAssessmenturl, saveRiskAssessmentResp.text))
        return saveRiskAssessmentResp

    # 步骤5
    def operatingWorkFlow内部人员审核(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("headers", headers)
        operatingWorkFlowturl = eddidhost + "/api/common/operatingWorkFlow"

        print("submitAuditurl为:", operatingWorkFlowturl)
        print("当前的applyId的值为：{}".format(applyId))
        data = {
            "applyId": applyId,
            "checkItemList": [
                {
                    "itemId": "1",
                    "itemCde": "Application Form",
                    "itemDesc": "Application Form",
                    "cscheckFlag": "true",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "2",
                    "itemCde": "Fee schedule",
                    "itemDesc": "Fee schedule",
                    "cscheckFlag": "true",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "3",
                    "itemCde": "ID card Copy",
                    "itemDesc": "ID card Copy",
                    "cscheckFlag": "true",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "4",
                    "itemCde": "SFC search",
                    "itemDesc": "SFC search",
                    "cscheckFlag": "true",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "5",
                    "itemCde": "Worldcheck",
                    "itemDesc": "Worldcheck",
                    "cscheckFlag": "false",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "6",
                    "itemCde": "Address Proof (if any)",
                    "itemDesc": "Address Proof (if any)",
                    "cscheckFlag": "false",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "7",
                    "itemCde": "Bank proof (if any)",
                    "itemDesc": "Bank proof (if any)",
                    "cscheckFlag": "false",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "8",
                    "itemCde": "Source of Fund (if any)",
                    "itemDesc": "Source of Fund (if any)",
                    "cscheckFlag": "false",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "9",
                    "itemCde": "Source of Wealth (if any)",
                    "itemDesc": "Source of Wealth (if any)",
                    "cscheckFlag": "false",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "10",
                    "itemCde": "Other",
                    "itemDesc": "Other",
                    "cscheckFlag": "false",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                }
            ],
            "workFlowCode": "openClient",
            "controlCode": "PASS",
            "isStaff": "false",
            "lockBy": "ED_RO",
            "licensedPersonSign": ""
        }
        print("data=", data)
        operatingWorkFlowResp = s.post(url=operatingWorkFlowturl, headers=headers, json=data)
        logging.info("提交审核接口'{}'的响应结果为:'{}'".format(operatingWorkFlowturl, operatingWorkFlowResp.text))
        return operatingWorkFlowResp

    # 步骤6
    def operatingWorkFlowNo不用锁定审核通过(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("headers", headers)
        operatingWorkFlowNourl = eddidhost + "/api/common/operatingWorkFlow"

        print("submitAuditurl为:", operatingWorkFlowNourl)

        # logging.info("接口请求url为：{}".format(submitAuditurl))

        # logging.info("提交审核获取到的手机号为：{}".format(phone))
        global applyId
        applyId = cd_clnt_apply_info(phone)
        logging.info("当前applyId为：{}".format(applyId))
        data = {
            "applyId": applyId,
            "workFlowCode": "openClient",
            "controlCode": "LOCK"
        }
        print("data=", data)
        operatingWorkFlowNoResp = s.post(url=operatingWorkFlowNourl, headers=headers, json=data)
        logging.info("提交审核接口'{}'的响应结果为:'{}'".format(operatingWorkFlowNourl, operatingWorkFlowNoResp.text))
        return operatingWorkFlowNoResp

    # 步骤7
    def operatingWorkFlowAgain提交锁(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("headers", headers)
        operatingWorkFlowAgainturl = eddidhost + "/api/common/operatingWorkFlow"

        print("submitAuditurl为:", operatingWorkFlowAgainturl)

        # logging.info("接口请求url为：{}".format(submitAuditurl))

        # logging.info("提交审核获取到的手机号为：{}".format(phone))
        global applyId
        applyId = cd_clnt_apply_info(phone)
        print("查询数据库cd_clnt_apply_info查询到applyId的值为：{}".format(applyId))
        data = {
            "applyId": applyId,
            "workFlowCode": "openClient",
            "controlCode": "LOCK"
        }
        print("data=", data)
        operatingWorkFlowAgaintResp = s.post(url=operatingWorkFlowAgainturl, headers=headers, json=data)
        logging.info("提交审核接口'{}'的响应结果为:'{}'".format(operatingWorkFlowAgainturl, operatingWorkFlowAgaintResp.text))
        return operatingWorkFlowAgaintResp

    # 步骤8
    def batchOperatingWorkFlow批量生成账号确定(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("headers", headers)
        batchOperatingWorkFlowurl = eddidhost + "/api/common/batchOperatingWorkFlow"

        print("submitAuditurl为:", batchOperatingWorkFlowurl)

        # logging.info("接口请求url为：{}".format(submitAuditurl))

        # logging.info("提交审核获取到的手机号为：{}".format(phone))
        global applyId
        applyId = cd_clnt_apply_info(phone)
        print("查询数据库cd_clnt_apply_info查询到applyId的值为：{}".format(applyId))
        data = {
            "applyIds": [
                applyId
            ],
            "workFlowCode": "openClient",
            "controlCode": "GENERATEACCTNO",
            "workFlowOperatingDTOList": [
                {
                    "applyId": applyId
                }
            ]
        }
        print("data=", data)
        batchOperatingWorkFlowResp = s.post(url=batchOperatingWorkFlowurl, headers=headers, json=data)
        logging.info("提交审核接口'{}'的响应结果为:'{}'".format(batchOperatingWorkFlowurl, batchOperatingWorkFlowResp.text))
        return batchOperatingWorkFlowResp

    # 步骤9
    def operatingWorkFlowThird提交锁(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("headers", headers)
        operatingWorkFlowThirdurl = eddidhost + "/api/common/operatingWorkFlow"

        print("submitAuditurl为:", operatingWorkFlowThirdurl)

        # logging.info("接口请求url为：{}".format(submitAuditurl))

        # logging.info("提交审核获取到的手机号为：{}".format(phone))
        global applyId
        applyId = cd_clnt_apply_info(phone)
        logging.info("当前applyId为：{}".format(applyId))
        data = {
            "applyId": applyId,
            "workFlowCode": "openClient",
            "controlCode": "LOCK"
        }
        print("data=", data)
        operatingWorkFlowThirdResp = s.post(url=operatingWorkFlowThirdurl, headers=headers, json=data)
        logging.info("提交审核接口'{}'的响应结果为:'{}'".format(operatingWorkFlowThirdurl, operatingWorkFlowThirdResp.text))
        return operatingWorkFlowThirdResp

    # 步骤10
    def batchOperatingWorkFlowEnd批量确认(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("headers", headers)
        batchOperatingWorkFlowEndurl = eddidhost + "/api/common/batchOperatingWorkFlow"

        print("submitAuditurl为:", batchOperatingWorkFlowEndurl)

        # logging.info("接口请求url为：{}".format(submitAuditurl))

        # logging.info("提交审核获取到的手机号为：{}".format(phone))
        global applyId
        applyId = cd_clnt_apply_info(phone)
        logging.info("当前applyId为：{}".format(applyId))
        data = {
            "applyIds": [
                applyId
            ],
            "workFlowCode": "openClient",
            "controlCode": "PASS",
            "workFlowOperatingDTOList": [
                {
                    "applyId": applyId
                }
            ]
        }
        print("data=", data)
        batchOperatingWorkFlowEndResp = s.post(url=batchOperatingWorkFlowEndurl, headers=headers, json=data)
        logging.info("提交审核接口'{}'的响应结果为:'{}'".format(batchOperatingWorkFlowEndurl, batchOperatingWorkFlowEndResp.text))
        return batchOperatingWorkFlowEndResp


# ”if __name__=="__main__":“的作用在当前文件run时会执行下面的代码，如果时外部调用就不会执行if里面的代码
if __name__ == "__main__":
    # 实例化CreatUser
    CreatUser = CreatUser()

    print(CreatUser.ApplyClinet资料提交().text)
    time.sleep(4)
    print(CreatUser.SubmitAudit提交审核().text)
    time.sleep(4)
    print(CreatUser.operatingWorkFlowFirst提交锁().text)