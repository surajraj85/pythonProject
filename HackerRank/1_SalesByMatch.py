#!/bin/python3
# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# socks pair matching
import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    dic={}
    print(set(ar))
    for i in set(ar):
        count = 0
        for j in ar:
            if i==j:
                count = count +1
                dic.update({j: count})

    add = 0
    print(dic)
    for k,l in dic.items():
        if l>1:
            if l%2==1:
                l=(l-1)/2
                add = add+l
            else:
                add = add +l/2
    print(int(add))
    # if add%2==1:
    #     return int((add-1)/2)
    # else:
    #     return int(add/2)


print(sockMerchant(15,[6,5,2,3,5,2,2,1,1, 5, 1, 3, 3, 3, 5]))
# print(sockMerchant(15,[1,1 ,3 ,1 ,2 ,1 ,3 ,3 ,3 ,3]))
