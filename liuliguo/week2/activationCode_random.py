import random

lowercase = "abcdefghijkmnpqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNPQRSTUVWXYZ"
digits = "23456789"
codes = lowercase + uppercase + digits

count = 200 #生成激活码的总数量
activationCodeList = []
while count > 0:
    activationCode = ""
    for j in range(6):#生成激活码位数
        #activationCode += (codes[random.randint(0,len(codes)-1)])
        activationCode += random.choice(codes)
    if activationCode not in activationCodeList:#不允许激活码重复
        activationCodeList.append(activationCode)
        count -= 1
for each in activationCodeList:
    print(each)
