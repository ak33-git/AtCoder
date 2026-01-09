N, S = map(int, input().split())
T = list(map(int, input().split()))
T.insert(0,0)
list = []
flag = True

for i in range(N):
    list.append(T[i+1]-T[i])

for i in range(len(list)):
    if list[i] > S + 0.5:
        flag = False

if flag == True:
    print("Yes")
else:
    print("No")