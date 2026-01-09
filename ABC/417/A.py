N, A, B = map(int, input().split())
S = list(input())
ans = ""
for i in range(A, N-B, 1):
    ans += S[i]
 
print(ans)