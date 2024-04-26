import csv


def load_metros():
    metros = []
    with open("db/metros.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            metros.append(row)
    return metros
