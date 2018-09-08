def getRecord(s):
    minRec = 0
    maxRec = 0
    currentMin = s[0]
    currentMax = s[0]
    for i in range(len(s)):
        if(s[i] > currentMax):
            maxRec = maxRec +1
            currentMax = s[i]
        if(s[i] < currentMin):
            minRec = minRec + 1
            currentMin = s[i]
    return maxRec,minRec

n = int(raw_input().strip())
s = map(int,raw_input().strip().split(' '))
result = getRecord(s)
print " ".join(map(str, result))
