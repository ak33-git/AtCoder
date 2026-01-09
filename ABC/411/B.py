N = int(input())
D = list(map(int, input().split()))
D.insert(0,0)
for i in range(N):
    list = []
    sum = 0
    for j in range(i+1, N):
        list.append(D[j] + sum)
        sum += D[j]
    print(*list)