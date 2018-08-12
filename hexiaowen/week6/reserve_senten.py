sentence = 'hello mage education.'

def re_seq(s):
    word_list = s.strip('.').split(' ')
    word_list.reverse()
    seq = ' '
    print(seq.join(word_list)+'.')

re_seq(sentence)