N, Q = map(int, input().split())
X = list(map(int, input().split()))

box = [0] * N
ball_box = []

for i in range(Q):
    if X[i] > 0:
        box[X[i]-1] += 1
        ball_box.append(X[i])
    if X[i] == 0:
        min = Q
        index = N
        for j in range(N):
            if box[j] < min:
                min = box[j]
                index = j
        box[index] += 1
        ball_box.append(index+1)

print(*ball_box)