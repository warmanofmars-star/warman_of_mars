import csv
from os import write

with open("users_1.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "email", "role"])
    writer.writerow(["anna", "anna@gmail.com", "admin"])
    writer.writerow(["bob", "bob@gmail.com", "user"])

with open("users_1.csv") as file:
    reader = csv.reader(file)
    print (type(reader))

    for row in reader:
        print(row)

print()

with open("users_1.csv", "r", encoding = "utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        print(row["name"], "-", row["role"])