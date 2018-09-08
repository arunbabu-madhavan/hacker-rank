#!/bin/python

import sys

def sockMerchant(n, ar):
    # Complete this function
    sockDrawer = [0] * 101
    noofPairs = 0
    for i in range(0,n):
        sockDrawer[ar[i]] +=1
    for i in range(1,101):
        noofPairs += sockDrawer[i]/2
    return noOfPairs

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = sockMerchant(n, ar)
print(result)
