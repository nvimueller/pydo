import argparse
from datetime import date
from pydo.models.task import Task
from dataclasses import dataclass
from pydo.commands.adder import Adder
from pydo.storage.writer import Writer
from pydo.storage.reader import Reader
from pydo.commands.lister import Lister
from pydo.commands.renamer import Renamer
from pydo.commands.completer import Completer


@dataclass
class Parser:
    def setup_argparse():
        parser = argparse.ArgumentParser(prog="pydo")
        subparsers = parser.add_subparsers(dest="command", required=True)

        add_parser = subparsers.add_parser("add")
        add_parser.add_argument("task", type=str)

        list_parser = subparsers.add_parser("list")

        done_parser = subparsers.add_parser("done")
        done_parser.add_argument("done_index", type=int)

        rename_parser = subparsers.add_parser("rename")
        rename_parser.add_argument("rename_index", type=int)
        rename_parser.add_argument("new_name", type=str)

        return parser

    def parse(tasks):
        parser = Parser.setup_argparse()
        args = parser.parse_args()
        match args.command:
            case "add":
                task = Task(args.task, date.today())
                adder = Adder.add(tasks, task)
                writer = Writer.write(tasks)
            case "done":
                if tasks and tasks[args.done_index - 1] and args.done_index != 0:
                    completer = Completer.complete(tasks, args.done_index)
                    writer = Writer.write(tasks)
                else:
                    print("your index is out of bounds")
            case "list":
                tasks = Reader.read()
                if tasks:
                    lister = Lister.list(tasks)
                else:
                    print("there are no tasks to be listed")
            case "rename":
                if tasks and tasks[args.rename_index - 1] and args.rename_index != 0:
                    renamer = Renamer.rename(tasks, args.rename_index, args.new_name)
                    writer = Writer.write(tasks)
                else:
                    print("your index is out of bounds")
