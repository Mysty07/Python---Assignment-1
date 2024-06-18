# Write a program that copies the contents of one text file to another

def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r') as source_file:
            content = source_file.read()

        with open(destination_path, 'w') as destination_file:
            destination_file.write(content)

        print(f"Contents copied from {source_path} to {destination_path} successfully.")
    except FileNotFoundError:
        print(f"Error: The file {source_path} does not exist.")
    except IOError as e:
        print(f"Error: {e}")

source_path = input("Enter the path of the source file: ")
destination_path = input("Enter the path of the destination file: ")
copy_file(source_path, destination_path)
