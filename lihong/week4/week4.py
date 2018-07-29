# judge the palindrome number
def palindrome(num):
    lst=[_ for _ in str(num)]
    lst0=lst.copy()
    lst.reverse()
    if lst0==lst:
        print('It is a palindrome number')
    else:
        print('It is not a palindrome number')

palindrome(12321)


# choice the top number
import random
lst=[random.randint(0,100) for _ in range(20)]
n=len(lst)
def topnum():
    for i in range(3):
        tmp=i
        for j in range(i,n-1):
            if lst[tmp]<lst[j+1]:
                tmp=j+1
        lst[i],lst[tmp]=lst[tmp],lst[i]
    print(lst[0],lst[1],lst[2])

topnum()