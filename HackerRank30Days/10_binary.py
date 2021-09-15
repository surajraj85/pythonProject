from collections import Counter
binary = "{0:b}".format(6)
# binary = "{0:b}".format(439)
# print(binary)
z = ""
# print(binary)
from itertools import groupby
res = [{_:len(list(j))} for _, j in groupby(binary)]
z=[]
for i in res:
    re3 = [val for key, val in i.items() if "1" in key]
    # print(re3)
    z.append(re3)

print(' '.join([str(elem) for elem in max(z)]))
# for i in range(len(binary)-1):
#     # print(binary[i])
#     # if i < len(binary) - 1:
#     if binary[i] == binary[i + 1]:
#         print(i)
#         z = z + binary[i]
#     else:
#         z = "1"
# print("\n")
# print(len(z + "1"))
print(bin(439))
n=439
numbers = str(bin(n)[2:]).split('0')
numbers = str("{0:b}".format(439)).split('0')
print(numbers)
lenghts = [len(num) for num in numbers]
print(max(lenghts))