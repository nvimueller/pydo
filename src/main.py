from pydo.storage.procedures import get_tasks
from pydo.parser.procedures import match


def main():
    tasks = get_tasks()
    match(tasks)


if "__name__" == "__main__":
    main()
