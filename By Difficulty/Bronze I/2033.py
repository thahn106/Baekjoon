N = int(input())
n = 10
while N > n:
    q, r = divmod(N, n)
    if 2*r >= n:
        N = (q+1)*n
    else:
        N = q*n
    n *= 10
print(N)
