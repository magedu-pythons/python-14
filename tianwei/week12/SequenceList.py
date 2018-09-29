#给出一个无序的整型列表，找出最长连续元素序列的长度，时间复杂度要求在线性时间内。
#例如：  输入：[8,1,9,3,2,4]，那么其最长连续序列是[1,2,3,4]，即输出长度为4

lst=[8,1,9,3,2,4]

def seqlist(lst):
    maxnumber=max(lst)
    lst1=[0]*maxnumber
    for i in lst:
        lst1[i-1]=i

    length=0
    maxlength=0

    for j in lst1:
        if j !=0:
            length+=1
        else:
            if maxlength<length:
                maxlength=length
            length=0
    return maxlength

print(seqlist(lst))


