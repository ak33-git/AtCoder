A, B, C = map(int, input().split())
ans = []
ans.append(A*100+B*10+C)
ans.append(A*100+C*10+B)
ans.append(B*100+A*10+C)
ans.append(B*100+C*10+A)
ans.append(C*100+A*10+B)
ans.append(C*100+B*10+A)

print(max(ans))

