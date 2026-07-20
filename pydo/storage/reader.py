import csv
from pydo.models.task import Task
from dataclasses import dataclass
from importlib.resources import files


@dataclass
class Reader:
    def read():
        tasks_path = files("pydo.storage").joinpath("tasks.csv")
        with tasks_path.open("r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            tasks = []
            for row in reader:
                task = Task(row[0], row[1])
                tasks.append(task)
            return tasks
