from dataclasses import dataclass

@dataclass
class Completer:
    def complete(tasks, index):
        tasks.pop(index - 1)
