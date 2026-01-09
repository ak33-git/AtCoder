N = int(input())
T = list(input())
A = list(input())
flag = False
for i in range(N):
    if T[i] == A[i] and T[i] == "o":
        flag = True

if flag == True:
    print("Yes")
else:
    print("No")