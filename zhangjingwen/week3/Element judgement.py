#要求： 给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0

def elementJudgement(lst,x=None):
    while type(lst)==list:
        return 1 if x in lst else 0
        break
    else:
        print('TypeError:the arguement lst must be list')
        return None

lst = [11,2,5,8,5,4]
print(elementJudgement(lst,5))
