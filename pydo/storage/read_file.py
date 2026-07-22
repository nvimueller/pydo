import csv
import pydo.models.task
from importlib.resources import files


@dataclass
class Reader:
    def read():
        # write something to replace this finding
        tasks_path = files("pydo.storage").joinpath("tasks.csv")
        with tasks_path.open("r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            tasks = []
            for row in reader:
                task = Task(row[0], row[1])
                tasks.append(task)
            return tasks
