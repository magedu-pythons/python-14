#根据字典，从一个抹去空格的字符串里面提取出全部单词组合，并且拼接成正常的句子:
#例如: 输入一个字符串："thisisanexample", 程序输出: "this is an example"

dic={'1':'this','2':'is','3':'an','4':'example','5':'hello'}
str="thisisanexample"
def sentence(dic,str):
    strout=""
    start=0
    while True:
      if start==len(str):
         break
      for v in dic.values():
         n=len(v)
         if str[start:n+start]==v:
           strout=strout+v+" "
           start+=n
    return strout

print(sentence(dic,str))

