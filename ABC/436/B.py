N = int(input())

ans = []
for i in range(N):
    ans.append([0]*N)

ans[0][(N-1)//2] = 1

r = 0
c = (N-1)//2
k = 1

for i in range(N**2-1): 
    """print((r-1)%N)
    print((c+1)%N)
    print("---")"""
    if ans[(r-1)%N][(c+1)%N] == 0:
        ans[(r-1)%N][(c+1)%N] = k+1
        r = (r-1)%N
        c = (c+1)%N
        #print("b")
    else:
        ans[(r+1)%N][c] = k+1
        r = (r+1)%N
        #print("a")
    k += 1

for i in range(N):
    print(*ans[i])