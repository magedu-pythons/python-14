import random

socks = ['WZ'] * 10
shoes  = ['XZ'] * 20
slippers  = ['TX'] * 30
necklace = ['XL'] * 40

All_Before = socks + shoes + slippers + necklace
All_After  = random.sample(All_Before, 40)
print (All_After.count('WZ'))
print(All_After.count('XZ'))
print(All_After.count('TX'))
print(All_After.count('XL'))
