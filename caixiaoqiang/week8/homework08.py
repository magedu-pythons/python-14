# 1.实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出现的地址；否则，返回None.

str1 = "One thing I know,that is I know nothing."
str2 = "now"
# str2 = "nw"


def find_str(str_1, str_2):
    if str_2 in str_1:
        for sub in range(len(str_1)):
            if str_2 == str_1[sub:sub + len(str_2)]:
                return sub
    return None


print("首次出现的地址：", find_str(str1, str2))

# 2.给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
# 如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
value = int(input("请输入目标值："))


def find_nums(val, lsts):
    for fst in range(len(lsts)-1):
        for scd in range(fst + 1, len(lsts)):
            if lsts[fst] + lsts[scd] == val:
                print('{} + {}'.format(lsts[fst], lsts[scd]))


find_nums(value, lst)
