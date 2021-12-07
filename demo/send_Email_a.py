import smtplib
from email.mime.text import MIMEText

# mailserver = "smtp.163.com"  #邮箱服务器地址
# username_send = 'ganjiexiang1@163.com'  #邮箱用户名
# password = 'RRHDLOCHTPOMODVY'   #邮箱密码：需要使用授权码

mailserver = "smtp.exmail.qq.com"  #邮箱服务器地址
username_send = 'zack.gan@edsz9.com'  #邮箱用户名
password = 'W9d7Dd48tC76xeMC'   #邮箱密码：需要使用授权码

# username_recv = "ganjiexiang@qq.com,544162008@qq.com"#收件人，多个收件人用逗号隔开
# username_recv = 'zack.gan<zack.gan@edsz9.com>,ganjiexiang<ganjiexiang@qq.com>'
username_recv = "544162008@qq.com,ganjiexiang@qq.com"
# mail = MIMEText('测试11112323')
message = '''
<p>Python 邮件发送测试...</p>
<p><a href="https://www.baidu.com">纵里寻她千百度</a></p>
'''
mail = MIMEText(message, 'html', _charset="utf-8")

mail['Subject'] = '这是甘杰祥'
mail['From'] = username_send  #发件人
mail['To'] = username_recv  #收件人；[]里的三个是固定写法，别问为什么，我只是代码的搬运工
smtp = smtplib.SMTP_SSL(mailserver,port=465) # 连接邮箱服务器，smtp的端口号是25
# smtp=smtplib.SMTP_SSL('smtp.qq.com',port=465) #QQ邮箱的服务器和端口号
smtp.login(username_send,password)  #登录邮箱
# smtp.sendmail(username_send,username_recv,mail.as_string())# 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
smtp.sendmail(from_addr = username_send, to_addrs=username_recv.split(','), msg=mail.as_string())

smtp.quit() # 发送完毕后退出smtp
print ('success')