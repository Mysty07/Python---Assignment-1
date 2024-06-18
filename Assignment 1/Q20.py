
# Write a python program that takes a list of numbers and returns their sum

a = int(input("Enter the no. of elements you want to add in the list: "))
list1 = []
for i in range(a):
    b = int(input("Enter the element: "))
    list1.append(b)

sum = 0
for i in list1:
    sum = sum+i
print("The sum of all the elements: ",sum)