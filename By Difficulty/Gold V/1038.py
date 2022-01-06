from math import comb
N = int(input())
if N>=1023:
    print(-1)
else:
    i=1
    while N>=comb(10,i):
        N-=comb(10,i)
        i+=1
    ans = ""
    for t in range(i):
        j=i-t
        while N>=comb(j,i-t):
            j+=1
        j-=1
        N-=comb(j,i-t)
        ans+=str(j)
    print(ans)
