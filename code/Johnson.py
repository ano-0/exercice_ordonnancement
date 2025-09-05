from Task import *

# METHOD 3 (Johnson and virtual machine)

def duration_virt_machine(tasks:list[Task], n: int, i:int):
    job = [t for t in tasks if t.number == n]
    if i==1:
        [d1] = [t.duration for t in job if t.machine == 1]
        [d2] = [t.duration for t in job if t.machine == 2]
        return d1 + d2
    if i==2:
        [d2] = [t.duration for t in job if t.machine == 2]
        [d3] = [t.duration for t in job if t.machine == 3]
        return d2 + d3


def johnson2(tasks: list[Task]) -> list[int]:
    jobs = list(dict.fromkeys([t.number for t in tasks]))
    L1, L2 = [], []
    for n in jobs:
        D1 = duration_virt_machine(tasks, n, 1)
        D2 = duration_virt_machine(tasks, n, 2)
        if D1 < D2 :
            L1.append(n)
        else:
            L2.insert(0, n)
    return sorted(L1, key= lambda n: duration_virt_machine(tasks, n, 1)) + sorted(L2, reverse = True, key= lambda n: duration_virt_machine(tasks, n, 2))
