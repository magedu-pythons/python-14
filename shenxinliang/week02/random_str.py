import random, string


# String模块ascii_letters和digits方法，其中ascii_letters是生成所有字母，从a-z和A-Z,digits是生成所有数字0-9
def rand_str(num, length=5):
    for i in range(num):
        chars = string.ascii_letters + string.digits  # 包含以下内容abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
        s = [random.choice(chars) for i in range(length)]  # 随机从chars抽取5个字符
        print('{0}\n'.format(''.join(s)))


if __name__ == '__main__':
    # rand_str(200)#生成200个激活
    print(rand_str(200))