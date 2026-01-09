from collections import deque

H, W = map(int, input().split())
S = []

w_dic = {}

for i in range(H):
    inp = list(input())
    for j in range(W):
        if inp[j] != "." and inp[j] != "#":
            #print(inp[j])
            if inp[j] in w_dic:
                w_dic[inp[j]].add((i, j))
            else:
                w_dic[inp[j]] = set()
                w_dic[inp[j]].add((i, j))
    S.append(inp)

#print(w_dic)
d = deque()
s = set()
d.append(((0, 0),0))
s.add((0,0))
ans = -1
p_set = set()

count = 0

while len(d) > 0:
    count += 1
    #print(d)
    now = d.popleft()
    #print(now)
    x = now[0][0]
    y = now[0][1]
    count = now[1]
    #s.add((x, y))
    #print(now)

    if x == H-1 and y == W-1:
        ans = count
        break

    if x > 0:
        if S[x-1][y] != "#":
            if not (x-1, y) in s:
                s.add((x-1, y))
                d.append(((x-1, y), count+1))
    if x < H-1:
        if S[x+1][y] != "#":
            if not (x+1, y) in s:
                s.add((x+1, y))
                d.append(((x+1, y), count+1))
    if y > 0:
        if S[x][y-1] != "#":
            if not (x, y-1) in s:
                s.add((x, y-1))
                d.append(((x, y-1), count+1))     
    if y < W-1:
        if S[x][y+1] != "#":
            if not (x, y+1) in s:
                s.add((x, y+1))
                d.append(((x, y+1), count+1))
        
    if S[x][y] != "." and S[x][y] != "#":
            if not S[x][y] in p_set:
                p_set.add(S[x][y])
                app = list(w_dic[S[x][y]])
                for i in range(len(app)):
                    #print(w_dic[S[x][y]])
                    w_dic[S[x][y]].remove(app[i])
                    #print(w_dic[S[x][y]])
                    if not app[i] in s:
                        #print(app[i])
                        s.add(app[i])
                        d.append((app[i], count+1))
#print(w_dic)
print(ans)
#print(count)