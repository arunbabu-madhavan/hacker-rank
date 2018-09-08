N,M = [long(x) for x in raw_input().split()]
A = [0]*N
maxValue = None
while M > 0:
    M = M-1
    maxValue = 0
    a,b,k = [long(x) for x in raw_input().split()]
    A[a-1] = A[a-1] + k
    if(b<N):
        A[b] = A[b] - k
for i in range(0,N):
    tempsum = A[i] + tempsum
    if(maxValue == None or tempsum > maxValue):
        maxValue = tempsum
print maxValue
