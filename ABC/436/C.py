N, M = map(int, input().split())
RC = [map(int, input().split()) for _ in range(M)]
R, C = [list(i) for i in zip(*RC)]

count = 0
s = set()
for i in range(M):
    flag = True
    if (R[i], C[i]) in s:
        flag = False
    if (R[i]+1, C[i]) in s:
        flag = False
    if (R[i], C[i]+1) in s:
        flag = False
    if (R[i]+1, C[i]+1) in s:
        flag = False
    
    if flag:
        count += 1
        s.add((R[i], C[i]))
        s.add((R[i]+1, C[i]))
        s.add((R[i], C[i]+1))
        s.add((R[i]+1, C[i]+1))

print(count)