import requests
import time
import smtplib
from email.mime.text import MIMEText

# tokenid为机器人的token，text为关键字
localtime = time.strftime("%Y-%m-%d %H:%M", time.localtime())
def send2robot(tokenid, text):
    s = requests.Session()

    headers = {
        "Content-Type": "application/json",
    }
    oapi_url = "https://oapi.dingtalk.com/robot/send?access_token=" + tokenid
    # 参考文档钉钉自定义机器人接入：https://developers.dingtalk.com/document/robots/custom-robot-access?spm=ding_open_doc.document.0.0.4de64fb1B2MnBT#topic-2026027
    # 没有链接的data
    # data = {
    #     "msgtype":"text",
    #     "text":{
    #         "content":text
    #     }
    # }
    # 获取当前时间
    # 有超链接的data
    print("当前时间为：", localtime)
    data = {
        "msgtype": "link",
        "link": {
            "text": localtime,
            # 钉钉机器人签名
            "title": text,
            "picUrl": "",
            # 自动化测试报告URL
            "messageUrl": "http://192.168.57.23:8080/job/cdms/HTML_20Report/"
        }
    }
    send2robotre = s.post(url=oapi_url, headers=headers, json=data)
    print("send2robotre::", send2robotre.text)
    print('success')
    return send2robotre


def post_Email(username):
    mailserver = "smtp.exmail.qq.com"  # 邮箱服务器地址
    username_send = 'zack.gan@edsz9.com'  # 邮箱用户名
    password = 'W9d7Dd48tC76xeMC'  # 邮箱密码：需要使用授权码
    # username_recv = "ganjiexiang@qq.com,544162008@qq.com"#收件人，多个收件人用逗号隔开
    username_recv = username
    message = '''
    <p><a href="http://192.168.57.23:8080/job/cdms/HTML_20Report/">自动化测试报告传送门</a></p>
    <p>-----如有疑问可咨询：甘杰祥</p>
    '''
    mail = MIMEText(message, 'html', _charset="utf-8")
    mail['Subject'] = 'CMDS自动化测试报告' + localtime
    mail['From'] = username_send  # 发件人
    mail['To'] = username_recv  # 收件人；[]里的三个是固定写法，别问为什么，我只是代码的搬运工
    smtp = smtplib.SMTP_SSL(mailserver, port=465)  # 连接邮箱服务器，smtp的端口号是25
    # smtp=smtplib.SMTP_SSL('smtp.qq.com',port=465) #QQ邮箱的服务器和端口号
    smtp.login(username_send, password)  # 登录邮箱
    smtp.sendmail(from_addr=username_send, to_addrs=username_recv.split(','), msg=mail.as_string())
    smtp.quit()  # 发送完毕后退出smtp
    print('success')
# tokenid为机器人的token，text为关键字
# 阿里群
# send2robot("fb8e9870d1a020b0e0b4c139b9455c399d39c80030545c7ced062afa5b5dac6a","CMDS自动化测试报告")
# 公司群
send2robot("38f7002387ae37a28bac18bd3b3fe6289de0703cf66994f65288a2b1fb9d35a1","CMDS自动化测试报告")
# 添加收件邮箱用”,“隔开
post_Email("王桂香<guixiang.wang@edsz9.com>,张小增<jenny.zhang@edsz9.com>,甘杰祥<zack.gan@edsz9.com>,孙加祯<jiazhen.sun@edsz9.com>,陈东平<dongping.chen@edsz9.com>")
# if __name__ == "__main__":
#     # result=send2robot(sys.argv[1], sys.argv[2])
#     token='fb8e9870d1a020b0e0b4c139b9455c399d39c80030545c7ced062afa5b5dac6a'
#     text="gzz123"
#     send2robot(token,text)
#     #print(result)
#
