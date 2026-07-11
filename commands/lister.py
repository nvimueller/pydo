from dataclasses import dataclass


@dataclass
class Lister:
    def list(tasks):
        for task in tasks:
            print(f"{task.text} | " f"urgent: {str(task.is_urgent).lower()}")
