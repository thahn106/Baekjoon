N = int(input())
P = list(map(int,input().split()))

bot = 10000
cur = 10000
ans = 0
for i in P:
    if i>cur:
        ans = max(ans, i-bot)
    else:
        bot = i
    cur = i
print(ans)
