#!/bin/python

import sys


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

result = 0
b = set()
for j in a:
    b.add(j)
print b
for i in range(0,len(b)):
    tempcount = 0
    uv = a[i]
    maxListCount = 0
    minListCount = 0
    for j in range(0,n):
        if(uv == a[j]):
            maxListCount +=1
            minListCount +=1
        if(uv + 1 == a[j]):
            maxListCount +=1
        if(uv - 1 == a[j]):
            minListCount +=1
    if(maxListCount >= minListCount) and maxListCount > result:
        result = maxListCount
    if(minListCount >= maxListCount) and minListCount > result:
        result = minListCount
print result
