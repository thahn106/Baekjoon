n = int(input())

ans = 0
temp = 0
for c in input():
    if c.isdigit():
        temp = 10*temp + int(c)
    else:
        ans += temp
        temp = 0

ans += temp
print(ans)
