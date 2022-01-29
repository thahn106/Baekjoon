win = 0
ans = 0
for i in range(5):
    a = list(map(int,input().split()))
    if sum(a)>ans:
        win = i+1
        ans = sum(a)
print("{} {}".format(win,ans))
