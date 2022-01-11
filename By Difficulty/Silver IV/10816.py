from bisect import bisect_left

N = int(input())
a = list(map(int,input().split()))
a.sort()

nl = []
cl = []
cur = -100000000
for n in a:
    if n == cur:
        cl[-1]+=1
    else:
        nl.append(n)
        cl.append(1)
        cur = n

M = int(input())
b =  list(map(int,input().split()))
ans = []
for n in b:
    i = bisect_left(nl,n)
    if i<len(nl) and nl[i] == n:
        ans.append(cl[i])
    else:
        ans.append(0)

print(*ans)
