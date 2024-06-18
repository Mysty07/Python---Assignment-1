
# Write a python program that returns the minimum and maximum values in a list of numbers.

a = int(input("Enter the no. of elements you want to add: "))
list1 = []
for i in range(a):
    ele = int(input("Enter the element: "))
    list1.append(ele)

print(list1)
print("Maximum number: ",max(list1))
print("Minimum number: ",min(list1))