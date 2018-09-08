#!/bin/python

import sys

def divisibleSumPairs(n, k, ar):
    num = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if ((ar[i]+ar[j])%k == 0):
                num+=1
    return num

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
result = divisibleSumPairs(n, k, ar)
print(result)
