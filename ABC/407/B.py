X, Y = map(int, input().split(" "))
list = []
for i in range(6):
    for j in range(6):
        list.append([i+1, j+1])

count = 0
for i in range(len(list)):
    if sum(list[i]) >= X or abs(list[i][0]-list[i][1]) >= Y:
        count += 1

print(count/36)