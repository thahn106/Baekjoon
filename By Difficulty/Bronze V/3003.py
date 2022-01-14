ref = [1, 1, 2, 2, 2, 8]
a = list(map(int,input().split()))
ans = [ref[i]-a[i] for i in range(6)]
print(*ans)
