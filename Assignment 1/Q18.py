
# Write a python program that checks if two strings are anagrams of each other

a = input("Enter string 1: ")
b = input("Enter string 2: ")
a1 = set(a)
for i in a1:
    if i not in b:
        if i==" ":
            continue
        else:
            flag = False
            break
    else:
        flag = True
if flag == True:
    print("string 1 and string 2 are anagrams")
else:
    print("string 1 and string 2 are not anagrams")
        