
# Write a program in python that checks if a string starts with a given prefix 
# or ends with a given suffix.

a = input("ENter a string: ")
pre = input("enter the prefix: ")
suf = input("Enter the suffix: ")

if (a.startswith(pre)):
    print("string starts with given prefix")
else:
    print("string does not start with given prefix")

if(a.endswith(suf)):
    print("string ends with given suffix")
else:
    print("string does not ends with given suffix")