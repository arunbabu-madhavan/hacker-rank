import sys

A = map(long,raw_input().strip().split(' '))
sum = 0
min = A[0]
max = A[0]
for i in range(0,len(A)):
    sum = sum + A[i]
    min = A[i] if A[i] < min else min
    max = A[i] if A[i] > max else max

print str(sum-max) + " " +str(sum-min)
