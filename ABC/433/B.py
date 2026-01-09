N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    p = -1
    for j in range(i):
        if A[i] < A[j]:
            p = j+1
    print(p)