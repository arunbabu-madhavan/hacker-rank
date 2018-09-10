#!/bin/python

import sys

def climbingLeaderboardWithAlltogether(scores,alice):
    rank = 1
    result = []
    i = 0
    shiftrank = 0
    j = len(scores) - 1
    while(j >=0 and i <len(scores)):
        while( i + 1 < len(scores) and scores[i] == scores[i+1]):
               i = i + 1

        if(alice[j] > scores[i]):
            result.append(rank + shiftrank)
            shiftrank = shiftrank + 1
            #print str(alice[j]) + " " + str(scores[i])
        elif(alice[j] == scores[i]):
            #print str(alice[j]) + " " + str(scores[i]) + "less"
            result.append(rank + shiftrank)
        else:
            #print str(alice[j]) + " " + str(scores[i]) + "else"
            rank = rank + 1
            i = i + 1
            j = j + 1
        j = j - 1
    while(j >= 0):
        result.append(rank + shiftrank)
        rank = rank + 1
        j = j - 1
    result.reverse()
    return result


        
def climbingLeaderboard(scores,alice):
    i = 0
    j = 0
    rank = 1
    j = len(alice) - 1
    result = []
    shiftrank = 0
    while(j >=0 and i <len(scores)):
        while( i + 1 < len(scores) and scores[i] == scores[i+1]):
               i = i + 1

        if(alice[j] > scores[i]):
            result.append(rank)
        elif(alice[j] == scores[i]):
            result.append(rank)
        else:
            rank = rank + 1
            i = i + 1
            j = j + 1
        j = j - 1
    while(j >= 0):
        result.append(rank)
        j = j - 1
    result.reverse()
    return result
        

scores_count = int(raw_input())
scores = map(int, raw_input().rstrip().split())
alice_count = int(raw_input())
alice = map(int, raw_input().rstrip().split())
print '\n'
result = climbingLeaderboard(scores,alice)
print '\n'
print '\n'.join(map(str,result))
print '\n'

