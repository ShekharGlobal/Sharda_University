import csv

with open("employee.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["salary"])