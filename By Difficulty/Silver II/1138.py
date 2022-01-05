N = int(input())
a = list(map(int,input().split()))
ans = []
for i in range(N):
    ans.insert(a[N-1-i],N-i)
print(*ans)
