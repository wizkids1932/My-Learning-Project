# Python program to read and write CSV files

import csv

# Writing to a CSV file
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'Los Angeles'])

# Reading from a CSV file
with open('example.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
