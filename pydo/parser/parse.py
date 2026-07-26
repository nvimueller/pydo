import sys
from datetime import date
from pydo.structs import task
from pydo.storage.procedures import save_task_list
from pydo.commands.procedures import add_to_task_list


def match_command():
    argv = split_argv()
    command = argv[0]
    if command == "add":
        match_add_command(argv)
    elif command == "print":
        match_print_command(argv)
    elif command == "delete":
        match_delete_command(argv)
    elif command == "rename":
        match_rename_command(argv)
    else: invalid_command_message() 


def match_add_command(argv):
    is_empty_after_description: not argv[1:]
    task_description = argv[1]
    if task_description and is_empty_after_description:
        convert_add_command(argv)
    else: invalid_command_message()


def convert_add_command(argv):
    task_description = argv[1]
    task_description.lower()
    addition_date = date.today()
    new_task = task(task_description, addition_date)
    add_to_task_list(task_list, new_task)
    save_task_list(task_list)


def is_natural_number(index):
    if index.isdecimal(): return True
    else: return False


def match_delete_command(argv):
    is_empty_after_index: not argv[1:]
    index = argv[1]
    is_index_valid = is_natural_number(index)
    if index and is_empty_after_index and is_index_valid:
        convert_delete_command(argv)
    else: invalid_command_message()


def convert_delete_command(argv):
    index = argv[1]
    delete_from_tasks(tasks, index)
    save_tasks(tasks)

    
def match_rename_command(argv):
def convert_rename_command(argv):


def match_print_command(argv):


def convert_print_command(argv):


def split_argv():
    return sys.argv[1:] # remove "pydo" from argv


def invalid_command_message():
    print("invalid command")
