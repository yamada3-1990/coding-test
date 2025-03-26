#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    l2r = 0
    r2l = 0
    n = len(arr)

    for i in range(n):
        l2r += arr[i][i]
        r2l += arr[i][n - 1 - i]

    return abs(l2r - r2l)

def diagonalDifference(arr):
    l2r = 0
    r2l = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                l2r += arr[i][j]
    print(l2r)
    
    i = 0
    j = len(arr)-1
    while i < len(arr):
        r2l += arr[i][j]
        i += 1
        j -= 1
    print(r2l)
    
    return abs(l2r - r2l)
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
