#输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变
sentence='while there is life there is hope'

def rever_sen(sentence):
    strlis=sentence.split()
    n=len(strlis)

    restr = ''
    for i in range(n-1,-1,-1):
        restr+=(strlis[i]+ ' ')

    print(restr)

    return restr

rever_sen(sentence)