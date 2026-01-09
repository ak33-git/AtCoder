N, Q = map(int, input().split())
XY = [map(int, input().split()) for _ in range(Q)]
X, Y = [list(i) for i in zip(*XY)]

list = [0]
for i in range(N):
    list.append(1)
last = 0

for i in range(Q):
    sum = 0
    if last < X[i]:
        for j in range(X[i]-last):
            sum += list[last+1+j]
        last = X[i]
    list[Y[i]] += sum
    print(sum)
