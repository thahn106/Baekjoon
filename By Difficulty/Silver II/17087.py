from math import gcd
N, S = map(int, input().split())
a = list(map(int, input().split()))

ans = abs(S-a[0])
for p in a[1:]:
    ans = gcd(ans, abs(S-p))
print(ans)
