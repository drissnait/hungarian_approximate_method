import time
start_time = time.time()
import numpy as np

cost = np.array([[2,1,5,4,3], [8,7,6,5,2], [11,12,20,28,30], [99,8,5,10,70], [88,77,6,50,30]])
from scipy.optimize import linear_sum_assignment
row_ind, col_ind = linear_sum_assignment(cost)
col_ind
dir([1, 0, 2])
print(cost[row_ind, col_ind].sum())
print("--- %s seconds ---" % (time.time() - start_time))
