N, Q = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A)

A_sum = [0]
count = 0
for i in range(1,A[N-1]+1):
    A_sum.append(A_sum[i-1] + len(A)-count)
    for j in range(count,N):
        if A[count] <= i:
            count += 1
        else:
            break

for i in range(Q):
    B = int(input())
    if B > A[N-1]:
        print(-1)
    else:
        print(A_sum[B-1] + 1)
        