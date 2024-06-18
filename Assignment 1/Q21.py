
# Write a python program that counts the occurrences of a specific element in a list

a = int(input("Enter the no. of elements you want to add: "))
list1 = []
for i in range(a):
    ele = input("Enter the element: ")
    list1.append(ele)

print(list1)
find = input("Enter the element you want to count: ")
print("No. of occurrences: ",list1.count(find))
