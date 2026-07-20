import argparse
from models.task import Task
from commands.adder import Adder
from storage.writer import Writer
from storage.reader import Reader
from dataclasses import dataclass
from commands.lister import Lister
from commands.renamer import Renamer
from commands.completer import Completer


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
                task = Task(args.task)
                adder = Adder.add(tasks, task)
                writer = Writer.write(tasks)
            case "done":
                completer = Completer.complete(tasks, args.done_index)
                writer = Writer.write(tasks)
            case "list":
                tasks = Reader.read()
                lister = Lister.list(tasks)
            case "rename":
                renamer = Renamer.rename(tasks, args.rename_index, args.new_name)
                writer = Writer.write(tasks)
