N = int(input())
a = list(map(int,input().split()))

ans = 0
for i in range(N):
    temp = 0
    y = a[i]
    dy = -1000000000
    dx = 1
    for j in range(i-1,-1,-1):
        if (a[j]-a[i])*dx > dy*(i-j):
            temp +=1
            dy = (a[j]-a[i])
            dx = (i-j)
    dy = -1000000000
    dx = 1
    for j in range(i+1,N):
        if (a[j]-a[i])*dx > dy*(j-i):
            temp +=1
            dy = (a[j]-a[i])
            dx = (j-i)
    ans = max(temp,ans)
print(ans)
