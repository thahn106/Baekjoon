N, T, P = map(int,input().split())
ans = 1
if N:
    rank = list(map(int,input().split()))
    for i in rank:
        ans += T<i
    if N == P and T <= rank[-1]:
        ans = -1
print(ans)
