N, M = map(int, input().split(" "))
A = input().split(" ")
for i in range(len(A)):
    A[i] = int(A[i])

n = []
for i in range(M):
    n.append(i+1)

x = 0
while True:
    if set(A) == set(n):
        del A[len(A)-1]
        x += 1
    else:
        break
print(x)