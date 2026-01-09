S = list(input())
if int(S[2]) == 8:
    S[0] = int(S[0]) + 1
    S[2] = 1
else:
    S[2] = int(S[2]) + 1

ans = ""
for i in S:
    ans += str(i)

print(ans)