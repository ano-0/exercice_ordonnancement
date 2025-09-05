from Task import *

# Plot Gantt

def determine_durations(tasks: list[Task]) -> dict:
    durations = {}
    for task in tasks:
        if task.number not in durations:
            durations[task.number] = [0] * NUMBER_OF_MACHINES
        durations[task.number][task.machine - 1] = task.duration

    return (durations)


def append_schedule(solution: list[int], durations: dict) -> list:
    schedule = []
    end_times = [[0] * (len(solution) + 1) for i in range(NUMBER_OF_MACHINES)]
    for j, task_id in enumerate(solution, start=1):
        for m in range(NUMBER_OF_MACHINES):
            if m == 0:
                start = end_times[m][j - 1]
            else:
                start = max(end_times[m][j - 1], end_times[m - 1][j])

            end = start + durations[task_id][m]
            end_times[m][j] = end
            schedule.append((m, start, end, task_id))

    return (schedule)


def plot_gantt(tasks: list[Task], solution: list[int]):
    durations = determine_durations(tasks)
    schedule = append_schedule(solution, durations)
    fig, ax = plt.subplots(figsize=(10, 5))
    colors = plt.cm.get_cmap("tab10", len(solution))
    for (m, start, end, task_id) in schedule:
        ax.barh(m, end - start, left=start, height=0.5,
                color=colors(task_id % 10), edgecolor="black")
        ax.text((start + end) / 2, m, f"T{task_id}", va="center", ha="center", color="white")

    ax.set_yticks(range(NUMBER_OF_MACHINES))
    ax.set_yticklabels([f"M{i + 1}" for i in range(NUMBER_OF_MACHINES)])
    ax.set_xlabel("Temps")
    ax.set_ylabel("Machines")
    ax.invert_yaxis()
    plt.title(f"Diagramme de Gantt pour un Flow Shop à {NUMBER_OF_MACHINES} machines")
    plt.tight_layout()
    plt.show()

