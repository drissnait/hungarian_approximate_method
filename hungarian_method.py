import time
start_time = time.time()
import numpy as np

cost = np.array([[9,5,4,3,8], [3,7,9,5,10], [8,4,6,10,3], [8,5,4,5,34], [2,8,2,5,7]])
#cost= np.array([[9,5,4,2], [5,7,9,5], [2,6,5,10], [8,5,4,5]])
from scipy.optimize import linear_sum_assignment
row_ind, col_ind = linear_sum_assignment(cost)
col_ind
dir([1, 0, 2])
for i in range (0,len(cost)):
    print(cost[row_ind, col_ind][i])

print("Solution : " + str(cost[row_ind, col_ind].sum()))
print("---Temps d'execution : %s seconds ---" % (time.time() - start_time))
