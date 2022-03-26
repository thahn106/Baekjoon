N,M = map(int,input().split())
ans = 0
while N:
    ans +=N
    N = N//M

print(ans)
