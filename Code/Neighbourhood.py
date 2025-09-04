from Task import *
# METHOD 2 (neighborhood)

def initialise_tasks_order(tasks: list[Task]) -> list[Task]:
    improvable_proposition = [[]]
    for task in tasks:
        improvable_proposition[task.machine - 1] += [task]
    return (improvable_proposition)


def evaluate(proposition: list[Task]) -> int:
    duration = 0
    t = 0
    time_per_machine = [0 for i in range(NUMBER_OF_MACHINES)]
    for task in proposition:
        time_per_machine[task.machine - 1] = task.duration


def neighborhood(tasks_to_manage: list[Task]) -> list[Task]:
    improvable_proposition = initialise_tasks_order(tasks_to_manage)
    duration = evaluate(improvable_proposition)
