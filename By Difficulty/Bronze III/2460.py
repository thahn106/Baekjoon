ans = 0
cur = 0
for i in range(10):
    a,b = map(int,input().split())
    cur += b-a
    ans = max(ans,cur)
print(ans)
