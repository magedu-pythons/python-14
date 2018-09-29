# 1、使用python给自己qq邮箱发送一份邮件

from email.mime.text import MIMEText
import smtplib

msg = MIMEText('hello world!', 'plain', 'utf-8')
username = 'houdinis@163.com'
password = 'cx19961127'
recv_add = '1281607807@qq.com'
smtp_server = 'smtp.163.com'

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(username, password)
server.sendmail(username, [recv_add], msg.as_string())
server.quit()



