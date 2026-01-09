N, L, R = map(int, input().split())
XY = [list(map(int, input().split())) for xy in range(N)]

count = 0
for i in range(N):
    if XY[i][0] <= L and R <= XY[i][1]:
        count += 1

print(count)