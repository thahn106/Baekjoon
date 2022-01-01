from math import ceil
A,B,C = map(int, input().split())
if C<=B:
    print(-1)
else:
    ans = A/(C-B)
    if ans == ceil(ans):
        ans = ceil(ans)+1
    else:
        ans = ceil(ans)
    print(ans)
