from models.task import Task
from commands.adder import Adder
from commands.lister import Lister
from commands.completer import Completer
from dataclasses import dataclass

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
            case "done":
                completer = Completer.complete(tasks, int(line[1])) 
            case "list":
                lister = Lister.list(tasks)
