from commands.parser import Parser

tasks = []
line = input().split()
command = line[0]

while line[0] != "exit":
    parser = Parser.parse(tasks, line)
    line = input().split()
