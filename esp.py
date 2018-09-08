
import sys

def getMoneySpent(keyboards, drives, s):
    # Complete this function
    maxMoney = -1
    tempsum =0
    for i in range(0,len(keyboards)):
        for j in range(0,len(drives)):
            tempsum = keyboards[i] + drives[j]
            if tempsum == s:
                return tempsum
            if tempsum < s and maxMoney < tempsum:
                maxMoney = tempsum
    return maxMoney

s,n,m = raw_input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = map(int, raw_input().strip().split(' '))
drives = map(int, raw_input().strip().split(' '))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
