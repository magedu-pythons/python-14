#!/usr/bin/env python
#.Author:Dyw
#coding:utf-8   #强制使用utf-8编码格式

#1、使用python给自己qq邮箱发送一份邮件

import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
my_sender='abc@qq.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
my_user='359989190@qq.com' #收件人邮箱账号，为了后面易于维护，所以写成了变量
def mail():
    ret=True
    try:
        msg=MIMEText('this is a test mail','plain','utf-8')
        msg['From']=formataddr(["dyw",my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["to dyw",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="test mail" #邮件的主题，也可以说是标题

        server=smtplib.SMTP("smtp.exmail.qq.com",25)  #发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender,"123456")    #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()   #这句是关闭连接的意思
    except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
        ret=False
    return ret
ret=mail()
if ret:
    print("ok") #如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
else:
    print("filed")  #如果发送失败则会返回filed

#2、实现一个函数获取一个目录下所有以.py结尾的文件（包含目录下的子目录中的.py文件）

from pathlib import Path
# In [24]: p = Path('/home/python/magedu/projects/')
#
# In [25]: list(p.glob('**/*.py'))
# Out[25]:
# [PosixPath('/home/python/magedu/projects/a.py'),
#  PosixPath('/home/python/magedu/projects/test.py'),
#  PosixPath('/home/python/magedu/projects/re.py'),
#  PosixPath('/home/python/magedu/projects/Django/MysqldbHelper.py'),
#  PosixPath('/home/python/magedu/projects/Django/aa.py'),
#  PosixPath('/home/python/magedu/projects/Django/12.py')]
#或者：
# In [26]: list(p.rglob('*.py'))
# Out[26]:
# [PosixPath('/home/python/magedu/projects/a.py'),
#  PosixPath('/home/python/magedu/projects/test.py'),
#  PosixPath('/home/python/magedu/projects/re.py'),
#  PosixPath('/home/python/magedu/projects/Django/MysqldbHelper.py'),
#  PosixPath('/home/python/magedu/projects/Django/aa.py'),
#  PosixPath('/home/python/magedu/projects/Django/12.py')]
