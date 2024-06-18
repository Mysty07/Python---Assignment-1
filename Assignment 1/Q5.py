
# Write a program that takes a string input from the user and writes it to a text file.

a = input("Enter a string of your choice: ")
f1 = open("Q5.txt",'w')
print(a, file = f1)
f1.close()
print("The text is written in the file!!")