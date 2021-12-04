import requests
import time

#tokenid为机器人的token，text为关键字
def send2robot(tokenid, text):
    s = requests.Session()
    headers = {
        "Content-Type": "application/json",
    }
    oapi_url = "https://oapi.dingtalk.com/robot/send?access_token=" +tokenid
    #参考文档钉钉自定义机器人接入：https://developers.dingtalk.com/document/robots/custom-robot-access?spm=ding_open_doc.document.0.0.4de64fb1B2MnBT#topic-2026027
    #没有链接的data
    # data = {
    #     "msgtype":"text",
    #     "text":{
    #         "content":text
    #     }
    # }
    #获取当前时间
    #有超链接的data
    localtime=time.strftime("%Y-%m-%d %H:%M", time.localtime())
    print("当前时间为：",localtime)
    data ={
        "msgtype": "link",
        "link": {
            "text": localtime,
            #钉钉机器人签名
            "title": text,
            "picUrl": "",
            #自动化测试报告URL
            "messageUrl": "http://192.168.57.23:8080/job/cdm_automated_testing/HTML_20Report/"
        }
    }
    send2robotre=s.post(url=oapi_url, headers=headers, json=data)
    print("send2robotre::",send2robotre.text)
    return send2robotre

send2robot("fb8e9870d1a020b0e0b4c139b9455c399d39c80030545c7ced062afa5b5dac6a","CMDS自动化测试报告")

# if __name__ == "__main__":
#     # result=send2robot(sys.argv[1], sys.argv[2])
#     token='fb8e9870d1a020b0e0b4c139b9455c399d39c80030545c7ced062afa5b5dac6a'
#     text="gzz123"
#     send2robot(token,text)
#     #print(result)
#
