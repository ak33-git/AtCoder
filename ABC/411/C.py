N, Q = map(int, input().split())
A = list(map(int, input().split()))
L = [0] * (N + 2)


num = 0
for i in range(Q):
    if L[A[i]] == 0:
        L[A[i]] = 1
        if L[A[i]-1] == 1 and L[A[i]+1] == 1:
            num -= 1
        elif L[A[i]-1] == 0 and L[A[i]+1] == 0:
            num += 1         
    else:
        L[A[i]] = 0
        if L[A[i]-1] == 1 and L[A[i]+1] == 1:
            num += 1
        elif L[A[i]-1] == 0 and L[A[i]+1] == 0:
            num -= 1
    
    print(num)
    