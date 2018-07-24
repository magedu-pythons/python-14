#!/usr/bin/env python
#.Author:Dyw
#-*- coding:utf-8 -*-
num = list(input('input a number for 5 lenght:'))

if len(num) != 5:
    print("please input length for 5!")
    exit(1)

def foo():
    for i in range(len(num)//2):
        if num[i] == num[-i-1]:
            return print('Yes! This is a Palindrome number!')
        else:
            return print('No! This is not a palindrome number!')
foo()