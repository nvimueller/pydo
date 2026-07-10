from models.task import Task
from commands.adder import Adder
from storage.writer import Writer
from storage.reader import Reader
from dataclasses import dataclass
from commands.lister import Lister
from commands.completer import Completer

@dataclass
class Parser:
    def parse(tasks, line):
        match line[0]:
            case "add":
                if line[2] == "yes":
                    task = Task(line[1], True)
                if line[2] == "no":
                    task = Task(line[1], False)
                adder = Adder.add(tasks, task)
                writer = Writer.write(tasks)
                print("---------------------")
            case "done":
                completer = Completer.complete(tasks, int(line[1]))
                writer = Writer.write(tasks)
                print("---------------------")
            case "list":
                tasks = Reader.read()
                lister = Lister.list(tasks)
                print("---------------------")
