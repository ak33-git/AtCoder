import math
N = int(input())
RC = [map(int, input().split()) for _ in range(N)]
R, C = [list(i) for i in zip(*RC)]
R_dif = max(R) - min(R)
C_dif = max(C) - min(C)

if R_dif >= C_dif:
    print(math.ceil(R_dif / 2))
else:
    print(math.ceil(C_dif / 2))