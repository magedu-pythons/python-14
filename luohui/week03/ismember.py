print("Input a list, separate elements by spaces")
ilist = input(">>> ").strip(' ,')

print("Input a element")
word = input(">>> ").strip(' ,')

print(1 if word in ilist else 0)
