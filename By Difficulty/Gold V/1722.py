N = int(input())
a = list(map(int,input().split()))

fac = [1]
for i in range(1,N+1):
    fac.append(fac[-1]*(i))
ref = list(range(1,N+1))

if a[0] == 1:
    K = a[1]-1
    k = N
    ans = []
    while k:
        k -= 1
        ind, K = divmod(K, fac[k])
        ans.append(ref.pop(ind))
    print(*ans)
else:
    A = a[1:]
    k = N
    ans = 0
    for k, a in enumerate(A):
        ind = ref.index(a)
        ref.pop(ind)
        ans += fac[N-1-k]*ind
    print(ans+1)
