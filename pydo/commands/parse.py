import argparse
from datetime import date
# from pydo.models.task import Task
# from dataclasses import dataclass
# from pydo.commands.adder import Adder
# from pydo.storage.writer import Writer
# from pydo.storage.reader import Reader
# from pydo.commands.lister import Lister
# from pydo.commands.renamer import Renamer
# from pydo.commands.completer import Completer

# TODO: study set_defaults function
def setup_argparse():
    parser = argparse.ArgumentParser(prog="pydo")
    subparsers = parser.add_subparsers(dest="command", required=True)
    get_args(parser)
    setup_add_command(subparsers, args)
    setup_list_command(subparsers)
    setup_delete_command(subparsers, args)
    setup_rename_command(subparsers, args)

def get_args(parser):
    return parser.parse_args()

def setup_add_command(subparsers, args):
    add_command_parser = subparsers.add_parser("add")
    add_command_parser.add_argument("description", type=str)
    add_command_parser.set_defaults(func=add_command(args))

def setup_list_command(subparsers, tasks):
    list_command_parser = subparsers.add_parser("list")
    list_command_parser.set_defaults(func=list_command())

def setup_delete_command(subparsers, args, tasks):
    delete_command_parser = subparsers.add_parser("delete")
    delete_command_parser.add_argument("deletion_index", type=int)
    delete_command_parser.set_defaults(func=delete_command(args))

def setup_rename_command(subparsers, args, tasks):
    rename_command_parser = subparsers.add_parser("rename")
    rename_command_parser.add_argument("renaming_index", type=int)
    rename_command_parser.add_argument("new_description", type=str)
    rename_command_parser.set_defaults(func=rename_command(args))

def add_command(args):
    new_task = task(args.description, date.today())
    add(tasks, new_task)
    write(tasks)

def rename_command(args):
    # if list not empty and index exists
def delete_command(args):
    # if list not empty and index exists
def list_command(args):
    tasks = read_tasks()
        if tasks:
            list_tasks(tasks)
        else:
            print("no tasks to be listed")
 
def parse(tasks):
    parser = Parser.setup_argparse()
        args = parser.parse_args()
        match args.command:
            case "add":
            case "done":
                if tasks and tasks[args.done_index - 1] and args.done_index != 0:
                    completer = Completer.complete(tasks, args.done_index)
                    writer = Writer.write(tasks)
                else:
                    print("your index is out of bounds")
            case "list":
           case "rename":
                if tasks and tasks[args.rename_index - 1] and args.rename_index != 0:
                    renamer = Renamer.rename(tasks, args.rename_index, args.new_name)
                    writer = Writer.write(tasks)
                else:
                    print("your index is out of bounds")
