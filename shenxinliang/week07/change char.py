#请将 "1,2,3"，变成 ["1","2","3"]
import re

str_1 = '"1,2,3"'
print(str_1)
lst_2 = re.findall(r'[^,"]+', str_1)   #取去除，" 的数字部分作为一个列表
print(lst_2)