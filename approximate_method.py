import time
start_time = time.time()
import numpy as np

affected=[]
#cost= [[9,5,4,3,8], [5,7,9,5,10], [8,4,6,10,3], [8,5,4,5,34], [2,8,2,5,7]]
cost= [[9,5,4,3,8], [3,7,9,5,10], [8,4,6,10,3], [8,5,4,5,34], [2,8,2,5,7]]

for i in range (0, len(cost)):

    liste=cost[i]
    j=0
    check=0
    liste2=[]
    for l in range(0,len(liste)):
        if l not in affected:
            liste2.append(liste[l])
    minimum=min(liste2)
    while j < len(liste):
        if(liste[j]==minimum):
            affected.append(j)
            j=len(liste)
        j+=1

res=0
for i in range (0, len(affected)):
    aj=affected[i]
    res+=cost[i][aj]
    print(cost[i][aj])

print("Solution = " + str(res))
print("---Temps d'execution : %s seconds ---" % (time.time() - start_time))
