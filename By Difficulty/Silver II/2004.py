def facpow(n, k):
    ans = 0
    while n:
        n = n//k
        ans += n
    return ans

n, m = map(int,input().split())
a = facpow(n,5)-facpow(m,5)-facpow(n-m,5)
b = facpow(n,2)-facpow(m,2)-facpow(n-m,2)
print(min(a,b))
