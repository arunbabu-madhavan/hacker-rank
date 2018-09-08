import sys

N = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))
p = 0.0
z = 0.0
n = 0.0
for i in range(0,N):
    if(A[i] > 0):
        p = p+1
    if(A[i] < 0):
        n = n +1
    if(A[i] == 0):
        z = z +1
print (float(p/N),float(n/N),float(z/N))
    
