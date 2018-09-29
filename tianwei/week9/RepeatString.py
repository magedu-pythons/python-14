#实现一个函数，输入字符串，判断该字符串是否不含有重复字符

def repeatstring(str):
    lst=[]
    for i in str:
        if i not in lst:
            lst.append(i)
        else:
            print("The string contains repeat characters")
            break
    else:
        print("The string does not contain repeat characters")

repeatstring('abcdef')
repeatstring('abadef')