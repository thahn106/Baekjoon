N,M = map(int,input().split())
a = list(range(1,N+1))
for m in range(M):
    i,j = map(int,input().split())
    a = a[:i-1]+a[i-1:j][::-1]+a[j:]

print(*a)
