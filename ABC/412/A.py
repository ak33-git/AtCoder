N = int(input())
AB = [list(map(int, input().split())) for l in range(N)]

ans = 0
for i in range(N):
    if AB[i][0] < AB[i][1]:
        ans += 1

print(ans)