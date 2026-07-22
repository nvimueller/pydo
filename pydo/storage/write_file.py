import csv
from dataclasses import dataclass
from importlib.resources import files


@dataclass
class Writer:
    def write(tasks):
        # write something to replace finding
        tasks_path = files("pydo.storage").joinpath("tasks.csv")
        with tasks_path.open("w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["text", "addition_date"])
            for task in tasks:
                row = [str(task.text), str(task.addition_date)]
                writer.writerow(row)
