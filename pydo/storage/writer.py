import csv
from dataclasses import dataclass


@dataclass
class Writer:
    def write(tasks):
        with open("pydo/storage/tasks.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["text", "addition_date"])
            for task in tasks:
                row = [str(task.text), str(task.addition_date)]
                writer.writerow(row)
