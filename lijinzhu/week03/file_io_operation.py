#!/usr/bin/env python
# author: Li Jinzhu
# blog: http://blog.51cto.com/limingyu

chars = '''
~!@#$%^&*()_+|{}[]'";:\\/<>,. 
'''

with open('test',encoding='utf-8') as f:
    word_dict = {}

    for line in f:
        words = line.strip(chars).split()
        for x,_ in list(zip(words,(1,)*len(words))):
            x = x.lower()
            if x not in word_dict:
                word_dict[x] = 1
            else:
                word_dict[x] +=1

for k,v in word_dict.items():
    print("{}......{}".format(k,v))

