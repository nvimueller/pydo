from dataclasses import dataclass

@dataclass
class Lister:
    def list_tasks(tasks):
        for task in tasks:
            number = 1
            print(
                f"{number}. {task.text} | "
                f"urgent: {str(task.is_urgent).lower()}"
            )
            number = number + 1
