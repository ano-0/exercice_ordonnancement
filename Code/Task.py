import random
import matplotlib.pyplot as plt

'''
class Task: # page 45
    def __init__(self, id: int, machine: int, duration: int, earliest_start_date: int, latest_end_date: int, start_date: int, end_date: int, priority: int):
        self.id = id
        self.machine = machine
        self.duration = duration
        self.earliest_start_date = earliest_start_date
        self.latest_end_date = latest_end_date
        self.start_date = start_date
        self.end_date = end_date
        #self.priority = priority
'''
class Task:
    def __init__(self, id: int, number: int, machine: int, duration: int):
        self.id = id
        self.number = number
        self.machine = machine
        self.duration = duration

tasks = [
    Task( 11,  1, 1,  6),
    Task( 12,  1, 2,  1),
    Task( 13,  1, 3,  5),
    Task( 21,  2, 1,  3),
    Task( 22,  2, 2,  5),
    Task( 23,  2, 3,  8),
    Task( 31,  3, 1, 10),
    Task( 32,  3, 2,  4),
    Task( 33,  3, 3,  1),
    Task( 41,  4, 1, 14),
    Task( 42,  4, 2,  6),
    Task( 43,  4, 3,  3),
    Task( 51,  5, 1,  5),
    Task( 52,  5, 2, 10),
    Task( 53,  5, 3,  6),
    Task( 61,  6, 1,  9),
    Task( 62,  6, 2,  6),
    Task( 63,  6, 3, 10),
    Task( 71,  7, 1,  7),
    Task( 72,  7, 2,  9),
    Task( 73,  7, 3, 12),
    Task( 81,  8, 1, 11),
    Task( 82,  8, 2,  8),
    Task( 83,  8, 3,  9),
    Task( 91,  9, 1,  2),
    Task( 92,  9, 2,  6),
    Task( 93,  9, 3,  6),
    Task(101, 10, 1,  3),
    Task(102, 10, 2,  1),
    Task(103, 10, 3,  7)
]

NUMBER_OF_MACHINES = 3
