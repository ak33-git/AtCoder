import sys
S, A, B, C = map(int, input().split())

ans = 0
while True:
    A_cp = A
    B_cp = B
    while A_cp > 0:
        ans += S
        A_cp -= 1
        C -= 1
        if C == 0:
            print(ans)
            sys.exit()
    while B_cp > 0:
        B_cp -= 1
        C -= 1
        if C == 0:
            print(ans)
            sys.exit()