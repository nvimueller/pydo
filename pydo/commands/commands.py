def add_task(tasks, new_task):
    tasks.append(new_task)


def delete_task(tasks, deletion_index):
    tasks.pop(deletion_index - 1)


def list_tasks(tasks):
    index = 1
    for task in tasks:
        print(f"[{index}] {task.description} | {task.addition_date}")
        index = index + 1


def rename_task(tasks, task_index, new_description):
    tasks[task_index - 1].description = new_description
