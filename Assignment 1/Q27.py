
# Write a program in python that converts a string into a list of its characters

a = input("enter a string = ")
list1 = list(a)
for i in list1:
    if i == " ":
        list1.remove(i)
print("list formed = ",list1)