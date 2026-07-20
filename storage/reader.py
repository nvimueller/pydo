import csv
from models.task import Task
from dataclasses import dataclass


@dataclass
class Reader:
    def read():
        with open("storage/tasks.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            tasks = []
            for row in reader:
                task = Task(row[0])
                tasks.append(task)
            return tasks
