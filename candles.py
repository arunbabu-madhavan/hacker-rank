import sys

def birthdayCakeCandles(n, ar):
    maxh = 0
    res = 1
    for i in range(0,n):
        if(ar[i] > maxh):
            maxh = ar[i]
            res = 1
        else:
            if(ar[i] == maxh):
                res = res + 1
    return res
        
n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
