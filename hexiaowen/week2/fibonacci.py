feibo_list=[1,1]
for i in range(50):
    new=feibo_list[i]+feibo_list[i+1]
    if new>100:
        break
    feibo_list.append(new)
print(feibo_list)