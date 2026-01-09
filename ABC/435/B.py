import math

N = int(input())
A = list(map(int, input().split()))

count = 0

for i in range(N):
    for j in range(i,N,1):
        s = sum(A[i:j+1])
        #print(s)
        flag = True
        for k in range(i,j+1,1):
            if s % A[k] == 0:
                #print(A[k])
                flag = False
        #print(flag)
        if flag:
            count += 1

print(count)