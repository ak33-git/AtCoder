N, M = map(int, input().split())
AB = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*AB)]

k = [0] * M
k_count = [0] * M
for i in range(N):
    k[A[i]-1] += B[i]
    k_count[A[i]-1] += 1

for i in range(M):
    print(k[i]/k_count[i])