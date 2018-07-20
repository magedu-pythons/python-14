



with open(r'D:\python-14\chengdexing\week3\word.txt',) as file:     #读出文本文件中的内容
    str = file.read()

number = []            #记录单词出现的次数
word = str.split()           #分离单词
sole = list(set(word))         #确保每个单词唯一

for i in sole:                  #统计单词出现的次数
    number.append(word.count(i))

word_dict = dict(zip(sole,number))   #将两个list组合成一个字典

for k,v in word_dict.items():
    print("单词'{0}'---------'{1}'次".format(k,v))

