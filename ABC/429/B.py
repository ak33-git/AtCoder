N, M = map(int,input().split())
A = list(map(int,input().split()))

flag = False
for i in range(N):
    count = 0
    for j in range(N):
        if i != j:
            count += A[j]
    if count == M:
        flag = True

if flag:
    print("Yes")
else:
    print("No")