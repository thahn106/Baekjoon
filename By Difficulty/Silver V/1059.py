from bisect import bisect_left
L = int(input())
S = list(map(int, input().split()))
S.sort()

n = int(input())
i = bisect_left(S,n)
if S[i] == n:
    print(0)
else:
    if i==0:
        upper = S[i]
        lower = 0
    else:
        upper =  S[i]
        lower =  S[i-1]
    ans = (upper-n)*(n-lower)-1
    print(ans)
