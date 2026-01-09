from collections import deque
import sys

N = int(input())
A = list(map(int, input().split()))
run = []
if N < 4:
    print(N)
    sys.exit()

prev = A[0]
count = 1
for i in range(1, N):
    if prev == A[i]:
        count += 1
    else:
        run.append((prev, count))
        prev = A[i]
        count = 1
    
    if i == N-1:
        run.append((prev, count))

#print(run)


stack = deque()
stack.appendleft((0, 0))
for i in range(len(run)):
    if len(stack) == 0:
        stack.appendleft((0, 0))
    #print(stack)

    pop = stack.pop()
    now = run[i]
    if pop[0] == now[0]:
        add = (pop[0], (pop[1] + now[1]) % 4)
        if add[1] == 0:
            continue
        else:
            stack.append(add)
    else:
        if now[1] % 4 == 0:
            stack.append(pop)
            continue
        else:
            add = (now[0], now[1] % 4)
            stack.append(pop)
            stack.append(add)
#print(stack)
ans = 0
while len(stack) > 0:
    now = stack.pop()
    ans += now[1]

print(ans)