S = list(input())

max = 0

for i in range(len(S)):
    for j in range(i,len(S)):
        if S[i] == "t" and S[j] == "t" and j - i >= 2:
            count = 0
            for k in range(i, j+1):
                if S[k] == "t":
                    count += 1
            if max < (count - 2) / (j - i - 1):
                max = (count - 2) / (j - i - 1)

print(max)