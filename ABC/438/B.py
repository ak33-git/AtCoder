N, M = map(int, input().split())
S = list(input())
T = list(input())
for i in range(N):
    S[i] = int(S[i])
for i in range(M):
    T[i] = int(T[i])

def comp(s, t):
    ret = s - t
    if ret < 0:
        ret = 10 - t + s
    return ret

min = 100000
for i in range(N-M+1):
    temp = 0
    for j in range(M):
        temp += comp(S[i+j], T[j])
    if temp < min:
        min = temp

print(min)