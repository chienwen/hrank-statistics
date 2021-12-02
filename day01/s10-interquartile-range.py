#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def getMedium(arr):
    length = len(arr)
    if length % 2 == 0:
        return (arr[int(length / 2)] + arr[int(length / 2) - 1]) / 2
    else:
        return arr[int(length / 2)]

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    flattenArr = []
    for i in range(len(values)):
        flattenArr += [values[i]] * freqs[i]
    flattenArr.sort()
    length = len(flattenArr)
    halfLen = int(length / 2)
    left = getMedium(flattenArr[0:halfLen])
    right = getMedium(flattenArr[halfLen + (length % 2):])
    print("%.1f" % (right - left))
    
if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)

