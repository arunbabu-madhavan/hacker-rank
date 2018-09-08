import sys

def migratoryBirds(n, ar):
    count =[0,0,0,0,0]
    for i in range(0,len(ar)):
        count[ar[i] - 1] = count[ar[i] - 1] + 1
    common = 0;
    
    for i in range(0,len(count)):
        if(count[i] > count[common]):
            common = i
            
    return common + 1
n = int(raw_input().strip())
ar = list(map(int, raw_input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
