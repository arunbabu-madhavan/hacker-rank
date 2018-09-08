N = int(raw_input())
s = {}
while N != 0:
    N = N - 1
    t = raw_input()
    if(t in s):
        s[t] = s[t] + 1
    else:
        s[t] = 1
Q = int(raw_input())
while Q != 0:
    Q = Q - 1
    t = raw_input()
    if(t in s):
        print s[t]
    else:
        print 0
        
