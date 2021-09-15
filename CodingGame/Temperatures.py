import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse

lst1 = []
lst2 = []
if n == 0:
    print(0)
else:
    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)
        lst1.append(abs(t))
        lst2.append(t)
    min_lst1_ix = lst1.index(min(lst1))
    if abs(lst2[min_lst1_ix]) == min(lst1):
        if min(lst1) >0 and lst2[min_lst1_ix]<0 and len(set(lst1)) == len(set(lst2)):
            print(-1*min(lst1))
        else:
            print(min(lst1))