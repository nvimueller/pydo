import csv
from dataclasses import dataclass


@dataclass
class Writer:
    def write(tasks):
        with open("storage/tasks.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["text"])
            for task in tasks:
                row = [str(task.text)]
                writer.writerow(row)
