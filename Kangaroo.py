#!/bin/python

import sys

def kangaroo(x1, v1, x2, v2):
    if(x1>x2):
        leading = [x1,v1]
        lagging = [x2,v2]
    else:
        lagging = [x1,v1]
        leading = [x2,v2]
    print str(leading[1]) + " " + str(lagging[1])        
    if(leading[1] >= lagging[1]):
        return "NO"
    while(leading[0] > lagging[0]):
        leading[0] = leading[0] + leading[1]
        lagging[0] = lagging[0] + lagging[1]
        
    
    if(leading[0] == lagging[0]):
        return "YES"
    return "NO"
    
    
        
    

x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
