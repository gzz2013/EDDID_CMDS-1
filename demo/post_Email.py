import smtplib
from email.mime.text import MIMEText

def post_Email(username):

    mailserver = "smtp.exmail.qq.com"  #邮箱服务器地址
    username_send = 'zack.gan@edsz9.com'  #邮箱用户名
    password = 'W9d7Dd48tC76xeMC'   #邮箱密码：需要使用授权码
    # username_recv = "ganjiexiang@qq.com,544162008@qq.com"#收件人，多个收件人用逗号隔开
    username_recv = username

    message = '''
    <p>Python 邮件发送测试...</p>
    <p><a href="http://192.168.57.23:8080/job/cdm_automated_testing/HTML_20Report/">CMDS自动化测试报告</a></p>
    '''
    mail = MIMEText(message, 'html', _charset="utf-8")

    mail['Subject'] = '这是甘杰祥'
    mail['From'] = username_send  #发件人
    mail['To'] = username_recv  #收件人；[]里的三个是固定写法，别问为什么，我只是代码的搬运工
    smtp = smtplib.SMTP_SSL(mailserver,port=465) # 连接邮箱服务器，smtp的端口号是25
    # smtp=smtplib.SMTP_SSL('smtp.qq.com',port=465) #QQ邮箱的服务器和端口号
    smtp.login(username_send,password)  #登录邮箱
    smtp.sendmail(from_addr = username_send, to_addrs=username_recv.split(','), msg=mail.as_string())

    smtp.quit() # 发送完毕后退出smtp
    print ('success')