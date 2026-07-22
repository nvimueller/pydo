# from pydo.commands.parser import Parser
# from pydo.storage.reader import Reader


def main():
    tasks = Reader.read()
    parser = Parser.parse(tasks)

main()
