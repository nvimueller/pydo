import csv
from dataclasses import dataclass

@dataclass
class Writer
    def write(tasks):
        with open("tasks.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow("text,is_done,is_urgent")
            for task in tasks:
                row = [task.text, task.is_done, task.is_urgent]
                writer.writerow(row)
