from Task import *
from List import *
from Neighbourhood import *
from Johnson import *
from Gantt import *

def main():
    solution = list_algorithm(tasks)
    plot_gantt(tasks, solution)
    solution = neighborhood(tasks)
    plot_gantt(tasks, solution)
    solution = johnson2(tasks)
    plot_gantt(tasks, solution)
    pass

if __name__ == "__main__":
    main()
