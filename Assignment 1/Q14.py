# Write a program that reads multiple lines of input from the user until they 
# enter an empty line, then prints all the line

lines = []
print("Enter lines of text (press Enter on an empty line to stop):")
    
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
    
print("\nYou entered:")
for line in lines:
    print(line)