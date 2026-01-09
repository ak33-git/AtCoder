N = int(input())
A = list(map(int, input().split()))

f = [False] * N
f[0] = True
hop = A[0]


for i in range(1, N):
    hop -= 1
    if hop > 0:
        f[i] = True
    if A[i] > hop and f[i]:
        hop =  A[i]
    
    #print(f)

count = 0
for i in f:
    if i:
        count += 1

print(count)