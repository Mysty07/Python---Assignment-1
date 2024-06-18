
# Write a program that reads the content of a text file and prints it to the console

a = input("Enter the name of file that you want to read: ")
f1 = open( a,'r') 
data = f1.read()
print("The content of the file is:")
print(data)
f1.close()