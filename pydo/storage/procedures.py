import csv
from pydo.structs.task import Task
from importlib.resources import files


def save(tasks):
    path = get_path()
    file = open(path, "w")
    writer = get_writer(file)
    write(tasks, writer)
    file.close()


def write(tasks, writer):
    writer.writerow(["desc", "add_date"])
    for task in tasks:
        row = [task.desc, task.add_date]
        writer.writerow(row)


def get_tasks():
    path = get_path()
    file = open(path, "r")
    reader = get_reader(file)
    tasks = read(reader)
    file.close()
    return tasks


def read(reader):
    next(reader, None)  # skip header
    tasks = []
    for row in reader:
        task = Task(row[0], row[1])
        tasks.append(task)
    return tasks


def get_writer(file):
    return csv.writer(file)


def get_reader(file):
    return csv.reader(file)


def get_path():
    return files("pydo.storage").joinpath("tasks.csv")
