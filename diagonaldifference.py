import sys

n = int(raw_input().strip())
a = []

for i in xrange(n):
    tempList = map(int,raw_input().strip().split(' '))
    a.append(tempList)

def getDDifference(array):
    pd = 0
    sd = 0
    for i in xrange(len(array)):
        pd = pd + array[i][i]
        sd = sd + array[i][len(array) - 1 -i]
    return abs(pd-sd)

print getDDifference(a)
