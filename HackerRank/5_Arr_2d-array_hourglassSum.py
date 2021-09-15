#!/bin/python3

#https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    print(arr)
    lst=[]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i<len(arr)-2 and j<len(arr[i])-2:
                print(str(arr[i][j])+" "+str(arr[i][j+1])+" "+str(arr[i][j+2])+"\n"+
                " "+" "+str(arr[i+1][j+1])+" "+" "+"\n"+
                str(arr[i+2][j])+" "+str(arr[i+2][j+1])+" "+str(arr[i+2][j+2]))
                cnt=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
                print(cnt)
                lst.append(cnt)
                print("\n")
    return max(lst)