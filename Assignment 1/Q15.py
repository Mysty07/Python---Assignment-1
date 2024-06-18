# Write a program that reads data from a CSV file and prints it to the console.

import csv

def read_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(', '.join(row))

if __name__ == "__main__":
    file_path = 'data.csv'  
    read_csv(file_path)
