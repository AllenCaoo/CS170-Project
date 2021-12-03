import os
from parse import read_input_file, write_output_file

def solve(tasks):
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
    
        maximum = -1
        historyMax = 0
        for i in range(0, W):
            if maximum < K[n][i]:
                maximum = K[n][i]
                historyMax = history[n][i]
        return historyMax, maximum
    W = 1440
    N = len(tasks)
    return knapSack(W, N, tasks)


if __name__ == '__main__':
    for inp in os.listdir('samples/'):
        if (inp[-2:] == 'in'):
            input_path = 'samples/' + inp
            # output_path = 'sample_outputs/' + inp[:-3] + '.out'
            tasks = read_input_file(input_path)
            actual = solve(tasks)
            h = bin(actual[0])
            i = len(tasks) - 1
            while i > 0:
                if h[i] == '1':
                    print(len(h) - i)
                i -= 1
            print(str(actual))
            # expected = get_correct(output_path, tasks)
            # print("expected profit:", str(expected))


# Here's an example of how to run your solver.
# if __name__ == '__main__':
#     for input_path in os.listdir('inputs/'):
#         output_path = 'outputs/' + input_path[:-3] + '.out'
#         tasks = read_input_file(input_path)
#         output = solve(tasks)
#         write_output_file(output_path, output)