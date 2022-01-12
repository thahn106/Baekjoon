N = int(input())
ans = 0
i = 5
while i<=N:
    ans += N//i
    i*=5
print(ans)
