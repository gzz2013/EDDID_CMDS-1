import requests
from Common.encry import MD5_Encrypt

# from Config.config import *
# from Common.token_写入 import tk_写入

#运营人员登录获取
def cdms_获取token():
    logins = requests.Session()
    #登录访问的接口
    url="http://sit-cdms.ynm3k.com/api/auth/login"
    #账号密码
    data = {"account": "ganjiexiang", "password": "111111"}
    data['password'] = MD5_Encrypt(str="111111")
    print("data=",data)
    res = logins.post(url=url, data=data)
    token = res.json()["data"]["token"]
    return token

print("token=",cdms_获取token())


