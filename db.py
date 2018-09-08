#!/bin/python

import sys

def solveG(n, p):
    return min(n/2, (n - p)/2)

def solve(n, p):
    finalLeft = n
    finalRight = 0
    if n%2 != 0:
        finalLeft = n - 1
        finalRight = n
    if(p == finalLeft or p == finalRight):
        return 0
    if p%2 == 0:
        destLeft = p
        destRight = p + 1
    else:
        destRight = p
        destLeft = p - 1
        
    startCount = (destRight - 1) / 2
    endCount = (finalLeft - destLeft)/2

    if(startCount < endCount):
        return startCount
    else:
        return endCount

n = int(raw_input().strip())
p = int(raw_input().strip())
result = solveG(n, p)
print(result)
