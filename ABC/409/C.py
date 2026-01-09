N, L = map(int,input().split())
d = list(map(int, input().split()))

for i in range(1,N-1):
    d[i] += d[i-1]

for i in range(N-1):
    d[i] = d[i] % L

d = sorted(d)
d.insert(0,0)

d_set = set(d)
d_list = list(d_set)
d_dict = {}
for i in range(len(d_list)):
    d_dict[d_list[i]] = 0
for i in range(len(d)):
    d_dict[d[i]] += 1

s = L / 3
count = 0

for i in range(N):
    if (d[i]+s in d_set) and (d[i]+(2*s)) in d_set:
        count += d_dict[d[i]+s] * d_dict[d[i]+(2*s)]

print(count)