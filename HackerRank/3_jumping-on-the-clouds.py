#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

"""
0 0 1 0 0 1 0
0 0 0 1 0 0
"""

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#
def safe_list_get(l, idx, default):
    try:
        return l[idx]
    except IndexError:
        return default


def jumpingOnClouds(c):
    # Write your code here
    print(c)
    # for i in range(len(c)-1):
    i = 0
    print(len(c))
    cnt = 0
    while (i < len(c) - 1):
        print("loop---" + str(i))
        if c[i] == 0 and safe_list_get(c, i + 2, None) == 0:
            i = i + 2
            print("when 0 and 0 , i= " + str(i))
            cnt = cnt + 1
        else:
            if c[i] == 0 and c[i + 1] == 1:
                i = i + 2
                print("when 0 and 1 , i= " + str(i))
                cnt = cnt + 1
            else:
                i = i + 1
                print("else , i= " + str(i))
                cnt = cnt + 1
    return cnt

