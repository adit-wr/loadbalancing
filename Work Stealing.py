def workstealing(tasks, numworkers):
    workers = [[] for a in range(numworkers)]
    for i, task in enumerate(tasks):
        workers[i % numworkers].append(task)

    for i in range(numworkers):
        processtasks(workers[i], workers[(i + 1) % numworkers])

def processtasks(tasks, otherworkertasks):
    print("Processing tasks:", tasks)
    if len(tasks) < len(otherworkertasks):
        stolentasks = otherworkertasks[:len(otherworkertasks)//2]
        print("Worker stole tasks:", stolentasks)

tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
numworkers = 3
workstealing(tasks, numworkers)
