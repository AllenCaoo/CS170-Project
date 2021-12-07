import os
from parse import read_input_file, write_output_file

def solve(tasks):
    def sort(tasks, t, d, p):
        for i in range(1, len(tasks)):
            key = tasks[i]
            j = i-1
            while j >= 0 and weight(key, t, d, p) < weight(tasks[j], t, d, p) :
                    tasks[j+1] = tasks[j]
                    j -= 1
            tasks[j+1] = key

    def weight(task, t, d, p):
        return t*task.get_deadline() + 25*d*task.get_duration() + 14*p*task.get_late_benefit(0)

    def knapSack(W, n, tasks):
        #W = time
        #n = num tasks
        K = [[0 for x in range(W + 1)] for x in range(n + 1)]
        history = [[0 for x in range(W + 1)] for x in range(n + 1)]

        # Build table K[][] in bottom up manner
        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif tasks[i-1].get_duration() <= w:
                    profit = tasks[i-1].get_late_benefit(w-tasks[i-1].get_deadline())
                    # profit = arrp[i-1]*math.exp(-0.0170*max(0, w-arrt[i-1]))
                    do = profit + K[i-1][w-tasks[i-1].get_duration()]
                    # do = profit + K[i-1][w-arrd[i-1]]
                    dont = K[i-1][w]
                    if do > dont:
                        K[i][w] = do
                        history[i][w] = history[i-1][w-tasks[i-1].get_duration()] + 2**(i-1)
                    else:
                        K[i][w] = dont
                        history[i][w] = history[i-1][w]
                else:
                    K[i][w] = K[i-1][w]
                    history[i][w] = history[i-1][w]
        maximum = -1
        historyMax = 0
        for i in range(0, W):
            if maximum < K[n][i]:
                maximum = K[n][i]
                historyMax = history[n][i]
        historyArray = []
        h = bin(historyMax)
        h = h[2:]
        h = h[::-1]
        for i in range(0, len(h)):
            if h[i] == '1':
                historyArray.append(tasks[i].get_task_id())
        return maximum, historyArray

    W = 1440
    N = len(tasks)
    maximum = -1
    maximumhistory = []
    at = 1
    
    tempmax, tempmaxhist = knapSack(W, N, tasks)
    if tempmax > maximum:
        maximum = tempmax
        maximumhistory = tempmaxhist
    for t in range(0, 4):
        for d in range(0, 4):
            for p in range(-3, 1):
                sort(tasks, t, d, p)
                tempmax, tempmaxhist = knapSack(W, N, tasks)
                #if at%10 == 0:
                #    out = ""
                #    for i in range(0, len(tasks)):
                #        out += str(tasks[i].get_task_id()) + " "
                #    print("[", out, "]")
                if tempmax > maximum:
                    maximum = tempmax
                    maximumhistory = tempmaxhist
                at+=1
    print("profit:", str(maximum))
    return maximumhistory


if __name__ == '__main__':
    for inp in os.listdir('inputs/large/'):
        if (inp[-2:] == 'in'):
            print('\n')
            input_path = 'inputs/large/' + inp
            print("Testing " + input_path)
            tasks = read_input_file(input_path)
            actual = solve(tasks)
            print(actual)
            output_path = 'outputs/large/' + inp[:-3] + '.out'
            print("wrote to: " + output_path)
            write_output_file(output_path, actual)
    for inp in os.listdir('inputs/medium/'):
        if (inp[-2:] == 'in'):
            print('\n')
            input_path = 'inputs/medium/' + inp
            print("Testing " + input_path)
            tasks = read_input_file(input_path)
            actual = solve(tasks)
            print(actual)
            output_path = 'outputs/medium/' + inp[:-3] + '.out'
            print("wrote to: " + output_path)
            write_output_file(output_path, actual)
    for inp in os.listdir('inputs/small/'):
        if (inp[-2:] == 'in'):
            print('\n')
            input_path = 'inputs/small/' + inp
            print("Testing " + input_path)
            tasks = read_input_file(input_path)
            actual = solve(tasks)
            print(actual)
            output_path = 'outputs/small/' + inp[:-3] + '.out'
            print("wrote to: " + output_path)
            write_output_file(output_path, actual)
    

# Here's an example of how to run your solver.
# if __name__ == '__main__':
#     for input_path in os.listdir('inputs/'):
#         output_path = 'outputs/' + input_path[:-3] + '.out'
#         tasks = read_input_file(input_path)
#         output = solve(tasks)
#         write_output_file(output_path, output)