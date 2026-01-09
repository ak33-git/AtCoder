from collections import deque
S = list(input())
q = deque()
for i in range(len(S)):
    S[i] = int(S[i])
    q.append(S[len(S)-1-i])

count = 0
re = 0
while q:
    x = int(q.popleft()) - count
    if x < 0:
        x = 10 - int(str(x)[-1])
    count += x
    re += 1

print(count)