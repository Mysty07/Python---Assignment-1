
# Write a python program that calculates the factorial of a given number.

a = int(input("Enter the number: "))
fac = 1
for i in range(1,a+1):
    fac = fac*i

print("The factorial of given number is: ",fac)

