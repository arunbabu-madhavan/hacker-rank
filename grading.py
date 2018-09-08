import sys

def solve(grades):
    # Complete this function
    for i in range(0,len(grades)):
        nextmulitple = ((grades[i]/5)+1) * 5
        grades[i] =  nextmulitple if (nextmulitple - grades[i]) < 3 and grades[i] > 35 else grades[i]

    return grades;

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))
