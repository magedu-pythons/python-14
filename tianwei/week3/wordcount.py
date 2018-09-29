#任一个英文的纯文本文件，统计其中的单词出现的个数

with open('E:\GitHub\python-14/tianwei\week3\python.txt') as file:
    dic={}
    for line in file:
        words = line.split()
        for k,v in enumerate(words):
            dic[v]=dic.get(v,0)+1

print(dic)



