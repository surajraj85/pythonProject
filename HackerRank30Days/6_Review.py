# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input().strip())
# print(n)
for i in range(0,n):
    s=input()
    # print(s)
    print(s[::2]+" "+s[1::2])
