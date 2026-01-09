S = list(input())
T = set(input())

flag = True

for i in range(1,len(S)):
    if S[i].isupper():
        if not S[i-1] in T:
            flag = False

if flag:
    print("Yes")
else:
    print("No")
