Q = int(input())
l = []
for i in range(Q):
    query = input().split()
    if query[0] == '1':
        l.append(int(query[1]))
        l = sorted(l)
    else:
        print(l[0])
        l = l[1:len(l)]
    