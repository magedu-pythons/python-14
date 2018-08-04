import random

goods = {"袜子": 10, "鞋子": 20, "拖鞋": 30, "项链": 40}


def outer(func):
    def inner(goods_deal):
        func(goods_deal)

        count = {}
        goods_lst = []
        for k in goods_deal:
            count[k] = 0
            goods_lst.append(k)

        times = int(input("返回的次数:"))
        lst = []
        num2 = 1
        while True:
            num = random.randint(1, times)
            if num not in lst:
                lst.append(num)
                print("第{:>2}次返回：".format(num2), end='')
                if num > times * 0.6:
                    count[goods_lst[3]] = (count[goods_lst[3]] + 1)
                    print(goods_lst[3])
                elif num > times * 0.3:
                    count[goods_lst[2]] = count[goods_lst[2]] + 1
                    print(goods_lst[2])
                elif num > times * 0.1:
                    count[goods_lst[1]] = count[goods_lst[1]] + 1
                    print(goods_lst[1])
                else:
                    count[goods_lst[0]] = count[goods_lst[0]] + 1
                    print(goods_lst[0])
                if len(lst) == times:
                    break
                num2 += 1
        return count
    return inner

@outer
def search_goods(goods_info):
    print("商品库存信息:", end=' ')
    for k, v in goods_info.items():
        print('{}:{}'.format(k, v), end=' ')
    print()
    return 0


goods_dict = search_goods(goods)
sum_value = 0
for value in goods_dict.values():
    sum_value += value
for key, value in goods_dict.items():
    print("商品:{}  返回概率:{:.1%}".format(key, value / sum_value))

