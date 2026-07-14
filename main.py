from commands.parser import Parser
from storage.reader import Reader

tasks = Reader.read()
parser = Parser.parse(tasks)
