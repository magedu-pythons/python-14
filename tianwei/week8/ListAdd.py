#给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11

lst=[1,5,2,7,4,9]
obj=11

def ListAdd(lst:list,obj:int):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==obj:
                print(('{0}+{1}={2}').format(lst[i],lst[j],obj))

ListAdd(lst,obj)