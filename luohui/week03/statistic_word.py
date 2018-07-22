import re

with open('man_bash.txt') as f:
    content = f.read()

word_list = re.findall('[a-zA-Z]+', content)
word_set = set(word_list)

result = dict()
for word in word_set:
    result[word] = word_list.count(word)

print(result)
