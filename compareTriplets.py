#!/bin/python

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    r = 0
    r = r + 10 if  a0 > b0 else r + 1 if a0 < b0 else r
    r = r + 10 if  a1 > b1 else r + 1 if a1 < b1 else r
    r = r + 10 if  a2 > b2 else r + 1 if a2 < b2 else r
    
    return  "00" if r  == 0 else "0" + str(r) + if r / 10 == 0 else r

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))



