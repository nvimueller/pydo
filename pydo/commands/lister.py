from dataclasses import dataclass


@dataclass
class Lister:
    def list(tasks):
        index = 1
        for task in tasks:
            print(f"{index}. {task.text} | added: {task.addition_date}")
            index = index + 1
