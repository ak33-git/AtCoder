N = int(input())
A = list(map(int, input().split()))

check = []
for i in range(N):
    check.append(0)
    check[i] = i+1

flag = True
count = 0
for i in A:
    if i == -1:
        count += 1
    else:
        try:
            check.remove(i)
        except:
            flag = False
            break

if len(check) != count:
    flag = False

if flag:
    for i in range(N):
        if A[i] == -1:
            A[i] = check.pop()
    print("Yes")
    print(*A)
else:
    print("No")
