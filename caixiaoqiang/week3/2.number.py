
numlst = []
path =r"E:\python-14\caixiaoqiang\week3\first.txt"
f = open(path, "r")
numlst.extend(f.readline().split())
print('单词出现的个数为：{}'.format(len(numlst)))
f.close()




