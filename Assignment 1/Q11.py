
#  Write a python program that generates the first n numbers in the Fibonacci sequence

n = int(input("Enter the value of n = "))
a = 0
b = 1
print(a)
print(b)
for i in range (n):
    next = a+b
    print(next)
    a = b
    b = next
