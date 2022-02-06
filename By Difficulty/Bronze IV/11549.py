t = int(input())
ans = 0
for i in list(map(int,input().split())):
    if i==t:
        ans +=1
print(ans)
