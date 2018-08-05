import random
lisa = []

for _ in range(20):
    lisa.append(random.choice(range(100)))
print (lisa)

length = len(lisa)

for i in range(3):
    maxindex = i
    for j in range(i+1,length):
        if lisa[maxindex] < lisa[j]:
            maxindex = j
    
    if i != maxindex:
        lisa[i],lisa[maxindex] = lisa[maxindex],lisa[i]
        print ('第{}大的数为：{}'.format(i+1,lisa[i]))
