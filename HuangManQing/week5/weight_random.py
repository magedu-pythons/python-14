import random
import bisect
def weight_random1(**kwargs):
    
    goods_list = [goods for goods,_ in kwargs.items()]
    weights_list = [weight for _, weight in kwargs.items()]
    
    sums = 0
    weights_accumulate = []
    for i in range(len(kwargs)):
        sums = sums + weights_list[i]
        weights_accumulate.append(sums)
        
    return random.choices(goods_list,weights=weights_accumulate)
	

def weight_random2(**kwargs):
    goods_list = [goods for goods,_ in kwargs.items()]
    weights_list = [weight for _, weight in kwargs.items()]
    
    sums = 0
    weights_accumulate = []
    for i in range(len(kwargs)):
        sums = sums + weights_list[i]
        weights_accumulate.append(sums)
    # Pick up a number from 0 to sums, and which range it falls which good will be return      
    reference_num = random.randint(0,sums)
    # Locate the insertion point for x in a to maintain sorted order. 
    pickup_key = bisect.bisect_left(weights_accumulate,reference_num) 
    return(goods_list[pickup_key])


	

def weight_random3(**kwargs):
    goods_list = [goods for goods,_ in kwargs.items()]
    weights_list = [weight for _, weight in kwargs.items()]
    
    sums = 0
    weights_accumulate = []
    for i in range(len(kwargs)):
        sums = sums + weights_list[i]
        weights_accumulate.append(sums)
    # Pick up a number from 0 to sums, and which range it falls which good will be return      
    reference_num = random.randint(0,sums)
    pickup_key = None
    for i in range(len(kwargs)):
        if reference_num <= weights_accumulate[i]:
            pickup_key = i
            break
        else:
            continue
    return(goods_list[pickup_key])

