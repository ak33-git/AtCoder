T = int(input())

for i in range(T):
    N, H = map(int, input().split())
    t = [0] * N
    l = [0] * N
    u = [0] * N
    for i in range(N):
        t[i], l[i], u[i] = map(int, input().split())
    
    flag = True
    prev_t = 0
    min = H
    max = H
    for i in range(N):
        dif = t[i] - prev_t
        prev_t = t[i]
        min -= dif
        if min < 0:
            min = 0
        max += dif

        #print("test1")
        #print(min)
        #print(max)

        if (min > u[i]):
            flag = False
        if (max < l[i]):
            flag = False
        
        #print(flag)
        if max > u[i]:
            max = u[i]
        if min < l[i]:
            min = l[i]
        
        #print("test2")
        #print(min)
        #print(max)
        
    if flag:
        print("Yes")
    else:
        print("No")