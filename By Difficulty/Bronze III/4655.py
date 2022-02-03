f = float(input())
while f!=0:
    ans = 0
    cur = 0
    i = 2
    while cur<f:
        cur += 1/i
        ans += 1
        i += 1
    print("{} card(s)".format(ans))
    f = float(input())
