import unittest
import os,time
import HTMLReport
# from tomorrow import threads
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#unittest_test目录，下有case和report
cur_path = os.path.dirname(__file__)

def all_case(casename="case",rule="test*.py"):
    '''第一加载所有的测试用例'''
    case_path = os.path.join(cur_path,casename) #用例路径拼接
    #如果不存在case文件夹，自动创建
    if not os.path.exists(case_path):os.mkdir(case_path)
    discover = unittest.TestLoader().discover(
        casename,
        pattern=rule,
        top_level_dir=None
    )
    return discover

# def getNowtime():
#     return time.strftime("%Y-%M-%D %H-%M-%S",time.localtime(time.time()))

def report():
    """第二执行所有用例，并把结果写入HTML测试报告中"""
    # now = time.strftime("%Y-%M-%D %H-%M-%S")
    report_path = os.path.join(cur_path,"report") #report文件夹
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path,"result.html")  # html报告文件路径
    # file = os.path.join(os.path.dirname(__file__), "Report", "testReport.html")
    # print("report_path:%s"%report_abspath)
    with open(report_abspath, "wb") as fp:
        runner = HTMLReport.TestRunner(
            stream=fp,
            title=u'自动化测试报告,测试结果如下：',
            description=u'用例执行情况：')
        # 调用add_case函数返回值
        runner.run(all_case())
    return report_abspath

def send_mail():
    """第三发送测试报告"""
    # ----------1.跟发件相关的参数------
    smtpserver = "smtp.163.com"  # 发件服务器
    # smtpserver = "smtp.qq.com"
    port = 25  # 非SSL协议端口号
    # sender = "XXXX" # 账号
    sender = "ganjiexiang1@163.com"
    psw = "gzz123456"
    # psw = "wmqtqbtnmyamhfjd" # 密码
    receiver = "zack.gan@edsz9.com" # 单个接收人也可以是 list
    # receiver = ["xxxxx@qq.com"]  # 多个收件人 list 对象
    # ----------2.编辑邮件的内容------
    # 读文件
    # file_path = "Result.html"
    # with open(file_path, "rb") as fp:
    #     mail_body = fp.read()
    with open(report(),"rb") as f:
        mail_body = f.read()
    msg = MIMEMultipart()
    msg["from"] = sender  # 发件人
    msg["to"] = receiver  # 收件人
    # msg["to"] = ";".join(receiver) # 多个收件人 list 转 str
    msg["subject"] = "我的主题报告-test"  # 主题

    # 正文
    body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(body)

    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="EDDID_CDMS项目接口测试.html"' #附件的名称
    msg.attach(att)
    # ----------3.发送邮件------
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)  # 连服务器
        smtp.login(sender, psw)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port) # QQ 邮箱
        smtp.login(sender, psw)  # 登录
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    smtp.quit()

def main():
    send_mail()

# if __name__ == '__main__':
    # runner = unittest_1.TextTestRunner()
    # runner.run(all_case())
    # main()

    # report_abspath = os.path.join(report_path, "result.html")  # html报告文件路径
    # fp = open(report_abspath, "wb")
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title=u'自动化测试报告,测试结果如下：',
    #     description=u'用例执行情况：')
    # # 调用add_case函数返回值
    # runner.run(all_case())
    # fp.close()