
# Write a python program that calculates the sum of the digits of a given number

a = int(input("Enter a number: "))
sum = 0
while(a!=0):
    digit = a%10
    sum = sum+digit
    a = int(a/10)
print("The sum of the digits of the number is: ",sum)