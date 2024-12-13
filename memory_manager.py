def firstFit(blockSize, m, processSize, n):

 #n = number of processes
 #m = number of blocks

    allocation = [-1] * n


    for i in range(n):
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                allocation[i] = j
                blockSize[j] = blockSize[j] - processSize[i]
                break

    return allocation



