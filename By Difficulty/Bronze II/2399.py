n = int(input())
ans = 0
a = list(map(int,input().split()))
a.sort()
for i in range(n):
    ans += a[i]*(2*i-2*(n-i-1))
print(ans)
