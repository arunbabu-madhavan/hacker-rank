def solve(n,s,d,m):
    result = 0
    tempsum = 0
    for i in range(0,n):
        tempSum = sum(s[i:i+m])
        if tempSum == d :
            result += 1
    return result

n = int(raw_input().strip())
s = map(int,raw_input().strip().split(' '))
d,m = map(int,raw_input().strip().split(' '))
result = solve(n,s,d,m)
print result
