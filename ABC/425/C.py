N, Q = map(int, input().split())
A = list(map(int, input().split()))
query = []
for i in range(Q):
    query.append(list(map(int,input().split())))

sum = []
s = 0
for i in range(N):
    s += A[i]
    sum.append(s)
for i in range(N):
    s += A[i]
    sum.append(s)

head = 0

for i in range(Q):
    if query[i][0] == 1:
        head += query[i][1]
        head %= N
    if query[i][0] == 2:
        query[i][1] -= 1
        query[i][2] -= 1
        start = head + query[i][1]
        start %= N
        end = start + (query[i][2] - query[i][1])
        print(sum[end] - sum[start] + A[start])
