from dataclasses import dataclass


@dataclass
class Renamer:
    def rename(tasks, index, new_text):
        tasks[index - 1].text = new_text
