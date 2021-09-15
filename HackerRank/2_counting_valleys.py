#https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

"""
UDDDUDUU
_/\
   \     /
    \/\/


DDUUDDUDUUUD


_          /\_
 \  /\    /
  \/  \/\/
[6,-6]
some issue coming in below test case
UDUUUDUDDD

     /\/\
    /    \
_/\/      \
[1 -1 1 1 1 -1 1 -1 -1-1]
5,-5
"""


def countingValleys(steps, path):
    # Write your code here
    pth = 0
    fnl = 0
    vl = 0
    cnt = 0
    for i in path:
        # maine ese uper es lea rakha hai because main 'D' ki value check kr rha hu
        # D nahi aega to ye problem fail ho jaegi
        # hume tabhi vl ki value increase krni hai jab i="D" hume mile and U and D ka sum 0(fnl) ho
        if fnl == 0 and i == 'D':
            print(i)
            vl = vl + 1
        if i == 'U':
            pth = 1
        if i == 'D':
            pth = -1
        fnl = fnl + pth
        # print(str(i)+' and fnl= '+str(fnl))

    # print(vl-1)
    return (vl)

