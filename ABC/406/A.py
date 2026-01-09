A, B, C, D = map(int, input().split(" "))

flag = 0

if A < C:
    flag = 1
if A == C:
    if B < D:
        flag = 1

if flag == 0:
    print("Yes")
else:
    print("No")