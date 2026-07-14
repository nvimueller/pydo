import argparse
from models.task import Task
from commands.adder import Adder
from storage.writer import Writer
from storage.reader import Reader
from dataclasses import dataclass
from commands.lister import Lister
from commands.completer import Completer


@dataclass
class Parser:
    def parse(tasks):
        parser = argparse.ArgumentParser(prog="pydo")
        subparsers = parser.add_subparsers(dest="command", required=True)
        add_parser = subparsers.add_parser("add")
        add_parser.add_argument("task")
        list_parser = subparsers.add_parser("list")
        done_parser = subparsers.add_parser("done")
        done_parser.add_argument("id", type=int)

        args = parser.parse_args()
        match args.command:
            case "add":
                task = Task(args.task)
                adder = Adder.add(tasks, task)
                writer = Writer.write(tasks)
                print("---------------------")
            case "done":
                completer = Completer.complete(tasks, args.id)
                writer = Writer.write(tasks)
                print("---------------------")
            case "list":
                tasks = Reader.read()
                lister = Lister.list(tasks)
                print("---------------------")
