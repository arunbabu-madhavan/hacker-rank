def getInput(numberOfinputs):
    i = 0
    result = []
    while i < numberOfinputs:
        result.append(raw_input())
        i = i + 1
    return result

N = int(raw_input())
S = getInput(N)
Q = int(raw_input())
q = getInput(Q)

for x in q[:]:
    counter = 0 
    for y in S[:]:
        if (x == y):
            counter = counter + 1
    print counter

            
    
