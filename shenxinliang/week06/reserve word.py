sentence = input('>>>输入一句英文\n')

def re_seq(s):
    word_list = s.split(' ')    # 以空格分列组成一个新列表
    word_list.reverse()       #reverse会对列表的元素进行反向排序
    seq = ' '
    print(seq.join(word_list))  #以sep作为分隔符，将所有的元素合并成一个新的字符串

re_seq(sentence)