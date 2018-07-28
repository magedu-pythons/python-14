while True:
    number = input("please input a five-digit number>>").strip().lstrip('0')
    if number.isdigit()and len(number)==5:
        break
length = len(number)
for i in range(length//2):
    if number[i]!=number[length-i-1]:
        print('The number you input is not a palindromic number.')
        break
else:
    print('The number you input is a palindromic number.')