N = int(input())
S = list(input())

while len(S) < N:
    S.insert(0, "o")

ans = ""
for i in S:
    ans += i

print(ans)