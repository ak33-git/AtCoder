X, Y, Z = map(int, input().split())

flag = False
while Y * Z <= X:
    if X % Y == 0 and X // Y == Z:
        flag = True
        break
    X += 1
    Y += 1

if flag:
    print("Yes")
else:
    print("No")