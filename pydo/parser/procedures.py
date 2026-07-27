import sys
from datetime import date
from pydo.structs.task import Task
from pydo.storage.procedures import save
from pydo.storage.procedures import get_tasks
from pydo.commands.procedures import add
from pydo.commands.procedures import display
from pydo.commands.procedures import rename
from pydo.commands.procedures import delete


def match(tasks):
    argv = split()
    command = argv[0]
    if command == "add":
        match_add(argv, tasks)
    elif command == "display":
        match_display(argv, tasks)
    elif command == "delete":
        match_delete(argv, tasks)
    elif command == "rename":
        match_rename(argv, tasks)
    else:
        invalid_msg()


def match_add(argv, tasks):
    is_right_len = not argv[1:]
    task_desc = argv[1]
    if task_desc and is_right_len:
        convert_add(argv, tasks)
    else:
        invalid_msg()


def convert_add(argv, tasks):
    desc = argv[1]
    desc.lower()
    add_date = date.today()
    task = Task(desc, add_date)
    add(task, tasks)
    save(tasks)


def is_natural(index):
    if index.isdecimal():
        return True
    else:
        return False


def match_delete(argv, tasks):
    is_right_len: not argv[1:]
    index = argv[1]
    is_index_valid = index and is_natural(index)
    if is_index_valid and is_right_len:
        convert_delete(argv, tasks)
    else:
        invalid_msg()


def convert_delete(argv, tasks):
    index = argv[1]
    delete(index, tasks)
    save(tasks)


def match_rename(argv, tasks):
    is_right_len = not argv[2:]
    desc = argv[2]
    index = argv[1]
    is_index_valid = index and is_natural(index)
    if is_index_valid and desc and is_right_len:
        convert_rename(argv, tasks)
    else:
        invalid_msg()


def convert_rename(argv, tasks):
    index = argv[1]
    desc = argv[2]
    rename(index, desc, tasks)
    save(tasks)


def match_display(argv, tasks):
    is_right_len = not argv[0:]
    if is_right_len:
        convert_display(tasks)
    else:
        invalid_msg()


def convert_display(tasks):
    display(tasks)


def split():
    return sys.argv[1:]


def invalid_msg():
    print("invalid command")
