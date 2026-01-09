S = list(input())

n = S.count(S[0])

if n == 1:
    print(S[0])
else:
    for i in range(len(S)):
        if S[i] != S[0]:
            print(S[i])