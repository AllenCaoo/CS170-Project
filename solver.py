import math
import sys
import os
from parse import read_input_file, write_output_file

def solve(tasks):
    def knapSack(W, n, tasks):
        K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    
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
                    K[i][w] = max(do, dont)
                else:
                    K[i][w] = K[i-1][w]
    
        maximum = -1
        for i in range(0, W):
            maximum = max(maximum, K[n][i])
        return maximum
    W = 1440
    N = len(tasks)
    return knapSack(W, N, tasks)


if __name__ == '__main__':
    for inp in os.listdir('samples/'):
        if (inp[-2:] == 'in'):
            input_path = 'samples/' + inp
            output_path = 'sample_outputs/' + inp[:-3] + '.out'
            tasks = read_input_file(input_path)
            output = solve(tasks)
            print("profit: " + str(output))


# Here's an example of how to run your solver.
# if __name__ == '__main__':
#     for input_path in os.listdir('inputs/'):
#         output_path = 'outputs/' + input_path[:-3] + '.out'
#         tasks = read_input_file(input_path)
#         output = solve(tasks)
#         write_output_file(output_path, output)