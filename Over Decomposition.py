def overdecomposition(tasks, numworkers):
    decomposedtasks = decomposetasks(tasks, numworkers)
    for i in range(numworkers):
        print("Processing tasks:", decomposedtasks[i])

def decomposetasks(tasks, numworkers):
    chunksize = (len(tasks) + numworkers - 1) // numworkers
    decomposedtasks = [tasks[i * chunksize:(i + 1) * chunksize] for i in range(numworkers)]
    return decomposedtasks

tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
numworkers = 3
overdecomposition(tasks, numworkers)
