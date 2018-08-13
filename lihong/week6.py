#to make a dict [{'a': 'c'}, {'b': 'd'}] with function lambda
[(lambda k,v:{k[i]:v[i]})((('a'),('b')) ,(('c'),('d')))for i in range(len((('a'),('b'))))]


#to reverse the words in sentence
def sentence():
    s=str(input(">>>"))
    s=s.strip().split()
    s.reverse()
    print(' '.join(s))

sentence()