N = int(input())
a = list(map(int,input().split()))
cur = 0
ans = 0
for i in a:
    if i == cur:
        cur = (cur+1)%3
        ans +=1
print(ans)
