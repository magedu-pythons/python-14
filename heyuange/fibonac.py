#!/usr/bin/python
def method1():
    lista = []
    for i in range(1,101):
        if i <3:
            lista.append(i)
        elif i>=3:
            if i == lista[len(lista)-1]+lista[len(lista)-2]:
                lista.append(i)
    for each in lista:
        print(each)
def method2():
    listq = []
    i = 0
    while True:
        i+=1
        if i<3:
            listq.append(i)
        elif i>=3 and i<100:
            if i==listq[-1]+listq[-2]:
                listq.append(i)
        else:
                    break
                            
    for each in listq:
        print(each)
def main():
    method1()
    method2()

if __name__ =='__main__':
    main()
