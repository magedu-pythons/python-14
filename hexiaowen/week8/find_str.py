def find_str(str1:str,str2:str):
    result = str2.split(str1)
    if len(result) == 0:
        return None
    if result[0] == '':
        return 0
    else:
        return len(result[0])

print(find_str('a','bbbabababab'))