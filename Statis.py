def static(tasks, numworkers):
    taskperworker = len(tasks) // numworkers
    for i in range(numworkers):
        workertasks = tasks[i * taskperworker: (i + 1) * taskperworker]
        print("Processing tasks:", workertasks)

tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
numworkers = 3
static(tasks, numworkers)