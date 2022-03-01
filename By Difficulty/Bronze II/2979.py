costs = list(map(int,input().split()))
time = []
for i in range(3):
    times = list(map(int,input().split()))
    time.append(times)

ans = 0
for i in range(1,101):
    c = 0
    for j in range(3):
        s,e = time[j]
        if s<=i<e:
            c+=1
    if c:
        ans += costs[c-1]*c
print(ans)
