from dataclasses import dataclass


@dataclass
class Lister:
    def list(tasks):
        index = 1
        for task in tasks:
            print(f"{index}. {task.text}")
            index = index + 1
