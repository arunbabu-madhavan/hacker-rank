n = int(raw_input().strip())
a =[]
s = raw_input().strip()
a = list(s)
level = 0
v = 0
im = 0
for i in range(0,n):
   
  
    if(level > 0):
        im = 0
    else:
        im = 1
    if(a[i] == 'D'):
        level-=1
    if(a[i] =='U'):
        level+=1
    
    if(level == 0):
        v = v + (1 * im)
print v
