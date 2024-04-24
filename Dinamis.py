import random

def dinamis(tasks, workersload):
    for task in tasks:
        worker = lowloads(workersload)
        print("Task", task, "sent to worker", worker+1)
        workersload[worker] += 1

def lowloads(workersload):
    minload = min(workersload)
    return workersload.index(minload)

tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numworkers = 4
workersload = [0] * numworkers 
dinamis(tasks, workersload)
