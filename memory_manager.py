# memory_manager.py

def firstFit(blockSize, m, processSize, n):

 #n = number of processes
 #m = number of blocks

    allocation = [-1] * n
    #allocation = [-1, -1, -1, -1]

    for i in range(n):
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                allocation[i] = j
                blockSize[j] = blockSize[j] - processSize[i]
                break

    return allocation



def print_allocation(allocation, processSize):

    print("Process No. Process Size  Block no.")

    for i in range(len(processSize)):
        print(f" {i + 1}             {processSize[i]}        ", end="")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

