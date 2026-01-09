import itertools

X = int(input())
N = l = [int(x) for x in list(str(X))]

a = list(itertools.permutations(N))
ans = []
for i in range(len(a)):
    app = 0
    for j in range(len(a[i])-1,-1,-1):
        app += (a[i][j]) * (10**(j))
    ans.append(app)

an = 0
ans = sorted(ans)
for i in ans:
    if i >= 10**(len(N)-1):
        an = i
        break

print(an)

