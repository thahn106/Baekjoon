N = int(input())
ans = 0
cur = 0
for i in list(map(int,input().split())):
    if i:
        cur +=1
        ans +=cur
    else:
        cur = 0
print(ans)
