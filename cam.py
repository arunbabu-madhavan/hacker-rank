#!/bin/python

import sys

result = []

q = int(raw_input().strip())
for a0 in xrange(q):
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    if(abs(x-z) > abs(y-z)):
        result.append('Cat B')
    elif (abs(x-z) < abs(y-z)):
        result.append('Cat A')
    else:
        result.append('Mouse C')

for i in range(len(result)):
    print result[i]
