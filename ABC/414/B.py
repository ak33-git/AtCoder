N = int(input())
cl = [list(map(str, input().split())) for xy in range(N)]

max = 0
c = ""

for i in range(N):
    max += int(cl[i][1])
    if max > 100:
        print("Too Long")
        break
    c += cl[i][0] * int(cl[i][1])

if max <= 100:
    print(c)