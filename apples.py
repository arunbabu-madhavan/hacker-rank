#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))
count = 0

for i in range(0,len(apple)):
    count = count + 1 if (apple[i] + a) >= s and (apple[i] + a) <=t else count
print count
count = 0
for i in range(0,len(orange)):
    count = count + 1 if (orange[i] + b) >= s and (orange[i] + b) <=t else count
print count
