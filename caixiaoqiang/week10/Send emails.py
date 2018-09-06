import smtplib
from email.mime.text import MIMEText

SMTPServer = "smtp.163.com"
sender = "cxiaoq951010@163.com"
passwd = "cxq1010"
message = "Have a nice day!"
recipients = "1229085103@qq.com"

send_email = MIMEText(message)
send_email["Subject"] = "An E-mail from you"
send_email["From"] = sender
send_email["To"] = recipients
smtpserver = smtplib.SMTP(SMTPServer, 25)
smtpserver.login(sender, passwd)
smtpserver.sendmail(sender, recipients, send_email.as_string())
smtpserver.quit()
