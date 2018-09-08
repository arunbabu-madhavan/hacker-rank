N,D = [int(x) for x in raw_input().split()]
#rotations
r = D % N
a = []
b = []
a = map(int,raw_input().split())
a = a[:N]
b = a[r:]
b.extend(a[:r])
for x in b[:]:
    print x,
