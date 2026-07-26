import csv
from pydo.structs.task import task
from importlib.resources import files


def save_task_list(task_list):
    file_path = get_file_path()
    file = open_file(file_path, "w")
    file_writer = get_file_writer(file)
    write_task_list(task_list, file_writer)
    close_file(file)


def write_task_list(task_list, file_writer):
    writer.writerow(["text", "addition_date"])
    for task in task_list:
        row = [task.description, task.addition_date]
        file_writer.writerow(row)


def get_task_list():
    file_path = get_file_path()
    file = open_file(file_path, "r")
    file_reader = get_file_reader(file)
    task_list = read_task_list(file_reader)
    close_file(file)
    return task_list


def read_task_list(file_reader):
    next(reader)  # skip header
    task_list = []
    for row in file_reader:
        new_task = task(row[0], row[1])
        task_list.append(new_task)
    return task_list


def open_file(file_path, mode):
    return open(file_path, mode)


def close_file(file):
    file.close()


def get_file_writer(file):
    return csv.writer(file)


def get_file_reader(file):
    return csv.reader(file)


def get_file_path():
    return files("pydo.storage").joinpath("tasks.csv")
