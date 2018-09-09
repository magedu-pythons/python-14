import smtplib
import re
import mimetypes
import datetime
import imghdr
from pathlib import Path
from email.message import EmailMessage

class MyMail:
    def __init__(self, me, subject):
        self.From = me
        self.receiver = []
        self.subject = subject
        self.date = datetime.datetime.now().strftime('%Y-%m-%d')
        self.msg = EmailMessage()

    @staticmethod
    def recursion_load(*path: str):
        """load all files Under the specified folder return a file's Path-obj list"""
        def _reload(path: Path):
            """recursion"""
            nonlocal file_list
            if not path.is_dir():
                return

            for file in path.iterdir():
                if file.is_file():
                    file_list.append(file)
                elif file.is_dir():
                    _reload(file)

        file_list = []
        if not path:
            path = '.'
        for file in path:
            p = Path(file)
            if not p.exists():
                continue
            if p.is_dir():
                _reload(p)
            elif p.is_file():
                file_list.append(p)

        return file_list

    def addReceiver(self, *args):
        """add target mail address,sep by ',',simplely check if target is vaild"""
        regex = re.compile(r'[0-9a-zA-Z_.-]+@[a-zA-Z\d-]+(\.[a-zA-Z0-9])*\.[a-zA-Z0-9]+')
        error = []
        for x in args:
            if regex.match(x):
                self.receiver.append(x)
            else:
                error.append(x)
        if error:
            print('the following address are invaild, plz check!\n{}'.format(error))

    def addText(self, path):
        file = self.recursion_load(path)
        for x in file:
            if x.suffixes[0] == '.txt':
                with open(str(x)) as fp:
                    self.msg.set_content(fp.read())

    def addImage(self, path):
        """add all pictures Under the specified folder"""
        file = self.recursion_load(path)
        for image in file:
            if image.suffixes in [['.png'], ['.bmp'], ['.jpg'], ['.gif']]:
                with open(image, 'rb') as fp:
                    img_data = fp.read()
                    self.msg.add_attachment(img_data, maintype='image', subtype=imghdr.what(None, img_data))

    def addEnclosure(self, path):
        target = self.recursion_load(path)
        for x in target:
            ctype, encoding = mimetypes.guess_type(str(x))
            if ctype is None or encoding is not None:
                ctype = 'application/octet-stream'
            maintype, subtype = ctype.split('/', 1)
            filename = x.name

            with open(x, 'rb') as fp:
                self.msg.add_attachment(fp.read(), maintype=maintype, subtype=subtype, filename=filename)

    def sendMessage(self):
        self.msg['Subject'] = self.subject
        self.msg['From'] = self.From
        self.msg['To'] = ','.join(self.receiver)
        # self.msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'

        server = smtplib.SMTP()
        server.connect('smtp.163.com')
        server.login(self.From, 'mail163')

        with server as s:
            s.send_message(self.msg, from_addr=self.From, to_addrs=','.join(self.receiver))

# --------------------测试-------------------------
mail = MyMail('xdzhangjingwen@163.com', 'Meeting')
mail.addReceiver('1756727919@qq.com')

# 添加正文，从txt文件中读取
mail.addText('F:/python-14/zhangjingwen/week10/test')
# mail.addImage('F:/python-14/zhangjingwen/week10')

# 添加附件，如果提供的路径是文件夹，会递归找出该文件夹及其子文件夹下的所有合法文件，并作为附件发送
mail.addEnclosure('F:/python-14/zhangjingwen/week10/test')
mail.sendMessage()

