#任一个英文的纯文本文件，统计其中的单词出现的个数


with open(r'E:\GitHub\python-14\tianwei\week3\python.txt', ) as file:
    str = file.read()

words = str.split()
word = set(words)

#print(word)

number=[]

for i in word:
    number.append(words.count(i))

wordcont = zip(word, number)

print(wordcont)





