#任一个英文的纯文本文件，统计其中的单词出现的个数。
a = """There is a girl but I let her get away\nIt is all my fault cause pride got in the way
And I would be lying if I said I was ok\nAbout that girl the one I let get away
I keep saying no\nThis can not be the way we are supposed to be
I keep saying no\nYou gotta
There is gotta be a way to get you close to me"""  #纯英文文本

print (a)
lisa = list(a.split())
print (lisa)
for i in range(len(lisa)):
    for j in range(i-1,0,-1):      #每次打印元素前，向前比较是否有一样的，有就break
        if lisa[i] == lisa[j]:
            break
    else:                          #如果没有break，说明前面没有相同的，可以打印
        print (lisa[i],'\t','出现次数：',lisa.count(lisa[i]))

