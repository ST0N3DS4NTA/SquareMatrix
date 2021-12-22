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
    primarySum = 0
    secondarySum = 0
    z = 0
    j = len(arr)
    for i in range(len(arr)):
        primarySum += arr[i][i]
    for j in range(len(arr) - 1, -1, -1):
        secondarySum += arr[j][z]
        z += 1
    return abs(primarySum - secondarySum)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
