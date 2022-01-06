N,M = map(int,input().split())
rows =[]
for i in range(N):
    rows.append(input())
K = int(input())

counts = {}
for row in rows:
    zeroes = 0
    for c in row:
        if c == "0":
            zeroes+=1
    if row in counts:
        counts[row][0]+=1
    else:
        counts[row] = [1,zeroes]

ans=0
for row in counts:
    a,b = counts[row]
    if (not (K-b)%2) and b<=K:
        ans = max(ans,a)

print(ans)
