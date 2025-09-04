from Task import *
# METHOD 1 (list)

def highest_priority(tasks: list[Task], id: int) -> int:
    #return(max(tasks, key = lambda task: task.priority))
    #return(min(tasks, key = lambda task: task.latest_end_date))
    tasks_filtered_by_id = []
    for task in tasks:
        if task.id == id:
            tasks_filtered_by_id += [task]

    return(min(tasks_filtered_by_id, key = lambda task: task.duration))

def remove(tasks: list[Task], task_to_remove: Task) -> list[Task]:
    removed_tasks = []
    for task in tasks:
        if task.id != task_to_remove.id:
            removed_tasks += [task]

    return(removed_tasks)

def list_algorithm(tasks_to_manage: list[Task]) -> list[int]:
    t = []
    ordered_tasks = []
    available_tasks = []
    remaining_tasks = tasks_to_manage
    available_machines = [True for i in range(NUMBER_OF_MACHINES)]
    i = 0
    while ordered_tasks != tasks_to_manage:
        if available_tasks != []:
            task_to_process = highest_priority(available_tasks)
            ordered_tasks += [task_to_process]
            remaining_tasks = remove(remaining_tasks, task_to_process)
            t += [task_to_process.duration]
            i += 1
        else:
            while available_machines == [False for i in range(NUMBER_OF_MACHINES)]:
                i += 1
                # ???

    return(ordered_tasks)

