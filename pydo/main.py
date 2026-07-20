from pydo.commands.parser import Parser
from pydo.storage.reader import Reader


def main():
    tasks = Reader.read()
    parser = Parser.parse(tasks)

if __name__ == "__main__":
    main()
