N = int(input())
S = input()
flag = False
if len(S) >= 3:
    if S[N-3] == "t" and S[N-2] == "e" and S[N-1] == "a":
        flag = True
if flag:
    print("Yes")
else:
    print("No") 