from Task import *
from List import *
from Neighbourhood import *
from Johnson import *
from Gantt import *

def main():
    # solution = neighborhood(tasks)
    solution = johnson2(tasks)
    plot_gantt(tasks, solution)
    pass

if __name__ == "__main__":
    main()
