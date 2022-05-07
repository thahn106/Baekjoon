x, y = map(int, input().split())
ans = 0
cur =x
d = 1
while True:
    if d>0:
        if cur<=y<=x+d:
            ans += y-cur
            break
        else:
            ans += x+d-cur
            cur = x+d
    else:
        if x+d<=y<=cur:
            ans += cur-y
            break
        else:
            ans += cur - (x+d)
            cur = x+d
    d *= -2
print(ans)
