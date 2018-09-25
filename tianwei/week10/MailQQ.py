#使用python给自己qq邮箱发送一份邮件
#qq授权码好难弄，用的126邮箱

import smtplib
from email.mime.text import MIMEText

user = "twaisy@126.com" #你的邮箱
pwd = "890986tw" #IMAP/SMTP服务授权码，在126邮箱中，找到设置，选择账户，在里面找到IMAP/SMTP服务服务，点击开启，获取授权码
to = "twaisy@126.com" #接收人邮箱

# 发送纯文本格式的邮件
msg = MIMEText("测试邮件内容。。。") #邮件发送内容
msg["Subject"] = "邮件主题测试。。。" #邮件主题
msg["From"]= user
msg["To"]= to

#smtp服务器
smtp_server = 'smtp.126.com'

s = smtplib.SMTP_SSL(smtp_server, 465)  #用smtplib来发送邮件,并且使用了SSL加密，这样相对安全
s.set_debuglevel(1) #可以打印出和SMTP服务器交互的所有信息
s.login(user, pwd)  # login()方法用来登录SMTP服务器
s.sendmail(user, to, msg.as_string())  # sendmail()方法就是发邮件，可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。
s.quit()  #结束当前会话


