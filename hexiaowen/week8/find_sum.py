def find_sum(num:int):
    lst = [1,3,5,7,9,11]
    lst.sort()                                  #给列表排序
    count = []
    x =0
    if lst[0] > num:                            #判断是否小于最小值
        print('输入数值过小')
        return
    for i in range(len(lst)):
        if i > num:
            break
        sub = num - lst[i]                      #一个一个数遍历求差
        for j in range(i+1,len(lst)):
            x += 1
            if lst[j] >sub:                     #当数值J大于差时，后面的数都不用算了
                break
            if lst[j] == sub:                   #当相等时，记录数据
                count.append((lst[i], lst[j]))
                break
    print(count)
    print(x)

find_sum(13)