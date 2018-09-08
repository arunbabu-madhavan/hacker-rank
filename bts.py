import sys
def getMax(a):
    max = a[0]
    for i in range(len(a)):
        if(a[i] > max):
            max = a[i]
    return max
def getMin(a):
    min = a[0]
    for i in range(len(a)):
        if(a[i] < min):
            min = a[i]
    return min

def getTotalX(a,b):
    minX = getMax(a)
    maxX = getMin(b)
    result = 0
    
    for i in range(minX,maxX +1):
        breakloop = False
        for counter in range(len(a)):
            if(i % a[counter] != 0):
                breakloop = True
                break
        if(breakloop):
            continue
        for counter in range(len(b)):
            if(b[counter] % i != 0):
                breakloop = True
                break
        if(breakloop):
            continue
        result = result + 1
    return result
        

n,m = map(int,raw_input().strip().split(' '))
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))
total = getTotalX(a, b)
print total
