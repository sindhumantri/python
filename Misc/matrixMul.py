"""input = 
1
 1 1 1
 1 1 1
 1 1 1
 1 1 1
 1 1 1
 1 1 1"""

import sys

num_tests = int(sys.stdin.readline())

for i in range(num_tests):
    matrixA = []
    matrixB = []
    for i in range(3):
        rows = sys.stdin.readline().split()
        row_list = [int(i) for i in rows]
        matrixA.append(row_list)
    for i in range(3):
        rows = sys.stdin.readline().split()
        row_list = [int(i) for i in rows]
        matrixB.append(row_list)
    matrixMul = [[0 for row in range(len(matrixA))] for col in range(len(matrixB[0]))]
    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixB)):
                matrixMul[i][j] += matrixA[i][k] * matrixB[k][j]
    print (matrixMul)
    

"""output = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]""" 
