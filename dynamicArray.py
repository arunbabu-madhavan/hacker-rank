N,Q = [int(j)  for j in raw_input().split()]
lastAnswer = 0;
seqList =[]
inputList = []
i=0
while (i < N):
    seqList.append([])
    i = i +1
i=0

while (i < Q):
    qType,X,Y =[int(j)  for j in  raw_input().split()]
    inputList.append([])
    inputList[i].append((qType))
    inputList[i].append((X))
    inputList[i].append((Y))
    i = i +1
i=0

while (i < Q):
    q = inputList[i][0]
    x = inputList[i][1]
    y = inputList[i][2]
    index = ((x) ^ (lastAnswer))% N
    if(q == 1):
        seqList[index].append(y)
    else:
        subIndex = y % len(seqList[index])
        lastAnswer = seqList[index][subIndex]     
        print lastAnswer
    i = i+1

