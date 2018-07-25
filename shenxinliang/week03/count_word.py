
file = open('E:\Github\python-14\shenxinliang\week03\Test.txt','r')      #读出文本文件中的内容
str = file.read()

count = []            #记录单词出现的次数
word = str.split()           #分离单词
a = set(word)
single_word = list(a)          #调用set函数，以分离出来的单词作为一个不重复的元素集，作为single_word list的内容
for _ in single_word:                  #以single_word的内容在word中统计单词出现的次数，并计数在count list中
    count.append(word.count(_))

word_dict = dict(zip(single_word,count))   #将两个list合并成一个字典

for k,v in word_dict.items():  #遍历输出word_dict字典中的元素和键值
    print("{}在文本中出现{}次".format(k,v))
