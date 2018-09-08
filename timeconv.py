#!/bin/python

import sys

def timeConversion(s):
    milTime = ''
    meridian = s[-2:]
    hour = int(s[:2])
    milhour = (hour + 12) if (meridian == 'PM' and hour < 12) else (hour%12) if meridian =='AM' else hour
    strmilhour = '0'+ str(milhour)  if((milhour) <10) else str(milhour)
    milTime = strmilhour + s[2:-2] 
    return milTime
    

s = raw_input().strip()
result = timeConversion(s)
print(result)
