#!/bin/python

import sys

s = []
for s_i in xrange(3):
    s_temp = map(int,raw_input().strip().split(' '))
    s.append(s_temp)
    
ms1  = [[4,9,2],[3,5,7],[8,1,6]]
ms2 = [[8,1,6],[3,5,7],[4,9,2]]
ms3 = [[6,1,8],[7,5,3],[2,9,4]]
ms4  = [[2,9,4],[7,5,3],[6,1,8]]
ms5  = [[8,3,4],[1,5,9],[6,7,2]]
ms6  = [[4,3,8],[9,5,1],[2,7,6]]
ms7  = [[6,7,2],[1,5,9],[8,3,4]]
ms8  = [[2,7,6],[9,5,1],[4,3,8]]
cost = 0
msa = [ms1,ms2,ms3,ms4,ms5,ms6,ms7,ms8]
costmin = 0
for x in range(8):
    ms = msa[x]
    cost = 0
    for i in range(3):
     for j in range(3):
         cost = cost + abs(ms[i][j] - s[i][j])
    if(x == 0):
        costmin = cost
    if cost < costmin:
        costmin = cost
    
print costmin

#  Print the minimum cost of converting 's' into a magic square
