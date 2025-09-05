from Task import *
# METHOD 1 (list)

def highest_priority(tasks: list[Task]) -> Task:
    return(min(tasks, key = lambda task: task.duration))

def update_cooldown(machine_cooldown: list[int]) -> list[int]:
    return [max(0, t-1) for t in machine_cooldown]

def machine_availability(machine_cooldown: list[int]) -> list[bool]:
    return [t == 0 for t in machine_cooldown]


def list_algorithm(tasks_to_manage: list[Task]) -> list[int]:
    solution = []
    remaining_tasks = tasks_to_manage.copy()
    machine_cooldown = [0 for i in range(NUMBER_OF_MACHINES)]
    i = 0
    while remaining_tasks != []:

        # Utile pour des versions plus complexes, mais avec d'autres expressions
        available_machines = machine_availability(machine_cooldown)
        available_tasks = [t for t in remaining_tasks if available_machines[t.machine-1]]

        if available_tasks != []:
            task_to_process = highest_priority(available_tasks)
            if task_to_process.machine == 1:
                solution += [task_to_process.number]
            remaining_tasks.remove(task_to_process)

            machine_cooldown[task_to_process.machine-1] = task_to_process.duration

        i+=1
        machine_cooldown = update_cooldown(machine_cooldown)

    return(solution)

if __name__ == "__main__" :
    x = tasks
    print(x)