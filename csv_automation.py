import csv


with open('sample.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"Name: {row['Name']}, Email: {row['Email']}")
