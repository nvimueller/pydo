from dataclasses import dataclass

@dataclass
class Completer:
    def complete_task(tasks, index):
        tasks.pop(index - 1)
