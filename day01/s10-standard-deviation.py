#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    average = sum(arr) / len(arr)
    ans = 0
    for n in arr:
        ans += (n - average) ** 2
    print("%.1f" % math.sqrt(ans / len(arr)))
        

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)

