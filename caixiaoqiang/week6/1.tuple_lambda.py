
tuple1 = (('a'),('b'))
tuple2 = (('c'),('d'))

tup_all = tuple1, tuple2

lst = [(lambda tup, x: {tup[0][x]: tup[1][x]})(tup_all, x) for x in range(2)]

print(lst)
