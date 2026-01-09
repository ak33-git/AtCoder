N, K = map(int, input().split())
S = list(input())

dic = {}

for i in range(N-K+1):
    text = ""
    for j in range(K):
        text += S[i+j]
    if text in dic:
        dic[text] += 1
    else:
        dic[text] = 1

max = 0
for s in dic:
    if dic[s] > max:
        max = dic[s]


ans = []
for s in dic:
    if dic[s] == max:
        ans.append(s)
ans = sorted(ans)

print(max)
print(*ans)