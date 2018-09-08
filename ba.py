#!/bin/python

import sys

def bonAppetit(n, k, b, ar):
    actual = 0
    for i in range(0,n):
        if(i != k):
            actual += ar[i]/2
    if(actual == b):
        return "Bon Appetit"
    else:
        return str(b - actual)

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
b = int(raw_input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
