N, X, Y = map(int, input().split())
A = list(map(int,input().split()))

flag = True
min_range = []
max_range = []
for i in range(N):
    min_range.append(A[i]*X)
    max_range.append(A[i]*Y)

ran = []
ran.append(max(min_range))
ran.append(min(max_range))

if ran[0] > ran[1]:
    flag = False

dif = Y - X
mod = (A[0]*X) % dif
for i in range(N):
    if (A[i]*X) % dif != mod:
        flag = False

W = max(ran)
k = (W - mod) // dif
W = mod + k*dif
if W < min(ran):
    flag = False

ans = 0
for i in range(N):
    ans += (X*A[i]-W) // (X-Y)

if flag:
    print(ans)
else:
    print(-1)