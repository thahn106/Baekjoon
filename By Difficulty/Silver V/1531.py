N,M = map(int,input().split())
p = []
for i in range(N):
    p.append(list(map(int,input().split())))

ans = 0
for i in range(1,101):
    for j in range(1,101):
        cur = 0
        for x1,y1,x2,y2 in p:
            if x1<=i<=x2 and y1<=j<=y2:
                cur+=1
                if cur>M:
                    ans +=1
                    break
print(ans)
