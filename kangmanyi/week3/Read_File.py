#任一个英文的纯文本文件，统计其中的单词出现的个数。
def read_file():
    f = open(r'D:\PycharmProjects\Week\week3\test3.txt')
    readline = f.readlines()
    word = []  # 存储单词
    # 得到文章的单词并且存入列表中：
    for line in readline:
        # 因为原文中每个单词都是用空格 或者逗号加空格分开的，
        line = line.replace(',', '')  # 除去逗号只要空格来分开单词
        line = line.strip()
        wo = line.split(' ')
        word.extend(wo)
    return word


def clear_account(lists):
    # 去除重复的值
    wokey = {}
    wokey = wokey.fromkeys(lists)
    word_1 = list(wokey.keys())
    # 然后统计单词出现的次数,并将它存入一个字典中
    for i in word_1:
        wokey[i] = lists.count(i)
    return wokey

def sort_1(wokey):
    # 删除''字符
    del [wokey['']]
    # 排序,按values进行排序，如果是按key进行排序用sorted(wokey.items(),key=lambda d:d[0],reverse=True)
    wokey_1 = {}
    wokey_1 = sorted(wokey.items(), key=lambda d: d[1], reverse=True)
    wokey_1 = dict(wokey_1)
    return wokey_1

def main(wokey_1):
    # 输出前10个
    i = 0
    for x, y in wokey_1.items():
        if i < 10:
            print('the word is "', '{}'.format(x), '"''"', ' and its amount is "', '{}'.format(y), '"')
            i += 1
            continue
        else:
            break

main(sort_1(clear_account(read_file())))