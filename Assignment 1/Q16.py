
# Write a program in python that counts the frequency of each character in a string

a = input("Enter a string: ")
b = set(a)
print("Requencies of each character present...")
print()
for i in b:
    print("frequency of "+i+" is: ",a.count(i))