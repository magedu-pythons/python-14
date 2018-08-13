import re

sentence = input("请输入一个英文句子：")
#  例句：you have a dream, you got to protect it.

lst_pun = re.findall(r'[.,]+', sentence)
lst_word = re.findall(r'[a-zA-Z]+', sentence)

print('句子：{}\n标点符号：{}\n单词：{}'.format(sentence, lst_pun, lst_word))

v = -1
sent_reversal = ''
count = len(sentence)

for i in range(count-1, -1, -1):
    if sentence[i] in lst_pun:
        sent_reversal = sent_reversal + sentence[i]
    if sentence[i] == ' ' or i == 0:
        sent_reversal = sent_reversal + lst_word[v] + ' '
        v = v - 1
print(sent_reversal)
