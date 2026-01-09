H, W = map(int, input().split())
S = []
for i in range(H):
    S.append(input())
    S[i] = list(S[i])

flag = True

for i in range(H):
    for j in range(W):
        count = 0
        if S[i][j] == '#':
            if i > 0:
                if S[i-1][j] == '#':
                    count += 1
            if i < H-1:
                if S[i+1][j] == '#':
                    count += 1
            if j > 0:
                if S[i][j-1] == '#':
                    count += 1
            if j < W-1:
                if S[i][j+1] == '#':
                    count += 1

            if count != 2 and count != 4:
                flag = False

if flag:
    print("Yes")
else:
    print("No")