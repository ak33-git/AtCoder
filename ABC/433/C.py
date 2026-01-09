S = list(input())
n = []
length = []


prev = -1
count = 0
for i in range(len(S)):
    now = int(S[i])
    if prev != now:
        n.append(prev)
        length.append(count)
        count = 0
    if i == len(S)-1:
        n.append(prev)
        length.append(count+1)
        count = 0
    
    prev = now
    count += 1

#print(n)
#print(length)

ans = 0
for i in range(len(n)-1):
    if n[i]+1 == n[i+1]:
        ans += min(length[i],length[i+1])

print(ans)