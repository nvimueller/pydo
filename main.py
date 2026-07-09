import sys
from commands.parser import Parser


tasks = []
while sys.argv[0] != "exit":
    parser = Parser.parse(sys.argv, tasks)
