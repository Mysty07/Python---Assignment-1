
# Write a program that acts as a simple calculator. It should take two 
# numbers and an operator (+, -, *, /) as input and print the result.

a = eval(input("Enter first number: "))
b = eval(input("Enter second number: "))
ope = input("Enter the operation you want to perform(+,-,*,/): ")

if ope=='+':
    print("a+b = ",a+b)
elif ope =='-':
    print("a-b = ",a-b)
elif ope == '*':
    print("a*b = ",a*b)
elif ope == '/':
    print("a/b = ",a/b)
else:
    print("Enter a valid operation")