#!/usr/bin/env python
#.Author:Dyw
#1、实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出 现的地址；否则，返回None
str1 = 'abcdxyzabc'
str2 = 'xz'
def sub(str1,str2):
    if str1.find(str2) == -1:
        print('str2 is not str1 sub')
        return None
    else:
        print('str2 is str1 sub')
        return print(str1.find(str2))

sub(str1,str2)

#2、给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
#如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11
lst =[1,5,2,7,4,9]
def sums(sum):
    print([(i,j) for i in lst for j in lst if i + j == sum ])
sums(sum=11)
