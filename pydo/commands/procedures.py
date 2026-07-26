def add_to_task_list(task_list, new_task):
    task_list.append(new_task)


def delete_from_task_list(task_list, deletion_index):
    task_list.pop(deletion_index - 1)


def print_task_list(task_list):
    printing_index = 1
    for task in task_list:
        print(f"[{printing_index}] {task.description} | {task.addition_date}")
        printing_index = printing_index + 1


def rename_task(task_list, renaming_index, new_description):
    task_list[renaming_index - 1].description = new_description
