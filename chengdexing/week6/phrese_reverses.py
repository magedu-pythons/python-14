
#输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变
phrese = 'Sentences can be broken up into clauses and clauses into phrases'


def phrese_reverse(phrese):

    phrese_list = phrese.split()
    length = len(phrese_list)

    for i in range(length//2):
        temp = phrese_list[i]
        phrese_list[i] = phrese_list[length-i-1]
        phrese_list[length-i-1] = temp

    phrese = ' '.join(phrese_list)
    return phrese


print(phrese)
print(phrese_reverse(phrese))