from dataclasses import dataclass

@dataclass
class Task:
    text: str
    is_done: bool
    is_urgent: bool
