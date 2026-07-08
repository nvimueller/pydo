import csv
from dataclasses import dataclass

@dataclass
class Reader:
    def read():
        with open("tasks.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            tasks = []
            for row in reader:
                task = Task(row[0], row[1], row[2])
                tasks.append(task)
