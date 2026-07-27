def add(task, tasks):
    tasks.append(task)


def delete(index, tasks):
    tasks.pop(index - 1)


def display(tasks):
    index = 1
    for task in tasks:
        print(f"[{index}] {task.desc} | {task.add_date}")
        index = index + 1


def rename(index, new_desc, tasks):
    tasks[index - 1].desc = new_desc
