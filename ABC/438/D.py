N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

DP = []
for i in range(3):
    DP.append([])
    for j in range(N):
        DP[i].append(0)

DP[0][0] = A[0]
DP[1][1] = DP[0][0] + B[1]
DP[2][2] = DP[1][1] + C[2]
#print(DP)
for i in range(1, N-2):
    DP[0][i] = DP[0][i-1] + A[i]
    max_B = DP[1][i] + B[i+1]
    if max_B < DP[0][i] + B[i+1]:
        max_B = DP[0][i] + B[i+1]
    DP[1][i+1] = max_B
    max_C = DP[2][i+1] + C[i+2]
    if max_C < DP[1][i+1] + C[i+2]:
        max_C = DP[1][i+1] + C[i+2]
    DP[2][i+2] = max_C
#print(DP)

print(DP[2][N-1])
    