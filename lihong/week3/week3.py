
# coding: utf-8

# In[198]:


#judge whether 'x' is in list
x=input('>>>')
lst=['aa','bb','cc','dd',1,2,3]
if x.isdigit():
    if int(x) in lst:
        print(1)
    else:
        print(0)
else:
    if x in lst:
        print(1)
    else:
        print(0)


# In[231]:


#count numble of the value
lst="""
The storm raged more and more ferociously as the night went on. Harry couldn’t sleep. He shivered and turned over, trying to get comfortable, his stomach rumbling with hunger. Dudley’s snores were drowned by the low rolls of thunder that started near midnight. The lighted dial of Dudley’s watch, which was dangling over the edge of the sofa on his fat wrist, told Harry he’d be eleven in ten minutes’ time. He lay and watched his birthday tick nearer, wondering if the Dursleys would remember at all, wondering where the letter-writer was now."""
print(len(lst.split()))

