t = 1000-int(input())
coins = [500,100,50,50,10,5,1]
ans = 0
for c in coins:
    r,t = divmod(t,c)
    ans += r
print(ans)
