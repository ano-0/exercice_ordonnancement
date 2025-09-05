from Task import *
# METHOD 2 (neighborhood)

def initialise_tasks_order(tasks: list[Task]) -> list[int]:
    improvable_solution = [i + 1 for i in range(len(tasks) // NUMBER_OF_MACHINES)]
    return(improvable_solution)

def evaluate(tasks: list[Task], solution: list[int]) -> int:
    time_per_machine = [0 for i in range(NUMBER_OF_MACHINES)]
    for task_id in solution:
        for i in range(NUMBER_OF_MACHINES):
            if i == 0:
                time_per_machine[i] += tasks[(task_id - 1) * NUMBER_OF_MACHINES + i].duration
            else:
                time_per_machine[i] = max(time_per_machine[i - 1], time_per_machine[i]) + tasks[(task_id - 1) * NUMBER_OF_MACHINES + i].duration

    return(max(time_per_machine))

def new_solution(solution: list[int]) -> list[int]:
    random.shuffle(solution)
    return(solution)

def neighborhood(tasks_to_manage: list[Task]) -> list[int]:
    NUMBER_OF_TRIES = 256
    improvable_solution = initialise_tasks_order(tasks_to_manage)
    improvable_duration = evaluate(tasks_to_manage, improvable_solution)
    for i in range(NUMBER_OF_TRIES):
        other_solution = new_solution(improvable_solution)
        other_duration = evaluate(tasks_to_manage, other_solution)
        if other_duration < improvable_duration:
            improvable_solution = other_solution
            improvable_duration = other_duration

    return(improvable_solution)

