#给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
# 如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print (lst)
sum = int(input("请输入总和值："))


def find_sum(sum, lst):
    for one in range(len(lst)-1):                             #第一个值为lst[0]到lst[7]
        for two in range(one + 1, len(lst)):                  #第二个值为lst[1]到lst[8]
            if lst[one] + lst[two] == sum:                    #如果两值相加则打印
                print('{} + {} = {}'.format(lst[one], lst[two],sum))

find_sum(sum, lst)