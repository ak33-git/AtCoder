N = int(input())
A = list(map(int,input().split()))

dic = {}
for i in range(N):
    if A[i] in dic:
        dic[A[i]] += 1
    else:
        dic[A[i]] = 1

com = {}
for i in dic:
    if dic[i] >= 2:
        com[i] = (dic[i] * (dic[i]-1)) // 2
    else:
        com[i] = 0

ans = 0

for i in com:
    ans += com[i] * (N - dic[i])

print(ans)