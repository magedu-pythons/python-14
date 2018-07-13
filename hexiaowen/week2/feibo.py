count=0
feibo_list=[]
i=1
for i in range(1,50):
    count+=i
    if count>100:
        break
    feibo_list.append(count)
print(feibo_list)