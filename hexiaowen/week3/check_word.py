word_list = {}

f =  open('E:\\马哥教育\\马哥课程\\课程笔记与程序\\python程序\\第三周\\作业\\homework.txt','r')
wordline = f.readline()
while wordline:
    word = wordline.split()
    for _ in word:
        if _ not in word_list:
            word_list[_] = 1
        else:
            word_list[_] += 1
    wordline = f.readline()
f.close()

for _ in word_list.keys():
    print('{}出现{}次'.format(_,word_list[_]))