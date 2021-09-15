#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    print(s)
    print(n)
    print(len(s))
    l = n // len(s)  # we can do math.floor also
    print(l)
    remain = n % len(s)  # we can do n-l
    cnt = 0
    print(remain)
    if len(s) > 1:
        cnt = s.count('a') * l + s[:remain].count('a')
        # for i in s_new:
        #     if i=='a':
        #         cnt=cnt+1
    else:
        if s == 'a':
            cnt = n
    return cnt

print(repeatedString("kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm",736778906400))



# took help from below
# s="kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm"
# n=736778906400
# print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))