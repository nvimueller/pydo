from commands.adder import Adder
from commands.lister import Lister
from models.task import Task
from commands.completer import Completer
from dataclasses import dataclass

@dataclass
class Parser:
    def parse(argv, tasks):
        match argv[1]:
            case "add":
                task = Task(argv[2], argv[3])                
                adder = Adder.add(tasks, task) 
            case "done":
                completer = Completer.complete(tasks, argv[2]) 
            case "list":
                lister = Lister.list(tasks)
