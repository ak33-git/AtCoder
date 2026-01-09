N = int(input())
A = list(map(int, input().split()))

A = sorted(A)
max = 1

if A[0] == 0 and N == 1:
    max = 0

for i in range(101):
    count = 0
    for j in range(N):
        if i <= A[j]:
            count += 1
    if i <= count:
        max = i

print(max)