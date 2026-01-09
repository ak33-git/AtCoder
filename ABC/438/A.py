D, F = map(int, input().split())
ans = F
while ans <= D:
    ans += 7
ans -= D
print(ans)