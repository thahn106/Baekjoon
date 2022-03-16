from math import pow, ceil
def sa(a):
    return a[0]*a[1]+a[1]*a[2]+a[0]*a[2]

n = int(input())

ans = [1,1,n]
ma = sa(ans)

for a in range(1, ceil(pow(n,1/3))+1):
    na,r = divmod(n,a)
    if not r:
        for b in range(a,ceil(pow(na,1/2))+1):
            c,r=divmod(na,b)
            if not r:
                tr = [a,b,c]
                ta = sa(tr)
                if ta<ma:
                    ma = ta
                    ans = tr
print(*ans)
