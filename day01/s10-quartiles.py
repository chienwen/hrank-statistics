#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getMedium(arr):
    length = len(arr)
    if length % 2 == 0:
        return (arr[int(length / 2)] + arr[int(length / 2) - 1]) / 2
    else:
        return arr[int(length / 2)]

def quartiles(arr):
    arr.sort()
    length = len(arr)
    halfLen = int(length / 2)
    results = []
    results.append(int(getMedium(arr[0:halfLen])))
    results.append(int(getMedium(arr)))
    results.append(int(getMedium(arr[halfLen + (length % 2):])))
    return results
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

