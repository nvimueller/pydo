from commands.parser import Parser
from storage.reader import Reader


def main():
    tasks = Reader.read()
    parser = Parser.parse(tasks)
