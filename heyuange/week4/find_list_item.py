#！usr/bin/python
def main():
    yourlist = list(input("请输入您的列表元素："))
    youritem = input("请输入您要查找的元素：")
    if youritem in yourlist:
        print("1")
    else:
        print("0")
    return

if __name__ == "__main__":
    main()
