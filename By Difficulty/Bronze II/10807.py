N = int(input())
a = list(map(int,input().split()))
v = int(input())
ans = 0
for c in a:
    if c==v:
        ans+=1
print(ans)
