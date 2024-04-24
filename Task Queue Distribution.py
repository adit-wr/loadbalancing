import queue

def taskqueuedistribution(tasks, taskqueue):
    for task in tasks:
        taskqueue.put(task)

    while not taskqueue.empty():
        task = taskqueue.get()
        print("Processing task:", task)

tasks = [1, 8, 3, 9, 7, 6, 5, 2, 4, 10]
taskqueue = queue.Queue()
taskqueuedistribution(tasks, taskqueue)
