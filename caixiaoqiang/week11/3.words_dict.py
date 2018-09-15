# 根据字典，从一个抹去空格的字符串里面提取出全部单词组合，并且拼接成正常的句子：
# 例如：输入一个字符串："thisisanexample"
#       程序输出："this is an example"


def WordsDict(strs):
    dict = {'is': 'is', 'this': 'this', 'example': 'example', 'an': 'an', 'any': 'any', 'and': 'and'}
    lens = len(strs)
    words = ""
    start = 0
    while start < lens:
        val = ""
        rec = start
        for end in range(start + 1, lens + 1):
            for value in dict.values():
                if strs[start:end] == value:
                    if val < value:
                        val = value
                        rec = end
        if rec != start:
            start = rec - 1
        if val != "":
            if words == "":
                 words += val
            else:
                words += " " + val

        start += 1
    return words


try:
    # strs = str(input("请输入字符串："))
    strs = 'thisisananyandexample'
    print(strs)
    deal = WordsDict(strs)
    print(deal)
except Exception as e:
    print(e)
