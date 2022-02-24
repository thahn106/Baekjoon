N = int(input())
a = [int(input()) for i in range(N)]
ans = 5
for i in a:
    ref = list(range(i+1,i+5))
    t = 0
    for c in ref:
        if c not in a:
            t+=1
    ans = min(ans,t)
print(ans)
